# -*- coding: utf-8 -*-
from .supportmodels import SupplierChannel, XPATH
from .utility_numbers import *
import time
import os
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

##### MAIN FUNC    
def support_sync(channel):
    supports = [
        SupplierChannel.FB_GROUP,
        SupplierChannel.FB_FANPAGE,
        SupplierChannel.FB_PERSONAL,
        SupplierChannel.TIKTOK_COMMUNITY,
        SupplierChannel.TIKTOK_PERSONAL,
        SupplierChannel.YOUTUBE_COMMUNITY,
        SupplierChannel.YOUTUBE_PERSONAL
    ]
    if channel in supports:
        return True

    # if channel == SupplierChannel.FB_GROUP:
    #     return True
    # if channel == SupplierChannel.FB_FANPAGE:
    #     return True
    # if channel == SupplierChannel.FB_PERSONAL:
    #     return True
    # if channel == SupplierChannel.TIKTOK_COMMUNITY:
    #     return True
    # if channel == SupplierChannel.TIKTOK_PERSONAL:
    #     return True
    # if channel == SupplierChannel.YOUTUBE_COMMUNITY:
    #     return True
    # if channel == SupplierChannel.YOUTUBE_PERSONAL:
    #     return True

    return False

def prepare_driver(shouldFbSetup = False):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    if shouldFbSetup:
        driver = login_facebook(driver)
    return driver

def close_driver(driver):
    driver.close()
    driver.quit()

def login_facebook(driver):
    print('Try Login fb')
    driver.get('https://www.facebook.com/')
    # Opening JSON file
    
    try:
        # actualTitle = driver.title
        emailView = driver.find_element(By.NAME,'email')
        pwdView = driver.find_element(By.NAME,'pass')
        submitView = None
        try:
            submitView = driver.find_element(By.ID,'loginbutton')
        except:
            try:
                submitView = driver.find_element(By.NAME,'login')
            except:
                print('SKip login page fb because can not find Login Button')
                return driver
        
        email = ''
        pwd = ''
        with open(os.path.join(settings.BASE_DIR, 'secrets.json')) as secrets_file:
            data = json.load(secrets_file)
            email = data['s1']
            pwd = data['s2']

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

def read_followers(driver, supplier):
    url = supplier.link
    channel = supplier.channel
    if driver == None:
        return -1
    
    if support_sync(channel) == False:
        return None

    xPathAddress = prepareXpath(channel)
    
    followers = None
    driver.get(url)
    if channel == SupplierChannel.TIKTOK_COMMUNITY or channel == SupplierChannel.TIKTOK_PERSONAL:
        element = findFollowerElementOfTiktok(driver)
        followers = read_element(element)
    elif channel == SupplierChannel.FB_PERSONAL or channel == SupplierChannel.FB_FANPAGE:
        element = findFbPersonalElement(driver)
        followers = read_element(element)
    elif channel == SupplierChannel.FB_GROUP:
        element = findFbGroupElement(driver)
        followers = read_element(element)
    
    if followers == None and (channel == SupplierChannel.FB_PERSONAL or channel == SupplierChannel.FB_FANPAGE or channel == SupplierChannel.FB_GROUP):
        if isFbLinkNotValid(driver):
            print('isFbLinkNotValid = TRUE, stop')
            return -1
        
    if followers == None and len(xPathAddress) > 0:
        try:
            for xpath in xPathAddress:
                try:
                    element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, xpath.value)))
                    followers = read_element(element)
                except Exception as e:
                    print('read not success for ', channel, url, xpath)
        except:
            print('read not success for ', channel, url)
        finally:
            pass
            # if should_close:
            #     driver.close()
            #     driver.quit()
    if followers:
        value = convert_to_float(followers)
        print('after followers = ', followers, ' - ', value)
        return value
    return -1

def isFbLinkNotValid(driver):
    try:
        className = 'xzueoph'
        allLinks = driver.find_elements(By.CLASS_NAME, className)
        for div in allLinks:
            try:
                contentDiv = div.text
                if contentDiv == 'Bạn hiện không xem được nội dung này' \
                    or contentDiv == 'Lỗi này thường do chủ sở hữu chỉ chia sẻ nội dung với một nhóm nhỏ, thay đổi người được xem hoặc đã xóa nội dung.':
                    return True
            except Exception as e:
                pass
    except Exception as e:
        pass
    return False

def findFbPersonalElement(driver):
    try:
        time.sleep(3)
        elements = driver.find_elements(By.XPATH, '//a[contains(@href, "%s")]' % 'followers')
        for a in elements:
            try:
                link = a.get_attribute('href')
                if link and 'followers' in link:
                    print('link', link)
                    element = a
                    return element
            except Exception as e:
                print('Can not read', str(e))
    except Exception as e:
        print('Can not read', str(e))
    
    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),' người theo dõi Trang này')]")
        if element:
            return element
    except:
        pass
    return None

def findFbGroupElement(driver):
    try:
        time.sleep(3)
        elements = driver.find_elements(By.XPATH, '//a[contains(@href, "%s")]' % 'members')
        for a in elements:
            try:
                link = a.get_attribute('href')
                if link and 'members' in link:
                    print('link', link)
                    element = a
                    return element
            except:
                pass 
    except:
        pass
    return None

def findFollowerElementOfTiktok(driver):
    try:
        element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-e2e="followers-count"]')))
        return element
    except:
        pass
    return None

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