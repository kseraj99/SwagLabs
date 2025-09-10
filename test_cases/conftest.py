import oracledb
import pytest
from pytest_metadata.plugin import metadata, metadata_key
from selenium import webdriver
from selenium.webdriver.edge.service import Service

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

driver_path = 'D:/PycharmProjects/msedgedriver.exe'
# Provide the path to the EdgeDriver executable
edge_service = Service(executable_path=driver_path)


## This is the standard function to get the browser here.
## Browser name is depend on our input what we are giving

def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "chrome",
                     help = "specify which browser to use:")


## To create the browser fixture.(this is the standard)
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

## we have to parameterize the setup for any browser

@pytest.fixture()
def setup(browser):
    global driver

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge(service=edge_service)
## If we will pass wrong driver value, for this using else condition
    else:
## It will through the value error what we are giving in the quote
        raise ValueError("Unknown browser type")
    return driver


### For pytest html report--
### hook for adding environment info in html report.
#
# def pytest_configure(config):
#     config.stash[metadata_key]['Project Name'] = 'Swag Labs'
#     config.stash[metadata_key]['Test Module Name'] = 'Admin Login Test'
#     config.stash[metadata_key]['Tester'] = 'Seraj Khan'
#
#
# ## hook for delete/modify environment info in html report
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('Packaged', None)
#     metadata.pop('Plugins', None)


import os, sys, pytest, contextlib

@contextlib.contextmanager
def suppress_stderr():
    with open(os.devnull, "w") as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stderr = old_stderr

@pytest.fixture(autouse=True, scope="session")
def silence_tflite_logs():
    with suppress_stderr():
        yield


@pytest.fixture(scope="module")
def db_connection():
    oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_23_8")
    dsn = oracledb.makedsn("localhost", 1521, sid="xe")
    conn = oracledb.connect(
        user="system",
        password="system",
        dsn=dsn
    )
    yield conn
    conn.close()
