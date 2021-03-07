from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.devices_pool import DevicesPool
from utils.manage_appium_server import ManageAppiumServer
from run_case import run_cases
import time
# 第一步：从设备池当中，获取当前连接的设备。若设备池为空，则无设备连接。
devices = DevicesPool().devices_pool()
platform_name = 'Android'
appium_server_path = 'C:\\Users\\stacy\\AppData\\Local\\Programs\\Appium'
# 第二步：若设备池不为空，启动appium server.与设备个数对应。起始server端口为4723，每多一个设备，端口号默认+4
if devices and platform_name and appium_server_path:
    # 创建线程池
    T = ThreadPoolExecutor()
    # 实例化appium服务管理类。
    mas = ManageAppiumServer(appium_server_path)
    for device in devices:
        # kill 端口，以免占用
        mas.stop_appium(platform_name, device["port"])
        # 启动appium server
        task = T.submit(mas.start_appium_server, device["port"])
        time.sleep(1)

    # 第三步：若设备池不为空，在appium server启动的情况下，执行app自动化测试。
    time.sleep(15)
    obj_list = []
    for device in devices:
        index = devices.index(device)
        task = T.submit(run_cases, device)
        obj_list.append(task)
        time.sleep(1)

    # 等待自动化任务执行完成
    for future in as_completed(obj_list):
        data = future.result()
        print(f"sub_thread: {data}")

    # kill 掉appium server服务,释放端口。
    for device in devices:
        ManageAppiumServer.stop_appium(platform_name, device["port"])
