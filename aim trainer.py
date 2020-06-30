import pyautogui
import time
from PIL import ImageGrab
from selenium import webdriver


def click_target():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://humanbenchmark.com/tests/aim")
    time.sleep(3)


def click():
    target = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[4]/div[1]/div/div[2]/div/div/div[6]")
    target.click()


click_target()
i = 0
while i < 31:
    click()
    i += 1
