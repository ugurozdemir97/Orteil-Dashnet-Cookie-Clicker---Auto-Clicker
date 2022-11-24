from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium import webdriver
from time import sleep, time

# --------------------- CONSTANTS ----------------------- #

# I was thinking about the most optimal way to get more points in the game in the shortest time. This program
# will not only click the cookie, it will also buy the products and upgrades after clicking the cookie 200 times.
# And after each iteration CLICK variable will increase 50 because upgrades and products get more and more expensive
# as the game goes on, so we need to click more and more. You can still use your internet while the auto clicker is on.

# This is what I find to be optimal, but you can change it and experiment with numbers.

CLICK = 200  # How many times to click the cookie before buying products and updates.
TIME = time() + 60 * 5  # This is how long the program will run. Current time + 5 minutes

# ------------ CONNECT TO THE CHROME DRIVER --------------- #

# You need to download chrome driver. If you have it in a different path, change the path below.
chrome_driver = "C:/Program Files/Chrome Driver/chromedriver"
service = Service(chrome_driver)  # Create a Service object with the driver passed in

driver = webdriver.Chrome(service=service)  # This is our driver which we will use
driver.get("https://orteil.dashnet.org/cookieclicker/")  # Open the game

sleep(5)  # Let the website download before clicking something otherwise you may get errors.

# ------- SELECT LANGUAGE AND FIND THE COOKIE --------- #

# Select language
language = driver.find_element(By.ID, "langSelect-EN")
language.click()

sleep(5)  # Be sure that the website is ready
cookie = driver.find_element(By.ID, "bigCookie")  # Find the big cookie

# ------------ CLICK THE COOKIE AND BUY PRODUCTS -------------- #

while time() < TIME:  # Until 5 minutes passes

    for i in range(CLICK):  # Click the big cookie 200 times.
        cookie.click()

    # --- Selenium crushes so easy, so we need to handle lots of common exceptions --- #

    try:
        # If there is something to upgrade, upgrade everything.
        while driver.find_element(By.CSS_SELECTOR, ".upgradeBox .enabled"):
            upgrade = driver.find_element(By.CSS_SELECTOR, ".upgradeBox .enabled")
            upgrade.click()
        # Errors I got when running the program
    except ElementClickInterceptedException:
        pass
    except NoSuchElementException:
        pass
    except StaleElementReferenceException:
        pass
    except IndexError:
        pass

    try:
        # If there is something to buy, buy everything.
        while driver.find_elements(By.CSS_SELECTOR, ".storeSection .enabled"):
            products = driver.find_elements(By.CSS_SELECTOR, ".storeSection .enabled")
            products[-1].click()

    except ElementClickInterceptedException:
        pass
    except NoSuchElementException:
        pass
    except StaleElementReferenceException:
        pass
    except IndexError:
        pass

    CLICK += 50  # Increase CLICK times per iteration because upgrades and products get more and more expensive.

# Print the current Cookies Per Second as a result.
cookies_per_second = driver.find_element(By.XPATH, '//*[@id="cookiesPerSecond"]')
print(cookies_per_second.text)
