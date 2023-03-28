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
from urllib.parse import urlparse

##### MAIN FUNC    
def prepare_driver(shouldFbSetup = False, shouldInstagramSetup = False):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--lang=en-US')
    #options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--crash-dumps-dir=/tmp/selenium_dump/')


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_size(1920, 1080)
    if shouldInstagramSetup:
        driver = login_instagram(driver)

    if shouldFbSetup:
        driver = login_facebook(driver)
    
    return driver

def close_driver(driver):
    driver.close()
    driver.quit()

def login_instagram(driver):
    print('Try Login instagram')

    try:
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(10)
    except:
        print('Can not load instagram page')
        return driver
    email = ''
    pwd = ''
    with open(os.path.join(settings.BASE_DIR, 'secrets.json')) as secrets_file:
        data = json.load(secrets_file)
        email = data['s1']
        pwd = data['s2']
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys(email)
    except:
        print('can not locate username')
        return driver
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))).send_keys(pwd)
    except:
        print('can not locate pwd')
        return driver
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]'))).click()
    except:
        print('can not locate submit')
        return driver
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click() 
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()  #search for a text="Not Now"
    except:
        pass

    time.sleep(2)

    actualTitle = driver.title
    currentUrl = driver.current_url
    print('Login instagram Done -> ', actualTitle, currentUrl)
    
    return driver

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
        time.sleep(2)
        actualTitle = driver.title
        currentUrl = driver.current_url
        print('Login fb success -> ', actualTitle, currentUrl)
    except Exception as e:
        print('SKip login page fb', str(e))
        time.sleep(2)
    return driver

def read_followers(driver, supplier):
    url = supplier.link.strip()
    if url.startswith('http://') or url.startswith('https://'):
        pass
    else:
        url = 'https://' + url

    channel = supplier.channel
    print('url-channel', url, channel)
    if driver == None:
        print('Dont know why drive is None')
        return -1
    
    if support_sync(channel) == False:
        print('Dont know why not support channel', channel)
        return -1

    xPathAddress = prepareXpath(channel)
    
    followers = None
    try:
        driver.get(url)
    except:
        print('Can not load this link', url)
        return -1
    if isFbChannel(channel):
        if isFbLinkNotValid(driver):
            print('This kol is not valid')
            return -1

    if channel == SupplierChannel.TIKTOK_COMMUNITY or channel == SupplierChannel.TIKTOK_PERSONAL:
        element = findFollowerElementOfTiktok(driver)
        if element:
            followers = read_element(element)
    elif isFbChannel(channel):
        element = findFbGeneralElement(driver)
        followers = read_element(element)
        if followers == None:
            element = findFbPersonalElement(driver)
            followers = read_element(element)
        if followers == None:
            element = findFbFanPageElement(driver, url)
            followers = read_element(element)
        if followers == None:
            element = findFbGroupElement(driver, url)
            followers = read_element(element)
    elif channel == SupplierChannel.INSTAGRAM:
        element = findFollowerElementOfInstagram(driver)
        if element:
            followers = read_element(element)
    elif channel == SupplierChannel.YOUTUBE_PERSONAL:
        element = findFollowerElementOfYoutubePersonal(driver)
        if element:
            followers = read_element(element)
    elif channel == SupplierChannel.YOUTUBE_COMMUNITY:
        element = findFollowerElementOfYoutubePersonal(driver)
        if element:
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
    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'Bạn hiện không xem được nội dung này')]")
        if element:
            return True
    except:
        pass
    return False

def findFbGeneralElement(driver):
    print('Find by fb general')
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
                print('Can not read')
    except Exception as e:
        print('Can not read followers')
    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'people follow this')]")
        if element:
            return element
    except Exception as e:
        print('Can not find people follow this')

    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'người theo dõi')]")
        if element:
            return element
    except Exception as e:
        print('Can not find người theo dõi')
    
    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'members')]")
        if element and element.text:
            print('found fb members tag')
            return element
    except Exception as e:
        print('Can not find members')

    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'Thành viên')]")
        if element and element.text:
            print('found fb ThanhVien tag')
            return element
    except Exception as e:
        print('Can not find Thành viên')
    
    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'thành viên')]")
        if element and element.text:
            print('found fb thanhVien tag')
            return element
    except Exception as e:
        print('Can not find thành viên')

    return None

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
                print('Can not read')
    except Exception as e:
        print('Can not read')
    
    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),' người theo dõi Trang này')]")
        if element:
            return element
    except:
        pass
    return None

