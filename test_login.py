from selenium import webdriver
import time
import pytest


def main():
    url = 'http://localhost/litecart'
    driver = webdriver.Chrome(executable_path=r'C:\Users\Roman\Downloads\chromedriver.exe')
    driver.get(url)

    assert url in driver.current_url

    driver.close()

if __name__ == '__main__':
    main()