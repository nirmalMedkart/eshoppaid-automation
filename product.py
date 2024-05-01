import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import logging



username_xpath = '//*[@id="txtUserName"]'
password_xpath = '//*[@id="txtPassword"]'
login_button_xpath = '//*[@id="btnLogin"]'
login_button_1_xpath = '//*[@id="btnProceed"]'
master_link_xpath = '//*[@id="ctl00_IDASPxMenu_DXI0_T"]'


product_link_xpath = '//*[@id="Menu0"]'
modify_link_xpath = '//*[@id="Menu1"]'

product_code_xpath = '//*[@id="Menu0"]'
product_full_name_xpath = '//*[@id="txtProductFullName"]'
alternate_product_codes_xpath = '//*[@id="txtAlternateProductCodes"]'
package_info_xpath = '//*[@id="txtPackageInformation"]'
combination_xpath = '//*[@id="ASBCombinationCode"]'
allow_indent_xpath = '//*[@id="ddlAllowIndent"]'
purchase_price_xpath = '//*[@id="txtPurchasePrice"]'
purchase_tax_code_xpath = '//*[@id="ASBPurchaseTaxCode"]'
sales_price_xpath = '//*[@id="txtSalesPrice"]'
sales_tax_code_xpath = '//*[@id="ASBSalesTaxCode"]'
mrp_xpath = '//*[@id="txtMRP"]'
unit_description_xpath = '//*[@id="txtUnitDescription"]'
tax_category_xpath = '//*[@id="ASBTaxCategoryCode"]'
chapter_number_xpath = '//*[@id="ASBChapter"]'
accept_rate_xpath = '//*[@id="chkAcceptRate"]'
is_billable_xpath = '//*[@id="chkIsBillable"]'



# Main method
if __name__ == "__main__":

    product_code = int(input('Enter last product code: '))

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
    time.sleep(10)

    driver.find_element(By.XPATH,master_link_xpath).click()
    time.sleep(2)


    iframe = driver.find_element(By.XPATH,"//iframe[@id='fContent']")
    
    # Switch to the iframe
    driver.switch_to.frame(iframe)
    print("Successfully entered iframe.")
    frame = driver.find_element(By.XPATH,"//frame[@name='main']")
    driver.switch_to.frame(frame)
    print("Successfully entered frame.")
    time.sleep(5)

    driver.find_element(By.XPATH,product_link_xpath).click()
    time.sleep(3)
        
    driver.find_element(By.XPATH,modify_link_xpath).click()
    time.sleep(5)

    while True:
        print(f"product_code:==========>{product_code}")
        driver.find_element(By.XPATH,'//*[@id="btnProductSelection"]').click()
        select = Select(driver.find_element(By.XPATH,'//*[@id="ddlProductDataType"]'))
        select.select_by_visible_text("Product Code")
        time.sleep(3)

        input_element = driver.find_element(By.XPATH,'//*[@id="ASBProduct"]')
        driver.execute_script("arguments[0].value = arguments[1]", input_element, product_code)
        time.sleep(1)
        input_element.send_keys(Keys.ENTER)
        time.sleep(2)

        product_name = driver.find_element(By.XPATH,'//*[@id="txtProductName"]').get_attribute('value')

        time.sleep(1)
        product_full_name = driver.find_element(By.XPATH,product_full_name_xpath)
        product_full_name.clear()
        product_full_name.send_keys(product_name)
        time.sleep(0.2)
        
        alternate_product_codes = driver.find_element(By.XPATH,alternate_product_codes_xpath)
        alternate_product_codes.clear()
        alternate_product_codes.send_keys(product_code)
        time.sleep(0.2)

        package_info = driver.find_element(By.XPATH,package_info_xpath)
        package_info.clear()
        package_info.send_keys('Voucher')
        time.sleep(0.2)

        input_element = driver.find_element(By.XPATH,combination_xpath)
        value_to_send = 'No molecule'
        driver.execute_script("arguments[0].value = arguments[1]", input_element, value_to_send)
        time.sleep(4)
        input_element.send_keys(Keys.ENTER)

        select = Select(driver.find_element(By.XPATH,allow_indent_xpath))
        select.select_by_visible_text("Not Allowed")
        time.sleep(0.8)
        
        purchase_price = driver.find_element(By.XPATH,purchase_price_xpath)
        purchase_price.clear()
        purchase_price.send_keys('1')
        time.sleep(0.2)

        purchase_tax_code = driver.find_element(By.XPATH,purchase_tax_code_xpath)
        purchase_tax_code.clear()
        purchase_tax_code.send_keys('GSTEXEMPT')
        time.sleep(2)

        input_element.send_keys(Keys.ENTER)
        time.sleep(0.2)

        sales_price = driver.find_element(By.XPATH,sales_price_xpath)
        sales_price.clear()
        sales_price.send_keys('1')
        time.sleep(0.2)

        sales_tax_code = driver.find_element(By.XPATH,sales_tax_code_xpath)
        sales_tax_code.clear()
        sales_tax_code.send_keys('GSTEXEMPT')
        time.sleep(2)

        input_element.send_keys(Keys.ENTER)
        time.sleep(0.2)

        mrp = driver.find_element(By.XPATH,mrp_xpath)
        mrp.clear()
        mrp.send_keys('1')
        time.sleep(0.2)

        unit_description = driver.find_element(By.XPATH,unit_description_xpath)
        unit_description.clear()
        unit_description.send_keys('1')
        time.sleep(0.2)
            
        tax_category = driver.find_element(By.XPATH,tax_category_xpath)
        tax_category.clear()
        tax_category.send_keys('1234_0')
        time.sleep(15)
        input_element.send_keys(Keys.ENTER)
        
        chapter_number = driver.find_element(By.XPATH,chapter_number_xpath)
        chapter_number.clear()
        chapter_number.send_keys('1234')
        time.sleep(5)
        input_element.send_keys(Keys.ENTER)

        driver.find_element(By.XPATH,accept_rate_xpath).click()
        time.sleep(0.2)

        driver.find_element(By.XPATH,is_billable_xpath).click()
        time.sleep(0.2)
       
        driver.find_element(By.XPATH,'//*[@id="btnUpdate"]').click()

        
        alert = WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())
        
        msg = alert.text
        time.sleep(10)
        alert.accept()
        time.sleep(5)
        product_code += 1
       
            
    driver.close()
