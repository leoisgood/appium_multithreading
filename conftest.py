import pytest
from appium import webdriver


@pytest.fixture(scope='package', name='android_setting_dict')
def android_setting():
    # des = {
    #     "platformName": "android",
    #     "platformVersion": "7.1.2",
    #     "deviceName": "Samsung Galaxy S8",
    #     "appPackage": "com.sky.jisuanji",
    #     "appActivity": ".JisuanjizixieActivity",
    #     "udid": "127.0.0.1:62001",
    #     "noReset": True,
    #     "unicodeKeyboard": True,
    #     "resetKeyboard": True,
    # }
    des = {
        "platformName": "android",
        "platformVersion": "7.1.2",
        "deviceName": "Samsung Galaxy S8",
        "appPackage": "com.italki.app",
        "appActivity": "com.italki.app.onboarding.welcome.GetStartedActivity",
        "udid": "127.0.0.1:62001",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True,
    }
    return des
