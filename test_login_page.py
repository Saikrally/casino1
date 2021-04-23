link = "https://finnplay:password@www.tempspins.pw/"


def test_open_login_page(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    login_button = browser.find_element_by_class_name("btn hoverable cta-primary size-primary uppercase bold flex")
    assert login_button.is_displayed(), "Login button isn't displayed"
