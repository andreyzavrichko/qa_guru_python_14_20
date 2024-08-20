from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search():
    with step('First onboarding page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('The Free Encyclopedia\n…in over 300 languages'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Second onboarding page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('New ways to explore'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Third onboarding page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Reading lists with sync'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Fourth onboarding page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Data & Privacy'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()

    with (step('Type search')):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('BrowserStack')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
