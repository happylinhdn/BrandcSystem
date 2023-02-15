# -*- coding: utf-8 -*-
from Supplier.supportmodels import SupplierChannel, XPATH
import time

def convert_to_float(follower_input):
    follower = follower_input or '-1'
    upperFollower = follower.upper().replace(",",".")
    value = 0
    if 'K' in upperFollower:
        tempK = upperFollower.split("K")
        try:
            value = float(tempK[0]) * 1000
        except:
            print("Can not convert follower thousands")
            raise Exception("The value of follower is not valid: " + str(follower_input  or ''))

    elif 'M' in upperFollower:
        tempK = upperFollower.split("M")
        try:
            value = float(tempK[0]) * 1000000
        except:
            print("Can not convert follower million")
            raise Exception("The value of follower is not valid: " + str(follower_input  or ''))
    else:
        try:
            if upperFollower.count(',') >= 2:
                upperFollower = upperFollower.replace(',','')
            if upperFollower.count('.') >= 2:
                upperFollower = upperFollower.replace('.','')
            value = float(upperFollower)
        except:
            value = 0
            raise Exception("The value of follower is not valid: " + str(follower_input or ''))
    
    return value

def convert_to_string_number(number):
    if number >= 1000000:
        temp = number/1000000
        return "{0}M".format(round(temp, 2))
    
    if number >= 1000:
        temp = number/1000
        return "{0}K".format(round(temp, 2))
    return "{0}".format(round(number, 2))

##### MAIN FUNC    
def read_followers(url, channel):
    from urllib.parse import quote
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    xPathAddress = []
    if channel == SupplierChannel.FB_GROUP:
        xPathAddress.append(XPATH.FB_GROUP)
    elif channel == SupplierChannel.FB_FANPAGE:
        xPathAddress.append(XPATH.FB_FANPAGE_1)
        xPathAddress.append(XPATH.FB_FANPAGE_2)
    elif channel == SupplierChannel.FB_PERSONAL:
        xPathAddress.append(XPATH.FB_PERSONAL_1)
        xPathAddress.append(XPATH.FB_PERSONAL_2)
    elif channel == SupplierChannel.TIKTOK_COMMUNITY:
        xPathAddress.append(XPATH.TIKTOK_COMMUNITY)
    elif channel == SupplierChannel.TIKTOK_PERSONAL:
        xPathAddress.append(XPATH.TIKTOK_PERSONAL)
    elif channel == SupplierChannel.YOUTUBE_COMMUNITY:
        xPathAddress.append(XPATH.YOUTUBE_COMMUNITY)
    elif channel == SupplierChannel.YOUTUBE_PERSONAL:
        xPathAddress.append(XPATH.YOUTUBE_PERSONAL)
    elif channel == SupplierChannel.INSTAGRAM:
        xPathAddress.append(XPATH.INSTAGRAM)
    elif channel == SupplierChannel.FORUM:
        xPathAddress.append(XPATH.FORUM)
    elif channel == SupplierChannel.WEBSITE:
        xPathAddress.append(XPATH.WEBSITE)
    elif channel == SupplierChannel.LINKED_IN:
        xPathAddress.append(XPATH.LINKED_IN)
    else:
        pass
    
    followers= None
    if len(xPathAddress) > 0:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        
        if channel == SupplierChannel.FB_PERSONAL:
            # check need login
            try:
                print('Login fb Start')
                #driver.get('https://www.facebook.com/')
                # actualTitle = driver.title
                # email = driver.find_element(By.ID,'email')
                # pwd = driver.find_element(By.ID,'pass')
                # submit = driver.find_element(By.ID,'loginbutton')
                # email.send_keys('brandcit2023@gmail.com')
                # pwd.send_keys('Aesx5099')

                # submit.click()
                # actualTitle = driver.title
                # currentUrl = driver.current_url
                # print('Login fb success -> ', actualTitle, currentUrl)

            except Exception as e:
                print('Check login page fb: ', str(e))
                # html = driver.page_source
                # time.sleep(2)
                # print('error current html', html)
                pass
        
        
        try:
            for xpath in xPathAddress:
                try:
                    if channel == SupplierChannel.TIKTOK_COMMUNITY or channel == SupplierChannel.TIKTOK_PERSONAL:
                        element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-e2e="followers-count"]')))
                    else:
                        element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, xpath.value)))
                    
                    if element:
                        text = element.text
                        print('read success for ', xpath, text, url)
                        followers = text.replace('followers','')
                        followers = followers.replace('people follow this','')
                        followers = followers.replace('members','')
                        followers = followers.replace('subscribers','')
                        followers = followers.replace('người theo dõi','')
                        followers = followers.replace('triệu ','M')
                        followers = followers.replace('ngàn ','K')
                        followers = followers.replace('nghìn ','K')
                        
                        followers = followers.strip()
                        try:
                            temp = convert_to_float(followers)
                            print('read success for followers = ', followers)
                            break
                        except Exception as e:
                            print('pass data success for ', channel, url, xpath)
                except Exception as e:
                    print('read not success for ', channel, url, xpath)
        except:
            print('read not success for ', channel, url)
        finally:
            driver.close()
            driver.quit()
        

    return convert_to_float(followers)