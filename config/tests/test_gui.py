from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webDriver
import chromedriver_bynary
from selenium.webdriver.chrome.options import Options
from django.contrib.auth.models import User
from snsapp.models import Post

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
        cls.selenium = webDriver()
        cls.selenium.implicitly_wait(10)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.selenium.quit()
    #     super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_id("id_login")
        username_input.send_keys('testuser')
        password_input = self.selenium.find_element_by_id("id_password")
        password_input.send_keys('testpass')
        self.selenium.find_element_by_xpath('/html/body/form/button').click()