def findFbFanPageElement(driver, url):
    try:
        path = url
        p = urlparse(path)
        new_url = str(p.scheme) + "://" + p.netloc + p.path.removesuffix('/') + '/members'
        driver.get(new_url)
        time.sleep(2)
        elements = driver.find_elements(By.XPATH, '//a[contains(@href, "%s")]' % 'members')
        for a in elements:
            try:
                link = a.get_attribute('href')
                if link and 'members' in link:
                    print('FbFanPage link', link, a.text)
                    element = a
                    element.click()
                    time.sleep(2)
                    break
            except Exception as e:
                print('Can not read')
    except Exception as e:
        print('Can not read')
    
    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'người theo dõi')]")
        if element:
            return element
    except Exception as e:
        print('Can not find tag')
    
    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'members')]")
        if element and element.text:
            print('found fb members tag')
            return element
    except:
        pass

    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'Thành viên')]")
        if element and element.text:
            print('found fb ThanhVien tag')
            return element
    except:
        pass

    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'thành viên')]")
        if element and element.text:
            print('found fb thanhVien tag')
            return element
    except:
        pass


    return None

def findFbGroupElement(driver, url):
    print('try find by group')
    try:
        path = url
        p = urlparse(path)
        new_url = str(p.scheme) + "://" + p.netloc + p.path.removesuffix('/') + '/members/'
        driver.get(new_url)
        print('new_url', new_url)
        time.sleep(2)

        elements = driver.find_elements(By.XPATH, "//a[contains(@href, 'members')]")
        for a in elements:
            try:
                link = a.get_attribute('href')
                if link and 'members' in link:
                    print('FbGroup link', link, a.text)
                    element = a
                    element.click()
                    time.sleep(2)
                    break
                    #return element
            except Exception as e:
                print('find fb group error', str(e))
    except Exception as e:
        print('find fb group error 2', str(e))
    
    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'members')]")
        #element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'members')]")))
        if element and element.text:
            print('found fb members tag')
            return element
    except:
        pass

    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'Thành viên')]")
        #element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Thành viên')]")))
        if element and element.text:
            print('found fb ThanhVien tag')
            return element
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
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),' followers')]")))
        return element
    except Exception as e:
        print('findFollowerElementOfInstagram err', str(e))
        pass
    return None

def findFollowerElementOfYoutubePersonal(driver):    
    try:
        element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[1]/yt-formatted-string[2]")))
        return element
    except Exception as e:
        print('path 1 err', str(e))
        pass

    try:
        element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytm-app/div[1]/ytm-watch/div[2]/ytm-single-column-watch-next-results-renderer/ytm-slim-video-metadata-section-renderer/ytm-slim-owner-renderer/a/div/div/span")))
        return element
    except Exception as e:
        print('path 1 err', str(e))
        pass
    
    # try:
    #     element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'subscribers')]")))
    #     return element
    # except Exception as e:
    #     print('findFollowerElementOfYoutubePersonal err', str(e))
    #     pass

    return None

    


def read_element(element):
    if element:
        try:
            text = element.text.upper()
            print('text', text)
            followers = text.replace('FOLLOWERS','')
            
            followers = followers.replace('PEOPLE FOLLOW THIS','')
            followers = followers.replace('NGƯỜI THEO DÕI','')
            followers = followers.replace('MEMBERS','')
            followers = followers.replace('THÀNH VIÊN','')
            followers = followers.replace('· ','')
            followers = followers.replace('SUBSCRIBERS','')
            
            followers = followers.replace('PEOPLE','')
            followers = followers.replace('NGƯỜI','')
            followers = followers.replace('THEO DÕI','')
            followers = followers.replace('TRIỆU ','M')
            followers = followers.replace('NGÀN ','K')
            followers = followers.replace('NGHÌN ','K')
            
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