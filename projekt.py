#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# dane do wpisywania we formularzu

FirstName='Stefan'
LastName='Zmyslony'
PhoneNumber='+666123456789'
Email='mojaszkrzynkapocztowa.com'
Password='tojestbardzotajnehasloniedozlamania'
ConfirmPassword='tojestbardzotajnehasloniedozlamania'
WarningNoticeAboutEmail='The Email field must contain a valid email address.'

# klasa testow strony dziedziczaca po TestCase z modulu unittest

class PhptravelsSignUp(unittest.TestCase):

    """"Wykonanie próby rejestracji nowego użytkownika w serwisie.
    Sprawdzenie reakcji strony na wprowadzenie niepoprawnego adresu
    konta email : brak @ w adresie. Testowaną stroną jest strona demo
    przygotowana dla testerów w celu doskonalenia umiejętności testerskich."""

    # Przygotowanie testow

    def setUp(self):
        Website='https://www.phptravels.net/home'
        profile = webdriver.FirefoxProfile()
        profile.set_preference("geo.enabled", False)
        profile.set_preference("geo.prompt.testing", True)
        self.driver=webdriver.Firefox(profile)
        self.driver.maximize_window()
        self.driver.get(Website)
        self.driver.implicitly_wait(5)

    # posprzatanie

    def tearDown(self):
        self.driver.quit()

    #testy

    def testWrongSignUp(self):

        dr=self.driver
        wait_on_web=WebDriverWait(dr,10)

        button_MY_ACCOUNT="//div[@class='dropdown dropdown-login dropdown-tab']"
        button_Sign_Up="//a[@class='dropdown-item tr']"
        field_First_Name='firstname'
        field_Last_Name='lastname'
        field_Mobile_Number='phone'
        field_Email='email'
        field_Password='password'
        field_Confirm_Password='confirmpassword'
        button_Green_Sign_Up="//button[@class='signupbtn btn_full btn btn-success btn-block btn-lg']"
        field_notice_from_website="//div[@class='resultsignup']/div/p[1]"

        wait_on_web.until(EC.element_to_be_clickable((By.XPATH,button_MY_ACCOUNT))).click()
        wait_on_web.until(EC.element_to_be_clickable((By.XPATH,button_Sign_Up))).click()
        dr.find_element_by_name(field_First_Name).send_keys(FirstName)
        dr.find_element_by_name(field_Last_Name).send_keys(LastName)
        dr.find_element_by_name(field_Mobile_Number).send_keys(PhoneNumber)
        dr.find_element_by_name(field_Email).send_keys(Email)
        dr.find_element_by_name(field_Password).send_keys(Password)
        dr.find_element_by_name(field_Confirm_Password).send_keys(ConfirmPassword)
        dr.find_element_by_xpath(button_Green_Sign_Up).click()

        #sprawdzenie komunikatu wyswietlonego przez strone

        Warning_Notice_from_Website=wait_on_web.until(EC.element_to_be_clickable \
                                            ((By.XPATH,field_notice_from_website))).text
        self.assertEqual(Warning_Notice_from_Website, WarningNoticeAboutEmail)

        #chwila dla publiki:
        sleep(5)

if __name__ == '__main__':
    unittest.main(verbosity=2)
