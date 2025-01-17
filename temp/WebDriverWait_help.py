#-*- coding:utf-8 -*-
'''

Created on 2018年9月14日

@author: zhilh

'''

#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

base_url = "https://www.baidu.com"
option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
driver = webdriver.Chrome(options=option)

driver.implicitly_wait=5
'''隐式等待和显示等待都存在时，超时时间取二者中较大的'''
locator = (By.ID,'kw')
driver.get(base_url)

WebDriverWait(driver,10).until(EC.title_is(u"百度一下，你就知道"))
'''判断title,返回布尔值'''

WebDriverWait(driver,10).until(EC.title_contains(u"百度一下"))
'''判断title，返回布尔值'''

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'kw')))
'''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement'''

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'su')))
'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''

WebDriverWait(driver,10).until(EC.visibility_of(driver.find_element(by=By.ID,value='kw')))
'''判断元素是否可见，如果可见就返回这个元素'''

WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.mnav')))
'''判断是否至少有1个元素存在于dom树中，如果定位到就返回列表'''

WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR,'.mnav')))
'''判断是否至少有一个元素在页面中可见，如果定位到就返回列表'''

WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='u1']/a[8]"),u'设置'))
'''判断指定的元素中是否包含了预期的字符串，返回布尔值'''

WebDriverWait(driver,10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,'#su'),u'百度一下'))
'''判断指定元素的属性值中是否包含了预期的字符串，返回布尔值'''

#WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it(locator))
'''判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False'''
#注意这里并没有一个frame可以切换进去

WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#swfEveryCookieWrap')))
'''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素'''
#注意#swfEveryCookieWrap在此页面中是一个隐藏的元素

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='u1']/a[8]"))).click()
'''判断某个元素中是否可见并且是enable的，代表可点击'''
driver.find_element_by_xpath("//*[@id='wrapper']/div[6]/a[1]").click()
#WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='wrapper']/div[6]/a[1]"))).click()

#WebDriverWait(driver,10).until(EC.staleness_of(driver.find_element(By.ID,'su')))
'''等待某个元素从dom树中移除'''
#这里没有找到合适的例子

#WebDriverWait(driver,10).until(EC.element_to_be_selected(driver.find_element(By.XPATH,"//*[@id='nr']/option[1]")))
#'''判断某个元素是否被选中了,一般用在下拉列表'''

#WebDriverWait(driver,10).until(EC.element_selection_state_to_be(driver.find_element(By.XPATH,"//*[@id='nr']/option[1]"),True))
#'''判断某个元素的选中状态是否符合预期'''

#WebDriverWait(driver,10).until(EC.element_located_selection_state_to_be((By.XPATH,"//*[@id='nr']/option[1]"),True))
#'''判断某个元素的选中状态是否符合预期'''
#driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").click()

#instance = WebDriverWait(driver,10).until(EC.alert_is_present())
#'''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''
#print (instance.text)
#instance.accept()

driver.close()