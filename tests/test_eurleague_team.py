import time
import random
import allure
import string

import pytest
import pytest_check as check
from locators.locators_euroleague_team import MainPage
from conftest import web_browser
from data.constanta import ConstantaUrlMainPage


@allure.story('Тест страницы "Команды')
@allure.feature('Тест страницы "Команды"')
def test_count_teams(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    check.equal(18, page.many_teams.count(), "Колличество не совпадает")


def test_team_all(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    teams = [(page.btn_tean_alba, "ALBA Berlin", ConstantaUrlMainPage.url_tean_alba),
             (page.btn_team_efes, "Anadolu Efes Istanbul", ConstantaUrlMainPage.url_team_efes),
             (page.btn_team_monaco, "AS Monaco", ConstantaUrlMainPage.url_team_monaco),
             (page.btn_team_baskonia, "Baskonia Vitoria-Gasteiz", ConstantaUrlMainPage.url_team_baskonia),
             (page.btn_team_zvezda, "Crvena Zvezda Meridianbet Belgrade", ConstantaUrlMainPage.url_team_zvezda),
             (page.btn_team_milan, "EA7 Emporio Armani Milan", ConstantaUrlMainPage.url_team_milan),
             (page.btn_team_barca, "FC Barcelona", ConstantaUrlMainPage.url_team_barca),
             (page.btn_team_munchen, "FC Bayern Munich", ConstantaUrlMainPage.url_team_munchen),
             (page.btn_team_fenerbahce, "Fenerbahce Beko Istanbul", ConstantaUrlMainPage.url_team_fenerbahce),
             (page.btn_team_asvel, "LDLC ASVEL Villeurbanne", ConstantaUrlMainPage.url_team_asvel),
             (page.btn_team_maccabi, "Maccabi Playtika Tel Aviv", ConstantaUrlMainPage.url_team_maccabi),
             (page.btn_team_olimp, "Olympiacos Piraeus", ConstantaUrlMainPage.url_team_olimp),
             (page.btn_team_panathinaikos, "Panathinaikos AKTOR Athens", ConstantaUrlMainPage.url_team_panathinaikos),
             (page.btn_team_partizan, "Partizan Mozzart Bet Belgrade", ConstantaUrlMainPage.url_team_partizan),
             (page.btn_team_paris, "Paris Basketball", ConstantaUrlMainPage.url_team_paris),
             (page.btn_team_madrid, "Real Madrid", ConstantaUrlMainPage.url_team_madrid),
             (page.btn_team_bologna, "Virtus Segafredo Bologna", ConstantaUrlMainPage.url_team_bologna),
             (page.btn_team_kaunas, "Zalgiris Kaunas", ConstantaUrlMainPage.url_team_kaunas)
             ]
    for team, text_team, url_team in teams:
        with allure.step(f'Тест проверки отображения на экране кнопки {text_team}'):
            check.is_true(team.is_visible())

        with allure.step(f'Тест проверки кликабельности кнопки {text_team}'):
            check.is_true(team.is_clickable())

        with allure.step(f'Проверка на орфографию "{text_team}"'):
            check.equal(team.get_text(), text_team)

        with allure.step(f'Проверка на корректный адрес кнопки {text_team}'):
            check.equal(team.get_attribute('href'), url_team)
            team.click(1)
            if page.wait_page_loaded():
                check.equal(page.get_current_url(), url_team)
            else:
                "Сам допиши че надо сюда написать"
            page.go_back()
