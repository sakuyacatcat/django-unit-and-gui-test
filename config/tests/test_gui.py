from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from django.contrib.auth.models import User
from snsapp.models import Post

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

############
# GUI test #
############


class MySeleniumTests(StaticLiveServerTestCase):

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

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_id("id_login")
        self.assertTrue(username_input)
        username_input.send_keys('testuser')
        password_input = self.selenium.find_element_by_id("id_password")
        self.assertTrue(password_input)
        password_input.send_keys('testpass')
        self.selenium.find_element_by_xpath('/html/body/form/button').click()

    # def test_make_post(self):
