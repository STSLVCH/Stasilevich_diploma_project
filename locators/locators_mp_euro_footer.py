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

    btn_cookies_accept = WebElement(xpath='//*[@id="onetrust-accept-btn-handler"]')

    # Кнопки Euroleague Basketball
    btn_main_league_footer = WebElement(xpath='(//*[@role="heading"])[3]')#
    btn_about_site_footer = WebElement(xpath='//a[text()="О сайте"]')
    btn_contact_footer = WebElement(xpath='//a[text()="Контакты"]')
    btn_vocation_footer = WebElement(xpath='//a[text()="Вакансии"]')
    btn_press_footer = WebElement(xpath='//a[@rel="noreferrer" and contains(text(),"Пресс-центр")]')
    btn_market_footer = WebElement(xpath='//a[text()="Маркетинговые партнеры"]')
    btn_brand_footer = WebElement(xpath='//a[text()="Бренд-центр"]')
    btn_kodex_footer = WebElement(xpath='//a[text()="Кодекс поведения"]')


    #Кнопки Turkish Airlines

    btn_main_turkish_footer = WebElement(xpath='(//*[@role="heading"])[4]')#
    btn_formatone_footer = WebElement(xpath='//a[@class="footer-nav-section_navLink__kJd_f" '
                                         'and contains(text(),"Формат")][1]')
    btn_mediapartner_footer = WebElement(xpath='//a[text()="Медиапартнеры"]')
    btn_charter_footer = WebElement(xpath='//a[text()="Устав"][1]')
    btn_fantasy_first_footer = WebElement(xpath='//a[text()="Fantasy Challenge"][1]')
    btn_efa_footer = WebElement(xpath='//a[text()="EFA"]')

    #Кнопки Eurocup
    btn_main_eurocup_footer = WebElement(xpath='(//*[@role="heading"])[5]')  #
    btn_formattwo_footer = WebElement(xpath='//a[@href="/eurocup/format-ec/"]')
    btn_chartettwo_footer = WebElement(xpath='//a[@href="https://ftpserver.euroleague.net/general'
                                             '/2024_25EuroCupBylaws.pdf"]')
    btn_fantasy_two_footer = WebElement(xpath='//a[@href="https://eurocupfantasy.euroleaguebasketball.net/en/home"]')


    #Кнопки other
    btn_main_other_footer = WebElement(xpath='(//*[@role="heading"])[6]')  #
    btn_eurotv_footer = WebElement(xpath='//a[text()="EuroLeague TV"]')
    btn_mobile_footer = WebElement(xpath='//a[text()="Мобильное приложение"]')
    btn_euroshop_footer = WebElement(xpath='//a[text()="EuroLeague Магазин"]')
    btn_cornerfan_footer = WebElement(xpath='//a[text()="Уголок болельщика"]')

    #Нижний футер social
    btn_politics_cookies_footer = WebElement(xpath='//a[@href="/cookie-policy-ev/"]')
    btn_cofedenc_footer = WebElement(xpath='//a[@href="/privacy-policy-ev/"]')
    btn_youtube_footer = WebElement(xpath='//a[@href="https://www.youtube.com/euroleague"]')
    btn_facebook_footer = WebElement(xpath='//a[@href="https://www.facebook.com/TheEuroleague"]')
    btn_x_footer = WebElement(xpath='//a[@href="https://twitter.com/Euroleague"]')
    btn_instagram_footer = WebElement(xpath='//a[@href="https://instagram.com/euroleague"]')
    btn_tick_tok_footer = WebElement(xpath='//a[@href="https://www.tiktok.com/@euroleague"]')
    btn_whats_up_footer = WebElement(xpath='//a[@href="https://whatsapp.com/channel/0029Va9Jmb3Ae5VkBsSAUs17"]')

    #Языки футер
    btn_language_footer = WebElement(xpath='(//button[@class="language-dropdown_buttonWrapper__KEl3I"])[3]')
    btn_deutsch_footer = WebElement(xpath='(//*[@aria-roledescription="footer"]//button)[2]')
    btn_greece_footer = WebElement(xpath='(//*[@aria-roledescription="footer"]//button)[3]')
    btn_english_footer = WebElement(xpath='(//*[@aria-roledescription="footer"]//button)[4]')
    btn_spain_footer = WebElement(xpath='(//*[@aria-roledescription="footer"]//button)[5]')
    btn_france_footer = WebElement(xpath='(//*[@aria-roledescription="footer"]//button)[6]')
    btn_italia_footer = WebElement(xpath='(//*[@aria-roledescription="footer"]//button)[7]')
    btn_litva_footer = WebElement(xpath='(//*[@aria-roledescription="footer"]//button)[8]')
    btn_serbska_footer = WebElement(xpath='(//*[@aria-roledescription="footer"]//button)[9]')
    btn_turkish_footer = WebElement(xpath='(//*[@aria-roledescription="footer"]//button)[10]')

    #Локатор для проверки колличества
    btn_a_test = ManyWebElements(xpath='//a[@class="footer-nav-section_navLink__kJd_f"]')




