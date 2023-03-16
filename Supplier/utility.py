# -*- coding: utf-8 -*-
from .supportmodels import SupplierChannel, XPATH, support_sync, isFbChannel
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
def prepare_driver(shouldFbSetup = False):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--crash-dumps-dir=/tmp/selenium_dump/')


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    if shouldFbSetup:
        driver = login_facebook(driver)
    return driver

def close_driver(driver):
    driver.close()
    driver.quit()

def login_facebook(driver):
    print('Try Login fb')

    try:
        driver.get('https://www.facebook.com/')
    except:
        print('Can not load fb page')
        return driver

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
        print('SKip login page fb', str(e))
        time.sleep(2)
    return driver

def read_followers(driver, supplier):
    url = supplier.link
    print('url', url)
    if url.startswith('http://') or url.startswith('https://') or url.startswith('www.'):
        pass
    else:
        url = 'https://' + url

    channel = supplier.channel
    if driver == None:
        print('Dont know why drive is None')
        return -1
    
    if support_sync(channel) == False:
        return -1

    xPathAddress = prepareXpath(channel)
    
    followers = None
    try:
        driver.get(url)
    except:
        print('Can not load this link', url)
        return -1
    
    if channel == SupplierChannel.TIKTOK_COMMUNITY or channel == SupplierChannel.TIKTOK_PERSONAL:
        element = findFollowerElementOfTiktok(driver)
        followers = read_element(element)
    elif channel == SupplierChannel.FB_PERSONAL or channel == SupplierChannel.FB_FANPAGE:
        element = findFbPersonalElement(driver)
        followers = read_element(element)
    elif channel == SupplierChannel.FB_GROUP:
        element = findFbGroupElement(driver)
        followers = read_element(element)
    elif channel == SupplierChannel.INSTAGRAM:
        element = findFollowerElementOfInstagram(driver)
        followers = read_element(element)
    
    if followers == None and isFbChannel(channel):
        if isFbLinkNotValid(driver):
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
    if followers:
        try:
            value = convert_to_float(followers)
            return value
        except:
            pass
    return -1

def isFbLinkNotValid(driver):
    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'This content isn't available at the moment')]")
        if element:
            return True
    except:
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
                    print('FbGroup link', link)
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

def findFollowerElementOfInstagram(driver):
    try:
        time.sleep(3)
        element = driver.find_element(By.XPATH, "//*[contains(text(),' followers')]")
        return element
    except Exception as e:
        print('findFollowerElementOfInstagram err', str(e))
        pass
    return None

def read_element(element):
    if element:
        try:
            text = element.text
            followers = text.replace('followers','')
            
            followers = followers.replace('people follow this','')
            followers = followers.replace('người theo dõi','')
            followers = followers.replace('members','')
            followers = followers.replace('thành viên','')
            followers = followers.replace('subscribers','')
            
            followers = followers.replace('people','')
            followers = followers.replace('người','')
            followers = followers.replace('theo dõi','')
            followers = followers.replace('triệu ','M')
            followers = followers.replace('ngàn ','K')
            followers = followers.replace('nghìn ','K')
            
            followers = followers.strip()
            print('read_element text -> followers: ', text, followers)
            temp = convert_to_float(followers)
            return followers
        except Exception as e:
            print('read_element not success ', str(e))
            return None
    return None

def prepareXpath(channel):
    xPathAddress = []
    if channel == SupplierChannel.YOUTUBE_COMMUNITY:
        xPathAddress.append(XPATH.YOUTUBE_COMMUNITY)
    elif channel == SupplierChannel.YOUTUBE_PERSONAL:
        xPathAddress.append(XPATH.YOUTUBE_PERSONAL)
    elif channel == SupplierChannel.FORUM:
        xPathAddress.append(XPATH.FORUM)
    elif channel == SupplierChannel.WEBSITE:
        xPathAddress.append(XPATH.WEBSITE)
    elif channel == SupplierChannel.LINKED_IN:
        xPathAddress.append(XPATH.LINKED_IN)
    else:
        pass
    return xPathAddress