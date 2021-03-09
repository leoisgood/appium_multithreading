import pytest
import time
from appium import webdriver

driver = None


# @pytest.fixture(scope="package")
# def cmdopt(request):
#     return request.config.getoption("--cmdopt")


# def pytest_addoption(parser):
#     parser.addoption(
#         "--cmdopt", action="store", default="{platformName:'Android',platformVersion:'7.1.1'}",
#         help="my devices info"
#     )


@pytest.fixture()
def start_app(android_setting_dict):
    # device = eval(cmdopt)
    # print("开始与设备 {} 进行会话，并执行测试用例 ！！".format(device["caps"]["deviceName"]))
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', android_setting_dict)
    return driver
#
#
# @pytest.fixture(params=[('18217116148@126.com', 'lz123456')])
# def params_setting_list(request):
#     return request.param









@pytest.fixture()
def tear_down():
    yield driver
    time.sleep(2)
    # driver.close()
    driver.close_app()
