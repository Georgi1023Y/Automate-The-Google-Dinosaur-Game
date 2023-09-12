# I made simple Python code that can automate Google Dinosaur Game.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Here I am initializing Microsoft Edge WebDriver.
driver = webdriver.Edge()

# Opening the dinosaur online game. This is the url for the game - "https://elgoog.im/dinosaur-game/".
driver.get("https://elgoog.im/dinosaur-game/")

# Locating the game window.
canvas = driver.find_element(By.XPATH, '//*[@id="t"]')

# Starting the game by pressing SPACE button.
# Makes the screen sleep for 5s.
time.sleep(5)

# Pressing space key automatically using Selenium.
canvas.send_keys(Keys.SPACE)
in_game = True

while in_game:
    # Sending the SPACE  key to jump when there is cactus in front of the dinosaur.
    canvas.send_keys(Keys.SPACE)
    # Waits one second before to jump again.
    time.sleep(1)

