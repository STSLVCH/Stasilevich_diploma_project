import time
import random
import allure
import string
import pytest_check as check
from locators.locators_registration_page import MainPage
from conftest import web_browser


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_text_registration_page(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    page.btn_income.click()
    page.btn_registr.click()

    words = [(page.text_first_name, "Имя"),
             (page.text_last_name, "Фамилия"),
             (page.text_income, "Войти"),
             (page.text_email, "Электронная почта"),
             (page.text_password, "Пароль"),
             (page.text_confirm_password, "Подтверждение пароля"),
             (page.text_create_acc, "Создать аккаунт")
            ]



    for word, text_word in words:

        with allure.step('Тест проверки отображения на экране'):
            check.is_true(word.is_visible())

        with allure.step('Проверка на орфографию'):
            check.equal(word.get_text(),text_word)



def test_form_registration(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    page.btn_income.click()
    page.btn_registr.click()

    def random_char(char_num):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))


    #Заполняем имя
    name = "Nikita"
    page.field_first_name.send_keys(name)
    #Заполняем фамилию
    page.field_last_name.send_keys("Stasilevich")
    #Заполняем mail
    email = (random_char(7) + '@gmail.com')
    email_final = email
    page.field_email.send_keys(email_final)
    #Заполняем пароль
    password = "StasilevichYaYa21$"
    page.field_password.send_keys(password)
    #Заполняем подтверждение пароль
    page.field_conf_password.send_keys(password)
    # Нажимаем да
    page.btn_yes.click()
    # Ставим галочку
    page.btn_politics.click()
    # Нажимаем создать аккаунт
    page.create_accaunt.click()
    # Выбираем страну Беларусь
    page.btn_country.click()
    page.btn_belarus.click()
    # Вводим город Минск
    page.btn_town.send_keys("Minsk")
    #Переходим на след страницу
    page.btn_next.click()
    # Закрывает регистрацию
    page.btn_finish.click()
    with allure.step("Проверка на успешную регистрацию"):
        check.is_true(page.field_vision.is_visible())
    time.sleep(2)
    page.btn_back_euro.click()
    with allure.step("Проверка что учетная забись создана"):
        check.equal(name, name, "Не совпадает")

    page.btn_explore.click()
    page.btn_income_after_registr.click()
    page.btn_exit_from_acc.click()
    page.btn_income_after_exit.click()
    page.field_income_email.send_keys(email)
    page.field_income_email.send_keys(email_final)
    page.field_income_password.send_keys(password)
    page.btn_login_income.click()
    time.sleep(2)
    with allure.step("Проверка на успешный вход после регистрации"):
        check.is_true(page.text_check_income.is_visible())