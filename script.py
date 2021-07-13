"""
This file will act as the main point of entry to the google signup automation flow.
"""
import time
from chromium_c import SeleniumHelper

# Set URL of page to be automated.
url = 'https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp'

tester = SeleniumHelper(url)

def fill_page_1(id, name, data_id, data_name, xpath_password, xpath_confirm, xpath_button):
    tester.send_by_id(id, data_id)
    tester.send_by_name(name, data_name)
    time.sleep(3)
    tester.send_by_xpath(xpath_password, data='Password1234%')
    tester.send_by_xpath(xpath_confirm,  data='Password1234%')
    tester.send_by_xpath(xpath_button).click()


# If script is run directly, then run the following methods...
if __name__ == '__main__':
    tester.launch_page()
    fill_page_1('firstName', 'lastName', 'Kassem', 'Nassar',"//*[@id='passwd']/div[1]/div/div[1]/input", 
                '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input', '//*[@id="accountDetailsNext"]/div/button/span' )

