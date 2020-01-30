from selenium import webdriver
import time
import pytest


def main():
    url = 'http://localhost/litecart/admin/'
    driver = webdriver.Chrome(executable_path=r'C:\Users\Roman\Downloads\chromedriver.exe')
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    time.sleep(1)
    # assert 'http://localhost/litecart/admin/' in driver.current_url
    driver.close()

if __name__ == '__main__':
    main()