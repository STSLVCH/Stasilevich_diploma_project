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


    #About me
    first_name = WebElement(xpath='//input[@id="signup_firstName"]')
    second_name = WebElement(xpath='//input[@id="signup_lastName"]')
    date_birthday = WebElement(xpath='//input[@id="signup_birthDate"]')

    # Living place
    country_living = WebElement(xpath='//*[@aria-haspopup="dialog"]')
    town_living = WebElement(xpath='//input[@id="signup_town"]')
    favorit_team = WebElement(xpath='//input[@id="signup_chtmc"]')
    registr_euroliga = WebElement(xpath='//*[contains(text(),"Select Competition EuroLeague")]')
    registr_eurocup = WebElement(xpath='//*[contains(text(),"Select Competition EuroCup")]')

    #Euroliga team
    team_monaco = WebElement(xpath='//span[contains(text(),"AS Monaco")]')
    team_efes = WebElement(xpath='//span[contains(text(),"Anadolu Efes Istanbul")]')
    team_crevna = WebElement(xpath='//span[contains(text(),"Crvena Zvezda Meridianbet Belgrade")]')
    team_barca = WebElement(xpath='//span[contains(text(),"FC Barcelona")]')
    team_fener = WebElement(xpath='//span[contains(text(),"Fenerbahce Beko Istanbul")]')
    team_maccabi = WebElement(xpath='//span[contains(text(),"Maccabi Playtika Tel Aviv")]')
    team_panatin = WebElement(xpath='//span[contains(text(),"Panathinaikos Aktor Athens")]')
    team_partizan = WebElement(xpath='//span[contains(text(),"Partizan Mozzart Bet Belgrade")]')
    team_virtus = WebElement(xpath='//span[contains(text(),"Virtus Segafredo Bologna")]')
    team_alba = WebElement(xpath='//span[contains(text(),"ALBA Berlin")]')
    team_baskonia = WebElement(xpath='//span[contains(text(),"Baskonia Vitoria-Gasteiz")]')
    team_milan = WebElement(xpath='//span[contains(text(),"EA7 Emporio Armani Milan")]')
    team_bayer = WebElement(xpath='//span[contains(text(),"FC Bayern Munich")]')
    team_acvel = WebElement(xpath='//span[contains(text(),"LDLC ASVEL Villeurbanne")]')
    team_olymp = WebElement(xpath='//span[contains(text(),"Olympiacos Piraeus")]')
    team_paris = WebElement(xpath='//span[contains(text(),"Paris Basketball")]')
    team_real = WebElement(xpath='//span[contains(text(),"Real Madrid")]')
    team_kaunas = WebElement(xpath='//span[contains(text(),"Zalgiris Kaunas")]')

        #EuroCup team
    team_panevezys = WebElement(xpath='//span[contains(text(),"7Bet-Lietkabelis Panevezys")]')
    team_bahcesehir = WebElement(xpath='//span[contains(text(),"Bahcesehir College Istanbul")]')
    team_buducnost = WebElement(xpath='//span[contains(text(),"Buducnost VOLI Podgorica")]')
    team_trento = WebElement(xpath='//span[contains(text(),"Dolomiti Energia Trento")]')
    team_hapoel = WebElement(xpath='//span[contains(text(),"Hapoel Bank Yahav Jerusalem")]')
    team_badalona = WebElement(xpath='//span[contains(text(),"Joventut Badalona")]')
    team_ulm = WebElement(xpath='//span[contains(text(),"ratiopharm Ulm")]')
    team_ankara = WebElement(xpath='//span[contains(text(),"Turk Telekom Ankara")]')
    team_venice = WebElement(xpath='//span[contains(text(),"Umana Reyer Venice")]')
    team_hamburg = WebElement(xpath='//span[contains(text(),"Veolia Towers Hamburg")]')
    team_thessaloniki = WebElement(xpath='//span[contains(text(),"Aris Midea Thessaloniki")]')
    team_besiktas = WebElement(xpath='//span[contains(text(),"Besiktas Fibabanka Istanbul")]')
    team_cedevita = WebElement(xpath='//span[contains(text(),"Cedevita Olimpija Ljubljana")]')
    team_canaria = WebElement(xpath='//span[contains(text(),"Dreamland Gran Canaria")]')
    team_tel_aviv = WebElement(xpath='//span[contains(text(),"Hapoel Shlomo Tel Aviv")]')
    team_bourg = WebElement(xpath='//span[contains(text(),"Cosea JL Bourg-en-Bresse")]')
    team_trefl = WebElement(xpath='//span[contains(text(),"Trefl Sopot")]')
    team_napoca = WebElement(xpath='//span[contains(text(),"U-BT Cluj-Napoca")]')
    team_valencia = WebElement(xpath='//span[contains(text(),"Valencia Basket")]')
    team_vilnius = WebElement(xpath='//span[contains(text(),"Wolves Twinsbet Vilnius")]')

        #Income
    btn_quit = WebElement(xpath='//*[@aria-label="modal window"]/*[3]')
    btn_fav_team = WebElement(xpath='//input[@id="signup_chtmc"]')
    btn_cookies_accept = WebElement(xpath='//button[contains(text(),"Accept All Cookies")]')
    btn_income = WebElement(xpath='(//*[@type="button"])[14]')
    btn_registr = WebElement(xpath=' //button[contains(text(),"Register")]')
    e_mail_reg = WebElement(xpath='//input[@id="signup_newEmail"]')
    password_reg = WebElement(xpath='//input[@id="signup_newPassword"]')
    confirm_password = WebElement(xpath='//input[@id="signup_confirmPassword"]')
    yes_news =WebElement(xpath='//button[contains(text(),"Да")]')
    no_news = WebElement(xpath='//button[contains(text(),"Нет")]')
    agree_terms = WebElement(xpath='//input[@id="signup_policy"]')
    create_accaunt = WebElement(xpath='//button[@type="submit"]')

        #Текст

    text_first_name = WebElement(xpath='//label[@id="lblsignup_firstName"]')
    text_last_name = WebElement(xpath='//label[@id="lblsignup_lastName"]')
    text_income = WebElement(xpath='//button[contains(text(),"Войти")]')
    text_email = WebElement(xpath='//label[@id="lblsignup_newEmail"]')
    text_password = WebElement(xpath='//label[@id="lblsignup_newPassword"]')
    text_confirm_password = WebElement(xpath='//label[@id="lblsignup_confirmPassword"]')
    text_create_acc = WebElement(xpath='//button[contains(text(),"Создать аккаунт")]')
    text_create_euro_id = WebElement(xpath='//label[@id="signup_main_title"]')
    # text_already_have  = WebElement(xpath='//label[@id="signup_subtitle"]')
    text_reclame = WebElement(xpath='(//*[@aria-labelledby="signup_tt"]//p)[1]')

    #Поля регистрации

    field_first_name = WebElement(xpath='//input[@id="signup_firstName"]')
    field_last_name = WebElement(xpath='//input[@id="signup_lastName"]')
    field_email = WebElement(xpath='//input[@id="signup_newEmail"]')
    field_password = WebElement(xpath='//input[@id="signup_newPassword"]')
    field_conf_password = WebElement(xpath='//input[@id="signup_confirmPassword"]')
    field_terms = WebElement(xpath='//*[@name="policy"]')
    btn_yes = WebElement(xpath='//button[contains(text(),"Yes")]')
    btn_no = WebElement(xpath='//button[contains(text(),"No")]')
    btn_politics = WebElement(xpath='//input[@id="signup_policy"]')
    btn_close = WebElement(xpath='//span[contains(text(),"CLOSE")]')
    btn_country = WebElement(xpath='//*[@aria-haspopup="dialog"]')
    btn_belarus = WebElement(xpath='//button[contains(text(),"Belarus")]')
    btn_town = WebElement(xpath='//input[@id="personalization_town"]')
    btn_next = WebElement(xpath='//button[contains(text(),"Next")]')
    btn_finish = WebElement(xpath='//button[contains(text(),"Finish")]')
    field_vision = WebElement(xpath='//h1[contains(text(),"You are all set!")]')
    btn_back_euro = WebElement(xpath='(//*[@aria-label="modal window"]//*[@data-sizes="auto"])[1]')
    check_succses = WebElement(xpath='//*[contains(text(),"")]')

    # Поля входа в аккаунт
    btn_explore = WebElement(xpath='//*[text() = "Explore Euroleague ID"]')
    btn_income_after_registr = WebElement(xpath='(//a[@href="/ru/euroleague/my-account/"])[3]')
    btn_exit_from_acc = WebElement(xpath='//button[text()="Выйти"]')
    btn_income_after_exit = WebElement(xpath='(//*[text()="Войти"])[6]')
    field_income_email = WebElement(xpath='//input[@id="signin_email"]')
    field_income_password = WebElement(xpath='//input[@id="signin_password"]')
    btn_login_income = WebElement(xpath='//*[text()="Login"]')
    text_check_income = WebElement(xpath='//h1[text()="Твой аккаунт"]')
