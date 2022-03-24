import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--maximized', action='store_true', help='Maximized browser windows')
    parser.addoption('--headless', action='store_true', help='Run headless')
    parser.addoption('--browser', action='store', default='chrome', choices=['chrome', 'firefox', 'opera'])
    parser.addoption('--url', action='store', default='http://demo-opencart.ru/')


@pytest.fixture
def url(request):
    url = request.config.getoption('--url')
    return url


@pytest.fixture
def browser(request):
    _browser = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    maximized = request.config.getoption('--maximized')

    driver = None

    if _browser == 'chrome':
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)

    elif _browser == 'firefox':
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(5)

    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver



