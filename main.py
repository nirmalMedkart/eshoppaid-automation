import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import datetime
from selenium.webdriver.common.alert import Alert
import logging


username_xpath = '//*[@id="txtUserName"]'
password_xpath = '//*[@id="txtPassword"]'
login_button_xpath = '//*[@id="btnLogin"]'
login_button_1_xpath = '//*[@id="btnProceed"]'
master_link_xpath = '//*[@id="ctl00_IDASPxMenu_DXI0_T"]'
payment_grouping_link_xpath = '//*[@id="Menu9"]'
gift_voucher_link_xpath = '//*[@id="Menu1"]'

gift_voucher_name = '//*[@id="txtGVDenominationName"]'
gift_voucher_type = '//*[@id="ASBGVTypeCode"]'
inventory_type = '//*[@id="ddlInventoryType"]'
gv_prefix = '//*[@id="txtGVPrefix"]'

gv_length = '//*[@id="txtGVLength"]'
discount_type = '//*[@id="ddlDiscountType"]'
discount_level = '//*[@id="ddlDiscountLevel"]'
point_value = '//*[@id="txtPoints"]'
gift_voucher_value = '//*[@id="txtGVValue"]'
validation_type = '//*[@id="ddlValidationType"]'
valid_from = '//*[@id="txtValidFrom"]'
valid_to = '//*[@id="txtValidTo"]'
minimum_bill_value = '//*[@id="txtMinimumBillValue"]'
usage_level = '//*[@id="ddlUsageLevel"]'
minimum_bill_value_to_redeem = '//*[@id="txtMinimumBillValuetoRedeem"]'
consider_is_discount = '//*[@id="chkConsiderIsDiscount"]'
is_active = '//*[@id="chkIsActive"]'
currency = '//*[@id="ASBCurrency"]'


# response = ['SUCCESS', 'ERROR']

def fileToDf(file_path):
    df = pd.read_excel(file_path)
    print(f"Excel file found and read.")
    return df


# Main method
if __name__ == "__main__":

     
    input_path = r"C:\Nirmal\Python\eshopaid pos\v.xlsx"
    # input_path = input("Enter file path with file name: ")

    df = fileToDf(input_path)

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    driver.get("https://medkart.eshopaid.com/shopaid/authpages/Login.aspx")

    driver.find_element(By.XPATH,username_xpath).send_keys('nilaksh')
    time.sleep(0.2)

    driver.find_element(By.XPATH,password_xpath).send_keys('P@ss@199')
    time.sleep(0.2)

    driver.find_element(By.XPATH,login_button_xpath).click()
    time.sleep(5)

    driver.find_element(By.XPATH,login_button_1_xpath).click()
    time.sleep(8)

    driver.find_element(By.XPATH,master_link_xpath).click()
    time.sleep(2)


    iframe = driver.find_element(By.XPATH,"//iframe[@id='fContent']")
    
    # Switch to the iframe
    driver.switch_to.frame(iframe)
    print("Successfully entered iframe.")
    frame = driver.find_element(By.XPATH,"//frame[@name='main']")
    driver.switch_to.frame(frame)
    print("Successfully entered frame.")
    time.sleep(2)

    driver.find_element(By.XPATH,payment_grouping_link_xpath).click()
    time.sleep(3)
        
    driver.find_element(By.XPATH,gift_voucher_link_xpath).click()
    time.sleep(3)

    for index, row in df.iterrows():
        print(row['gift_voucher_name'])
        print(row['gv_length'])
        print(row['gift_voucher_value'])

    
    
        # driver.get('https://medkart.eshopaid.com/shopaid/rpt_shopaidpages/eShopaidMenu.aspx?MenuID=2380')
        # time.sleep(15)
        


        # fill up the gift voucher form

        driver.find_element(By.XPATH,gift_voucher_name).send_keys(row['gift_voucher_name'])
        time.sleep(0.8)

        # driver.find_element(By.XPATH,gift_voucher_type).send_keys('01_WA_CASH_IN_WALLET_WONDERSOFT_OFFER_ACTIVATION')

        input_element = driver.find_element(By.XPATH,gift_voucher_type)
        value_to_send = '01_WA_CASH_IN_WALLET_WONDERSOFT_OFFER_ACTIVATION'
        driver.execute_script("arguments[0].value = arguments[1]", input_element, value_to_send)
        time.sleep(8)
        input_element.send_keys(Keys.ENTER)


        select = Select(driver.find_element(By.XPATH,inventory_type))
        select.select_by_visible_text("NonInventory")
        time.sleep(0.8)
        
        driver.find_element(By.XPATH,gv_prefix).send_keys('0')

        driver.find_element(By.XPATH,gv_length).send_keys(row['gv_length'])

        select = Select(driver.find_element(By.XPATH,discount_type))
        select.select_by_visible_text("Value")
        time.sleep(0.8)
        
        select = Select(driver.find_element(By.XPATH,discount_level))
        select.select_by_visible_text("BillLevel")
        time.sleep(0.8)

        driver.find_element(By.XPATH,point_value).send_keys('0')
        time.sleep(0.8)

        driver.find_element(By.XPATH,gift_voucher_value).send_keys(row['gift_voucher_value'])
        
        select = Select(driver.find_element(By.XPATH,validation_type))
        select.select_by_visible_text("FromToDate")
        time.sleep(0.8)

        
        fromDate = driver.find_element(By.XPATH,valid_from)
        driver.execute_script("arguments[0].removeAttribute('readonly')", fromDate)
        fromDate.send_keys(datetime.now().strftime("%d/%m/%Y"))

        toDate = driver.find_element(By.XPATH,valid_to)
        driver.execute_script("arguments[0].removeAttribute('readonly')", toDate)
        toDate.send_keys('31/12/2025')

        driver.find_element(By.XPATH,minimum_bill_value).send_keys('0')


        select = Select(driver.find_element(By.XPATH,usage_level))
        select.select_by_visible_text("AnyWhere")
        time.sleep(0.8)


        driver.find_element(By.XPATH,minimum_bill_value_to_redeem).send_keys('0')
        time.sleep(0.2)
        driver.find_element(By.XPATH,consider_is_discount).click()
        time.sleep(0.2)
        driver.find_element(By.XPATH,is_active).click()
        time.sleep(0.2)
        driver.find_element(By.XPATH,currency).send_keys('Rupees')
        time.sleep(4)
        input_element.send_keys(Keys.ENTER)
        time.sleep(0.2)
        driver.find_element(By.XPATH,'//*[@id="btnUpdate"]').click()

        time.sleep(5)

        alert = WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())

        msg = alert.text
        
        alert.accept()
        time.sleep(5)
        
    driver.close()


