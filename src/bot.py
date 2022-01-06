from time import sleep

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.config import URL
from src.config import create_driver, INCREASE_COUNT
from src.email_manager import get_access_code
from src.helpers import wait_for_shield_invisibility, MarketError


class Bot:
    def __init__(self):
        self.driver = create_driver()
        self.action = ActionChains(self.driver)
        self.driver.get(URL)
        print("Starting sniping bot...")

    wait_for_market_available
    @staticmethod
    def read(text, language='en'):
        if ALLOW_NOTIFICATIONS:
            message = gTTS(text=text, lang=language, slow=False)
            message.save("message.mp3")
            os.system("mpg123 message.mp3")
            os.system("rm message.mp3")

    def quit(self):
        self.driver.quit()

    def login(self, user):
=======
    def go_to_login_page(self):
        add_windows_compatibility
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="ut-login-content"]//button'))
        )
        print("Logging in...")
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@class="ut-login-content"]//button').click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'email'))
        )

    def login(self, user):
        self.go_to_login_page()

        self.driver.find_element(By.ID, 'email').send_keys(user["email"])
        self.driver.find_element(By.ID, 'password').send_keys(user["password"])
        self.driver.find_element(By.ID, 'btnLogin').click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, 'btnSendCode'))
        ).click()

        access_code = get_access_code()

        self.driver.find_element(By.ID, 'oneTimeCode').send_keys(access_code)
        self.driver.find_element(By.ID, 'btnSubmit').click()

        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'icon-transfer'))
        )
        sleep(2)

    def login_manually(self):
        self.go_to_login_page()

        print("Enter your account credentials and click login button.")
        print("Waiting 5 minutes...")

        WebDriverWait(self.driver, 300).until(
            EC.element_to_be_clickable((By.ID, 'btnSendCode'))
        ).click()

        print("Provide EA access code and click submit button.")
        print("Waiting 5 minutes...")

        WebDriverWait(self.driver, 300).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'icon-transfer'))
        )
        sleep(2)

    def go_to_transfer_market(self):
        self.driver.find_element(By.CLASS_NAME, 'icon-transfer').click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'ut-tile-transfer-market'))
        )
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'ut-tile-transfer-market').click()

    def search_player(self, player, max_price):
        count = 1
        coins = self.driver.find_element(By.CLASS_NAME, 'view-navbar-currency-coins').text.replace(" ", "")
        print("Number of coins: " + coins)

        while int(coins) >= max_price:
            if count % INCREASE_COUNT == 0:
                min_price_input = self.driver.find_element(By.XPATH, '(//input[contains(@class, "numericInput")])[3]')
                min_price_input.click()
                sleep(0.05)
                min_price_input.send_keys(0)

            self.driver.find_element(By.XPATH, '(//*[@class="button-container"]/button)[2]').click()
            result = WebDriverWait(self.driver, 10).until(lambda d:
                                                          d.find_elements(By.CLASS_NAME, 'no-results-icon') or
                                                          d.find_elements(By.CLASS_NAME, 'DetailView'))[0]

            # Buy a player when result appears
            if "DetailView" in result.get_attribute("class"):
                coins = self.driver.find_element(By.CLASS_NAME, 'view-navbar-currency-coins').text.replace(" ", "")

                try:
                    self.driver.find_element(By.XPATH, '//button[contains(@class, "buyButton")]').click()
                except WebDriverException:
                    wait_for_shield_invisibility(self.driver, 0.1)
                    self.driver.find_element(By.XPATH, '//button[contains(@class, "buyButton")]').click()

                self.driver.find_element(By.XPATH, '//div[contains(@class,"view-modal-container")]//button').click()
                wait_for_shield_invisibility(self.driver)

                new_coins = self.driver.find_element(By.CLASS_NAME, 'view-navbar-currency-coins').text.replace(" ", "")

                if int(coins) == int(new_coins):
                    print("Found something, but it was too late.")
                else:
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, '(//div[@class="DetailPanel"]/div[@class="ut-button-group"]/button)[8]'))
                    ).click()
                    price = int(coins) - int(new_coins)
                    print("Success! You bought " + player + " for " + str(price) + " coins.")
                    coins = new_coins
wait_for_market_available
                    self.read("Success")
=======
                    success_count += 1
add_windows_compatibility

            # Wait 5 minutes if transfer market doesn't work
            if "Notification negative" in result.get_attribute("class"):
                raise MarketError

            try:
                self.driver.find_element(By.XPATH, '//button[contains(@class, "ut-navigation-button-control")]').click()
            except WebDriverException:
                wait_for_shield_invisibility(self.driver, 0.1)
                self.driver.find_element(By.XPATH, '//button[contains(@class, "ut-navigation-button-control")]').click()

            inc_max_price_button = self.driver.find_element(By.XPATH, '(//div[@class="price-filter"]//button)[6]')

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '(//div[@class="price-filter"]//button)[6]'))
            )

            wait_for_shield_invisibility(self.driver)

            inc_max_price_button.click()

            count += 1

        print("You have no coins for more players.")
        return True

    def buy_player(self, player, max_price):
        while True:
            try:
                self.go_to_transfer_market()

                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'ut-player-search-control'))
                )
                wait_for_shield_invisibility(self.driver)

                self.driver.find_element(By.XPATH, '//div[contains(@class, "ut-player-search-control")]//input').click()
                sleep(0.1)
                self.driver.find_element(By.XPATH, '//div[contains(@class, "ut-player-search-control")]//input').send_keys(player)

                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//ul[contains(@class, "playerResultsList")]/button'))
                )
                sleep(1)

                self.driver.find_element(By.XPATH, '//ul[contains(@class, "playerResultsList")]/button').click()

                self.driver.find_element(By.XPATH, '(//input[contains(@class, "numericInput")])[4]').click()
                sleep(0.1)
                self.driver.find_element(By.XPATH, '(//input[contains(@class, "numericInput")])[4]').clear()
                self.driver.find_element(By.XPATH, '(//input[contains(@class, "numericInput")])[4]').send_keys(max_price)

                print("Looking for " + player + " with max price " + str(max_price) + "...")

                if self.search_player(player, max_price):
                    break

       wait_for_market_available
            except TimeoutException:
                print("Error, you have to wait some time, until the transfer market will be available again.")
                print("Waiting 5 minutes...")
                sleep(300)
                continue
=======
        except TimeoutException:
            print("Error, check the browser")
      add_windows_compatibility
