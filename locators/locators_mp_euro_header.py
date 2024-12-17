import os
from xml.etree.ElementPath import xpath_tokenizer

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.euroleaguebasketball.net/ru/'

        super().__init__(web_driver, url)

    #Языки
    btn_language_header = WebElement(xpath='(//*[@type="button"])[15]')
    btn_cookies_accept = WebElement(xpath='//button[contains(text(),"Accept All Cookies")]')
    btn_english_header = WebElement(xpath='(//*[@type="button"])[18]')
    btn_deutsch_header = WebElement(xpath='(//*[@type="button"])[16]')
    btn_greece_header = WebElement(xpath='(//*[@type="button"])[17]')
    btn_spain_header = WebElement(xpath='(//*[@type="button"])[19]')
    btn_france_header = WebElement(xpath='(//*[@type="button"])[20]')
    btn_italy_header = WebElement(xpath='(//*[@type="button"])[21]')
    btn_lituania_header = WebElement(xpath='(//*[@type="button"])[22]')
    btn_serbiga_header = WebElement(xpath='(//*[@type="button"])[23]')
    btn_turky_header = WebElement(xpath='(//*[@type="button"])[24]')

    #Остальное
    btn_career_header = WebElement(xpath='(//a[@href="/ru/about-ru/"])[3]')
    btn_news_header = WebElement(xpath=' (//a[@href="/ru/news/"])[3]')
    btn_ebinstitute_header = WebElement(xpath='(//a[text()="eb institute"])[2]')
    btn_logo_oneteam_header = WebElement(xpath='(//a[text()="one team"])[2]')
    btn_logo_euroleage_header = WebElement(xpath='(//*[@id="__next"]//a)[18]')

    #Лого
    btn_euroliga_header = WebElement(xpath='(//a[@class="logo_logoLink__KaqlO"])[3] ')
    btn_logo_nextgen_header = WebElement(xpath='(//a[@href="/ru/ngt/"])[2]')
    btn_logo_cup_header = WebElement(xpath='(//a[@href="/ru/eurocup/"])[2]')
    btn_logo_euro_header = WebElement(xpath='(//a[@href="/ru/euroleague/"])[2]')
    btn_main_page_income = WebElement(xpath='(//*[@type="button"])[14]')