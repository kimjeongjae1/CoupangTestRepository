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


            #수량 변경 테스트 진행
            item_add_button_xpath = "//*[@id='cartTable-other']/tr[2]/td[2]/div[3]/div[1]/div[2]"

            # 반복적으로 수량 추가 버튼 클릭
            while True:
                try:
                    # 수량 추가 버튼을 찾기
                    item_add_button = ws(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, item_add_button_xpath))
                    )

                    # 버튼 클릭
                    item_add_button.click()

                    
                    time.sleep(random.uniform(1, 2))

                    # 수량이 더 이상 추가되지 않으면 종료
                    # 수량 추가 버튼이 비활성화되었는지 확인
                    if not item_add_button.is_enabled():
                        print("더 이상 수량을 추가할 수 없습니다.")
                        break

                except Exception as e:
                    print(f"Error while adding quantity: {e}")
                    break

            item_delete_xpath = "//*[@id='cartTable-other']/tr[2]/td[2]/div[1]/a"
            item_delete = ws(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, item_delete_xpath))
                ).click()

            time.sleep(random.uniform(1, 2))

            # 장바구니 페이지 새로고침
            driver.refresh()
            time.sleep(2)

            # 장바구니가 비어있는지 확인
            empty_cart_xpath = "//*[@id='cartTable-other']/tr"  # 장바구니 항목을 확인할 XPath
            cart_items = driver.find_elements(By.XPATH, empty_cart_xpath)

            if not cart_items:
                print("장바구니가 비었습니다.")
            else:
                print("장바구니에 항목이 남아 있습니다.")    

        except Exception as e:
            print(f"Error: {e}")