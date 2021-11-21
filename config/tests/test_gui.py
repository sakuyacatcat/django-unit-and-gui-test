from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from django.contrib.auth.models import User

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

############
# GUI test #
############


class MySeleniumTests(StaticLiveServerTestCase):

    # Prepare relational data and library
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User.objects.create(
            username='testuser',
            password='testpass',
            email='example@gmail.com'
        )
        cls.selenium = webdriver.Chrome(options=options)
        cls.selenium.implicitly_wait(10)

    # Test case: Confirm login workflow
    def test_login_workflow(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_id("id_login")
        self.assertTrue(username_input)
        username_input.send_keys('testuser')
        password_input = self.selenium.find_element_by_id("id_password")
        self.assertTrue(password_input)
        password_input.send_keys('testpass')
        login_button = self.selenium.find_element_by_xpath(
            '/html/body/form/button')
        self.assertTrue(login_button)
        login_button.click()
        self.client.force_login(User.objects.get(id=1))
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
