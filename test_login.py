from selenium import webdriver
import time


def main():
    url = 'http://localhost/litecart'
    driver = webdriver.Chrome()
    driver.get(url)

if __name__ == '__main__':
    main()