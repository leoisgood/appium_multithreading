import pytest
import allure


@allure.epic('italki安卓版')
@allure.feature('italki V3.29 stage')
class TestAdd:
    @allure.story('登出操作')
    @allure.title('[case01] 验证app能否正常登录登出')
    def test_logout(self, set_up, tear_down):
        with allure.step('1、启动italki'):
            driver = set_up
            driver.implicitly_wait(5)
        with allure.step('2、登陆操作'):
            driver.find_element_by_xpath(
                '//android.widget.TextView[@resource-id="com.italki.app:id/tv_have_account"]').click()
            driver.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="电子邮箱"]').click()
            driver.find_element_by_xpath(
                '//android.widget.EditText[@resource-id="com.italki.app:id/et_email"]').send_keys('1178472868@qq.com')
            # driver.find_element_by_xpath('//android.widget.EditText[@resource-id="com.italki.app:id/et_email"]').send_keys(params_setting_list[0])
            driver.find_element_by_xpath(
                '//android.widget.EditText[@resource-id="com.italki.app:id/et_pwd"]').send_keys('Lz123456')
            driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.italki.app:id/btn_submit"]').click()
            actual_result = driver.find_element_by_xpath('//android.widget.TextView[starts-with(@text,"你好")]').text
        with allure.step('3、点击我的页面'):
            driver.find_element_by_xpath(
                '//android.widget.FrameLayout[@resource-id="com.italki.app:id/bottom_item4"]').click()
        with allure.step('4、点击设置'):
            driver.find_element_by_xpath(
                '//android.widget.ImageView[@resource-id="com.italki.app:id/iv_settings"]').click()
        with allure.step('5、点击退出'):
            driver.find_element_by_xpath(
                '//android.widget.TextView[@resource-id="com.italki.app:id/tv_log_out"]').click()
        with allure.step('6、验证是否登出成功'):
            actual_result = driver.find_element_by_xpath('//android.widget.TextView['
                                                         '@resource-id="com.italki.app:id/tv_have_account"]').text
            assert actual_result == '已是会员？ 登录'
        with allure.step('7、关闭italki'):
            driver = tear_down


if __name__ == '__main__':
    pytest.main(['-s'])
