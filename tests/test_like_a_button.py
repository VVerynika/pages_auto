from pages.like_a_button import LikeAButton
import allure


@allure.feature('Like a button')
@allure.story('Existence')
def test_button2_exist(browser):
    like_a_button = LikeAButton(browser)
    like_a_button.open()
    assert like_a_button.button_is_displayed


@allure.feature('Like a button')
@allure.story('Clickability')
def test_button2_clicked(browser):
    like_a_button = LikeAButton(browser)
    like_a_button.open()
    like_a_button.click_button()
    with allure.step('Check result text'):
        assert 'Submitted' == like_a_button.result_text
