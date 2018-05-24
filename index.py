import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import config
from selenium import webdriver

browser = webdriver.Chrome(config.chromedriver_path)
browser.get("https://www.showroom-live.com/onlive")  # 開啟連結

browser.execute_script("showLoginDialog();")
time.sleep(1)

pdtfamily = browser.find_element_by_css_selector("#js-login .js-input-account-id")
print(pdtfamily)
pdtfamily.click()
pdtfamily.send_keys(config.ACCOUNT)
time.sleep(1)

pdtfamily = browser.find_element_by_css_selector("#js-login .js-input-password")
pdtfamily.send_keys(config.PASSWORD)
time.sleep(1)

pdtfamily = browser.find_element_by_id("js-login-submit").click()

time.sleep(2)

# living = browser.find_elements_by_class_name("contentlist-link")

watchIndex = 0

enter_id_list = []

def go_room():
    print("go_room")
    # global watchIndex
    living = browser.find_elements_by_class_name("contentlist-link")
    for index, live in enumerate(living):
        print("index", index)
        print("live", live.tag_name)

        # if index <= watchIndex:
        #     continue
        room_id = live.find_element_by_class_name("js-liveroom").get_attribute("data-roomid")

        if room_id in enter_id_list:
            print( room_id, "in enter_id_list")
            continue
        try:
            live.find_element_by_class_name("icon-official")
            live.find_element_by_class_name("listcard-join-btn").click()
            enter_id_list.append(room_id)
            time.sleep(4)
            browser.find_element_by_id("icon-room-twitter-post").click()
            time.sleep(2)
            browser.find_element_by_id("twitter-post-button").click()
            try:
                WebDriverWait(browser, 100, 1).until(lambda x: x.find_element_by_id("bonus").is_displayed())
            except TimeoutException:
                browser.back()
                time.sleep(4)
                # watchIndex = index
                go_room()
                break

            time.sleep(10)
            count = browser.find_elements_by_class_name("gift-free-num-label")[2].text
            if count == '× 99':
                browser.close()
            else:
                browser.back()
                time.sleep(4)
                # watchIndex = index
                go_room()
            break
        except:
            print( room_id, "try except")
            continue


go_room()

# driver.close() #關閉連結
