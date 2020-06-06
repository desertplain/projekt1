#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

email='llolla@op.pl'
birthday='3'
aliasss='buda'

print('hellou mai frend')

# tworzymy klase wspplcheck dziedziczaca po z modulu unittest

class WizRegistration(unittest.TestCase):
    """"scenariusz testowy"""
    # Warunki wstepne
    # Przygotowanie testow
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("geo.enabled", False)
        self.driver=webdriver.Firefox(profile)
        # profile.set_preference("geo.prompt.testing", True)
        self.driver.maximize_window()
        self.driver.get('https://wizzair.com/pl-pl/#/')

        #self.driver.implicitly_wait(50)
    #wlasciwe testy
    def testWrongRegitration(self):
        #odnajdz i kliknij sign in ,
        dr=self.driver

"""
        imie='misiek'
        nazwisko='misiowy'
        wait_onweb=WebDriverWait(dr, 50)
        gender='female'
        fon='111111111'
        emaijl='misiek.op.pl'
        haslo='Olaboga7'
        narod='Polska'
        button_sign1='//button[@data-test="navigation-menu-signin"]'
        button_sign2='//button[text()=" Rejestracja "]'
        pole1='firstName'
        pole2='lastName'
        kod_kraju='+48'
        pole3='phone-number-country-code'
        button_sign3='//label[@data-test="register-gendermale"]'
        button_sign4='//label[@data-test="register-genderfemale"]'
        button_sign5='//div[@data-test="booking-register-country-code"]'
        button_sign6='//input[@name="phone-number-country-code"]'
        button_sign7='//li[@data-test="PL"]'
        pole4='phoneNumberValidDigits'
        pole5='email'
        pole6='//input[@data-test="booking-register-password"]'
        pole7='//input[@data-test="booking-register-country"]'
        pole8="//div[@class='register-form__country-container__locations']"
        pole9="label"
        check1='//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]'
        button_sign8='//button[@data-test="booking-register-submit"]'
"""

        """wait_onweb.until(EC.element_to_be_clickable((By.XPATH,button_sign1))).click()
        wait_onweb.until(EC.element_to_be_clickable((By.XPATH,button_sign2))).click()
        wpis_lewy=wait_onweb.until(EC.element_to_be_clickable((By.NAME,pole1)))
        wpis_prawy=wait_onweb.until(EC.element_to_be_clickable((By.NAME,pole2)))
        #wait_onweb.until(EC.element_to_be_clickable((By.NAME,pole1))).send_keys(imie)
        #wait_onweb.until(EC.element_to_be_clickable((By.NAME,pole2))).send_keys(nazwisko)
        if gender=='male':
            wpis_prawy.send_keys(nazwisko)
            wpis_lewy.send_keys(imie)
            dr.find_element_by_xpath(button_sign3).click()
        else:
            wpis_lewy.send_keys(imie)
            wpis_prawy.send_keys(nazwisko)
            dr.find_element_by_xpath(button_sign4).click()

        wait_onweb.until(EC.element_to_be_clickable((By.XPATH,button_sign5))).click()
        wait_onweb.until(EC.element_to_be_clickable((By.XPATH,button_sign6))).send_keys(kod_kraju)
        wait_onweb.until(EC.element_to_be_clickable((By.XPATH,button_sign7))).click()

        dr.find_element_by_name(pole4).send_keys(fon)

        dr.find_element_by_name(pole5).send_keys(emaijl)

        dr.find_element_by_xpath(pole6).send_keys(haslo)

        dr.find_element_by_xpath(pole7).click()
        # Wyszukaj kraje
        country_to_choose = dr.find_element_by_xpath(pole8)
        # Poszukaj elementow "label" wewnatrz listy "countries"
        countries = country_to_choose.find_elements_by_tag_name(pole9)
        # Iteruj po kazdym elemencie w liscie "countries"
        for label in countries:
            # Wewnatrz "label" znajdz element "strong"
            option=label.find_element_by_tag_name('strong')
            # Jesli tekst elementu jest taki jak zadany w valid_country
            if option.get_attribute("innerText") == narod:
                # Przewin do tego elementu
                option.location_once_scrolled_into_view
                # Kliknij
                option.click()
                # Wyjdz z petli - juz znalazlem i kliknalem
                break

        dr.find_element_by_xpath(check1).click()

        dr.find_element_by_xpath(button_sign8).click()

        #dr.find_element_by_xpath(pole7).send_keys(nar)

        #dr.find_element_by_name(pole3).send_keys(kod_kraju)


        #<input type="text" name="phone-number-country-code" maxlength="256" autocomplete="off" placeholder="Wyszukaj…">
        #driver.find_element_by_id('SubmitCreate').click()

        #Select(driver.find_element_by_id('days')).select_by_value(birthday)

        #email_text=driver.find_element_by_id('email').get_attribute('value')
        #assert email_text == email


        #driver.find_element_by_id('alias').clear()
        #driver.find_element_by_id('alias').send_keys(aliasss)

        sleep(10)
        #self.assertIn('Bankowe',driver.title)
        #print(driver.title)
"""

    # sprztanie
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
