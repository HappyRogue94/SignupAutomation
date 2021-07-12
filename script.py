"""
This file will act as the main point of entry to the google signup automation flow.
"""
from chromium_c import SeleniumHelper

# Set URL of page to be automated.
url = "https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp"

# If script is run directly, then run the following methods...
if __name__ == '__main__':
    tester = SeleniumHelper(url)
    tester.launch_page()
    tester.send_by_id("firstName", "Kassem")
