import self


class Homerediff():
    # create constructor

    def __init__(self, driver):
        self.driver = driver
        self.kal = "NEWS"

        # actions

    def click_News(self):
        self.driver.find_element_by_link_text("NEWS").click()

    def click_BUSINESS(self):
        self.driver.find_element_by_link_text("BUSINESS").click()

    def click_MOVIES(self):
        self.driver.find_element_by_link_text("MOVIES").click();

    def click_CRICKET(self):
        self.driver.find_element_by_link_text("CRICKET").click();

    def click_SPORTS(self):
        self.driver.find_element_by_link_text("SPORTS").click();

    def click_GETAHEAD(self):
        self.driver.find_element_by_link_text("GET AHEAD").click();

    def click_REALTIMENEWS(self):
        self.driver.find_element_by_link_text("REALTIME NEWS").click();

    #def click_FARMERSSTIR(self):
     #   self.driver.find_elements_by_xpath("//a[@innerstringmarker="FARMERS' STIR"]").click();

