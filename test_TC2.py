import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException , TimeoutException
from selenium.webdriver.common.by import By
from main_page import MainPage
from selenium.webdriver.common.action_chains import ActionChains
import random


class Test_TC2:
    def test_basket(self, driver: WebDriver):
        try:
        

            ITEMS_XPATH = "//form//ul/li"  # 상품 리스트 XPath
            main_page = MainPage(driver)
            main_page.open()
            
            time.sleep(2)

            main_page.login()
            time.sleep(2)

            wait = ws(driver, 10)  # 페이지가 열릴 때까지 10초 대기
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url

            time.sleep(2)

            # '노트북' 검색
            main_page.search_items('노트북')

            # 상품들이 로드될 때까지 대기
            ws(driver, 20).until(EC.presence_of_element_located((By.XPATH, ITEMS_XPATH)))
            items = driver.find_elements(By.XPATH, ITEMS_XPATH)

            # 상품 리스트 중에서 랜덤으로 하나 선택
            if items:
                # 랜덤으로 상품 하나 선택
                random_item = random.choice(items)
                
                # 해당 상품을 클릭할 수 있도록 대기
                ws(driver, 10).until(EC.element_to_be_clickable(random_item))
                
                # 클릭하기 전에 마우스를 해당 상품으로 이동
                actions = ActionChains(driver)
                actions.move_to_element(random_item).perform()  # 마우스를 상품으로 이동
                time.sleep(random.uniform(0.5, 1))  # 자연스러운 대기

                random_item.click()  # 상품 클릭
                time.sleep(random.uniform(2, 4))  # 클릭 후 기다리기
            else:
                print("검색된 상품이 없습니다.")
                return

            # 장바구니에 추가하기
            add_basket = ws(driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='contents']/div[2]/div[1]/div[3]/div[16]/div[2]/div[2]/div/button[1]")
                )
            )
            add_basket.click()

            # 장바구니 페이지로 이동
            time.sleep(random.uniform(2, 4))
            main_page.click_LINK_TEXT('장바구니')

        except Exception as e:
            print(f"Error: {e}")