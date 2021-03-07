"""
@Title   : 管理adb连接的设备，返回设备信息列表
@Author  : Leo.liu
@Email   : Leo.liu@italki.com
"""


class ManageDevices:
    def __init__(self):
        self.devices_info = self.get_devices_info()

    def get_devices_info(self):
        # 设备信息存放在字典当中，设备uuid,version,占用端口
        # 要使用到python命令行参数模块
        # 获取uuid，截取端口号
        # 返回设备信息列表
        device_lists = []
        uuid = ['127.0.0.1:62001', '127.0.0.1:62002']
        version = ['7.0.1', '7.0.1']
        # port = [62001, 62002]
        first_device_info = {'uuid': uuid[0], 'version': version[0]}
        second_device_info = {'uuid': uuid[1], 'version': version[1]}
        device_lists.append(first_device_info)
        # device_lists.append(second_device_info)
        return device_lists


if __name__ == '__main__':
    m = ManageDevices()
    print(m.get_devices_info())
