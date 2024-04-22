from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.contrib.auth.models import User, Group
from django.conf import settings

import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from .models import teacher

# Create your tests here.
class Hosttest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user('test0001','test0001@gmail.com','1357qetu')
        group, created = Group.objects.get_or_create(name='teacher_role')
        self.user.groups.add(group)
        self.login()
        

    #go to home
    #click create button
    #enter Name
    #enter Studio
    #enter email
    #enter phone number
    #enter message
    #enter about
    #choose photo (use default)
    #press create profile

    def test010createTeacher(self):
        self.browser.get(self.live_server_url)
        self.browser.get_screenshot_as_file("login1.png")
        self.browser.get(self.live_server_url + reverse('create_teacher'))
        self.browser.find_element(By.ID, "id_name").send_keys("test010")
        self.browser.find_element(By.ID, "id_studio").send_keys("test studio")
        self.browser.find_element(By.ID, "id_email").send_keys("test010@gmail.com")
        self.browser.find_element(By.ID, "id_phone_number").send_keys("(123)456-7890")
        self.browser.find_element(By.ID, "id_message").send_keys("this is a test message")
        self.browser.find_element(By.ID, "id_about").send_keys("this is a test about")

        photo_path = os.path.join(settings.MEDIA_ROOT, 'images\Default_Picture.png')
        self.browser.find_element(By.ID, "id_photo").send_keys(photo_path)

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        submit_button = WebDriverWait(self.browser, 1000000).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        self.browser.get_screenshot_as_file("test010-results.png")
        submit_button.click()
        user_exists = User.objects.filter(username='test0001').exists()
        self.assertTrue(user_exists, "The user does not exist.")
        #assert "Profile Created Successfully"

    #you may think this test is unimportant
    #it is very important
    #really make sure that a user exists before trying to log in as one

    def test011Usertest(self):
        user_exists = User.objects.filter(username='test0001').exists()
        self.assertTrue(user_exists, "The user does not exist.")
    
    #go to home
    #click on details button under test020's div
    #click delete button
    #click submit

    def test020deleteTeacher(self):
        teacher020 = teacher.objects.create(
            name = "test020",
            studio = "test studio",
            email = "test020@gmail.com",
            phone_number = "(123)456-7890",
            message = "this is a test message",
            about = "this is a test about",
            photo = r'C:\Users\rytti\CS3300\piano_project\media\images\Default_Picture.png',
            slug = "test020"
        )
        self.browser.get(self.live_server_url)

        self.browser.get_screenshot_as_file("test020-home.png")
        details_button = self.browser.find_element(By.XPATH, "//li[contains(text(), 'test020')]//a[contains(text(), 'Details')]")
        details_button.click()

        self.browser.get_screenshot_as_file("test020-details.png")
        delete_button = self.browser.find_element(By.XPATH, "//a[@id='delete-button']")
        delete_button.click()

        submit_button = WebDriverWait(self.browser, 1000000).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()

    def test030updateTeacher(self):
        teacher020 = teacher.objects.create(
            name = "test020",
            studio = "test studio",
            email = "test020@gmail.com",
            phone_number = "(123)456-7890",
            message = "this is a test message",
            about = "this is a test about",
            photo = r'C:\Users\rytti\CS3300\piano_project\media\images\Default_Picture.png',
            slug = "test020"
        )
        self.browser.get(self.live_server_url)

        self.browser.get_screenshot_as_file("test020-home.png")
        details_button = self.browser.find_element(By.XPATH, "//li[contains(text(), 'test020')]//a[contains(text(), 'Details')]")
        details_button.click()

        update_button = self.browser.find_element(By.XPATH, "//a[@id='update-button']")
        update_button.click()

        self.browser.find_element(By.ID, "id_name").send_keys("test030")
        self.browser.find_element(By.ID, "id_studio").send_keys("new test studio")
        self.browser.find_element(By.ID, "id_email").send_keys("test030@gmail.com")
        self.browser.find_element(By.ID, "id_phone_number").send_keys("(098)765-4321")
        self.browser.find_element(By.ID, "id_message").send_keys("this is a new test message")
        self.browser.find_element(By.ID, "id_about").send_keys("this is a new test about")

        photo_path = os.path.join(settings.MEDIA_ROOT, 'images\Default_Picture.png')
        self.browser.find_element(By.ID, "id_photo").send_keys(photo_path)

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        submit_button = WebDriverWait(self.browser, 1000000).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        self.browser.get_screenshot_as_file("test030-results.png")
        submit_button.click()




    def login(self):
        self.browser.get(self.live_server_url + '/accounts/login/')

        WebDriverWait(self.browser, 10).until(
            ec.presence_of_element_located((By.NAME, "username"))
        )

        username_field = self.browser.find_element(By.NAME, "username")
        username_field.send_keys("test0001")

        password_field = self.browser.find_element(By.NAME, "password")
        password_field.send_keys("1357qetu")
        login_button = self.browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
        login_button.click()

        
    