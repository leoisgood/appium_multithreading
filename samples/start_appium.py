import pytest
from appium import webdriver


def start_appium():  # TODO(Leo. @italki.com): start appium
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
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
    return driver


if __name__ == '__main__':
    driver = start_appium()
    # driver.start_client()
    pytest.main(['-s', '-v'])
