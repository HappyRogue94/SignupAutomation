"""
This file will act as the main point of entry to the google signup automation flow.
"""
from chromium_c import SeleniumHelper

# Set URL of page to be automated.
url = "https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp"

tester = SeleniumHelper(url)

def fill_page_1(id, name, data_id, data_name):
    tester.send_by_id(id, data_id)
    tester.send_by_name(name, data_name)
    tester.fill_password()
    tester.confirm_password()



# If script is run directly, then run the following methods...
if __name__ == '__main__':
    tester.launch_page()
    fill_page_1("firstName", "lastName", "Kassem", "Nassar")

