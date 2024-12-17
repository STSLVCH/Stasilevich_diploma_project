import time

import allure
import pytest_check as check
from locators.locators_mp_euro_header import MainPage
from conftest import web_browser
@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')

def test_main_pages(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    elements = [(page.btn_career_header, "Карьера...", "https://www.euroleaguebasketball.net/ru/about-ru/"),
                (page.btn_news_header, "Новости", "https://www.euroleaguebasketball.net/ru/news/"),
                (page.btn_ebinstitute_header, "EB INSTITUTE", "https://www.euroleaguebasketball.net/ru/ebinstitute"),
                (page.btn_logo_oneteam_header, "ONE TEAM", "https://www.euroleaguebasketball.net/ru/one-team"),
                (page.btn_logo_euroleage_header, "EUROLEAGUE BASKETBALL", "https://www.euroleaguebasketball.net/ru/")
                ]
    for element, text_element, url_element in elements:

        with allure.step('Тест проверки отображения на экране'):
            check.is_true(element.is_visible())

        with allure.step('Тест проверки кликабельности'):
            check.is_true((element.is_clickable()))

        with allure.step('Проверка на орфографию'):
            check.equal(element.get_text(),text_element)

        with allure.step('Проверка на корректный адрес кнопки'):
            check.equal(element.get_attribute('href'),url_element)




def test_main_pages_languages(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    page.btn_language_header.click()
    languages = [(page.btn_deutsch_header, 'Deutsch'),
                 (page.btn_greece_header, 'Ελληνικά'),
                 (page.btn_english_header, 'English'),
                 (page.btn_spain_header, 'Español'),
                 (page.btn_france_header, 'Français'),
                 (page.btn_italy_header, 'Italiano'),
                 (page.btn_lituania_header, 'Lietuviškai'),
                 (page.btn_serbiga_header, 'Srpski'),
                 (page.btn_turky_header, 'Türkçe')
                 ]

    for language, text_language in languages:

        with allure.step('Проверка на видимость языков'):
            check.is_true(language.is_visible())

        with allure.step('Проверка на кликабельность'):
            check.is_true(language.is_clickable())


        with allure.step('Проверка на орфографию'):
            check.equal(language.get_text(),text_language)




def test_main_pages_logo(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    logos = [(page.btn_euroliga_header, "https://www.euroleaguebasketball.net/ru/"),
             (page.btn_logo_nextgen_header, "https://www.euroleaguebasketball.net/ru/ngt/"),
             (page.btn_logo_cup_header, "https://www.euroleaguebasketball.net/ru/eurocup/"),
             (page.btn_logo_euro_header, "https://www.euroleaguebasketball.net/ru/euroleague/"),
             ]

    for logo, logo_url in logos:

        with allure.step('Проверка на видимость языков'):
            check.is_true(logo.is_visible())

        with allure.step('Проверка на кликабельность'):
            check.is_true(logo.is_clickable())

        with allure.step('Проверка на корректный адрес кнопки'):
            check.equal(logo.get_attribute('href'),logo_url)

def test_main_page_income(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    check.is_true(page.btn_main_page_income.is_visible())
    check.is_true(page.btn_main_page_income.is_clickable())