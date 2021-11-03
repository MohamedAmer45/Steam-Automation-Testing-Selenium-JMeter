# Name: Mohamed Mahmoud Ahmed Amer
# ID: 17107584
# Project: Steam_Test_Script
# Note : Most of these scripts will not work properly unless the user is logged in.
# Description of each test Scenario/Case is commented above it.
# Total Number of Test Scenarios in this script : 4.
# Total Number of Test Cases in this script : 9.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

path = "C:/Users/moham/Downloads/Chromedriver/chromedriver.exe"
driver = webdriver.Chrome(path)

###################################################################
# Test Scenario ID : TS_Browse_store
# Test scenario description: Validate if the user is able to browse
# the store and open game pages and interact with each game without
# any issues.
# No. of Test Cases : 5
###################################################################

# Test Case ID : TC_Browse_Store_01
# Test Summery :Check if the user can
# open Steam Store page without any issues.
driver.get("https://store.steampowered.com/")
element = WebDriverWait(driver, 40)

# Test Case ID : TC_Browse_Store_02
# Test Summery :Check if the user can
# open any game page on the store without any issues.
Open_Game_Page = '//*[@id="home_browsemore_carousel2"]/div[1]/div/div[2]/a'
loc_1 = driver.find_element_by_xpath(Open_Game_Page)
loc_1.click()

# Test Case ID : TC_Browse_Store_03
# Test Summery :Check if the user can
# Add any game to his Wishlist without any issues
Open_Game_Page_1 = '//*[@id="home_browsemore_carousel2"]/div[1]/div/div[2]/a'
loc_2 = driver.find_element_by_xpath(Open_Game_Page_1)
loc_2.click()
Add_to_Wishlist = '//*[@id="add_to_wishlist_area"]/a/span'
loc_3 = driver.find_element_by_xpath(Add_to_Wishlist)
loc_3.click()

# Test Case ID : TC_Browse_Store_04
# Test Summery :Check if the user can
# Follow any game on the store without any issues
Open_Game_Page_2 = '//*[@id="home_browsemore_carousel2"]/div[1]/div/div[2]/a'
loc_4 = driver.find_element_by_xpath(Open_Game_Page_2)
loc_4.click()
Follow_Game = '/html/body/div[1]/div[7]/div[4]/div[1]/div[3]/div[4]/div[2]/div/div/div[4]/div[1]/span'
loc_5 = driver.find_element_by_xpath(Follow_Game)
loc_5.click()

# Test Case ID : TC_Browse_Store_05
# Test Summery :Check if the user can
# Ignore any game on the store without any issues
Open_Game_Page_3 = '//*[@id="home_browsemore_carousel2"]/div[1]/div/div[2]/a'
loc_6 = driver.find_element_by_xpath(Open_Game_Page_3)
loc_6.click()
Ignore_Game = '/html/body/div[1]/div[7]/div[4]/div[1]/div[3]/div[4]/div[2]/div/div/div[5]/div[1]/div[1]/span'
loc_7 = driver.find_element_by_xpath(Ignore_Game)
loc_7.click()

###################################################################
# Test Scenario ID : TS_Search
# Test scenario description: Validate if the user is able to search
# for a game in the store without any issues.
# No. of Test Cases : 2
###################################################################

# Test Case ID : TC_Search_01
# Test Summery :Check if the user can
# Search for any game in the store without any issues.
SearchBox = '//*[@id="store_nav_search_term"]'
loc_8 = driver.find_element_by_xpath(SearchBox)
loc_8.send_keys("Battlefield V")
SearchButton = '//*[@id="store_search_link"]/img'
loc_9 = driver.find_element_by_xpath(SearchButton)
loc_9.click()

# Test Case ID : TC_Search_02
# Test Summery :Check if the user can
# Search for an invalid game in the store without any issues.
SearchBox = '//*[@id="store_nav_search_term"]'
loc_10 = driver.find_element_by_xpath(SearchBox)
loc_10.send_keys("InvalidGameName")
SearchButton = '//*[@id="store_search_link"]/img'
loc_11 = driver.find_element_by_xpath(SearchButton)
loc_11.click()

###################################################################
# Test Scenario ID : TS_Add_Item
# Test scenario description: Validate if the user is able to add
# games to cart without any issues.
# No. of Test Cases : 1
###################################################################

# Test Case ID : TC_Add_Item_01
# Test Summery :Check if the user can add any game to cart without
# any issues
Open_Game_Page_4 = '//*[@id="home_browsemore_carousel2"]/div[1]/div/div[2]/a'
loc_12 = driver.find_element_by_xpath(Open_Game_Page_4)
loc_12.click()
Add_to_Cart = '//*[@id="btn_add_to_cart_415372"]/span'
loc_13 = driver.find_element_by_xpath(Add_to_Cart)
loc_13.click()

###################################################################
# Test Scenario ID : TS_Remove_Item
# Test scenario description: Validate if the user is able to remove
# games from cart without any issues
# No. of Test Cases : 1
###################################################################

# Test Case ID : TC_Remove_Item_01
# Test Summery :Check if the user can remove any game
# from cart without any issues
Open_Cart = '//*[@id="cart_link"]'
loc_14 = driver.find_element_by_xpath(Open_Cart)
loc_14.click()
Remove_From_Cart = '//*[@id="cart_row_3923163864899041812"]/div[1]/div[1]/div/a'
loc_15 = driver.find_element_by_xpath(Remove_From_Cart)
loc_15.click()
