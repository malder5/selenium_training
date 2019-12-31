from selenium import webdriver
import time


def main():
    url = 'http://localhost/litecart'
    driver = webdriver.Chrome()
    driver.get(url)
    assert url in driver.current_url

    driver.close()

if __name__ == '__main__':
    main()