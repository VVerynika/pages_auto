from pages.simple_button import SimpleButton
import allure


@allure.feature('Simple button')
@allure.story('Existence')
def test_button1_exist(browser):
    with allure.step('Open Simple button page'):
        simple_button = SimpleButton(browser)
        simple_button.open()
    with allure.step('Check the button'):
        assert simple_button.button_is_displayed


@allure.feature('Simple button')
@allure.story('Clickability')
def test_button1_clicked(browser):
    with allure.step('Open Simple button page'):
        simple_button = SimpleButton(browser)
        simple_button.open()
    with allure.step('Click the button'):
        simple_button.click_button()
    with allure.step('Check result text'):
        assert 'Submitted' == simple_button.result_text
