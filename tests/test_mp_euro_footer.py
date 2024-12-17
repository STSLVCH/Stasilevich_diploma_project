# import time
import time

import allure
import pytest_check as check
from locators.locators_mp_euro_footer import MainPage
from conftest import web_browser

@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')

def test_url_footer(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    middles  =  [(page.btn_about_site_footer, "О сайте", "https://www.euroleaguebasketball.net/about/"),
              (page.btn_contact_footer, "Контакты", "https://www.euroleaguebasketball.net/contact-us/"),
              (page.btn_vocation_footer, "Вакансии", "https://careers.euroleague.net/"),
              (page.btn_press_footer, "Пресс-центр", "https://mediacentre.euroleague.net/"),
              (page.btn_market_footer, "Маркетинговые партнеры", "https://www.euroleaguebasketball.net"
                                                                 "/marketing-partners/"),

              (page.btn_brand_footer, "Бренд-центр", "https://brandcenter.euroleague.net/en/?section=Brand-Assets"),
              (page.btn_kodex_footer, "Кодекс поведения", "https://inform.euroleague.net/"),
              (page.btn_formatone_footer, "Формат", "https://www.euroleaguebasketball.net/euroleague/format-el/"),

              (page.btn_mediapartner_footer,"Медиапартнеры", "https://www.euroleaguebasketball.net"
                                                             "/euroleague/media-partners/"),

              (page.btn_charter_footer, "Устав", "https://ftpserver.euroleague.net/general"
                                                 "/2024_25EuroLeagueBylaws.pdf"),

              (page.btn_fantasy_first_footer, "Fantasy Challenge", "https://euroleaguefantasy.euroleaguebasketball.net"
                                                                   "/en/home"),

              (page.btn_efa_footer, "EFA","https://ftpserver.euroleague.net/general/"
                                          "euroleague_framework_agreement.pdf"),

              (page.btn_formattwo_footer, "Формат", "https://www.euroleaguebasketball.net/eurocup/format-ec/"),
              (page.btn_chartettwo_footer, "Устав", "https://ftpserver.euroleague.net/general/"
                                                    "2024_25EuroCupBylaws.pdf"),

              (page.btn_fantasy_two_footer, "Fantasy Challenge","https://eurocupfantasy.euroleaguebasketball.net/en"
                                                                "/home"),
              (page.btn_eurotv_footer, "EuroLeague TV", "https://www.euroleague.tv/"),
              (page.btn_mobile_footer, "Мобильное приложение","https://www.euroleaguebasketball.net/"
                                                              "euroleague-basketball-app/"),
              (page.btn_euroshop_footer, "EuroLeague Магазин", "https://euroleaguestore.net/"),
              (page.btn_cornerfan_footer, "Уголок болельщика","https://linktr.ee/EuroleagueBasketball"),
              (page.btn_main_league_footer, "Euroleague Basketball", "https://www.euroleaguebasketball.net/"),
              (page.btn_main_turkish_footer, "Turkish Airlines EuroLeague", "https://www.euroleaguebasketball.net/"
                                                                               "euroleague/"),
              (page.btn_main_eurocup_footer, "BKT EuroCup", "https://www.euroleaguebasketball.net/eurocup"),
              (page.btn_main_other_footer, "Прочее", "https://www.euroleaguebasketball.net/")
                ]

    for middle,text_middle,middle_url in middles:

        with allure.step('Тест проверки отображения на экране'):
            check.is_true(middle.is_visible())

        with allure.step('Тест проверки кликабельности'):
            check.is_true((middle.is_clickable()))

        with allure.step('Проверка на орфографию'):
            check.equal(middle.get_text(), text_middle)

        with allure.step('Проверка на корректный адрес кнопки'):
            check.equal(middle.get_attribute('href'), middle_url)

        page.switch_to_window(1)

def test_social_footer(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    socials = [
               (page.btn_youtube_footer, "https://www.youtube.com/euroleague", "youtube"),
               (page.btn_facebook_footer, "https://www.facebook.com/TheEuroleague", "facebook"),
               (page.btn_x_footer, "https://twitter.com/Euroleague", "twitter"),
               (page.btn_instagram_footer, "https://instagram.com/euroleague", "instagram"),
               (page.btn_tick_tok_footer, "https://www.tiktok.com/@euroleague", "tiktok"),
               (page.btn_whats_up_footer, "https://whatsapp.com/channel/0029Va9Jmb3Ae5VkBsSAUs17", "whatsapp"),
               (page.btn_politics_cookies_footer, "https://www.euroleaguebasketball.net/cookie-policy-ev/",
                    "Политика в отношении куки-файлов"),
               (page.btn_cofedenc_footer, "https://www.euroleaguebasketball.net/privacy-policy-ev/",
                    "Privacy policy"),
               ]
    for social, url_social, window_social in socials:
        with allure.step('Тест проверки отображения на экране'):
            time.sleep(2)
            check.is_true(social.is_visible())
            # if window_social != 'та же страница' or 'эта же страница':
            #     page.switch_to_window(1)


        with allure.step('Тест проверки кликабельности'):
            check.is_true(social.is_clickable())

        with allure.step('Проверка на корректный адрес кнопки'):
            check.equal(social.get_attribute('href'), url_social)

        with allure.step('Проверка на корректный адрес кнопки'):
            social.click()
            check.equal(page.get_current_url(), url_social)
            if window_social != 'Политика в отношении куки-файлов' or 'Privacy policy':
                page.switch_to_window(1)
                check.equal(page.get_current_url(), url_social)
                page.switch_to_window(0)
                page.go_back()




def test_language_footer(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    page.btn_language_footer.click()
    languages = [(page.btn_deutsch_footer, 'Deutsch'),
                 (page.btn_greece_footer, 'Ελληνικά'),
                 (page.btn_english_footer, 'English'),
                 (page.btn_spain_footer, 'Español'),
                 (page.btn_france_footer, 'Français'),
                 (page.btn_italia_footer, 'Italiano'),
                 (page.btn_litva_footer, 'Lietuviškai'),
                 (page.btn_serbska_footer, 'Srpski'),
                 (page.btn_turkish_footer, 'Türkçe')
                 ]
    for language, text_language in languages:

        with allure.step('Проверка на видимость языков'):
            check.is_true(language.is_visible())

        with allure.step('Проверка на кликабельность'):
            check.is_true(language.is_clickable())


        with allure.step('Проверка на орфографию'):
            check.equal(language.get_text(),text_language)


def test_count_footer(web_browser):
    page = MainPage(web_browser)
    page.btn_cookies_accept.click()
    # print(page.btn_a_test.count())
    with allure.step("Проверяем на колличество элементов этого класса"):
        check.equal(19, page.btn_a_test.count(), "Колличество не подходит")