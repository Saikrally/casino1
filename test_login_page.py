link = "https://finnplay:password@www.tempspins.pw/"


def test_open_login_page(browser):
    browser.get(link)
    browser.maximize_window()
    browser.implicitly_wait(5)
    login_button = browser.find_element_by_css_selector("body > app-root > app-common-layout > mat-sidenav-container "
                                                        "> mat-sidenav > div.mat-drawer-inner-container.ng-tns-c94-0 "
                                                        "> app-sidebar-content > div > app-desk-head-sidebar > div > "
                                                        "div.logged-out-content.flex-content-c.ng-tns-c104-17.ng-star"
                                                        "-inserted > div > app-button.login-btn.ng-tns-c104-17 > span")
    assert login_button.is_displayed(), "Login button isn't displayed"
