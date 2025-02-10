from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import time

from robot.api.deco import keyword

SYNAPSE_PATH = "C:\Program Files\Razer\RazerAppEngine\RazerAppEngine.exe"
CHROME_DRIVER_PATH = ".\chromedriver.exe"
REMOTE_DEBUGGING_PORT = 9229        # Synapse default port, don't modify.

# Ensure that Synapse is running in the background before doing anything...
class SynapseWebDriverClass:
    def __init__(self):
        
        try: 
            # Tab Name
            self.tab:str = ""

            # Define options for webdriver...
            self.options = Options()
            self.options.add_argument("--no-sandbox")
            self.options.add_argument("--headless")
            self.options.add_argument('--start-maximized')
            self.options.add_argument("--disable-dev-shm-usage")
            self.options.add_argument("--web-log-stream-to-console")
            self.options.add_argument("--hibernate-timeout=999999999")
            self.options.add_argument("--log-level=3")
            self.options.add_argument("--disable-background-timer-throttling")
            self.options.add_experimental_option("debuggerAddress", "localhost:" + str(REMOTE_DEBUGGING_PORT))

            # Define service...
            self.service = Service(executable_path=CHROME_DRIVER_PATH)

            # Define driver...
            self.driver = webdriver.Chrome(service=self.service, options=self.options)
            print("SYNAPSE ATTACHED: PASS")
        except:
            print("SYNAPSE ATTACHED: FAIL")
    
    def getDriver(self)->WebDriver:
        return self.driver

    @keyword("SwitchSynapseTabTo")
    def switchSynapseTabTo(self, tab_name):
        elems = self.driver.find_elements(By.CSS_SELECTOR, "*")
        for index, element in enumerate(elems):
            if element.text == tab_name:
                try:
                    self.tab = tab_name
                    element.click()
                    break
                except:
                    print(f"Cannot find element: {tab_name}. Exiting")

    @keyword("ClickOnElement")
    def clickOnElement(self, elem_name):
        driver = self.driver
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if driver.title == self.tab:
                driver.find_element(By.CSS_SELECTOR, elem_name).click()


# # TODO: Create enum for chroma selector... static is ()
# # Blade 18
# class Blade18:
#     lighting_selector = '#root > div > div.nav-tabs > div.navs-wrapper > div:nth-child(6)'
#     chroma_effect_dropdown_menu_selector = '#body-wrapper > div > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-dropdown'
#     chroma_effect_static_selector = '#body-wrapper > div > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex > div:nth-child(9)'

# # BlackWidow V4
# class BlackWidowV4:
#     lighting_selector = '#root > div > div.nav-tabs > div.navs-wrapper > div:nth-child(2)'
#     tmp = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-dropdown > div.selected.raw-text'
#     static = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex.expand > div:nth-child(9)'

# sdc = SynapseWebDriverClass(CHROME_DRIVER_PATH, SYNAPSE_PATH) 

# sdc.switchSynapseTabTo("BLADE 18")
# sdc.clickOnElement(Blade18.lighting_selector)
# sdc.clickOnElement(Blade18.chroma_effect_dropdown_menu_selector)
# sdc.clickOnElement(Blade18.chroma_effect_static_selector)
# print("BLADE 18: PASS")

# time.sleep(3)

# sdc.switchSynapseTabTo("BLACKWIDOW V4 75%")
# sdc.clickOnElement(BlackWidowV4.lighting_selector)
# sdc.clickOnElement(BlackWidowV4.tmp)
# sdc.clickOnElement(BlackWidowV4.static)
# print("BLACKWIDOW V4 75%: PASS")


# # END OF DEMO
# print("END OF DEMO")
