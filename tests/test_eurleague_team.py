import time
import random
import allure
import string
import pytest_check as check
from locators.locators_euroleague_team import MainPage
from conftest import web_browser


@allure.story('Тест страницы "Команды')
@allure.feature('Тест страницы "Команды"')
def test_count_teams(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    check.equal(18, page.many_teams.count(), "Колличество не совпадает")

def test_team_all(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    teams = [(page.btn_tean_alba, "ALBA Berlin",
              "https://www.euroleaguebasketball.net/ru/euroleague/teams/alba-berlin/roster/ber/?season=2024-25"),
             (page.btn_team_efes, "Anadolu Efes Istanbul",
              "https://www.euroleaguebasketball.net/ru/euroleague/teams/anadolu-efes-istanbul/roster/ist/?season=2024-25"),
             (page.btn_team_monaco, "AS Monaco",
              "https://www.euroleaguebasketball.net/ru/euroleague/teams/as-monaco/roster/mco/?season=2024-25"),
             (page.btn_team_baskonia, "Baskonia Vitoria-Gasteiz",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/baskonia-vitoria-gasteiz/roster/bas/?season=2024-25"),
             (page.btn_team_zvezda, "Crvena Zvezda Meridianbet Belgrade",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/crvena-zvezda-meridianbet-belgrade/roster/red/?season=2024-25"),
             (page.btn_team_milan, "EA7 Emporio Armani Milan",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/ea7-emporio-armani-milan/roster/mil/?season=2024-25"),
             (page.btn_team_barca, "FC Barcelona",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/fc-barcelona/roster/bar/?season=2024-25"),
             (page.btn_team_munchen, "FC Bayern Munich",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/fc-bayern-munich/roster/mun/?season=2024-25"),
             (page.btn_team_fenerbahce, "Fenerbahce Beko Istanbul",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/fenerbahce-beko-istanbul/roster/ulk/?season=2024-25"),
             (page.btn_team_asvel, "LDLC ASVEL Villeurbanne",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/ldlc-asvel-villeurbanne/roster/asv/?season=2024-25"),
             (page.btn_team_maccabi, "Maccabi Playtika Tel Aviv",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/maccabi-playtika-tel-aviv/roster/tel/?season=2024-25"),
             (page.btn_team_olimp, "Olympiacos Piraeus",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/olympiacos-piraeus/roster/oly/?season=2024-25"),
             (page.btn_team_panathinaikos, "Panathinaikos AKTOR Athens",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/panathinaikos-aktor-athens/roster/pan/?season=2024-25"),
             (page.btn_team_partizan, "Partizan Mozzart Bet Belgrade",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/partizan-mozzart-bet-belgrade/roster/par/?season=2024-25"),
             (page.btn_team_paris, "Paris Basketball",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/paris-basketball/roster/prs/?season=2024-25"),
             (page.btn_team_madrid, "Real Madrid",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/real-madrid/roster/mad/?season=2024-25"),
             (page.btn_team_bologna, "Virtus Segafredo Bologna",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/virtus-segafredo-bologna/roster/vir/?season=2024-25"),
             (page.btn_team_kaunas, "Zalgiris Kaunas",
             "https://www.euroleaguebasketball.net/ru/euroleague/teams/zalgiris-kaunas/roster/zal/?season=2024-25")
             ]
    for team, text_team, url_team in teams:
        with allure.step('Тест проверки отображения на экране'):
            check.is_true(team.is_visible())

        with allure.step('Тест проверки кликабельности'):
            check.is_true(team.is_clickable())

        with allure.step('Проверка на орфографию'):
            check.equal(team.get_text(),text_team)

        with allure.step('Проверка на корректный адрес кнопки'):
            check.equal(team.get_attribute('href'),url_team)

        with allure.step('Проверка на корректный адрес кнопки'):
            team.click()
            check.equal(page.get_current_url(), url_team)
