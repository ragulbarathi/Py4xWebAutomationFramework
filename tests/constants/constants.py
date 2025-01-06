import allure
from allure_commons.types import AttachmentType


class Constants:
    def __init__(self):
        print("constants loaded")

    @staticmethod
    def app_url():
        return "https://app.vwo.com"

    @staticmethod
    def app_dashboard_url():
        return "https://app.vwo.com/#/dashboard"

    @staticmethod
    def take_screenshot(driver, name):
        allure.attach(driver.get_screenshot_as_png(), name=name,
                      attachment_type=AttachmentType.PNG)
