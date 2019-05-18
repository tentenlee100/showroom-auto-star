#showroom-auto-star

從0到99蒐集完成約10分鐘左右，若嫌慢可在執行的時候再開分頁去其他房間同步蒐集。

## 環境說明
開發環境: windows 10<br/>
使用python版本: 3.6

## 使用方式
1. 前往 https://sites.google.com/a/chromium.org/chromedriver/downloads [開啟](https://sites.google.com/a/chromium.org/chromedriver/downloads)
下載另外的chrome來做程式執行 (本程式目前使用74版本執行正常中，其他版本不確定，但應該沒問題)
1. 開啟`config.py`檔案，將上方chrome下載後放到的路徑(建議路徑不要有中文字)複製到取代掉 `chromedriver_path = "C:\\aaaa\\chromedriver.exe"` 後面的路徑，`注意一個\要改成兩個\\` 
1. 呈上，將帳號密碼輸入於`config.py` 中，`注意帳號大小寫有差異` <br/> 
`ACCOUNT = "account" ` <br/>
`PASSWORD = "password" `
1. 此帳號要跟twitter連結，才可以使用分享twitter取的免費星星的功能。
1. 其他的一般的python pip install 則不多做說明

## 已知問題
1. 若此網頁twitter分享已重複了沒有獲得星星，還是會慢慢等1分鐘看有沒有免費的星星。
1. 一次只會使用一個分頁做蒐集星星，若要更快速的多分頁，目前沒辦法。
