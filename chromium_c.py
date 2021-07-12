"""This module will serve as the main logic behind the google singup page automatation. 
   This module is still under development. More functionality will be added. 
"""
from selenium import webdriver

class SeleniumHelper():
    def __init__(self, url, driver = None):
        """Populates webdriver with required fields. 

        Args: 
            self.driver(String): Path of the webdriver on system, specific to browser used. Defaults to chromium.
            self.url(String): URL of webstibe on which the automation will occur.
        """
        if driver:
            self.driver = driver
        
        self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        self.url    = url
    
    def launch_page(self):
        """ This method will launch the page specified by the URL. 

        Args:
            None
        """
        return self.driver.get(self.url)
    
    def send_by_id(self, id, data):
        """This method is reponsible for finding the "id" of the HTML element &
           inserting the "data" into that field ID. 
        
        Args:
            id(string)  : id of the HTML webpage field
            data(string): data to be inserting to the specified id. 
        """
        return self.driver.find_element_by_id(id).send_keys(data)