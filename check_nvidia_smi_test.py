import unittest
import check_nvidia_smi
import xmltodict
import nagiosplugin


XML_OUTPUT_NORMAL = None


class NvidiaSmiTestCase(unittest.TestCase):

    def setUp(self):
        self.smi = check_nvidia_smi.NvidiaSMI('mem_usage', 'localhost', port=22, username=None, password=None, gpu_uuid=None, xmldata=XML_OUTPUT_NORMAL)

    def test_get_device_data(self):
        self.assertEqual(len(self.smi.get_device_data()['gpus']), 4)

    def test_check(self):
        check = nagiosplugin.Check(
            self.smi,
            *self.smi.context('80', '90'),
            self.smi.summary())
        try:
            check.main()
        except SystemExit:
            pass


XML_OUTPUT_NORMAL = xmltodict.parse('''<?xml version="1.0" ?>
<!DOCTYPE nvidia_smi_log SYSTEM "nvsmi_device_v9.dtd">
<nvidia_smi_log>
	<timestamp>Tue May  7 09:03:41 2019</timestamp>
	<driver_version>390.94</driver_version>
	<attached_gpus>4</attached_gpus>
	<gpu id="00000000:1A:00.0">
		<product_name>Tesla M10</product_name>
		<product_brand>Tesla</product_brand>
		<display_mode>Enabled</display_mode>
		<display_active>Disabled</display_active>
		<persistence_mode>Enabled</persistence_mode>
		<accounting_mode>Enabled</accounting_mode>
		<accounting_mode_buffer_size>4000</accounting_mode_buffer_size>
		<driver_model>
			<current_dm>N/A</current_dm>
			<pending_dm>N/A</pending_dm>
		</driver_model>
		<serial>0424217033069</serial>
		<uuid>GPU-74f1301f-aa41-e5c6-f5c7-e15484997833</uuid>
		<minor_number>0</minor_number>
		<vbios_version>82.07.AB.00.12</vbios_version>
		<multigpu_board>Yes</multigpu_board>
		<board_id>0x1800</board_id>
		<gpu_part_number>900-22405-0000-000</gpu_part_number>
		<inforom_version>
			<img_version>2405.0070.00.02</img_version>
			<oem_object>1.1</oem_object>
			<ecc_object>N/A</ecc_object>
			<pwr_object>N/A</pwr_object>
		</inforom_version>
		<gpu_operation_mode>
			<current_gom>N/A</current_gom>
			<pending_gom>N/A</pending_gom>
		</gpu_operation_mode>
		<gpu_virtualization_mode>
			<virtualization_mode>Host VGPU</virtualization_mode>
		</gpu_virtualization_mode>
		<pci>
			<pci_bus>1A</pci_bus>
			<pci_device>00</pci_device>
			<pci_domain>0000</pci_domain>
			<pci_device_id>13BD10DE</pci_device_id>
			<pci_bus_id>00000000:1A:00.0</pci_bus_id>
			<pci_sub_system_id>116010DE</pci_sub_system_id>
			<pci_gpu_link_info>
				<pcie_gen>
					<max_link_gen>3</max_link_gen>
					<current_link_gen>1</current_link_gen>
				</pcie_gen>
				<link_widths>
					<max_link_width>16x</max_link_width>
					<current_link_width>8x</current_link_width>
				</link_widths>
			</pci_gpu_link_info>
			<pci_bridge_chip>
				<bridge_chip_type>N/A</bridge_chip_type>
				<bridge_chip_fw>N/A</bridge_chip_fw>
			</pci_bridge_chip>
			<replay_counter>0</replay_counter>
			<tx_util>0 KB/s</tx_util>
			<rx_util>0 KB/s</rx_util>
		</pci>
		<fan_speed>N/A</fan_speed>
		<performance_state>P8</performance_state>
		<clocks_throttle_reasons>
			<clocks_throttle_reason_gpu_idle>Active</clocks_throttle_reason_gpu_idle>
			<clocks_throttle_reason_applications_clocks_setting>Not Active</clocks_throttle_reason_applications_clocks_setting>
			<clocks_throttle_reason_sw_power_cap>Not Active</clocks_throttle_reason_sw_power_cap>
			<clocks_throttle_reason_hw_slowdown>Not Active</clocks_throttle_reason_hw_slowdown>
			<clocks_throttle_reason_hw_thermal_slowdown>N/A</clocks_throttle_reason_hw_thermal_slowdown>
			<clocks_throttle_reason_hw_power_brake_slowdown>N/A</clocks_throttle_reason_hw_power_brake_slowdown>
			<clocks_throttle_reason_sync_boost>Not Active</clocks_throttle_reason_sync_boost>
			<clocks_throttle_reason_sw_thermal_slowdown>Not Active</clocks_throttle_reason_sw_thermal_slowdown>
			<clocks_throttle_reason_display_clocks_setting>Not Active</clocks_throttle_reason_display_clocks_setting>
		</clocks_throttle_reasons>
		<fb_memory_usage>
			<total>8191 MiB</total>
			<used>8141 MiB</used>
			<free>50 MiB</free>
		</fb_memory_usage>
		<bar1_memory_usage>
			<total>256 MiB</total>
			<used>1 MiB</used>
			<free>255 MiB</free>
		</bar1_memory_usage>
		<compute_mode>Default</compute_mode>
		<utilization>
			<gpu_util>0 %</gpu_util>
			<memory_util>0 %</memory_util>
			<encoder_util>0 %</encoder_util>
			<decoder_util>0 %</decoder_util>
		</utilization>
		<encoder_stats>
			<session_count>0</session_count>
			<average_fps>0</average_fps>
			<average_latency>0</average_latency>
		</encoder_stats>
		<ecc_mode>
			<current_ecc>N/A</current_ecc>
			<pending_ecc>N/A</pending_ecc>
		</ecc_mode>
		<ecc_errors>
			<volatile>
				<single_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</single_bit>
				<double_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</double_bit>
			</volatile>
			<aggregate>
				<single_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</single_bit>
				<double_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</double_bit>
			</aggregate>
		</ecc_errors>
		<retired_pages>
			<multiple_single_bit_retirement>
				<retired_count>N/A</retired_count>
				<retired_page_addresses>N/A</retired_page_addresses>
			</multiple_single_bit_retirement>
			<double_bit_retirement>
				<retired_count>N/A</retired_count>
				<retired_page_addresses>N/A</retired_page_addresses>
			</double_bit_retirement>
			<pending_retirement>N/A</pending_retirement>
		</retired_pages>
		<temperature>
			<gpu_temp>37 C</gpu_temp>
			<gpu_temp_max_threshold>96 C</gpu_temp_max_threshold>
			<gpu_temp_slow_threshold>91 C</gpu_temp_slow_threshold>
			<gpu_temp_max_gpu_threshold>N/A</gpu_temp_max_gpu_threshold>
			<memory_temp>N/A</memory_temp>
			<gpu_temp_max_mem_threshold>N/A</gpu_temp_max_mem_threshold>
		</temperature>
		<power_readings>
			<power_state>P8</power_state>
			<power_management>Supported</power_management>
			<power_draw>10.43 W</power_draw>
			<power_limit>53.00 W</power_limit>
			<default_power_limit>53.00 W</default_power_limit>
			<enforced_power_limit>53.00 W</enforced_power_limit>
			<min_power_limit>26.50 W</min_power_limit>
			<max_power_limit>53.00 W</max_power_limit>
		</power_readings>
		<clocks>
			<graphics_clock>135 MHz</graphics_clock>
			<sm_clock>135 MHz</sm_clock>
			<mem_clock>405 MHz</mem_clock>
			<video_clock>405 MHz</video_clock>
		</clocks>
		<applications_clocks>
			<graphics_clock>1032 MHz</graphics_clock>
			<mem_clock>2600 MHz</mem_clock>
		</applications_clocks>
		<default_applications_clocks>
			<graphics_clock>1032 MHz</graphics_clock>
			<mem_clock>2600 MHz</mem_clock>
		</default_applications_clocks>
		<max_clocks>
			<graphics_clock>1202 MHz</graphics_clock>
			<sm_clock>1202 MHz</sm_clock>
			<mem_clock>2600 MHz</mem_clock>
			<video_clock>1081 MHz</video_clock>
		</max_clocks>
		<max_customer_boost_clocks>
			<graphics_clock>N/A</graphics_clock>
		</max_customer_boost_clocks>
		<clock_policy>
			<auto_boost>N/A</auto_boost>
			<auto_boost_default>N/A</auto_boost_default>
		</clock_policy>
		<supported_clocks>
			<supported_mem_clock>
				<value>2600 MHz</value>
				<supported_graphics_clock>1306 MHz</supported_graphics_clock>
				<supported_graphics_clock>1293 MHz</supported_graphics_clock>
				<supported_graphics_clock>1280 MHz</supported_graphics_clock>
				<supported_graphics_clock>1267 MHz</supported_graphics_clock>
				<supported_graphics_clock>1254 MHz</supported_graphics_clock>
				<supported_graphics_clock>1241 MHz</supported_graphics_clock>
				<supported_graphics_clock>1228 MHz</supported_graphics_clock>
				<supported_graphics_clock>1215 MHz</supported_graphics_clock>
				<supported_graphics_clock>1202 MHz</supported_graphics_clock>
				<supported_graphics_clock>1189 MHz</supported_graphics_clock>
				<supported_graphics_clock>1176 MHz</supported_graphics_clock>
				<supported_graphics_clock>1163 MHz</supported_graphics_clock>
				<supported_graphics_clock>1150 MHz</supported_graphics_clock>
				<supported_graphics_clock>1137 MHz</supported_graphics_clock>
				<supported_graphics_clock>1124 MHz</supported_graphics_clock>
				<supported_graphics_clock>1110 MHz</supported_graphics_clock>
				<supported_graphics_clock>1097 MHz</supported_graphics_clock>
				<supported_graphics_clock>1084 MHz</supported_graphics_clock>
				<supported_graphics_clock>1071 MHz</supported_graphics_clock>
				<supported_graphics_clock>1058 MHz</supported_graphics_clock>
				<supported_graphics_clock>1045 MHz</supported_graphics_clock>
				<supported_graphics_clock>1032 MHz</supported_graphics_clock>
				<supported_graphics_clock>1019 MHz</supported_graphics_clock>
				<supported_graphics_clock>1006 MHz</supported_graphics_clock>
				<supported_graphics_clock>993 MHz</supported_graphics_clock>
				<supported_graphics_clock>980 MHz</supported_graphics_clock>
				<supported_graphics_clock>967 MHz</supported_graphics_clock>
				<supported_graphics_clock>954 MHz</supported_graphics_clock>
				<supported_graphics_clock>941 MHz</supported_graphics_clock>
				<supported_graphics_clock>928 MHz</supported_graphics_clock>
				<supported_graphics_clock>915 MHz</supported_graphics_clock>
				<supported_graphics_clock>901 MHz</supported_graphics_clock>
				<supported_graphics_clock>888 MHz</supported_graphics_clock>
				<supported_graphics_clock>875 MHz</supported_graphics_clock>
				<supported_graphics_clock>862 MHz</supported_graphics_clock>
				<supported_graphics_clock>849 MHz</supported_graphics_clock>
				<supported_graphics_clock>836 MHz</supported_graphics_clock>
				<supported_graphics_clock>823 MHz</supported_graphics_clock>
				<supported_graphics_clock>810 MHz</supported_graphics_clock>
				<supported_graphics_clock>797 MHz</supported_graphics_clock>
				<supported_graphics_clock>784 MHz</supported_graphics_clock>
				<supported_graphics_clock>771 MHz</supported_graphics_clock>
				<supported_graphics_clock>758 MHz</supported_graphics_clock>
				<supported_graphics_clock>745 MHz</supported_graphics_clock>
				<supported_graphics_clock>732 MHz</supported_graphics_clock>
				<supported_graphics_clock>719 MHz</supported_graphics_clock>
				<supported_graphics_clock>705 MHz</supported_graphics_clock>
				<supported_graphics_clock>692 MHz</supported_graphics_clock>
				<supported_graphics_clock>679 MHz</supported_graphics_clock>
				<supported_graphics_clock>666 MHz</supported_graphics_clock>
				<supported_graphics_clock>653 MHz</supported_graphics_clock>
				<supported_graphics_clock>640 MHz</supported_graphics_clock>
				<supported_graphics_clock>627 MHz</supported_graphics_clock>
				<supported_graphics_clock>614 MHz</supported_graphics_clock>
				<supported_graphics_clock>601 MHz</supported_graphics_clock>
				<supported_graphics_clock>588 MHz</supported_graphics_clock>
				<supported_graphics_clock>575 MHz</supported_graphics_clock>
				<supported_graphics_clock>562 MHz</supported_graphics_clock>
				<supported_graphics_clock>549 MHz</supported_graphics_clock>
				<supported_graphics_clock>405 MHz</supported_graphics_clock>
				<supported_graphics_clock>392 MHz</supported_graphics_clock>
				<supported_graphics_clock>379 MHz</supported_graphics_clock>
				<supported_graphics_clock>366 MHz</supported_graphics_clock>
				<supported_graphics_clock>353 MHz</supported_graphics_clock>
				<supported_graphics_clock>340 MHz</supported_graphics_clock>
				<supported_graphics_clock>327 MHz</supported_graphics_clock>
				<supported_graphics_clock>324 MHz</supported_graphics_clock>
				<supported_graphics_clock>314 MHz</supported_graphics_clock>
				<supported_graphics_clock>301 MHz</supported_graphics_clock>
				<supported_graphics_clock>288 MHz</supported_graphics_clock>
				<supported_graphics_clock>275 MHz</supported_graphics_clock>
				<supported_graphics_clock>270 MHz</supported_graphics_clock>
				<supported_graphics_clock>267 MHz</supported_graphics_clock>
				<supported_graphics_clock>265 MHz</supported_graphics_clock>
				<supported_graphics_clock>263 MHz</supported_graphics_clock>
				<supported_graphics_clock>261 MHz</supported_graphics_clock>
				<supported_graphics_clock>259 MHz</supported_graphics_clock>
				<supported_graphics_clock>257 MHz</supported_graphics_clock>
				<supported_graphics_clock>255 MHz</supported_graphics_clock>
				<supported_graphics_clock>253 MHz</supported_graphics_clock>
				<supported_graphics_clock>251 MHz</supported_graphics_clock>
				<supported_graphics_clock>249 MHz</supported_graphics_clock>
				<supported_graphics_clock>247 MHz</supported_graphics_clock>
				<supported_graphics_clock>245 MHz</supported_graphics_clock>
				<supported_graphics_clock>243 MHz</supported_graphics_clock>
				<supported_graphics_clock>241 MHz</supported_graphics_clock>
				<supported_graphics_clock>239 MHz</supported_graphics_clock>
				<supported_graphics_clock>237 MHz</supported_graphics_clock>
				<supported_graphics_clock>235 MHz</supported_graphics_clock>
				<supported_graphics_clock>233 MHz</supported_graphics_clock>
				<supported_graphics_clock>231 MHz</supported_graphics_clock>
				<supported_graphics_clock>229 MHz</supported_graphics_clock>
				<supported_graphics_clock>226 MHz</supported_graphics_clock>
				<supported_graphics_clock>224 MHz</supported_graphics_clock>
				<supported_graphics_clock>222 MHz</supported_graphics_clock>
				<supported_graphics_clock>220 MHz</supported_graphics_clock>
				<supported_graphics_clock>218 MHz</supported_graphics_clock>
				<supported_graphics_clock>216 MHz</supported_graphics_clock>
				<supported_graphics_clock>214 MHz</supported_graphics_clock>
				<supported_graphics_clock>212 MHz</supported_graphics_clock>
				<supported_graphics_clock>210 MHz</supported_graphics_clock>
				<supported_graphics_clock>208 MHz</supported_graphics_clock>
				<supported_graphics_clock>206 MHz</supported_graphics_clock>
				<supported_graphics_clock>204 MHz</supported_graphics_clock>
				<supported_graphics_clock>202 MHz</supported_graphics_clock>
				<supported_graphics_clock>200 MHz</supported_graphics_clock>
				<supported_graphics_clock>198 MHz</supported_graphics_clock>
				<supported_graphics_clock>196 MHz</supported_graphics_clock>
				<supported_graphics_clock>194 MHz</supported_graphics_clock>
				<supported_graphics_clock>192 MHz</supported_graphics_clock>
				<supported_graphics_clock>190 MHz</supported_graphics_clock>
				<supported_graphics_clock>188 MHz</supported_graphics_clock>
				<supported_graphics_clock>186 MHz</supported_graphics_clock>
				<supported_graphics_clock>183 MHz</supported_graphics_clock>
				<supported_graphics_clock>181 MHz</supported_graphics_clock>
				<supported_graphics_clock>179 MHz</supported_graphics_clock>
				<supported_graphics_clock>177 MHz</supported_graphics_clock>
				<supported_graphics_clock>175 MHz</supported_graphics_clock>
				<supported_graphics_clock>173 MHz</supported_graphics_clock>
				<supported_graphics_clock>171 MHz</supported_graphics_clock>
				<supported_graphics_clock>169 MHz</supported_graphics_clock>
				<supported_graphics_clock>167 MHz</supported_graphics_clock>
				<supported_graphics_clock>165 MHz</supported_graphics_clock>
				<supported_graphics_clock>163 MHz</supported_graphics_clock>
				<supported_graphics_clock>161 MHz</supported_graphics_clock>
				<supported_graphics_clock>159 MHz</supported_graphics_clock>
				<supported_graphics_clock>157 MHz</supported_graphics_clock>
				<supported_graphics_clock>155 MHz</supported_graphics_clock>
				<supported_graphics_clock>153 MHz</supported_graphics_clock>
				<supported_graphics_clock>151 MHz</supported_graphics_clock>
				<supported_graphics_clock>149 MHz</supported_graphics_clock>
				<supported_graphics_clock>147 MHz</supported_graphics_clock>
				<supported_graphics_clock>145 MHz</supported_graphics_clock>
				<supported_graphics_clock>143 MHz</supported_graphics_clock>
				<supported_graphics_clock>140 MHz</supported_graphics_clock>
				<supported_graphics_clock>138 MHz</supported_graphics_clock>
				<supported_graphics_clock>136 MHz</supported_graphics_clock>
			</supported_mem_clock>
			<supported_mem_clock>
				<value>405 MHz</value>
				<supported_graphics_clock>405 MHz</supported_graphics_clock>
				<supported_graphics_clock>402 MHz</supported_graphics_clock>
				<supported_graphics_clock>400 MHz</supported_graphics_clock>
				<supported_graphics_clock>398 MHz</supported_graphics_clock>
				<supported_graphics_clock>396 MHz</supported_graphics_clock>
				<supported_graphics_clock>394 MHz</supported_graphics_clock>
				<supported_graphics_clock>392 MHz</supported_graphics_clock>
				<supported_graphics_clock>390 MHz</supported_graphics_clock>
				<supported_graphics_clock>388 MHz</supported_graphics_clock>
				<supported_graphics_clock>386 MHz</supported_graphics_clock>
				<supported_graphics_clock>384 MHz</supported_graphics_clock>
				<supported_graphics_clock>382 MHz</supported_graphics_clock>
				<supported_graphics_clock>380 MHz</supported_graphics_clock>
				<supported_graphics_clock>378 MHz</supported_graphics_clock>
				<supported_graphics_clock>376 MHz</supported_graphics_clock>
				<supported_graphics_clock>374 MHz</supported_graphics_clock>
				<supported_graphics_clock>372 MHz</supported_graphics_clock>
				<supported_graphics_clock>370 MHz</supported_graphics_clock>
				<supported_graphics_clock>368 MHz</supported_graphics_clock>
				<supported_graphics_clock>366 MHz</supported_graphics_clock>
				<supported_graphics_clock>364 MHz</supported_graphics_clock>
				<supported_graphics_clock>361 MHz</supported_graphics_clock>
				<supported_graphics_clock>359 MHz</supported_graphics_clock>
				<supported_graphics_clock>357 MHz</supported_graphics_clock>
				<supported_graphics_clock>355 MHz</supported_graphics_clock>
				<supported_graphics_clock>353 MHz</supported_graphics_clock>
				<supported_graphics_clock>351 MHz</supported_graphics_clock>
				<supported_graphics_clock>349 MHz</supported_graphics_clock>
				<supported_graphics_clock>347 MHz</supported_graphics_clock>
				<supported_graphics_clock>345 MHz</supported_graphics_clock>
				<supported_graphics_clock>343 MHz</supported_graphics_clock>
				<supported_graphics_clock>341 MHz</supported_graphics_clock>
				<supported_graphics_clock>339 MHz</supported_graphics_clock>
				<supported_graphics_clock>337 MHz</supported_graphics_clock>
				<supported_graphics_clock>335 MHz</supported_graphics_clock>
				<supported_graphics_clock>333 MHz</supported_graphics_clock>
				<supported_graphics_clock>331 MHz</supported_graphics_clock>
				<supported_graphics_clock>329 MHz</supported_graphics_clock>
				<supported_graphics_clock>327 MHz</supported_graphics_clock>
				<supported_graphics_clock>325 MHz</supported_graphics_clock>
				<supported_graphics_clock>323 MHz</supported_graphics_clock>
				<supported_graphics_clock>321 MHz</supported_graphics_clock>
				<supported_graphics_clock>318 MHz</supported_graphics_clock>
				<supported_graphics_clock>316 MHz</supported_graphics_clock>
				<supported_graphics_clock>314 MHz</supported_graphics_clock>
				<supported_graphics_clock>312 MHz</supported_graphics_clock>
				<supported_graphics_clock>310 MHz</supported_graphics_clock>
				<supported_graphics_clock>308 MHz</supported_graphics_clock>
				<supported_graphics_clock>306 MHz</supported_graphics_clock>
				<supported_graphics_clock>304 MHz</supported_graphics_clock>
				<supported_graphics_clock>302 MHz</supported_graphics_clock>
				<supported_graphics_clock>300 MHz</supported_graphics_clock>
				<supported_graphics_clock>298 MHz</supported_graphics_clock>
				<supported_graphics_clock>296 MHz</supported_graphics_clock>
				<supported_graphics_clock>294 MHz</supported_graphics_clock>
				<supported_graphics_clock>292 MHz</supported_graphics_clock>
				<supported_graphics_clock>290 MHz</supported_graphics_clock>
				<supported_graphics_clock>288 MHz</supported_graphics_clock>
				<supported_graphics_clock>286 MHz</supported_graphics_clock>
				<supported_graphics_clock>284 MHz</supported_graphics_clock>
				<supported_graphics_clock>282 MHz</supported_graphics_clock>
				<supported_graphics_clock>280 MHz</supported_graphics_clock>
				<supported_graphics_clock>278 MHz</supported_graphics_clock>
				<supported_graphics_clock>275 MHz</supported_graphics_clock>
				<supported_graphics_clock>273 MHz</supported_graphics_clock>
				<supported_graphics_clock>271 MHz</supported_graphics_clock>
				<supported_graphics_clock>269 MHz</supported_graphics_clock>
				<supported_graphics_clock>267 MHz</supported_graphics_clock>
				<supported_graphics_clock>265 MHz</supported_graphics_clock>
				<supported_graphics_clock>263 MHz</supported_graphics_clock>
				<supported_graphics_clock>261 MHz</supported_graphics_clock>
				<supported_graphics_clock>259 MHz</supported_graphics_clock>
				<supported_graphics_clock>257 MHz</supported_graphics_clock>
				<supported_graphics_clock>255 MHz</supported_graphics_clock>
				<supported_graphics_clock>253 MHz</supported_graphics_clock>
				<supported_graphics_clock>251 MHz</supported_graphics_clock>
				<supported_graphics_clock>249 MHz</supported_graphics_clock>
				<supported_graphics_clock>247 MHz</supported_graphics_clock>
				<supported_graphics_clock>245 MHz</supported_graphics_clock>
				<supported_graphics_clock>243 MHz</supported_graphics_clock>
				<supported_graphics_clock>241 MHz</supported_graphics_clock>
				<supported_graphics_clock>239 MHz</supported_graphics_clock>
				<supported_graphics_clock>237 MHz</supported_graphics_clock>
				<supported_graphics_clock>235 MHz</supported_graphics_clock>
				<supported_graphics_clock>232 MHz</supported_graphics_clock>
				<supported_graphics_clock>230 MHz</supported_graphics_clock>
				<supported_graphics_clock>228 MHz</supported_graphics_clock>
				<supported_graphics_clock>226 MHz</supported_graphics_clock>
				<supported_graphics_clock>224 MHz</supported_graphics_clock>
				<supported_graphics_clock>222 MHz</supported_graphics_clock>
				<supported_graphics_clock>220 MHz</supported_graphics_clock>
				<supported_graphics_clock>218 MHz</supported_graphics_clock>
				<supported_graphics_clock>216 MHz</supported_graphics_clock>
				<supported_graphics_clock>214 MHz</supported_graphics_clock>
				<supported_graphics_clock>212 MHz</supported_graphics_clock>
				<supported_graphics_clock>210 MHz</supported_graphics_clock>
				<supported_graphics_clock>208 MHz</supported_graphics_clock>
				<supported_graphics_clock>206 MHz</supported_graphics_clock>
				<supported_graphics_clock>204 MHz</supported_graphics_clock>
				<supported_graphics_clock>202 MHz</supported_graphics_clock>
				<supported_graphics_clock>200 MHz</supported_graphics_clock>
				<supported_graphics_clock>198 MHz</supported_graphics_clock>
				<supported_graphics_clock>196 MHz</supported_graphics_clock>
				<supported_graphics_clock>194 MHz</supported_graphics_clock>
				<supported_graphics_clock>192 MHz</supported_graphics_clock>
				<supported_graphics_clock>189 MHz</supported_graphics_clock>
				<supported_graphics_clock>187 MHz</supported_graphics_clock>
				<supported_graphics_clock>185 MHz</supported_graphics_clock>
				<supported_graphics_clock>183 MHz</supported_graphics_clock>
				<supported_graphics_clock>181 MHz</supported_graphics_clock>
				<supported_graphics_clock>179 MHz</supported_graphics_clock>
				<supported_graphics_clock>177 MHz</supported_graphics_clock>
				<supported_graphics_clock>175 MHz</supported_graphics_clock>
				<supported_graphics_clock>173 MHz</supported_graphics_clock>
				<supported_graphics_clock>171 MHz</supported_graphics_clock>
				<supported_graphics_clock>169 MHz</supported_graphics_clock>
				<supported_graphics_clock>167 MHz</supported_graphics_clock>
				<supported_graphics_clock>165 MHz</supported_graphics_clock>
				<supported_graphics_clock>163 MHz</supported_graphics_clock>
				<supported_graphics_clock>161 MHz</supported_graphics_clock>
				<supported_graphics_clock>159 MHz</supported_graphics_clock>
				<supported_graphics_clock>157 MHz</supported_graphics_clock>
				<supported_graphics_clock>155 MHz</supported_graphics_clock>
				<supported_graphics_clock>153 MHz</supported_graphics_clock>
				<supported_graphics_clock>151 MHz</supported_graphics_clock>
				<supported_graphics_clock>149 MHz</supported_graphics_clock>
				<supported_graphics_clock>146 MHz</supported_graphics_clock>
				<supported_graphics_clock>144 MHz</supported_graphics_clock>
				<supported_graphics_clock>142 MHz</supported_graphics_clock>
				<supported_graphics_clock>140 MHz</supported_graphics_clock>
				<supported_graphics_clock>138 MHz</supported_graphics_clock>
				<supported_graphics_clock>136 MHz</supported_graphics_clock>
			</supported_mem_clock>
		</supported_clocks>
		<processes>
			<process_info>
				<pid>42818686</pid>
				<type>C+G</type>
				<process_name>TS-526                     </process_name>
				<used_memory>4064 MiB</used_memory>
			</process_info>
			<process_info>
				<pid>43962378</pid>
				<type>C+G</type>
				<process_name>TS-530                     </process_name>
				<used_memory>4064 MiB</used_memory>
			</process_info>
		</processes>
		<accounted_processes>Insufficient Size</accounted_processes>
	</gpu>

	<gpu id="00000000:1B:00.0">
		<product_name>Tesla M10</product_name>
		<product_brand>Tesla</product_brand>
		<display_mode>Enabled</display_mode>
		<display_active>Disabled</display_active>
		<persistence_mode>Enabled</persistence_mode>
		<accounting_mode>Enabled</accounting_mode>
		<accounting_mode_buffer_size>4000</accounting_mode_buffer_size>
		<driver_model>
			<current_dm>N/A</current_dm>
			<pending_dm>N/A</pending_dm>
		</driver_model>
		<serial>0424217033069</serial>
		<uuid>GPU-5e9b8082-77de-41fe-5c44-176ebbfb1c78</uuid>
		<minor_number>1</minor_number>
		<vbios_version>82.07.AB.00.13</vbios_version>
		<multigpu_board>Yes</multigpu_board>
		<board_id>0x1800</board_id>
		<gpu_part_number>900-22405-0000-000</gpu_part_number>
		<inforom_version>
			<img_version>2405.0070.00.02</img_version>
			<oem_object>1.1</oem_object>
			<ecc_object>N/A</ecc_object>
			<pwr_object>N/A</pwr_object>
		</inforom_version>
		<gpu_operation_mode>
			<current_gom>N/A</current_gom>
			<pending_gom>N/A</pending_gom>
		</gpu_operation_mode>
		<gpu_virtualization_mode>
			<virtualization_mode>Host VGPU</virtualization_mode>
		</gpu_virtualization_mode>
		<pci>
			<pci_bus>1B</pci_bus>
			<pci_device>00</pci_device>
			<pci_domain>0000</pci_domain>
			<pci_device_id>13BD10DE</pci_device_id>
			<pci_bus_id>00000000:1B:00.0</pci_bus_id>
			<pci_sub_system_id>116010DE</pci_sub_system_id>
			<pci_gpu_link_info>
				<pcie_gen>
					<max_link_gen>3</max_link_gen>
					<current_link_gen>1</current_link_gen>
				</pcie_gen>
				<link_widths>
					<max_link_width>16x</max_link_width>
					<current_link_width>8x</current_link_width>
				</link_widths>
			</pci_gpu_link_info>
			<pci_bridge_chip>
				<bridge_chip_type>N/A</bridge_chip_type>
				<bridge_chip_fw>N/A</bridge_chip_fw>
			</pci_bridge_chip>
			<replay_counter>15</replay_counter>
			<tx_util>0 KB/s</tx_util>
			<rx_util>0 KB/s</rx_util>
		</pci>
		<fan_speed>N/A</fan_speed>
		<performance_state>P8</performance_state>
		<clocks_throttle_reasons>
			<clocks_throttle_reason_gpu_idle>Active</clocks_throttle_reason_gpu_idle>
			<clocks_throttle_reason_applications_clocks_setting>Not Active</clocks_throttle_reason_applications_clocks_setting>
			<clocks_throttle_reason_sw_power_cap>Not Active</clocks_throttle_reason_sw_power_cap>
			<clocks_throttle_reason_hw_slowdown>Not Active</clocks_throttle_reason_hw_slowdown>
			<clocks_throttle_reason_hw_thermal_slowdown>N/A</clocks_throttle_reason_hw_thermal_slowdown>
			<clocks_throttle_reason_hw_power_brake_slowdown>N/A</clocks_throttle_reason_hw_power_brake_slowdown>
			<clocks_throttle_reason_sync_boost>Not Active</clocks_throttle_reason_sync_boost>
			<clocks_throttle_reason_sw_thermal_slowdown>Not Active</clocks_throttle_reason_sw_thermal_slowdown>
			<clocks_throttle_reason_display_clocks_setting>Not Active</clocks_throttle_reason_display_clocks_setting>
		</clocks_throttle_reasons>
		<fb_memory_usage>
			<total>8191 MiB</total>
			<used>8141 MiB</used>
			<free>50 MiB</free>
		</fb_memory_usage>
		<bar1_memory_usage>
			<total>256 MiB</total>
			<used>1 MiB</used>
			<free>255 MiB</free>
		</bar1_memory_usage>
		<compute_mode>Default</compute_mode>
		<utilization>
			<gpu_util>0 %</gpu_util>
			<memory_util>0 %</memory_util>
			<encoder_util>0 %</encoder_util>
			<decoder_util>0 %</decoder_util>
		</utilization>
		<encoder_stats>
			<session_count>0</session_count>
			<average_fps>0</average_fps>
			<average_latency>0</average_latency>
		</encoder_stats>
		<ecc_mode>
			<current_ecc>N/A</current_ecc>
			<pending_ecc>N/A</pending_ecc>
		</ecc_mode>
		<ecc_errors>
			<volatile>
				<single_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</single_bit>
				<double_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</double_bit>
			</volatile>
			<aggregate>
				<single_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</single_bit>
				<double_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</double_bit>
			</aggregate>
		</ecc_errors>
		<retired_pages>
			<multiple_single_bit_retirement>
				<retired_count>N/A</retired_count>
				<retired_page_addresses>N/A</retired_page_addresses>
			</multiple_single_bit_retirement>
			<double_bit_retirement>
				<retired_count>N/A</retired_count>
				<retired_page_addresses>N/A</retired_page_addresses>
			</double_bit_retirement>
			<pending_retirement>N/A</pending_retirement>
		</retired_pages>
		<temperature>
			<gpu_temp>37 C</gpu_temp>
			<gpu_temp_max_threshold>96 C</gpu_temp_max_threshold>
			<gpu_temp_slow_threshold>91 C</gpu_temp_slow_threshold>
			<gpu_temp_max_gpu_threshold>N/A</gpu_temp_max_gpu_threshold>
			<memory_temp>N/A</memory_temp>
			<gpu_temp_max_mem_threshold>N/A</gpu_temp_max_mem_threshold>
		</temperature>
		<power_readings>
			<power_state>P8</power_state>
			<power_management>Supported</power_management>
			<power_draw>10.38 W</power_draw>
			<power_limit>53.00 W</power_limit>
			<default_power_limit>53.00 W</default_power_limit>
			<enforced_power_limit>53.00 W</enforced_power_limit>
			<min_power_limit>26.50 W</min_power_limit>
			<max_power_limit>53.00 W</max_power_limit>
		</power_readings>
		<clocks>
			<graphics_clock>135 MHz</graphics_clock>
			<sm_clock>135 MHz</sm_clock>
			<mem_clock>405 MHz</mem_clock>
			<video_clock>405 MHz</video_clock>
		</clocks>
		<applications_clocks>
			<graphics_clock>1032 MHz</graphics_clock>
			<mem_clock>2600 MHz</mem_clock>
		</applications_clocks>
		<default_applications_clocks>
			<graphics_clock>1032 MHz</graphics_clock>
			<mem_clock>2600 MHz</mem_clock>
		</default_applications_clocks>
		<max_clocks>
			<graphics_clock>1202 MHz</graphics_clock>
			<sm_clock>1202 MHz</sm_clock>
			<mem_clock>2600 MHz</mem_clock>
			<video_clock>1081 MHz</video_clock>
		</max_clocks>
		<max_customer_boost_clocks>
			<graphics_clock>N/A</graphics_clock>
		</max_customer_boost_clocks>
		<clock_policy>
			<auto_boost>N/A</auto_boost>
			<auto_boost_default>N/A</auto_boost_default>
		</clock_policy>
		<supported_clocks>
			<supported_mem_clock>
				<value>2600 MHz</value>
				<supported_graphics_clock>1306 MHz</supported_graphics_clock>
				<supported_graphics_clock>1293 MHz</supported_graphics_clock>
				<supported_graphics_clock>1280 MHz</supported_graphics_clock>
				<supported_graphics_clock>1267 MHz</supported_graphics_clock>
				<supported_graphics_clock>1254 MHz</supported_graphics_clock>
				<supported_graphics_clock>1241 MHz</supported_graphics_clock>
				<supported_graphics_clock>1228 MHz</supported_graphics_clock>
				<supported_graphics_clock>1215 MHz</supported_graphics_clock>
				<supported_graphics_clock>1202 MHz</supported_graphics_clock>
				<supported_graphics_clock>1189 MHz</supported_graphics_clock>
				<supported_graphics_clock>1176 MHz</supported_graphics_clock>
				<supported_graphics_clock>1163 MHz</supported_graphics_clock>
				<supported_graphics_clock>1150 MHz</supported_graphics_clock>
				<supported_graphics_clock>1137 MHz</supported_graphics_clock>
				<supported_graphics_clock>1124 MHz</supported_graphics_clock>
				<supported_graphics_clock>1110 MHz</supported_graphics_clock>
				<supported_graphics_clock>1097 MHz</supported_graphics_clock>
				<supported_graphics_clock>1084 MHz</supported_graphics_clock>
				<supported_graphics_clock>1071 MHz</supported_graphics_clock>
				<supported_graphics_clock>1058 MHz</supported_graphics_clock>
				<supported_graphics_clock>1045 MHz</supported_graphics_clock>
				<supported_graphics_clock>1032 MHz</supported_graphics_clock>
				<supported_graphics_clock>1019 MHz</supported_graphics_clock>
				<supported_graphics_clock>1006 MHz</supported_graphics_clock>
				<supported_graphics_clock>993 MHz</supported_graphics_clock>
				<supported_graphics_clock>980 MHz</supported_graphics_clock>
				<supported_graphics_clock>967 MHz</supported_graphics_clock>
				<supported_graphics_clock>954 MHz</supported_graphics_clock>
				<supported_graphics_clock>941 MHz</supported_graphics_clock>
				<supported_graphics_clock>928 MHz</supported_graphics_clock>
				<supported_graphics_clock>915 MHz</supported_graphics_clock>
				<supported_graphics_clock>901 MHz</supported_graphics_clock>
				<supported_graphics_clock>888 MHz</supported_graphics_clock>
				<supported_graphics_clock>875 MHz</supported_graphics_clock>
				<supported_graphics_clock>862 MHz</supported_graphics_clock>
				<supported_graphics_clock>849 MHz</supported_graphics_clock>
				<supported_graphics_clock>836 MHz</supported_graphics_clock>
				<supported_graphics_clock>823 MHz</supported_graphics_clock>
				<supported_graphics_clock>810 MHz</supported_graphics_clock>
				<supported_graphics_clock>797 MHz</supported_graphics_clock>
				<supported_graphics_clock>784 MHz</supported_graphics_clock>
				<supported_graphics_clock>771 MHz</supported_graphics_clock>
				<supported_graphics_clock>758 MHz</supported_graphics_clock>
				<supported_graphics_clock>745 MHz</supported_graphics_clock>
				<supported_graphics_clock>732 MHz</supported_graphics_clock>
				<supported_graphics_clock>719 MHz</supported_graphics_clock>
				<supported_graphics_clock>705 MHz</supported_graphics_clock>
				<supported_graphics_clock>692 MHz</supported_graphics_clock>
				<supported_graphics_clock>679 MHz</supported_graphics_clock>
				<supported_graphics_clock>666 MHz</supported_graphics_clock>
				<supported_graphics_clock>653 MHz</supported_graphics_clock>
				<supported_graphics_clock>640 MHz</supported_graphics_clock>
				<supported_graphics_clock>627 MHz</supported_graphics_clock>
				<supported_graphics_clock>614 MHz</supported_graphics_clock>
				<supported_graphics_clock>601 MHz</supported_graphics_clock>
				<supported_graphics_clock>588 MHz</supported_graphics_clock>
				<supported_graphics_clock>575 MHz</supported_graphics_clock>
				<supported_graphics_clock>562 MHz</supported_graphics_clock>
				<supported_graphics_clock>549 MHz</supported_graphics_clock>
				<supported_graphics_clock>405 MHz</supported_graphics_clock>
				<supported_graphics_clock>392 MHz</supported_graphics_clock>
				<supported_graphics_clock>379 MHz</supported_graphics_clock>
				<supported_graphics_clock>366 MHz</supported_graphics_clock>
				<supported_graphics_clock>353 MHz</supported_graphics_clock>
				<supported_graphics_clock>340 MHz</supported_graphics_clock>
				<supported_graphics_clock>327 MHz</supported_graphics_clock>
				<supported_graphics_clock>324 MHz</supported_graphics_clock>
				<supported_graphics_clock>314 MHz</supported_graphics_clock>
				<supported_graphics_clock>301 MHz</supported_graphics_clock>
				<supported_graphics_clock>288 MHz</supported_graphics_clock>
				<supported_graphics_clock>275 MHz</supported_graphics_clock>
				<supported_graphics_clock>270 MHz</supported_graphics_clock>
				<supported_graphics_clock>267 MHz</supported_graphics_clock>
				<supported_graphics_clock>265 MHz</supported_graphics_clock>
				<supported_graphics_clock>263 MHz</supported_graphics_clock>
				<supported_graphics_clock>261 MHz</supported_graphics_clock>
				<supported_graphics_clock>259 MHz</supported_graphics_clock>
				<supported_graphics_clock>257 MHz</supported_graphics_clock>
				<supported_graphics_clock>255 MHz</supported_graphics_clock>
				<supported_graphics_clock>253 MHz</supported_graphics_clock>
				<supported_graphics_clock>251 MHz</supported_graphics_clock>
				<supported_graphics_clock>249 MHz</supported_graphics_clock>
				<supported_graphics_clock>247 MHz</supported_graphics_clock>
				<supported_graphics_clock>245 MHz</supported_graphics_clock>
				<supported_graphics_clock>243 MHz</supported_graphics_clock>
				<supported_graphics_clock>241 MHz</supported_graphics_clock>
				<supported_graphics_clock>239 MHz</supported_graphics_clock>
				<supported_graphics_clock>237 MHz</supported_graphics_clock>
				<supported_graphics_clock>235 MHz</supported_graphics_clock>
				<supported_graphics_clock>233 MHz</supported_graphics_clock>
				<supported_graphics_clock>231 MHz</supported_graphics_clock>
				<supported_graphics_clock>229 MHz</supported_graphics_clock>
				<supported_graphics_clock>226 MHz</supported_graphics_clock>
				<supported_graphics_clock>224 MHz</supported_graphics_clock>
				<supported_graphics_clock>222 MHz</supported_graphics_clock>
				<supported_graphics_clock>220 MHz</supported_graphics_clock>
				<supported_graphics_clock>218 MHz</supported_graphics_clock>
				<supported_graphics_clock>216 MHz</supported_graphics_clock>
				<supported_graphics_clock>214 MHz</supported_graphics_clock>
				<supported_graphics_clock>212 MHz</supported_graphics_clock>
				<supported_graphics_clock>210 MHz</supported_graphics_clock>
				<supported_graphics_clock>208 MHz</supported_graphics_clock>
				<supported_graphics_clock>206 MHz</supported_graphics_clock>
				<supported_graphics_clock>204 MHz</supported_graphics_clock>
				<supported_graphics_clock>202 MHz</supported_graphics_clock>
				<supported_graphics_clock>200 MHz</supported_graphics_clock>
				<supported_graphics_clock>198 MHz</supported_graphics_clock>
				<supported_graphics_clock>196 MHz</supported_graphics_clock>
				<supported_graphics_clock>194 MHz</supported_graphics_clock>
				<supported_graphics_clock>192 MHz</supported_graphics_clock>
				<supported_graphics_clock>190 MHz</supported_graphics_clock>
				<supported_graphics_clock>188 MHz</supported_graphics_clock>
				<supported_graphics_clock>186 MHz</supported_graphics_clock>
				<supported_graphics_clock>183 MHz</supported_graphics_clock>
				<supported_graphics_clock>181 MHz</supported_graphics_clock>
				<supported_graphics_clock>179 MHz</supported_graphics_clock>
				<supported_graphics_clock>177 MHz</supported_graphics_clock>
				<supported_graphics_clock>175 MHz</supported_graphics_clock>
				<supported_graphics_clock>173 MHz</supported_graphics_clock>
				<supported_graphics_clock>171 MHz</supported_graphics_clock>
				<supported_graphics_clock>169 MHz</supported_graphics_clock>
				<supported_graphics_clock>167 MHz</supported_graphics_clock>
				<supported_graphics_clock>165 MHz</supported_graphics_clock>
				<supported_graphics_clock>163 MHz</supported_graphics_clock>
				<supported_graphics_clock>161 MHz</supported_graphics_clock>
				<supported_graphics_clock>159 MHz</supported_graphics_clock>
				<supported_graphics_clock>157 MHz</supported_graphics_clock>
				<supported_graphics_clock>155 MHz</supported_graphics_clock>
				<supported_graphics_clock>153 MHz</supported_graphics_clock>
				<supported_graphics_clock>151 MHz</supported_graphics_clock>
				<supported_graphics_clock>149 MHz</supported_graphics_clock>
				<supported_graphics_clock>147 MHz</supported_graphics_clock>
				<supported_graphics_clock>145 MHz</supported_graphics_clock>
				<supported_graphics_clock>143 MHz</supported_graphics_clock>
				<supported_graphics_clock>140 MHz</supported_graphics_clock>
				<supported_graphics_clock>138 MHz</supported_graphics_clock>
				<supported_graphics_clock>136 MHz</supported_graphics_clock>
			</supported_mem_clock>
			<supported_mem_clock>
				<value>405 MHz</value>
				<supported_graphics_clock>405 MHz</supported_graphics_clock>
				<supported_graphics_clock>402 MHz</supported_graphics_clock>
				<supported_graphics_clock>400 MHz</supported_graphics_clock>
				<supported_graphics_clock>398 MHz</supported_graphics_clock>
				<supported_graphics_clock>396 MHz</supported_graphics_clock>
				<supported_graphics_clock>394 MHz</supported_graphics_clock>
				<supported_graphics_clock>392 MHz</supported_graphics_clock>
				<supported_graphics_clock>390 MHz</supported_graphics_clock>
				<supported_graphics_clock>388 MHz</supported_graphics_clock>
				<supported_graphics_clock>386 MHz</supported_graphics_clock>
				<supported_graphics_clock>384 MHz</supported_graphics_clock>
				<supported_graphics_clock>382 MHz</supported_graphics_clock>
				<supported_graphics_clock>380 MHz</supported_graphics_clock>
				<supported_graphics_clock>378 MHz</supported_graphics_clock>
				<supported_graphics_clock>376 MHz</supported_graphics_clock>
				<supported_graphics_clock>374 MHz</supported_graphics_clock>
				<supported_graphics_clock>372 MHz</supported_graphics_clock>
				<supported_graphics_clock>370 MHz</supported_graphics_clock>
				<supported_graphics_clock>368 MHz</supported_graphics_clock>
				<supported_graphics_clock>366 MHz</supported_graphics_clock>
				<supported_graphics_clock>364 MHz</supported_graphics_clock>
				<supported_graphics_clock>361 MHz</supported_graphics_clock>
				<supported_graphics_clock>359 MHz</supported_graphics_clock>
				<supported_graphics_clock>357 MHz</supported_graphics_clock>
				<supported_graphics_clock>355 MHz</supported_graphics_clock>
				<supported_graphics_clock>353 MHz</supported_graphics_clock>
				<supported_graphics_clock>351 MHz</supported_graphics_clock>
				<supported_graphics_clock>349 MHz</supported_graphics_clock>
				<supported_graphics_clock>347 MHz</supported_graphics_clock>
				<supported_graphics_clock>345 MHz</supported_graphics_clock>
				<supported_graphics_clock>343 MHz</supported_graphics_clock>
				<supported_graphics_clock>341 MHz</supported_graphics_clock>
				<supported_graphics_clock>339 MHz</supported_graphics_clock>
				<supported_graphics_clock>337 MHz</supported_graphics_clock>
				<supported_graphics_clock>335 MHz</supported_graphics_clock>
				<supported_graphics_clock>333 MHz</supported_graphics_clock>
				<supported_graphics_clock>331 MHz</supported_graphics_clock>
				<supported_graphics_clock>329 MHz</supported_graphics_clock>
				<supported_graphics_clock>327 MHz</supported_graphics_clock>
				<supported_graphics_clock>325 MHz</supported_graphics_clock>
				<supported_graphics_clock>323 MHz</supported_graphics_clock>
				<supported_graphics_clock>321 MHz</supported_graphics_clock>
				<supported_graphics_clock>318 MHz</supported_graphics_clock>
				<supported_graphics_clock>316 MHz</supported_graphics_clock>
				<supported_graphics_clock>314 MHz</supported_graphics_clock>
				<supported_graphics_clock>312 MHz</supported_graphics_clock>
				<supported_graphics_clock>310 MHz</supported_graphics_clock>
				<supported_graphics_clock>308 MHz</supported_graphics_clock>
				<supported_graphics_clock>306 MHz</supported_graphics_clock>
				<supported_graphics_clock>304 MHz</supported_graphics_clock>
				<supported_graphics_clock>302 MHz</supported_graphics_clock>
				<supported_graphics_clock>300 MHz</supported_graphics_clock>
				<supported_graphics_clock>298 MHz</supported_graphics_clock>
				<supported_graphics_clock>296 MHz</supported_graphics_clock>
				<supported_graphics_clock>294 MHz</supported_graphics_clock>
				<supported_graphics_clock>292 MHz</supported_graphics_clock>
				<supported_graphics_clock>290 MHz</supported_graphics_clock>
				<supported_graphics_clock>288 MHz</supported_graphics_clock>
				<supported_graphics_clock>286 MHz</supported_graphics_clock>
				<supported_graphics_clock>284 MHz</supported_graphics_clock>
				<supported_graphics_clock>282 MHz</supported_graphics_clock>
				<supported_graphics_clock>280 MHz</supported_graphics_clock>
				<supported_graphics_clock>278 MHz</supported_graphics_clock>
				<supported_graphics_clock>275 MHz</supported_graphics_clock>
				<supported_graphics_clock>273 MHz</supported_graphics_clock>
				<supported_graphics_clock>271 MHz</supported_graphics_clock>
				<supported_graphics_clock>269 MHz</supported_graphics_clock>
				<supported_graphics_clock>267 MHz</supported_graphics_clock>
				<supported_graphics_clock>265 MHz</supported_graphics_clock>
				<supported_graphics_clock>263 MHz</supported_graphics_clock>
				<supported_graphics_clock>261 MHz</supported_graphics_clock>
				<supported_graphics_clock>259 MHz</supported_graphics_clock>
				<supported_graphics_clock>257 MHz</supported_graphics_clock>
				<supported_graphics_clock>255 MHz</supported_graphics_clock>
				<supported_graphics_clock>253 MHz</supported_graphics_clock>
				<supported_graphics_clock>251 MHz</supported_graphics_clock>
				<supported_graphics_clock>249 MHz</supported_graphics_clock>
				<supported_graphics_clock>247 MHz</supported_graphics_clock>
				<supported_graphics_clock>245 MHz</supported_graphics_clock>
				<supported_graphics_clock>243 MHz</supported_graphics_clock>
				<supported_graphics_clock>241 MHz</supported_graphics_clock>
				<supported_graphics_clock>239 MHz</supported_graphics_clock>
				<supported_graphics_clock>237 MHz</supported_graphics_clock>
				<supported_graphics_clock>235 MHz</supported_graphics_clock>
				<supported_graphics_clock>232 MHz</supported_graphics_clock>
				<supported_graphics_clock>230 MHz</supported_graphics_clock>
				<supported_graphics_clock>228 MHz</supported_graphics_clock>
				<supported_graphics_clock>226 MHz</supported_graphics_clock>
				<supported_graphics_clock>224 MHz</supported_graphics_clock>
				<supported_graphics_clock>222 MHz</supported_graphics_clock>
				<supported_graphics_clock>220 MHz</supported_graphics_clock>
				<supported_graphics_clock>218 MHz</supported_graphics_clock>
				<supported_graphics_clock>216 MHz</supported_graphics_clock>
				<supported_graphics_clock>214 MHz</supported_graphics_clock>
				<supported_graphics_clock>212 MHz</supported_graphics_clock>
				<supported_graphics_clock>210 MHz</supported_graphics_clock>
				<supported_graphics_clock>208 MHz</supported_graphics_clock>
				<supported_graphics_clock>206 MHz</supported_graphics_clock>
				<supported_graphics_clock>204 MHz</supported_graphics_clock>
				<supported_graphics_clock>202 MHz</supported_graphics_clock>
				<supported_graphics_clock>200 MHz</supported_graphics_clock>
				<supported_graphics_clock>198 MHz</supported_graphics_clock>
				<supported_graphics_clock>196 MHz</supported_graphics_clock>
				<supported_graphics_clock>194 MHz</supported_graphics_clock>
				<supported_graphics_clock>192 MHz</supported_graphics_clock>
				<supported_graphics_clock>189 MHz</supported_graphics_clock>
				<supported_graphics_clock>187 MHz</supported_graphics_clock>
				<supported_graphics_clock>185 MHz</supported_graphics_clock>
				<supported_graphics_clock>183 MHz</supported_graphics_clock>
				<supported_graphics_clock>181 MHz</supported_graphics_clock>
				<supported_graphics_clock>179 MHz</supported_graphics_clock>
				<supported_graphics_clock>177 MHz</supported_graphics_clock>
				<supported_graphics_clock>175 MHz</supported_graphics_clock>
				<supported_graphics_clock>173 MHz</supported_graphics_clock>
				<supported_graphics_clock>171 MHz</supported_graphics_clock>
				<supported_graphics_clock>169 MHz</supported_graphics_clock>
				<supported_graphics_clock>167 MHz</supported_graphics_clock>
				<supported_graphics_clock>165 MHz</supported_graphics_clock>
				<supported_graphics_clock>163 MHz</supported_graphics_clock>
				<supported_graphics_clock>161 MHz</supported_graphics_clock>
				<supported_graphics_clock>159 MHz</supported_graphics_clock>
				<supported_graphics_clock>157 MHz</supported_graphics_clock>
				<supported_graphics_clock>155 MHz</supported_graphics_clock>
				<supported_graphics_clock>153 MHz</supported_graphics_clock>
				<supported_graphics_clock>151 MHz</supported_graphics_clock>
				<supported_graphics_clock>149 MHz</supported_graphics_clock>
				<supported_graphics_clock>146 MHz</supported_graphics_clock>
				<supported_graphics_clock>144 MHz</supported_graphics_clock>
				<supported_graphics_clock>142 MHz</supported_graphics_clock>
				<supported_graphics_clock>140 MHz</supported_graphics_clock>
				<supported_graphics_clock>138 MHz</supported_graphics_clock>
				<supported_graphics_clock>136 MHz</supported_graphics_clock>
			</supported_mem_clock>
		</supported_clocks>
		<processes>
			<process_info>
				<pid>44450601</pid>
				<type>C+G</type>
				<process_name>TS-527                     </process_name>
				<used_memory>4064 MiB</used_memory>
			</process_info>
			<process_info>
				<pid>44714933</pid>
				<type>C+G</type>
				<process_name>TS-532                     </process_name>
				<used_memory>4064 MiB</used_memory>
			</process_info>
		</processes>
		<accounted_processes>Insufficient Size</accounted_processes>
	</gpu>

	<gpu id="00000000:1C:00.0">
		<product_name>Tesla M10</product_name>
		<product_brand>Tesla</product_brand>
		<display_mode>Enabled</display_mode>
		<display_active>Disabled</display_active>
		<persistence_mode>Enabled</persistence_mode>
		<accounting_mode>Enabled</accounting_mode>
		<accounting_mode_buffer_size>4000</accounting_mode_buffer_size>
		<driver_model>
			<current_dm>N/A</current_dm>
			<pending_dm>N/A</pending_dm>
		</driver_model>
		<serial>0424217033069</serial>
		<uuid>GPU-9a90d633-6239-77db-9db6-fb4acf3bd980</uuid>
		<minor_number>2</minor_number>
		<vbios_version>82.07.AB.00.15</vbios_version>
		<multigpu_board>Yes</multigpu_board>
		<board_id>0x1800</board_id>
		<gpu_part_number>900-22405-0000-000</gpu_part_number>
		<inforom_version>
			<img_version>2405.0070.00.02</img_version>
			<oem_object>1.1</oem_object>
			<ecc_object>N/A</ecc_object>
			<pwr_object>N/A</pwr_object>
		</inforom_version>
		<gpu_operation_mode>
			<current_gom>N/A</current_gom>
			<pending_gom>N/A</pending_gom>
		</gpu_operation_mode>
		<gpu_virtualization_mode>
			<virtualization_mode>Host VGPU</virtualization_mode>
		</gpu_virtualization_mode>
		<pci>
			<pci_bus>1C</pci_bus>
			<pci_device>00</pci_device>
			<pci_domain>0000</pci_domain>
			<pci_device_id>13BD10DE</pci_device_id>
			<pci_bus_id>00000000:1C:00.0</pci_bus_id>
			<pci_sub_system_id>116010DE</pci_sub_system_id>
			<pci_gpu_link_info>
				<pcie_gen>
					<max_link_gen>3</max_link_gen>
					<current_link_gen>1</current_link_gen>
				</pcie_gen>
				<link_widths>
					<max_link_width>16x</max_link_width>
					<current_link_width>8x</current_link_width>
				</link_widths>
			</pci_gpu_link_info>
			<pci_bridge_chip>
				<bridge_chip_type>N/A</bridge_chip_type>
				<bridge_chip_fw>N/A</bridge_chip_fw>
			</pci_bridge_chip>
			<replay_counter>0</replay_counter>
			<tx_util>0 KB/s</tx_util>
			<rx_util>0 KB/s</rx_util>
		</pci>
		<fan_speed>N/A</fan_speed>
		<performance_state>P8</performance_state>
		<clocks_throttle_reasons>
			<clocks_throttle_reason_gpu_idle>Active</clocks_throttle_reason_gpu_idle>
			<clocks_throttle_reason_applications_clocks_setting>Not Active</clocks_throttle_reason_applications_clocks_setting>
			<clocks_throttle_reason_sw_power_cap>Not Active</clocks_throttle_reason_sw_power_cap>
			<clocks_throttle_reason_hw_slowdown>Not Active</clocks_throttle_reason_hw_slowdown>
			<clocks_throttle_reason_hw_thermal_slowdown>N/A</clocks_throttle_reason_hw_thermal_slowdown>
			<clocks_throttle_reason_hw_power_brake_slowdown>N/A</clocks_throttle_reason_hw_power_brake_slowdown>
			<clocks_throttle_reason_sync_boost>Not Active</clocks_throttle_reason_sync_boost>
			<clocks_throttle_reason_sw_thermal_slowdown>Not Active</clocks_throttle_reason_sw_thermal_slowdown>
			<clocks_throttle_reason_display_clocks_setting>Not Active</clocks_throttle_reason_display_clocks_setting>
		</clocks_throttle_reasons>
		<fb_memory_usage>
			<total>8191 MiB</total>
			<used>8141 MiB</used>
			<free>50 MiB</free>
		</fb_memory_usage>
		<bar1_memory_usage>
			<total>256 MiB</total>
			<used>1 MiB</used>
			<free>255 MiB</free>
		</bar1_memory_usage>
		<compute_mode>Default</compute_mode>
		<utilization>
			<gpu_util>0 %</gpu_util>
			<memory_util>0 %</memory_util>
			<encoder_util>0 %</encoder_util>
			<decoder_util>0 %</decoder_util>
		</utilization>
		<encoder_stats>
			<session_count>0</session_count>
			<average_fps>0</average_fps>
			<average_latency>0</average_latency>
		</encoder_stats>
		<ecc_mode>
			<current_ecc>N/A</current_ecc>
			<pending_ecc>N/A</pending_ecc>
		</ecc_mode>
		<ecc_errors>
			<volatile>
				<single_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</single_bit>
				<double_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</double_bit>
			</volatile>
			<aggregate>
				<single_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</single_bit>
				<double_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</double_bit>
			</aggregate>
		</ecc_errors>
		<retired_pages>
			<multiple_single_bit_retirement>
				<retired_count>N/A</retired_count>
				<retired_page_addresses>N/A</retired_page_addresses>
			</multiple_single_bit_retirement>
			<double_bit_retirement>
				<retired_count>N/A</retired_count>
				<retired_page_addresses>N/A</retired_page_addresses>
			</double_bit_retirement>
			<pending_retirement>N/A</pending_retirement>
		</retired_pages>
		<temperature>
			<gpu_temp>29 C</gpu_temp>
			<gpu_temp_max_threshold>96 C</gpu_temp_max_threshold>
			<gpu_temp_slow_threshold>91 C</gpu_temp_slow_threshold>
			<gpu_temp_max_gpu_threshold>N/A</gpu_temp_max_gpu_threshold>
			<memory_temp>N/A</memory_temp>
			<gpu_temp_max_mem_threshold>N/A</gpu_temp_max_mem_threshold>
		</temperature>
		<power_readings>
			<power_state>P8</power_state>
			<power_management>Supported</power_management>
			<power_draw>10.38 W</power_draw>
			<power_limit>53.00 W</power_limit>
			<default_power_limit>53.00 W</default_power_limit>
			<enforced_power_limit>53.00 W</enforced_power_limit>
			<min_power_limit>26.50 W</min_power_limit>
			<max_power_limit>53.00 W</max_power_limit>
		</power_readings>
		<clocks>
			<graphics_clock>135 MHz</graphics_clock>
			<sm_clock>135 MHz</sm_clock>
			<mem_clock>405 MHz</mem_clock>
			<video_clock>405 MHz</video_clock>
		</clocks>
		<applications_clocks>
			<graphics_clock>1032 MHz</graphics_clock>
			<mem_clock>2600 MHz</mem_clock>
		</applications_clocks>
		<default_applications_clocks>
			<graphics_clock>1032 MHz</graphics_clock>
			<mem_clock>2600 MHz</mem_clock>
		</default_applications_clocks>
		<max_clocks>
			<graphics_clock>1202 MHz</graphics_clock>
			<sm_clock>1202 MHz</sm_clock>
			<mem_clock>2600 MHz</mem_clock>
			<video_clock>1081 MHz</video_clock>
		</max_clocks>
		<max_customer_boost_clocks>
			<graphics_clock>N/A</graphics_clock>
		</max_customer_boost_clocks>
		<clock_policy>
			<auto_boost>N/A</auto_boost>
			<auto_boost_default>N/A</auto_boost_default>
		</clock_policy>
		<supported_clocks>
			<supported_mem_clock>
				<value>2600 MHz</value>
				<supported_graphics_clock>1306 MHz</supported_graphics_clock>
				<supported_graphics_clock>1293 MHz</supported_graphics_clock>
				<supported_graphics_clock>1280 MHz</supported_graphics_clock>
				<supported_graphics_clock>1267 MHz</supported_graphics_clock>
				<supported_graphics_clock>1254 MHz</supported_graphics_clock>
				<supported_graphics_clock>1241 MHz</supported_graphics_clock>
				<supported_graphics_clock>1228 MHz</supported_graphics_clock>
				<supported_graphics_clock>1215 MHz</supported_graphics_clock>
				<supported_graphics_clock>1202 MHz</supported_graphics_clock>
				<supported_graphics_clock>1189 MHz</supported_graphics_clock>
				<supported_graphics_clock>1176 MHz</supported_graphics_clock>
				<supported_graphics_clock>1163 MHz</supported_graphics_clock>
				<supported_graphics_clock>1150 MHz</supported_graphics_clock>
				<supported_graphics_clock>1137 MHz</supported_graphics_clock>
				<supported_graphics_clock>1124 MHz</supported_graphics_clock>
				<supported_graphics_clock>1110 MHz</supported_graphics_clock>
				<supported_graphics_clock>1097 MHz</supported_graphics_clock>
				<supported_graphics_clock>1084 MHz</supported_graphics_clock>
				<supported_graphics_clock>1071 MHz</supported_graphics_clock>
				<supported_graphics_clock>1058 MHz</supported_graphics_clock>
				<supported_graphics_clock>1045 MHz</supported_graphics_clock>
				<supported_graphics_clock>1032 MHz</supported_graphics_clock>
				<supported_graphics_clock>1019 MHz</supported_graphics_clock>
				<supported_graphics_clock>1006 MHz</supported_graphics_clock>
				<supported_graphics_clock>993 MHz</supported_graphics_clock>
				<supported_graphics_clock>980 MHz</supported_graphics_clock>
				<supported_graphics_clock>967 MHz</supported_graphics_clock>
				<supported_graphics_clock>954 MHz</supported_graphics_clock>
				<supported_graphics_clock>941 MHz</supported_graphics_clock>
				<supported_graphics_clock>928 MHz</supported_graphics_clock>
				<supported_graphics_clock>915 MHz</supported_graphics_clock>
				<supported_graphics_clock>901 MHz</supported_graphics_clock>
				<supported_graphics_clock>888 MHz</supported_graphics_clock>
				<supported_graphics_clock>875 MHz</supported_graphics_clock>
				<supported_graphics_clock>862 MHz</supported_graphics_clock>
				<supported_graphics_clock>849 MHz</supported_graphics_clock>
				<supported_graphics_clock>836 MHz</supported_graphics_clock>
				<supported_graphics_clock>823 MHz</supported_graphics_clock>
				<supported_graphics_clock>810 MHz</supported_graphics_clock>
				<supported_graphics_clock>797 MHz</supported_graphics_clock>
				<supported_graphics_clock>784 MHz</supported_graphics_clock>
				<supported_graphics_clock>771 MHz</supported_graphics_clock>
				<supported_graphics_clock>758 MHz</supported_graphics_clock>
				<supported_graphics_clock>745 MHz</supported_graphics_clock>
				<supported_graphics_clock>732 MHz</supported_graphics_clock>
				<supported_graphics_clock>719 MHz</supported_graphics_clock>
				<supported_graphics_clock>705 MHz</supported_graphics_clock>
				<supported_graphics_clock>692 MHz</supported_graphics_clock>
				<supported_graphics_clock>679 MHz</supported_graphics_clock>
				<supported_graphics_clock>666 MHz</supported_graphics_clock>
				<supported_graphics_clock>653 MHz</supported_graphics_clock>
				<supported_graphics_clock>640 MHz</supported_graphics_clock>
				<supported_graphics_clock>627 MHz</supported_graphics_clock>
				<supported_graphics_clock>614 MHz</supported_graphics_clock>
				<supported_graphics_clock>601 MHz</supported_graphics_clock>
				<supported_graphics_clock>588 MHz</supported_graphics_clock>
				<supported_graphics_clock>575 MHz</supported_graphics_clock>
				<supported_graphics_clock>562 MHz</supported_graphics_clock>
				<supported_graphics_clock>549 MHz</supported_graphics_clock>
				<supported_graphics_clock>405 MHz</supported_graphics_clock>
				<supported_graphics_clock>392 MHz</supported_graphics_clock>
				<supported_graphics_clock>379 MHz</supported_graphics_clock>
				<supported_graphics_clock>366 MHz</supported_graphics_clock>
				<supported_graphics_clock>353 MHz</supported_graphics_clock>
				<supported_graphics_clock>340 MHz</supported_graphics_clock>
				<supported_graphics_clock>327 MHz</supported_graphics_clock>
				<supported_graphics_clock>324 MHz</supported_graphics_clock>
				<supported_graphics_clock>314 MHz</supported_graphics_clock>
				<supported_graphics_clock>301 MHz</supported_graphics_clock>
				<supported_graphics_clock>288 MHz</supported_graphics_clock>
				<supported_graphics_clock>275 MHz</supported_graphics_clock>
				<supported_graphics_clock>270 MHz</supported_graphics_clock>
				<supported_graphics_clock>267 MHz</supported_graphics_clock>
				<supported_graphics_clock>265 MHz</supported_graphics_clock>
				<supported_graphics_clock>263 MHz</supported_graphics_clock>
				<supported_graphics_clock>261 MHz</supported_graphics_clock>
				<supported_graphics_clock>259 MHz</supported_graphics_clock>
				<supported_graphics_clock>257 MHz</supported_graphics_clock>
				<supported_graphics_clock>255 MHz</supported_graphics_clock>
				<supported_graphics_clock>253 MHz</supported_graphics_clock>
				<supported_graphics_clock>251 MHz</supported_graphics_clock>
				<supported_graphics_clock>249 MHz</supported_graphics_clock>
				<supported_graphics_clock>247 MHz</supported_graphics_clock>
				<supported_graphics_clock>245 MHz</supported_graphics_clock>
				<supported_graphics_clock>243 MHz</supported_graphics_clock>
				<supported_graphics_clock>241 MHz</supported_graphics_clock>
				<supported_graphics_clock>239 MHz</supported_graphics_clock>
				<supported_graphics_clock>237 MHz</supported_graphics_clock>
				<supported_graphics_clock>235 MHz</supported_graphics_clock>
				<supported_graphics_clock>233 MHz</supported_graphics_clock>
				<supported_graphics_clock>231 MHz</supported_graphics_clock>
				<supported_graphics_clock>229 MHz</supported_graphics_clock>
				<supported_graphics_clock>226 MHz</supported_graphics_clock>
				<supported_graphics_clock>224 MHz</supported_graphics_clock>
				<supported_graphics_clock>222 MHz</supported_graphics_clock>
				<supported_graphics_clock>220 MHz</supported_graphics_clock>
				<supported_graphics_clock>218 MHz</supported_graphics_clock>
				<supported_graphics_clock>216 MHz</supported_graphics_clock>
				<supported_graphics_clock>214 MHz</supported_graphics_clock>
				<supported_graphics_clock>212 MHz</supported_graphics_clock>
				<supported_graphics_clock>210 MHz</supported_graphics_clock>
				<supported_graphics_clock>208 MHz</supported_graphics_clock>
				<supported_graphics_clock>206 MHz</supported_graphics_clock>
				<supported_graphics_clock>204 MHz</supported_graphics_clock>
				<supported_graphics_clock>202 MHz</supported_graphics_clock>
				<supported_graphics_clock>200 MHz</supported_graphics_clock>
				<supported_graphics_clock>198 MHz</supported_graphics_clock>
				<supported_graphics_clock>196 MHz</supported_graphics_clock>
				<supported_graphics_clock>194 MHz</supported_graphics_clock>
				<supported_graphics_clock>192 MHz</supported_graphics_clock>
				<supported_graphics_clock>190 MHz</supported_graphics_clock>
				<supported_graphics_clock>188 MHz</supported_graphics_clock>
				<supported_graphics_clock>186 MHz</supported_graphics_clock>
				<supported_graphics_clock>183 MHz</supported_graphics_clock>
				<supported_graphics_clock>181 MHz</supported_graphics_clock>
				<supported_graphics_clock>179 MHz</supported_graphics_clock>
				<supported_graphics_clock>177 MHz</supported_graphics_clock>
				<supported_graphics_clock>175 MHz</supported_graphics_clock>
				<supported_graphics_clock>173 MHz</supported_graphics_clock>
				<supported_graphics_clock>171 MHz</supported_graphics_clock>
				<supported_graphics_clock>169 MHz</supported_graphics_clock>
				<supported_graphics_clock>167 MHz</supported_graphics_clock>
				<supported_graphics_clock>165 MHz</supported_graphics_clock>
				<supported_graphics_clock>163 MHz</supported_graphics_clock>
				<supported_graphics_clock>161 MHz</supported_graphics_clock>
				<supported_graphics_clock>159 MHz</supported_graphics_clock>
				<supported_graphics_clock>157 MHz</supported_graphics_clock>
				<supported_graphics_clock>155 MHz</supported_graphics_clock>
				<supported_graphics_clock>153 MHz</supported_graphics_clock>
				<supported_graphics_clock>151 MHz</supported_graphics_clock>
				<supported_graphics_clock>149 MHz</supported_graphics_clock>
				<supported_graphics_clock>147 MHz</supported_graphics_clock>
				<supported_graphics_clock>145 MHz</supported_graphics_clock>
				<supported_graphics_clock>143 MHz</supported_graphics_clock>
				<supported_graphics_clock>140 MHz</supported_graphics_clock>
				<supported_graphics_clock>138 MHz</supported_graphics_clock>
				<supported_graphics_clock>136 MHz</supported_graphics_clock>
			</supported_mem_clock>
			<supported_mem_clock>
				<value>405 MHz</value>
				<supported_graphics_clock>405 MHz</supported_graphics_clock>
				<supported_graphics_clock>402 MHz</supported_graphics_clock>
				<supported_graphics_clock>400 MHz</supported_graphics_clock>
				<supported_graphics_clock>398 MHz</supported_graphics_clock>
				<supported_graphics_clock>396 MHz</supported_graphics_clock>
				<supported_graphics_clock>394 MHz</supported_graphics_clock>
				<supported_graphics_clock>392 MHz</supported_graphics_clock>
				<supported_graphics_clock>390 MHz</supported_graphics_clock>
				<supported_graphics_clock>388 MHz</supported_graphics_clock>
				<supported_graphics_clock>386 MHz</supported_graphics_clock>
				<supported_graphics_clock>384 MHz</supported_graphics_clock>
				<supported_graphics_clock>382 MHz</supported_graphics_clock>
				<supported_graphics_clock>380 MHz</supported_graphics_clock>
				<supported_graphics_clock>378 MHz</supported_graphics_clock>
				<supported_graphics_clock>376 MHz</supported_graphics_clock>
				<supported_graphics_clock>374 MHz</supported_graphics_clock>
				<supported_graphics_clock>372 MHz</supported_graphics_clock>
				<supported_graphics_clock>370 MHz</supported_graphics_clock>
				<supported_graphics_clock>368 MHz</supported_graphics_clock>
				<supported_graphics_clock>366 MHz</supported_graphics_clock>
				<supported_graphics_clock>364 MHz</supported_graphics_clock>
				<supported_graphics_clock>361 MHz</supported_graphics_clock>
				<supported_graphics_clock>359 MHz</supported_graphics_clock>
				<supported_graphics_clock>357 MHz</supported_graphics_clock>
				<supported_graphics_clock>355 MHz</supported_graphics_clock>
				<supported_graphics_clock>353 MHz</supported_graphics_clock>
				<supported_graphics_clock>351 MHz</supported_graphics_clock>
				<supported_graphics_clock>349 MHz</supported_graphics_clock>
				<supported_graphics_clock>347 MHz</supported_graphics_clock>
				<supported_graphics_clock>345 MHz</supported_graphics_clock>
				<supported_graphics_clock>343 MHz</supported_graphics_clock>
				<supported_graphics_clock>341 MHz</supported_graphics_clock>
				<supported_graphics_clock>339 MHz</supported_graphics_clock>
				<supported_graphics_clock>337 MHz</supported_graphics_clock>
				<supported_graphics_clock>335 MHz</supported_graphics_clock>
				<supported_graphics_clock>333 MHz</supported_graphics_clock>
				<supported_graphics_clock>331 MHz</supported_graphics_clock>
				<supported_graphics_clock>329 MHz</supported_graphics_clock>
				<supported_graphics_clock>327 MHz</supported_graphics_clock>
				<supported_graphics_clock>325 MHz</supported_graphics_clock>
				<supported_graphics_clock>323 MHz</supported_graphics_clock>
				<supported_graphics_clock>321 MHz</supported_graphics_clock>
				<supported_graphics_clock>318 MHz</supported_graphics_clock>
				<supported_graphics_clock>316 MHz</supported_graphics_clock>
				<supported_graphics_clock>314 MHz</supported_graphics_clock>
				<supported_graphics_clock>312 MHz</supported_graphics_clock>
				<supported_graphics_clock>310 MHz</supported_graphics_clock>
				<supported_graphics_clock>308 MHz</supported_graphics_clock>
				<supported_graphics_clock>306 MHz</supported_graphics_clock>
				<supported_graphics_clock>304 MHz</supported_graphics_clock>
				<supported_graphics_clock>302 MHz</supported_graphics_clock>
				<supported_graphics_clock>300 MHz</supported_graphics_clock>
				<supported_graphics_clock>298 MHz</supported_graphics_clock>
				<supported_graphics_clock>296 MHz</supported_graphics_clock>
				<supported_graphics_clock>294 MHz</supported_graphics_clock>
				<supported_graphics_clock>292 MHz</supported_graphics_clock>
				<supported_graphics_clock>290 MHz</supported_graphics_clock>
				<supported_graphics_clock>288 MHz</supported_graphics_clock>
				<supported_graphics_clock>286 MHz</supported_graphics_clock>
				<supported_graphics_clock>284 MHz</supported_graphics_clock>
				<supported_graphics_clock>282 MHz</supported_graphics_clock>
				<supported_graphics_clock>280 MHz</supported_graphics_clock>
				<supported_graphics_clock>278 MHz</supported_graphics_clock>
				<supported_graphics_clock>275 MHz</supported_graphics_clock>
				<supported_graphics_clock>273 MHz</supported_graphics_clock>
				<supported_graphics_clock>271 MHz</supported_graphics_clock>
				<supported_graphics_clock>269 MHz</supported_graphics_clock>
				<supported_graphics_clock>267 MHz</supported_graphics_clock>
				<supported_graphics_clock>265 MHz</supported_graphics_clock>
				<supported_graphics_clock>263 MHz</supported_graphics_clock>
				<supported_graphics_clock>261 MHz</supported_graphics_clock>
				<supported_graphics_clock>259 MHz</supported_graphics_clock>
				<supported_graphics_clock>257 MHz</supported_graphics_clock>
				<supported_graphics_clock>255 MHz</supported_graphics_clock>
				<supported_graphics_clock>253 MHz</supported_graphics_clock>
				<supported_graphics_clock>251 MHz</supported_graphics_clock>
				<supported_graphics_clock>249 MHz</supported_graphics_clock>
				<supported_graphics_clock>247 MHz</supported_graphics_clock>
				<supported_graphics_clock>245 MHz</supported_graphics_clock>
				<supported_graphics_clock>243 MHz</supported_graphics_clock>
				<supported_graphics_clock>241 MHz</supported_graphics_clock>
				<supported_graphics_clock>239 MHz</supported_graphics_clock>
				<supported_graphics_clock>237 MHz</supported_graphics_clock>
				<supported_graphics_clock>235 MHz</supported_graphics_clock>
				<supported_graphics_clock>232 MHz</supported_graphics_clock>
				<supported_graphics_clock>230 MHz</supported_graphics_clock>
				<supported_graphics_clock>228 MHz</supported_graphics_clock>
				<supported_graphics_clock>226 MHz</supported_graphics_clock>
				<supported_graphics_clock>224 MHz</supported_graphics_clock>
				<supported_graphics_clock>222 MHz</supported_graphics_clock>
				<supported_graphics_clock>220 MHz</supported_graphics_clock>
				<supported_graphics_clock>218 MHz</supported_graphics_clock>
				<supported_graphics_clock>216 MHz</supported_graphics_clock>
				<supported_graphics_clock>214 MHz</supported_graphics_clock>
				<supported_graphics_clock>212 MHz</supported_graphics_clock>
				<supported_graphics_clock>210 MHz</supported_graphics_clock>
				<supported_graphics_clock>208 MHz</supported_graphics_clock>
				<supported_graphics_clock>206 MHz</supported_graphics_clock>
				<supported_graphics_clock>204 MHz</supported_graphics_clock>
				<supported_graphics_clock>202 MHz</supported_graphics_clock>
				<supported_graphics_clock>200 MHz</supported_graphics_clock>
				<supported_graphics_clock>198 MHz</supported_graphics_clock>
				<supported_graphics_clock>196 MHz</supported_graphics_clock>
				<supported_graphics_clock>194 MHz</supported_graphics_clock>
				<supported_graphics_clock>192 MHz</supported_graphics_clock>
				<supported_graphics_clock>189 MHz</supported_graphics_clock>
				<supported_graphics_clock>187 MHz</supported_graphics_clock>
				<supported_graphics_clock>185 MHz</supported_graphics_clock>
				<supported_graphics_clock>183 MHz</supported_graphics_clock>
				<supported_graphics_clock>181 MHz</supported_graphics_clock>
				<supported_graphics_clock>179 MHz</supported_graphics_clock>
				<supported_graphics_clock>177 MHz</supported_graphics_clock>
				<supported_graphics_clock>175 MHz</supported_graphics_clock>
				<supported_graphics_clock>173 MHz</supported_graphics_clock>
				<supported_graphics_clock>171 MHz</supported_graphics_clock>
				<supported_graphics_clock>169 MHz</supported_graphics_clock>
				<supported_graphics_clock>167 MHz</supported_graphics_clock>
				<supported_graphics_clock>165 MHz</supported_graphics_clock>
				<supported_graphics_clock>163 MHz</supported_graphics_clock>
				<supported_graphics_clock>161 MHz</supported_graphics_clock>
				<supported_graphics_clock>159 MHz</supported_graphics_clock>
				<supported_graphics_clock>157 MHz</supported_graphics_clock>
				<supported_graphics_clock>155 MHz</supported_graphics_clock>
				<supported_graphics_clock>153 MHz</supported_graphics_clock>
				<supported_graphics_clock>151 MHz</supported_graphics_clock>
				<supported_graphics_clock>149 MHz</supported_graphics_clock>
				<supported_graphics_clock>146 MHz</supported_graphics_clock>
				<supported_graphics_clock>144 MHz</supported_graphics_clock>
				<supported_graphics_clock>142 MHz</supported_graphics_clock>
				<supported_graphics_clock>140 MHz</supported_graphics_clock>
				<supported_graphics_clock>138 MHz</supported_graphics_clock>
				<supported_graphics_clock>136 MHz</supported_graphics_clock>
			</supported_mem_clock>
		</supported_clocks>
		<processes>
			<process_info>
				<pid>44713050</pid>
				<type>C+G</type>
				<process_name>TS-525                     </process_name>
				<used_memory>4064 MiB</used_memory>
			</process_info>
			<process_info>
				<pid>44717029</pid>
				<type>C+G</type>
				<process_name>TS-529                     </process_name>
				<used_memory>4064 MiB</used_memory>
			</process_info>
		</processes>
		<accounted_processes>Insufficient Size</accounted_processes>
	</gpu>

	<gpu id="00000000:1D:00.0">
		<product_name>Tesla M10</product_name>
		<product_brand>Tesla</product_brand>
		<display_mode>Enabled</display_mode>
		<display_active>Disabled</display_active>
		<persistence_mode>Enabled</persistence_mode>
		<accounting_mode>Enabled</accounting_mode>
		<accounting_mode_buffer_size>4000</accounting_mode_buffer_size>
		<driver_model>
			<current_dm>N/A</current_dm>
			<pending_dm>N/A</pending_dm>
		</driver_model>
		<serial>0424217033069</serial>
		<uuid>GPU-feca4508-bf49-839b-0135-49c73ab3f73b</uuid>
		<minor_number>3</minor_number>
		<vbios_version>82.07.AB.00.14</vbios_version>
		<multigpu_board>Yes</multigpu_board>
		<board_id>0x1800</board_id>
		<gpu_part_number>900-22405-0000-000</gpu_part_number>
		<inforom_version>
			<img_version>2405.0070.00.02</img_version>
			<oem_object>1.1</oem_object>
			<ecc_object>N/A</ecc_object>
			<pwr_object>N/A</pwr_object>
		</inforom_version>
		<gpu_operation_mode>
			<current_gom>N/A</current_gom>
			<pending_gom>N/A</pending_gom>
		</gpu_operation_mode>
		<gpu_virtualization_mode>
			<virtualization_mode>Host VGPU</virtualization_mode>
		</gpu_virtualization_mode>
		<pci>
			<pci_bus>1D</pci_bus>
			<pci_device>00</pci_device>
			<pci_domain>0000</pci_domain>
			<pci_device_id>13BD10DE</pci_device_id>
			<pci_bus_id>00000000:1D:00.0</pci_bus_id>
			<pci_sub_system_id>116010DE</pci_sub_system_id>
			<pci_gpu_link_info>
				<pcie_gen>
					<max_link_gen>3</max_link_gen>
					<current_link_gen>1</current_link_gen>
				</pcie_gen>
				<link_widths>
					<max_link_width>16x</max_link_width>
					<current_link_width>8x</current_link_width>
				</link_widths>
			</pci_gpu_link_info>
			<pci_bridge_chip>
				<bridge_chip_type>N/A</bridge_chip_type>
				<bridge_chip_fw>N/A</bridge_chip_fw>
			</pci_bridge_chip>
			<replay_counter>0</replay_counter>
			<tx_util>0 KB/s</tx_util>
			<rx_util>1000 KB/s</rx_util>
		</pci>
		<fan_speed>N/A</fan_speed>
		<performance_state>P8</performance_state>
		<clocks_throttle_reasons>
			<clocks_throttle_reason_gpu_idle>Active</clocks_throttle_reason_gpu_idle>
			<clocks_throttle_reason_applications_clocks_setting>Not Active</clocks_throttle_reason_applications_clocks_setting>
			<clocks_throttle_reason_sw_power_cap>Not Active</clocks_throttle_reason_sw_power_cap>
			<clocks_throttle_reason_hw_slowdown>Not Active</clocks_throttle_reason_hw_slowdown>
			<clocks_throttle_reason_hw_thermal_slowdown>N/A</clocks_throttle_reason_hw_thermal_slowdown>
			<clocks_throttle_reason_hw_power_brake_slowdown>N/A</clocks_throttle_reason_hw_power_brake_slowdown>
			<clocks_throttle_reason_sync_boost>Not Active</clocks_throttle_reason_sync_boost>
			<clocks_throttle_reason_sw_thermal_slowdown>Not Active</clocks_throttle_reason_sw_thermal_slowdown>
			<clocks_throttle_reason_display_clocks_setting>Not Active</clocks_throttle_reason_display_clocks_setting>
		</clocks_throttle_reasons>
		<fb_memory_usage>
			<total>8191 MiB</total>
			<used>8141 MiB</used>
			<free>50 MiB</free>
		</fb_memory_usage>
		<bar1_memory_usage>
			<total>256 MiB</total>
			<used>1 MiB</used>
			<free>255 MiB</free>
		</bar1_memory_usage>
		<compute_mode>Default</compute_mode>
		<utilization>
			<gpu_util>0 %</gpu_util>
			<memory_util>0 %</memory_util>
			<encoder_util>0 %</encoder_util>
			<decoder_util>0 %</decoder_util>
		</utilization>
		<encoder_stats>
			<session_count>0</session_count>
			<average_fps>0</average_fps>
			<average_latency>0</average_latency>
		</encoder_stats>
		<ecc_mode>
			<current_ecc>N/A</current_ecc>
			<pending_ecc>N/A</pending_ecc>
		</ecc_mode>
		<ecc_errors>
			<volatile>
				<single_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</single_bit>
				<double_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</double_bit>
			</volatile>
			<aggregate>
				<single_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</single_bit>
				<double_bit>
					<device_memory>N/A</device_memory>
					<register_file>N/A</register_file>
					<l1_cache>N/A</l1_cache>
					<l2_cache>N/A</l2_cache>
					<texture_memory>N/A</texture_memory>
					<texture_shm>N/A</texture_shm>
					<cbu>N/A</cbu>
					<total>N/A</total>
				</double_bit>
			</aggregate>
		</ecc_errors>
		<retired_pages>
			<multiple_single_bit_retirement>
				<retired_count>N/A</retired_count>
				<retired_page_addresses>N/A</retired_page_addresses>
			</multiple_single_bit_retirement>
			<double_bit_retirement>
				<retired_count>N/A</retired_count>
				<retired_page_addresses>N/A</retired_page_addresses>
			</double_bit_retirement>
			<pending_retirement>N/A</pending_retirement>
		</retired_pages>
		<temperature>
			<gpu_temp>34 C</gpu_temp>
			<gpu_temp_max_threshold>96 C</gpu_temp_max_threshold>
			<gpu_temp_slow_threshold>91 C</gpu_temp_slow_threshold>
			<gpu_temp_max_gpu_threshold>N/A</gpu_temp_max_gpu_threshold>
			<memory_temp>N/A</memory_temp>
			<gpu_temp_max_mem_threshold>N/A</gpu_temp_max_mem_threshold>
		</temperature>
		<power_readings>
			<power_state>P8</power_state>
			<power_management>Supported</power_management>
			<power_draw>10.18 W</power_draw>
			<power_limit>53.00 W</power_limit>
			<default_power_limit>53.00 W</default_power_limit>
			<enforced_power_limit>53.00 W</enforced_power_limit>
			<min_power_limit>26.50 W</min_power_limit>
			<max_power_limit>53.00 W</max_power_limit>
		</power_readings>
		<clocks>
			<graphics_clock>135 MHz</graphics_clock>
			<sm_clock>135 MHz</sm_clock>
			<mem_clock>405 MHz</mem_clock>
			<video_clock>405 MHz</video_clock>
		</clocks>
		<applications_clocks>
			<graphics_clock>1032 MHz</graphics_clock>
			<mem_clock>2600 MHz</mem_clock>
		</applications_clocks>
		<default_applications_clocks>
			<graphics_clock>1032 MHz</graphics_clock>
			<mem_clock>2600 MHz</mem_clock>
		</default_applications_clocks>
		<max_clocks>
			<graphics_clock>1202 MHz</graphics_clock>
			<sm_clock>1202 MHz</sm_clock>
			<mem_clock>2600 MHz</mem_clock>
			<video_clock>1081 MHz</video_clock>
		</max_clocks>
		<max_customer_boost_clocks>
			<graphics_clock>N/A</graphics_clock>
		</max_customer_boost_clocks>
		<clock_policy>
			<auto_boost>N/A</auto_boost>
			<auto_boost_default>N/A</auto_boost_default>
		</clock_policy>
		<supported_clocks>
			<supported_mem_clock>
				<value>2600 MHz</value>
				<supported_graphics_clock>1306 MHz</supported_graphics_clock>
				<supported_graphics_clock>1293 MHz</supported_graphics_clock>
				<supported_graphics_clock>1280 MHz</supported_graphics_clock>
				<supported_graphics_clock>1267 MHz</supported_graphics_clock>
				<supported_graphics_clock>1254 MHz</supported_graphics_clock>
				<supported_graphics_clock>1241 MHz</supported_graphics_clock>
				<supported_graphics_clock>1228 MHz</supported_graphics_clock>
				<supported_graphics_clock>1215 MHz</supported_graphics_clock>
				<supported_graphics_clock>1202 MHz</supported_graphics_clock>
				<supported_graphics_clock>1189 MHz</supported_graphics_clock>
				<supported_graphics_clock>1176 MHz</supported_graphics_clock>
				<supported_graphics_clock>1163 MHz</supported_graphics_clock>
				<supported_graphics_clock>1150 MHz</supported_graphics_clock>
				<supported_graphics_clock>1137 MHz</supported_graphics_clock>
				<supported_graphics_clock>1124 MHz</supported_graphics_clock>
				<supported_graphics_clock>1110 MHz</supported_graphics_clock>
				<supported_graphics_clock>1097 MHz</supported_graphics_clock>
				<supported_graphics_clock>1084 MHz</supported_graphics_clock>
				<supported_graphics_clock>1071 MHz</supported_graphics_clock>
				<supported_graphics_clock>1058 MHz</supported_graphics_clock>
				<supported_graphics_clock>1045 MHz</supported_graphics_clock>
				<supported_graphics_clock>1032 MHz</supported_graphics_clock>
				<supported_graphics_clock>1019 MHz</supported_graphics_clock>
				<supported_graphics_clock>1006 MHz</supported_graphics_clock>
				<supported_graphics_clock>993 MHz</supported_graphics_clock>
				<supported_graphics_clock>980 MHz</supported_graphics_clock>
				<supported_graphics_clock>967 MHz</supported_graphics_clock>
				<supported_graphics_clock>954 MHz</supported_graphics_clock>
				<supported_graphics_clock>941 MHz</supported_graphics_clock>
				<supported_graphics_clock>928 MHz</supported_graphics_clock>
				<supported_graphics_clock>915 MHz</supported_graphics_clock>
				<supported_graphics_clock>901 MHz</supported_graphics_clock>
				<supported_graphics_clock>888 MHz</supported_graphics_clock>
				<supported_graphics_clock>875 MHz</supported_graphics_clock>
				<supported_graphics_clock>862 MHz</supported_graphics_clock>
				<supported_graphics_clock>849 MHz</supported_graphics_clock>
				<supported_graphics_clock>836 MHz</supported_graphics_clock>
				<supported_graphics_clock>823 MHz</supported_graphics_clock>
				<supported_graphics_clock>810 MHz</supported_graphics_clock>
				<supported_graphics_clock>797 MHz</supported_graphics_clock>
				<supported_graphics_clock>784 MHz</supported_graphics_clock>
				<supported_graphics_clock>771 MHz</supported_graphics_clock>
				<supported_graphics_clock>758 MHz</supported_graphics_clock>
				<supported_graphics_clock>745 MHz</supported_graphics_clock>
				<supported_graphics_clock>732 MHz</supported_graphics_clock>
				<supported_graphics_clock>719 MHz</supported_graphics_clock>
				<supported_graphics_clock>705 MHz</supported_graphics_clock>
				<supported_graphics_clock>692 MHz</supported_graphics_clock>
				<supported_graphics_clock>679 MHz</supported_graphics_clock>
				<supported_graphics_clock>666 MHz</supported_graphics_clock>
				<supported_graphics_clock>653 MHz</supported_graphics_clock>
				<supported_graphics_clock>640 MHz</supported_graphics_clock>
				<supported_graphics_clock>627 MHz</supported_graphics_clock>
				<supported_graphics_clock>614 MHz</supported_graphics_clock>
				<supported_graphics_clock>601 MHz</supported_graphics_clock>
				<supported_graphics_clock>588 MHz</supported_graphics_clock>
				<supported_graphics_clock>575 MHz</supported_graphics_clock>
				<supported_graphics_clock>562 MHz</supported_graphics_clock>
				<supported_graphics_clock>549 MHz</supported_graphics_clock>
				<supported_graphics_clock>405 MHz</supported_graphics_clock>
				<supported_graphics_clock>392 MHz</supported_graphics_clock>
				<supported_graphics_clock>379 MHz</supported_graphics_clock>
				<supported_graphics_clock>366 MHz</supported_graphics_clock>
				<supported_graphics_clock>353 MHz</supported_graphics_clock>
				<supported_graphics_clock>340 MHz</supported_graphics_clock>
				<supported_graphics_clock>327 MHz</supported_graphics_clock>
				<supported_graphics_clock>324 MHz</supported_graphics_clock>
				<supported_graphics_clock>314 MHz</supported_graphics_clock>
				<supported_graphics_clock>301 MHz</supported_graphics_clock>
				<supported_graphics_clock>288 MHz</supported_graphics_clock>
				<supported_graphics_clock>275 MHz</supported_graphics_clock>
				<supported_graphics_clock>270 MHz</supported_graphics_clock>
				<supported_graphics_clock>267 MHz</supported_graphics_clock>
				<supported_graphics_clock>265 MHz</supported_graphics_clock>
				<supported_graphics_clock>263 MHz</supported_graphics_clock>
				<supported_graphics_clock>261 MHz</supported_graphics_clock>
				<supported_graphics_clock>259 MHz</supported_graphics_clock>
				<supported_graphics_clock>257 MHz</supported_graphics_clock>
				<supported_graphics_clock>255 MHz</supported_graphics_clock>
				<supported_graphics_clock>253 MHz</supported_graphics_clock>
				<supported_graphics_clock>251 MHz</supported_graphics_clock>
				<supported_graphics_clock>249 MHz</supported_graphics_clock>
				<supported_graphics_clock>247 MHz</supported_graphics_clock>
				<supported_graphics_clock>245 MHz</supported_graphics_clock>
				<supported_graphics_clock>243 MHz</supported_graphics_clock>
				<supported_graphics_clock>241 MHz</supported_graphics_clock>
				<supported_graphics_clock>239 MHz</supported_graphics_clock>
				<supported_graphics_clock>237 MHz</supported_graphics_clock>
				<supported_graphics_clock>235 MHz</supported_graphics_clock>
				<supported_graphics_clock>233 MHz</supported_graphics_clock>
				<supported_graphics_clock>231 MHz</supported_graphics_clock>
				<supported_graphics_clock>229 MHz</supported_graphics_clock>
				<supported_graphics_clock>226 MHz</supported_graphics_clock>
				<supported_graphics_clock>224 MHz</supported_graphics_clock>
				<supported_graphics_clock>222 MHz</supported_graphics_clock>
				<supported_graphics_clock>220 MHz</supported_graphics_clock>
				<supported_graphics_clock>218 MHz</supported_graphics_clock>
				<supported_graphics_clock>216 MHz</supported_graphics_clock>
				<supported_graphics_clock>214 MHz</supported_graphics_clock>
				<supported_graphics_clock>212 MHz</supported_graphics_clock>
				<supported_graphics_clock>210 MHz</supported_graphics_clock>
				<supported_graphics_clock>208 MHz</supported_graphics_clock>
				<supported_graphics_clock>206 MHz</supported_graphics_clock>
				<supported_graphics_clock>204 MHz</supported_graphics_clock>
				<supported_graphics_clock>202 MHz</supported_graphics_clock>
				<supported_graphics_clock>200 MHz</supported_graphics_clock>
				<supported_graphics_clock>198 MHz</supported_graphics_clock>
				<supported_graphics_clock>196 MHz</supported_graphics_clock>
				<supported_graphics_clock>194 MHz</supported_graphics_clock>
				<supported_graphics_clock>192 MHz</supported_graphics_clock>
				<supported_graphics_clock>190 MHz</supported_graphics_clock>
				<supported_graphics_clock>188 MHz</supported_graphics_clock>
				<supported_graphics_clock>186 MHz</supported_graphics_clock>
				<supported_graphics_clock>183 MHz</supported_graphics_clock>
				<supported_graphics_clock>181 MHz</supported_graphics_clock>
				<supported_graphics_clock>179 MHz</supported_graphics_clock>
				<supported_graphics_clock>177 MHz</supported_graphics_clock>
				<supported_graphics_clock>175 MHz</supported_graphics_clock>
				<supported_graphics_clock>173 MHz</supported_graphics_clock>
				<supported_graphics_clock>171 MHz</supported_graphics_clock>
				<supported_graphics_clock>169 MHz</supported_graphics_clock>
				<supported_graphics_clock>167 MHz</supported_graphics_clock>
				<supported_graphics_clock>165 MHz</supported_graphics_clock>
				<supported_graphics_clock>163 MHz</supported_graphics_clock>
				<supported_graphics_clock>161 MHz</supported_graphics_clock>
				<supported_graphics_clock>159 MHz</supported_graphics_clock>
				<supported_graphics_clock>157 MHz</supported_graphics_clock>
				<supported_graphics_clock>155 MHz</supported_graphics_clock>
				<supported_graphics_clock>153 MHz</supported_graphics_clock>
				<supported_graphics_clock>151 MHz</supported_graphics_clock>
				<supported_graphics_clock>149 MHz</supported_graphics_clock>
				<supported_graphics_clock>147 MHz</supported_graphics_clock>
				<supported_graphics_clock>145 MHz</supported_graphics_clock>
				<supported_graphics_clock>143 MHz</supported_graphics_clock>
				<supported_graphics_clock>140 MHz</supported_graphics_clock>
				<supported_graphics_clock>138 MHz</supported_graphics_clock>
				<supported_graphics_clock>136 MHz</supported_graphics_clock>
			</supported_mem_clock>
			<supported_mem_clock>
				<value>405 MHz</value>
				<supported_graphics_clock>405 MHz</supported_graphics_clock>
				<supported_graphics_clock>402 MHz</supported_graphics_clock>
				<supported_graphics_clock>400 MHz</supported_graphics_clock>
				<supported_graphics_clock>398 MHz</supported_graphics_clock>
				<supported_graphics_clock>396 MHz</supported_graphics_clock>
				<supported_graphics_clock>394 MHz</supported_graphics_clock>
				<supported_graphics_clock>392 MHz</supported_graphics_clock>
				<supported_graphics_clock>390 MHz</supported_graphics_clock>
				<supported_graphics_clock>388 MHz</supported_graphics_clock>
				<supported_graphics_clock>386 MHz</supported_graphics_clock>
				<supported_graphics_clock>384 MHz</supported_graphics_clock>
				<supported_graphics_clock>382 MHz</supported_graphics_clock>
				<supported_graphics_clock>380 MHz</supported_graphics_clock>
				<supported_graphics_clock>378 MHz</supported_graphics_clock>
				<supported_graphics_clock>376 MHz</supported_graphics_clock>
				<supported_graphics_clock>374 MHz</supported_graphics_clock>
				<supported_graphics_clock>372 MHz</supported_graphics_clock>
				<supported_graphics_clock>370 MHz</supported_graphics_clock>
				<supported_graphics_clock>368 MHz</supported_graphics_clock>
				<supported_graphics_clock>366 MHz</supported_graphics_clock>
				<supported_graphics_clock>364 MHz</supported_graphics_clock>
				<supported_graphics_clock>361 MHz</supported_graphics_clock>
				<supported_graphics_clock>359 MHz</supported_graphics_clock>
				<supported_graphics_clock>357 MHz</supported_graphics_clock>
				<supported_graphics_clock>355 MHz</supported_graphics_clock>
				<supported_graphics_clock>353 MHz</supported_graphics_clock>
				<supported_graphics_clock>351 MHz</supported_graphics_clock>
				<supported_graphics_clock>349 MHz</supported_graphics_clock>
				<supported_graphics_clock>347 MHz</supported_graphics_clock>
				<supported_graphics_clock>345 MHz</supported_graphics_clock>
				<supported_graphics_clock>343 MHz</supported_graphics_clock>
				<supported_graphics_clock>341 MHz</supported_graphics_clock>
				<supported_graphics_clock>339 MHz</supported_graphics_clock>
				<supported_graphics_clock>337 MHz</supported_graphics_clock>
				<supported_graphics_clock>335 MHz</supported_graphics_clock>
				<supported_graphics_clock>333 MHz</supported_graphics_clock>
				<supported_graphics_clock>331 MHz</supported_graphics_clock>
				<supported_graphics_clock>329 MHz</supported_graphics_clock>
				<supported_graphics_clock>327 MHz</supported_graphics_clock>
				<supported_graphics_clock>325 MHz</supported_graphics_clock>
				<supported_graphics_clock>323 MHz</supported_graphics_clock>
				<supported_graphics_clock>321 MHz</supported_graphics_clock>
				<supported_graphics_clock>318 MHz</supported_graphics_clock>
				<supported_graphics_clock>316 MHz</supported_graphics_clock>
				<supported_graphics_clock>314 MHz</supported_graphics_clock>
				<supported_graphics_clock>312 MHz</supported_graphics_clock>
				<supported_graphics_clock>310 MHz</supported_graphics_clock>
				<supported_graphics_clock>308 MHz</supported_graphics_clock>
				<supported_graphics_clock>306 MHz</supported_graphics_clock>
				<supported_graphics_clock>304 MHz</supported_graphics_clock>
				<supported_graphics_clock>302 MHz</supported_graphics_clock>
				<supported_graphics_clock>300 MHz</supported_graphics_clock>
				<supported_graphics_clock>298 MHz</supported_graphics_clock>
				<supported_graphics_clock>296 MHz</supported_graphics_clock>
				<supported_graphics_clock>294 MHz</supported_graphics_clock>
				<supported_graphics_clock>292 MHz</supported_graphics_clock>
				<supported_graphics_clock>290 MHz</supported_graphics_clock>
				<supported_graphics_clock>288 MHz</supported_graphics_clock>
				<supported_graphics_clock>286 MHz</supported_graphics_clock>
				<supported_graphics_clock>284 MHz</supported_graphics_clock>
				<supported_graphics_clock>282 MHz</supported_graphics_clock>
				<supported_graphics_clock>280 MHz</supported_graphics_clock>
				<supported_graphics_clock>278 MHz</supported_graphics_clock>
				<supported_graphics_clock>275 MHz</supported_graphics_clock>
				<supported_graphics_clock>273 MHz</supported_graphics_clock>
				<supported_graphics_clock>271 MHz</supported_graphics_clock>
				<supported_graphics_clock>269 MHz</supported_graphics_clock>
				<supported_graphics_clock>267 MHz</supported_graphics_clock>
				<supported_graphics_clock>265 MHz</supported_graphics_clock>
				<supported_graphics_clock>263 MHz</supported_graphics_clock>
				<supported_graphics_clock>261 MHz</supported_graphics_clock>
				<supported_graphics_clock>259 MHz</supported_graphics_clock>
				<supported_graphics_clock>257 MHz</supported_graphics_clock>
				<supported_graphics_clock>255 MHz</supported_graphics_clock>
				<supported_graphics_clock>253 MHz</supported_graphics_clock>
				<supported_graphics_clock>251 MHz</supported_graphics_clock>
				<supported_graphics_clock>249 MHz</supported_graphics_clock>
				<supported_graphics_clock>247 MHz</supported_graphics_clock>
				<supported_graphics_clock>245 MHz</supported_graphics_clock>
				<supported_graphics_clock>243 MHz</supported_graphics_clock>
				<supported_graphics_clock>241 MHz</supported_graphics_clock>
				<supported_graphics_clock>239 MHz</supported_graphics_clock>
				<supported_graphics_clock>237 MHz</supported_graphics_clock>
				<supported_graphics_clock>235 MHz</supported_graphics_clock>
				<supported_graphics_clock>232 MHz</supported_graphics_clock>
				<supported_graphics_clock>230 MHz</supported_graphics_clock>
				<supported_graphics_clock>228 MHz</supported_graphics_clock>
				<supported_graphics_clock>226 MHz</supported_graphics_clock>
				<supported_graphics_clock>224 MHz</supported_graphics_clock>
				<supported_graphics_clock>222 MHz</supported_graphics_clock>
				<supported_graphics_clock>220 MHz</supported_graphics_clock>
				<supported_graphics_clock>218 MHz</supported_graphics_clock>
				<supported_graphics_clock>216 MHz</supported_graphics_clock>
				<supported_graphics_clock>214 MHz</supported_graphics_clock>
				<supported_graphics_clock>212 MHz</supported_graphics_clock>
				<supported_graphics_clock>210 MHz</supported_graphics_clock>
				<supported_graphics_clock>208 MHz</supported_graphics_clock>
				<supported_graphics_clock>206 MHz</supported_graphics_clock>
				<supported_graphics_clock>204 MHz</supported_graphics_clock>
				<supported_graphics_clock>202 MHz</supported_graphics_clock>
				<supported_graphics_clock>200 MHz</supported_graphics_clock>
				<supported_graphics_clock>198 MHz</supported_graphics_clock>
				<supported_graphics_clock>196 MHz</supported_graphics_clock>
				<supported_graphics_clock>194 MHz</supported_graphics_clock>
				<supported_graphics_clock>192 MHz</supported_graphics_clock>
				<supported_graphics_clock>189 MHz</supported_graphics_clock>
				<supported_graphics_clock>187 MHz</supported_graphics_clock>
				<supported_graphics_clock>185 MHz</supported_graphics_clock>
				<supported_graphics_clock>183 MHz</supported_graphics_clock>
				<supported_graphics_clock>181 MHz</supported_graphics_clock>
				<supported_graphics_clock>179 MHz</supported_graphics_clock>
				<supported_graphics_clock>177 MHz</supported_graphics_clock>
				<supported_graphics_clock>175 MHz</supported_graphics_clock>
				<supported_graphics_clock>173 MHz</supported_graphics_clock>
				<supported_graphics_clock>171 MHz</supported_graphics_clock>
				<supported_graphics_clock>169 MHz</supported_graphics_clock>
				<supported_graphics_clock>167 MHz</supported_graphics_clock>
				<supported_graphics_clock>165 MHz</supported_graphics_clock>
				<supported_graphics_clock>163 MHz</supported_graphics_clock>
				<supported_graphics_clock>161 MHz</supported_graphics_clock>
				<supported_graphics_clock>159 MHz</supported_graphics_clock>
				<supported_graphics_clock>157 MHz</supported_graphics_clock>
				<supported_graphics_clock>155 MHz</supported_graphics_clock>
				<supported_graphics_clock>153 MHz</supported_graphics_clock>
				<supported_graphics_clock>151 MHz</supported_graphics_clock>
				<supported_graphics_clock>149 MHz</supported_graphics_clock>
				<supported_graphics_clock>146 MHz</supported_graphics_clock>
				<supported_graphics_clock>144 MHz</supported_graphics_clock>
				<supported_graphics_clock>142 MHz</supported_graphics_clock>
				<supported_graphics_clock>140 MHz</supported_graphics_clock>
				<supported_graphics_clock>138 MHz</supported_graphics_clock>
				<supported_graphics_clock>136 MHz</supported_graphics_clock>
			</supported_mem_clock>
		</supported_clocks>
		<processes>
			<process_info>
				<pid>44324356</pid>
				<type>C+G</type>
				<process_name>TS-531                     </process_name>
				<used_memory>4064 MiB</used_memory>
			</process_info>
			<process_info>
				<pid>44458026</pid>
				<type>C+G</type>
				<process_name>TS-528                     </process_name>
				<used_memory>4064 MiB</used_memory>
			</process_info>
		</processes>
		<accounted_processes>Insufficient Size</accounted_processes>
	</gpu>

</nvidia_smi_log>
''')


if __name__ == '__main__':
    unittest.main()
