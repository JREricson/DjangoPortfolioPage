import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")  # look up function vs model
def chrome_browser_instance(request):
    """Provides a selenium webdriver instance

    Args:
        request ([type]): [description]
    """
    # used service to handle depreciation warning in orig video- https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
    options = Options()
    options.headless = False
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s, options=options)
    yield browser
    browser.close()
