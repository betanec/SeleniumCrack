from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time
from selenium.webdriver.common.by import By
import random

class InstCrack:
    def __init__(self, driver, username, password, param, scrolls):
        self.driver = driver
        self.scrolls = scrolls
        self.username = username
        self.password = password
        self.param = param
    def wait(self, delay = 0):
        time.sleep(random.randint(1000,4000)/1000+delay)#spec par
        # WebDriverWait(driver, 15).until(EC.presence_of_element_located([By.LINK_TEXT, "Сохранить данные"]))  ?????????? 
    def login(self):  
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.wait()
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)
        self.wait()
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div").click()
        self.wait()
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
        self.wait()
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        self.wait()
    def scroll_page(self):
        self.driver.find_element_by_partial_link_text("подписок").click()
        self.wait()
        fBody  = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll < self.scrolls:
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            self.wait()
            scroll += 1

    def before_refresh(self, way):
        self.wait()
        self.driver.find_element_by_xpath(way).click()
        self.wait()
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[1]').click()

    def refresh_page(self, way):
        self.driver.refresh()
        self.scroll_page()
        self.before_refresh(way)

    def scrape_followers(self, account):
        xpath_fall_unfall = "/html/body/div[6]/div/div/div[3]/ul/div/li[X]/div/div[2]/button"
        driver.get("https://www.instagram.com/{0}/".format(account))
        time.sleep(4)
        self.scroll_page()
        count_subs = len(driver.find_elements_by_xpath("//div[@class='isgrP']//li"))
        way_subs = [xpath_fall_unfall.replace(xpath_fall_unfall[xpath_fall_unfall.find("li[")+len("li[")], str(i)) for i in range(1, count_subs+1)]#re.findall(r'\d+',y)
        count = -1  
        for i in way_subs:
            count += 1
            if count in [i for i in range(self.param, count_subs, self.param)]:
                r_ch = random.choice(way_subs)
                way_subs.pop(way_subs.index(r_ch))
                self.refresh_page(r_ch)
            else:
                r_ch = random.choice(way_subs)
                way_subs.pop(way_subs.index(r_ch))
                self.before_refresh(r_ch)
        return "unfollow {}".format(count_subs)

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="C:\\Users\\User\\chromedriver_win32\\chromedriver.exe")
    try:
        a = InstCrack(driver, scrolls = 30, username = "Username", password="Password", param = 15)
        a.login()
        print(a.scrape_followers("morgen_shtern"))
    finally:
        driver.quit()
