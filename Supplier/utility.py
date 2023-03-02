# -*- coding: utf-8 -*-
from .supportmodels import SupplierChannel, XPATH
import time
import re, os
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from django.conf import settings

def detectNumber(input):
    detec_input = (input or '').replace('  ', '')
    nums2 = re.compile(r"[+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d)?[\s]?[kK]?[mM]?")
    match = nums2.search(detec_input)
    if match:
        output = match.group(0)
        return output
    return None

def convert_to_float(follower_input):
    follower = follower_input or '-1'
    upperFollower = follower.upper()#.replace(",",".")
    if upperFollower.count(',') >= 2:
        upperFollower = upperFollower.replace(',','')
    if upperFollower.count('.') >= 2:
        upperFollower = upperFollower.replace('.','')
        
    value = 0
    if 'K' in upperFollower:
        upperFollower = upperFollower.replace(',', '.')
        tempK = upperFollower.split("K")
        try:
            value = float(tempK[0]) * 1000
        except:
            print("Can not convert follower thousands")
            raise Exception("The value of follower is not valid: " + str(follower_input  or ''))

    elif 'M' in upperFollower:
        upperFollower = upperFollower.replace(',', '.')
        tempK = upperFollower.split("M")
        try:
            value = float(tempK[0]) * 1000000
        except:
            print("Can not convert follower million")
            raise Exception("The value of follower is not valid: " + str(follower_input  or ''))
    else:
        try:
            upperFollower = upperFollower.replace('.','') #todo: consider In VN 1.000 -> 1000
            value = float(upperFollower)
        except:
            try:
                upperFollower = detectNumber(upperFollower)
                value = float(upperFollower)
            except:
                value = 0
                raise Exception("The value of follower is not valid: " + str(follower_input or ''))
    print('convert_to_float input = ', follower_input, ' - ', value)
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
def support_sync(channel):
    if channel == SupplierChannel.FB_GROUP:
        return True
    if channel == SupplierChannel.FB_FANPAGE:
        return True
    if channel == SupplierChannel.FB_PERSONAL:
        return True
    if channel == SupplierChannel.TIKTOK_COMMUNITY:
        return True
    if channel == SupplierChannel.TIKTOK_PERSONAL:
        return True
    if channel == SupplierChannel.TIKTOK_PERSONAL:
        return True
    if channel == SupplierChannel.YOUTUBE_COMMUNITY:
        return True
    if channel == SupplierChannel.YOUTUBE_PERSONAL:
        return True

    return False

def prepare_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def close_driver(driver):
    driver.close()
    driver.quit()

def login_facebook(driver):
    print('Try Login fb')
    #driver.get('https://www.facebook.com/')
    # Opening JSON file
    
    try:
        # actualTitle = driver.title
        emailView = driver.find_element(By.NAME,'email')
        pwdView = driver.find_element(By.NAME,'pass')
        submitView = driver.find_element(By.ID,'loginbutton')
        email = ''
        pwd = ''
        with open(os.path.join(settings.BASE_DIR, 'secrets.json')) as secrets_file:
            data = json.load(secrets_file)
            email = data['s1']
            pwd = data['s2']
        print(email)

        emailView.send_keys(email)
        pwdView.send_keys(pwd)
        submitView.click()
        actualTitle = driver.title
        currentUrl = driver.current_url
        print('Login fb success -> ', actualTitle, currentUrl)
    except Exception as e:
        print('SKip login page fb')
        time.sleep(2)
    return driver

def read_followers(driver, url, channel, should_close = True):
    if driver == None:
        return -1
    
    if support_sync(channel) == False:
        return None

    xPathAddress = prepareXpath(channel)
    
    followers= None
    if len(xPathAddress) > 0:
        if channel == SupplierChannel.FB_PERSONAL:
            # check need login
            driver.get(url)
            #time.sleep(5)
            driver = login_facebook(driver)

        driver.get(url)
        try:
            for xpath in xPathAddress:
                try:
                    if channel == SupplierChannel.TIKTOK_COMMUNITY or channel == SupplierChannel.TIKTOK_PERSONAL:
                        element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-e2e="followers-count"]')))
                    elif channel == SupplierChannel.FB_PERSONAL or channel == SupplierChannel.FB_FANPAGE:
                        time.sleep(3)
                        tag = 'x1i10hfl'
                        allLinks = driver.find_elements(By.CLASS_NAME, tag)
                        for a in allLinks:
                            try:
                                link = a.get_attribute('href')
                                if link and 'followers' in link:
                                    print('link', link)
                                    element = a
                                    break
                            except:
                                pass
                    else:
                        element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, xpath.value)))
                    followers = read_element(element)
                except Exception as e:
                    print('read not success for ', channel, url, xpath)
        except:
            print('read not success for ', channel, url)
        finally:
            if should_close:
                driver.close()
                driver.quit()
        

    return convert_to_float(followers)

def read_element(element):
    if element:
        try:
            text = element.text
            followers = text.replace('followers','')
            
            followers = followers.replace('people follow this','')
            followers = followers.replace('members','')
            followers = followers.replace('subscribers','')
            followers = followers.replace('người theo dõi','')
            followers = followers.replace('people','')
            followers = followers.replace('người','')
            followers = followers.replace('theo dõi','')
            followers = followers.replace('triệu ','M')
            followers = followers.replace('ngàn ','K')
            followers = followers.replace('nghìn ','K')
            
            followers = followers.strip()
            print('read_element followers = ', followers)
            temp = convert_to_float(followers)
            return followers
        except Exception as e:
            print('read_element not success for ', text)
            return None
    return None

def prepareXpath(channel):
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
    return xPathAddress