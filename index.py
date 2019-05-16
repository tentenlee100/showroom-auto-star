import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
from selenium import webdriver

def go_room():
    print("go_room")
    # global watchIndex
    # 等待畫面渲染完成
    WebDriverWait(browser, 60).until(lambda x: x.find_element_by_class_name("contentlist-link"))
    living = browser.find_elements_by_class_name("contentlist-link")
    for index, live in enumerate(living):
        print("index", index)
        print("live", live.tag_name)

        if index < watchIndex:
            continue
        room_id = live.find_element_by_class_name("js-liveroom").get_attribute("data-roomid")

        if room_id in enter_id_list:
            #  room id 已加拿過，跳過下一段
            #  print(room_id, "in enter_id_list")
            continue
        try:
            live.find_element_by_class_name("icon-official")
            # 進入房間
            live.find_element_by_class_name("listcard-join-btn").click()

            #  將本次進入的room id 記錄下來
            enter_id_list.append(room_id)

            WebDriverWait(browser, 20).until(lambda x: x.find_element_by_id("room-gift-item-wrapper").find_element_by_class_name("gift-free-num-label").text != "×")

            all99 = False
            for index2, element in enumerate(browser.find_element_by_id("room-gift-item-wrapper").find_elements_by_class_name("gift-free-num-label")) :
                print("element.text :" + element.text)
                all99 = element.text == '× 99'
                if index2 == 4:
                    break
                if not all99:
                    break

            if all99 :
                browser.close()
                break

            browser.find_element_by_id("icon-room-twitter-post").click()
            WebDriverWait(browser, 10).until(lambda x: x.find_element_by_id("twitter-dialog").is_displayed())
            browser.find_element_by_id("twitter-post-button").click()
            print("twitter-post-button click")

            try:
                element = WebDriverWait(browser, 5).until(lambda x: x.find_element_by_class_name("toast-error"))
                print("element.text", element.text)
                if '免費獲得禮物的數量將限制在' in element.text:
                    browser.close()
                    break
                else:
                    browser.back()
                    go_room()
                    break
            except TimeoutException:
                print("presence_of_element_located time out")
                pass

            try:
                print("wait bonus")
                element = WebDriverWait(browser, 60, 1).until(lambda x: x.find_element_by_id("bonus").is_displayed() or x.find_element_by_class_name("toast-error"))
                if "toast-error" == element.getAttribute("class") and '免費獲得禮物的數量將限制在' in element.text:
                    browser.close()
                    break
            except TimeoutException:
                print("bonus time out")
                browser.back()
                # watchIndex = index
                go_room()
                break

            time.sleep(1)
            count = browser.find_elements_by_class_name("gift-free-num-label")[2].text
            if count == '× 99':
                browser.close()
            else:
                browser.back()
                # watchIndex = index
                go_room()
            break
        except:
            print(room_id, "try except")
            if browser.current_url == "https://www.showroom-live.com/onlive":
                continue
            else:
                browser.get("https://www.showroom-live.com/onlive")
                go_room()
                break

browser = webdriver.Chrome(config.chromedriver_path)
browser.get("https://www.showroom-live.com/onlive")  # 開啟連結

# 開啟登入視窗
browser.execute_script("showLoginDialog();")
time.sleep(1)

# 輸入帳號
pdtfamily = browser.find_element_by_css_selector("#js-login .js-input-account-id")
print(pdtfamily)
pdtfamily.click()
pdtfamily.send_keys(config.ACCOUNT)
time.sleep(1)

# 輸入密碼
pdtfamily = browser.find_element_by_css_selector("#js-login .js-input-password")
pdtfamily.send_keys(config.PASSWORD)

browser.find_element_by_id("js-login-submit").click()


# 等待手動輸入驗證碼
WebDriverWait(browser, 120).until(lambda x: not x.find_element_by_id("js-account-dialog").is_displayed())

print("login dialog close")
#
# time.sleep(2)

# living = browser.find_elements_by_class_name("contentlist-link")

watchIndex = 0

enter_id_list = []

go_room()

# driver.close() #關閉連結
