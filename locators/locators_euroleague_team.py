import os
from xml.etree.ElementPath import xpath_tokenizer

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.euroleaguebasketball.net/ru/euroleague/teams/'

        super().__init__(web_driver, url)

    #Начало теста
    btn_cookies_accept = WebElement(xpath='//*[@id="onetrust-accept-btn-handler"]')
    btn_euroleaguer = WebElement(xpath='(//a[@href="/ru/euroleague/"])[2]')
    btn_team = WebElement(xpath='((//*[@id="__next"]//nav)[2]//a)[4]')

    #Проверка колличества
    many_teams = ManyWebElements(xpath='//span[@class="teams-card_name__UR_gA"]')

    #Проверка команд
    btn_tean_alba = WebElement(xpath='(//a[@href="/ru/euroleague/teams/alba-berlin/roster/ber/?season=2024-25"])[3]')
    btn_team_efes = WebElement(xpath='(//a[@href="/ru/euroleague/teams/anadolu-efes-istanbul/roster/ist/?season=2024-25"])[3]')
    btn_team_monaco = WebElement(xpath='(//a[@href="/ru/euroleague/teams/as-monaco/roster/mco/?season=2024-25"])[3]')
    btn_team_baskonia = WebElement(xpath='//a[@href="/ru/euroleague/teams/baskonia-vitoria-gasteiz/roster/bas/?season=2024-25"]')
    btn_team_zvezda = WebElement(xpath='(//a[@href="/ru/euroleague/teams/crvena-zvezda-meridianbet-belgrade/roster/red/?season=2024-25"])[3]')
    btn_team_milan = WebElement(xpath='(//a[@href="/ru/euroleague/teams/ea7-emporio-armani-milan/roster/mil/?season=2024-25"])[3]')
    btn_team_barca = WebElement(xpath='(//a[@href="/ru/euroleague/teams/fc-barcelona/roster/bar/?season=2024-25"])[3]')
    btn_team_munchen = WebElement(xpath='(//a[@href="/ru/euroleague/teams/fc-bayern-munich/roster/mun/?season=2024-25"])[3]')
    btn_team_fenerbahce = WebElement(xpath='(//a[@href="/ru/euroleague/teams/fenerbahce-beko-istanbul/roster/ulk/?season=2024-25"])[3]')
    btn_team_asvel = WebElement(xpath='(//a[@href="/ru/euroleague/teams/ldlc-asvel-villeurbanne/roster/asv/?season=2024-25"])[3]')
    btn_team_maccabi = WebElement(xpath='(//a[@href="/ru/euroleague/teams/maccabi-playtika-tel-aviv/roster/tel/?season=2024-25"])[3]')
    btn_team_olimp = WebElement(xpath='(//a[@href="/ru/euroleague/teams/olympiacos-piraeus/roster/oly/?season=2024-25"])[3]')
    btn_team_panathinaikos = WebElement(xpath='//a[@href="/ru/euroleague/teams/panathinaikos-aktor-athens/roster/pan/?season=2024-25"]')
    btn_team_partizan = WebElement(xpath='//a[@href="/ru/euroleague/teams/partizan-mozzart-bet-belgrade/roster/par/?season=2024-25"]')
    btn_team_paris = WebElement(xpath='(//a[@href="/ru/euroleague/teams/paris-basketball/roster/prs/?season=2024-25"])[3]')
    btn_team_madrid = WebElement(xpath='(//a[@href="/ru/euroleague/teams/real-madrid/roster/mad/?season=2024-25"])[3]')
    btn_team_bologna = WebElement(xpath='(//a[@href="/ru/euroleague/teams/virtus-segafredo-bologna/roster/vir/?season=2024-25"])[3]')
    btn_team_kaunas = WebElement(xpath='(//a[@href="/ru/euroleague/teams/zalgiris-kaunas/roster/zal/?season=2024-25"])[3]')

