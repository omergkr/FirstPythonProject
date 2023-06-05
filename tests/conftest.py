import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# @pytest.fixture(params=["chrome", "firefox", "edge"])
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"Creating {browser} driver...")

    if browser == "chrome":
        my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        my_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome', 'firefox' or 'edge', but got {browser}")
    # my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver...")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome, firefox or edge)"
    )
