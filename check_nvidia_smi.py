#!/usr/bin/env python3

"""
Author: it-novum GmbH - Johannes Drummer 2019

Checks the health of nvidia graphics card within vmware esxi via ssh
"""


import nagiosplugin
import argparse
import paramiko
import xmltodict
import re
import math
import warnings


warnings.filterwarnings("ignore")


class NvidiaSMIError(Exception):

    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


def units_convert_to_int(s, val_type=int):
    units = {
        'tib': 1024^4,
        'gib': 1024^3,
        'mib': 1024^2,
        'kib': 1024,
        'tb': 1000^4,
        'gb': 1000^3,
        'mb': 1000^2,
        'kb': 1000,
        'b': 1,
        'mw': 1000^2,
        'kw': 1000,
        'w': 1,
        '%': 1,
        'c': 1,
    }
    if s == 'N/A':
        return math.nan
    splits = re.split(r'\s+', s)
    if len(splits) == 1:
        return val_type(float(splits[0]))
    val, unit = splits
    return val_type(float(val)) * units[unit.lower()]


class GPU:

    def __init__(self, xmldata):
        self.product_brand = xmldata['product_brand']
        self.product_name = xmldata['product_name']
        self.uuid = xmldata['uuid']
        self.serial = xmldata['serial']
        self.fan_speed = units_convert_to_int(xmldata['fan_speed'])
        self.mem_total = units_convert_to_int(xmldata['fb_memory_usage']['total'])
        self.mem_used = units_convert_to_int(xmldata['fb_memory_usage']['used'])
        self.mem_free = units_convert_to_int(xmldata['fb_memory_usage']['free'])
        self.gpu_util = units_convert_to_int(xmldata['utilization']['gpu_util'])
        self.memory_util = units_convert_to_int(xmldata['utilization']['memory_util'])
        self.encoder_util = units_convert_to_int(xmldata['utilization']['encoder_util'])
        self.decoder_util = units_convert_to_int(xmldata['utilization']['decoder_util'])
        self.gpu_temp = units_convert_to_int(xmldata['temperature']['gpu_temp'])
        self.power_limit = units_convert_to_int(xmldata['power_readings']['power_limit'])
        self.power_draw = units_convert_to_int(xmldata['power_readings']['power_draw'])
        self.num_processes = len(xmldata['processes']['process_info'])

    @property
    def mem_usage(self):
        return int(self.mem_total / self.mem_used * 100)


class NvidiaSMISummary(nagiosplugin.Summary):

    def __init__(self, smi):
        self.smi = smi

    def ok(self, results):
        driver_version = ''
        try:
            driver_version = self.smi.get_device_data()['driver_version']
        except:
            pass
        return '(Driver: {}) {}'.format(driver_version, ', '.join([str(r) for r in results]))

    def problem(self, results):
        driver_version = ''
        try:
            driver_version = self.smi.get_device_data()['driver_version']
        except:
            pass
        return '(Driver: {}) {}'.format(driver_version, ', '.join([str(r) for r in results]))


