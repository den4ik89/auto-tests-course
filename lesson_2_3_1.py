#Задание: принимаем alert
#В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

from selenium import webdriver
import math


link = "http://suninjuly.github.io/alert_accept.html"

#Открыть страницу
browser = webdriver.Chrome()
browser.get(link)

#Нажать на кнопку
browser.find_element_by_class_name("btn-primary").click()

#Принять confirm
confirm = browser.switch_to.alert
confirm.accept()

#На новой странице решить капчу для роботов, чтобы получить число с ответом
number = browser.find_element_by_id('input_value')
x = int(number.text)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)

input1 = browser.find_element_by_class_name('form-control')
input1.send_keys(y)

browser.find_element_by_class_name("btn-primary").click()
