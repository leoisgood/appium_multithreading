from appium import webdriver
from utils.manage_devices import ManageDevices
from utils import get_yaml_data

desired_template = get_yaml_data.get_yaml('first')


class DevicesPool:
    def __init__(self, port=4723, system_port=8200):
        self.port = port  # 系统指定的端口
        self.system_port = system_port  # appium服务的端口
        self.des = desired_template  # 设备的配置参数

    def devices_pool(self):  # 返回一个appium的启动命令
        m = ManageDevices()
        all_devices_info = m.get_devices_info()
        # print(all_devices_info)
        devices_pool = []
        # 补充每一个设备的启动信息，以及配置对应的appium server端口号
        if all_devices_info:
            for dev_info in all_devices_info:
                dev_info.update(desired_template)
                dev_info["systemPort"] = self.system_port
                new_dict = {
                    "caps": dev_info,
                    "port": self.port
                }
                devices_pool.append(new_dict)
                self.port += 4
                self.system_port += 4
                # print(dev_info)
                # print(devices_pool)
        return devices_pool


if __name__ == '__main__':
    print(DevicesPool().devices_pool())
