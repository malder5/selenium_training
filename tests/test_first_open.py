import pytest
import time
from fixture.application import Application
from selenium import webdriver


def test_first_open(app):
    app.session.open_home_page()
    time.sleep(2)
    assert app.driver.find_element_by_id('header').is_displayed() == True

def test_open_admin(app):
    app.session.open_home_page()

