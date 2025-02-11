
from driver import SynapseWebDriverClass
from robot.api.deco import keyword

def PerformChromaTestBlade18():
    lighting_selector = '#root > div > div.nav-tabs > div.navs-wrapper > div:nth-child(7)'
    chroma_effect_dropdown_menu_selector = '#body-wrapper > div > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-dropdown'
    chroma_effect_static_selector = '#body-wrapper > div > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex > div:nth-child(9)'
    driver = SynapseWebDriverClass()
    driver.switchSynapseTabTo("BLADE 18")
    driver.clickOnElement(lighting_selector)
    driver.clickOnElement(chroma_effect_dropdown_menu_selector)
    driver.clickOnElement(chroma_effect_static_selector)

    