class NvidiaSMI(nagiosplugin.Resource):
    check_types = [
        'mem_usage',
        'gpu_util',
        'memory_util',
        'encoder_util',
        'decoder_util',
        'gpu_temp',
        'power_draw',
        'num_processes',
    ]

    def __init__(self, check_type, hostname, port=22, username=None, password=None, gpu_uuid=None, xmldata=None):
        self.check_type = check_type
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.gpu_uuid = gpu_uuid
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.load_system_host_keys()
        self.connected = False
        self._xmldata = xmldata
        self._device_data = None

    def context(self, warning, critical):
        return [nagiosplugin.ScalarContext(ctx, warning, critical) for ctx in self.check_types]

    def summary(self):
        return NvidiaSMISummary(self)

    def _connect(self):
        if not self.connected:
            self.ssh_client.connect(self.hostname, self.port, self.username, self.password)
            self.connected = True

    def _disconnect(self):
        if self.connected:
            self.ssh_client.close()

    def gather_xml(self):
        if self._xmldata is not None:
            return self._xmldata
        self._connect()
        stdin, stdout, stderr = self.ssh_client.exec_command('nvidia-smi -q --xml-format', timeout=30)
        stdin.close()
        nvidia_data = None
        try:
            nvidia_data = xmltodict.parse(stdout.read())
        except ValueError as e:
            raise NvidiaSMIError('Could not parse XML structure from nvidia-smi -q --xml-format command: {}\nError Output:\n{}'.format(str(e), stderr.read()))
        self._disconnect()
        self.xmldata = nvidia_data
        return nvidia_data

    def get_device_data(self, xmldata=None):
        if self._device_data is not None:
            return self._device_data
        if xmldata is None:
            xmldata = self.gather_xml()
        device_data = {
            'gpus': [],
            'driver_version': xmldata['nvidia_smi_log']['driver_version'],
        }
        for gpudata in xmldata['nvidia_smi_log']['gpu']:
            device_data['gpus'].append(GPU(gpudata))
        self._device_data = device_data
        return device_data

    def probe(self):
        device_data = self.get_device_data()
        gpus = device_data['gpus']
        if self.gpu_uuid is not None and self.gpu_uuid != '':
            gpus = [gpu for gpu in gpus if gpu.uuid == self.gpu_uuid]

        for gpu in gpus:
            if self.check_type == 'mem_usage':
                yield nagiosplugin.Metric('{}::Memory Usage'.format(gpu.uuid), gpu.mem_usage, min=0, max=100, uom='%', context='mem_usage')
            elif self.check_type == 'gpu_util':
                yield nagiosplugin.Metric('{}::GPU Util'.format(gpu.uuid), gpu.gpu_util, min=0, max=100, uom='%', context='gpu_util')
            elif self.check_type == 'memory_util':
                yield nagiosplugin.Metric('{}::Memory Util'.format(gpu.uuid), gpu.memory_util, min=0, max=100, uom='%', context='memory_util')
            elif self.check_type == 'encoder_util':
                yield nagiosplugin.Metric('{}::Encoder Util'.format(gpu.uuid), gpu.encoder_util, min=0, max=100, uom='%', context='encoder_util')
            elif self.check_type == 'decoder_util':
                yield nagiosplugin.Metric('{}::Decoder Util'.format(gpu.uuid), gpu.decoder_util, min=0, max=100, uom='%', context='decoder_util')
            elif self.check_type == 'gpu_temp':
                yield nagiosplugin.Metric('{}::GPU Temp'.format(gpu.uuid), gpu.gpu_temp, min=0, uom='C', context='gpu_temp')
            elif self.check_type == 'power_draw':
                yield nagiosplugin.Metric('{}::Power Draw'.format(gpu.uuid), gpu.power_draw, min=0, uom='W', max=gpu.power_limit, context='power_draw')
            elif self.check_type == 'num_processes':
                yield nagiosplugin.Metric('{}::Processes'.format(gpu.uuid), gpu.num_processes, min=0, uom='c', context='num_processes')


@nagiosplugin.guarded
def main():
    argp = argparse.ArgumentParser(description='Check status of nvidia graphics card in vmware esxi')
    argp.add_argument('-H', '--hostname', metavar='HOSTNAMEIP', required=True, help='hostname or ip adress of esxi host')
    argp.add_argument('-P', '--port', metavar='SSHPORT', help='SSH Port', default=22)
    argp.add_argument('-u', '--username', metavar='USER', help='SSH Username', default=None)
    argp.add_argument('-p', '--password', metavar='PASSWORD', help='SSH Password', default=None)
    argp.add_argument('-t', '--type', metavar='TYPE', required=True,
                      choices=NvidiaSMI.check_types,
                      help='Choose metric for limits: {}'.format(', '.join(NvidiaSMI.check_types)))
    argp.add_argument('-g', '--gpu-uuid', metavar='UUID', help='monitor a specific graphics card (nvidia-smi -L)')
    argp.add_argument('-w', '--warning', metavar='RANGE', default='',
                      help='return warning if load is outside RANGE')
    argp.add_argument('-c', '--critical', metavar='RANGE', default='',
                      help='return critical if load is outside RANGE')
    args = argp.parse_args()

    res = NvidiaSMI(args.type, args.hostname, args.port, args.username, args.password, args.gpu_uuid)

    check = nagiosplugin.Check(
        res,
        *res.context(args.warning, args.critical),
        res.summary())
    check.main()


if __name__ == '__main__':
    main()
