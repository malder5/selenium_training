import pytest
from fixture.application import Application
fixture = None

@pytest.fixture
def app(request):
    global fixture

    # browser = request.config.getoption('--browser')

    if fixture is None or fixture.is_valid():
        fixture = Application()
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

# def pytest_addoption(parser):
#     parser.addoption('--browser', action='store', default = 'chrome')
    # parser.addoption('--headless', action='store', default = False)