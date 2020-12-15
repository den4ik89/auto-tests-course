#Задание: переход на новую вкладку
#В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.
from selenium import webdriver
import math

link = "http://suninjuly.github.io/redirect_accept.html"

#Открыть страницу
browser = webdriver.Chrome()
browser.get(link)

#Нажать на кнопку
browser.find_element_by_class_name("btn-primary").click()

#Переключиться на новую вкладку
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

#Пройти капчу для робота и получить число-ответ
number = browser.find_element_by_id('input_value')
x = int(number.text)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)

input1 = browser.find_element_by_class_name('form-control')
input1.send_keys(y)

browser.find_element_by_class_name("btn-primary").click()
