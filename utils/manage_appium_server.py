import subprocess
import os


# from common.handle_path import appium_logs_dir


class ManageAppiumServer:
    """
    appium desktop通过命令行启动appium服务。
    不同平台上安装的appium，默认的appium服务路径不一样。
    初始化时，设置appium服务启动路径
    再根据给定的端口号启动appium
    """

    def __init__(self, appium_server_apth):
        self.server_install_path = appium_server_apth
        self.server_path = '0.0.0.0'

    # 启动appium server服务
    def start_appium_server(self, port=4723, bport=4724):
        appium_logs_dir = os.path.dirname(__file__)
        print(appium_logs_dir)
        appium_log_path = os.path.join(appium_logs_dir, "appium_server_{0}.log".format(port))
        print(appium_log_path)
        command = "node {0} -a {1} -p {2} -bp {3} -g {4} " \
                  "--session-override " \
                  "--local-timezone " \
                  "--log-timestamp & ".format(self.server_install_path, self.server_path, port, bport, appium_log_path)
        print(command)
        subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
        print('appium server已启动')

    # 关闭appium服务
    @classmethod
    def stop_appium(cls, pc, port_num=4723):
        '''关闭appium服务'''
        print('stop函数')
        if pc.upper() == 'WIN':
            print('进入WIN')
            p = os.popen(f'netstat  -aon|findstr {port_num}')
            p0 = p.read().strip()
            if p0 != '' and 'LISTENING' in p0:
                p1 = int(p0.split('LISTENING')[1].strip()[0:4])  # 获取进程号
                os.popen(f'taskkill /F /PID {p1}')  # 结束进程
                print('taskkill /F /PID {p1}')
                print('appium server已结束')
        elif pc.upper() == 'MAC':
            p = os.popen(f'lsof -i tcp:{port_num}')
            p0 = p.read()
            if p0.strip() != '':
                p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
                os.popen(f'kill {p1}')  # 结束进程
                print('appium server已结束')


if __name__ == '__main__':
    # path = 'C:\\Users\\stacy\\AppData\\Local\\Programs\\Appium'
    path = 'C:\\Users\\stacy\\AppData\\Roaming\\npm\\node_modules\\appium\\build\\lib\\main.js'
    m = ManageAppiumServer(path)
    m.start_appium_server()
    print('to next')
    m.stop_appium('WIN')
