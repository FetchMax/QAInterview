from selenium import webdriver
import time

# This instantiates the driver for the browser that the test will use, in this case chrome.
driver = webdriver.Chrome('./chromedriver')

# This is the URL for the test.
url = "http://ec2-54-208-152-154.compute-1.amazonaws.com/"

# This navigates the instantiated browser to the URL above.
driver.get(url)

# This uses what's called an x-path to find the value representing the fake bar of gold.
path = "//*[@data-value='0']"

# This is where we navigate to the value we are seeking for this test.
# The requirements were to find the fake bar of gold in the fastest possible way. This does
# so in n time which is written as value of T(n) when compared with other algorithms.
button = driver.find_element_by_xpath(path)

# This button is clicked and we see the message that we have completed the challenge.
button.click()

# This is here to pause the program so we can verify the winning message.
time.sleep(5)

# This closes the browser and the program.
driver.quit()

