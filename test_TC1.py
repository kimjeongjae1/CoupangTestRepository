import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException , TimeoutException
from selenium.webdriver.common.by import By
from main_page import MainPage
from urllib import parse





class TestMainPage:
    
    def test_search_items_Nologin(self, driver: WebDriver):
        try:
            time.sleep(2)

            ITEMS_XPATH = "//form//ul/li"
            main_page = MainPage(driver)
            main_page.open()
            
            time.sleep(2)

            wait = ws(driver, 10) #페이지가 열릴 때 까지 10초간 대기
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url

            time.sleep(2) 


            main_page.search_items('노트북')

            ws(driver,20).until(EC.presence_of_element_located((By.XPATH, ITEMS_XPATH)))
            items = driver.find_elements(By.XPATH, ITEMS_XPATH)

            item_name = parse.quote('노트북')
            assert len(items) > 0
            assert item_name in driver.current_url


            driver.save_screenshot('메인페이지_검색_성공.jpg')
        except NoSuchElementException as e:
            driver.save_screenshot('메인페이지_검색_실패_노서치.png')
            assert False

        except TimeoutException as e:
            driver.save_screenshot('메인페이지_검색_실패_노서치.png')
            assert False



    #로그인 상태 검색
    
    def test_search_items_login(self, driver: WebDriver):
        try:
            time.sleep(2)

            ITEMS_XPATH = "//form//ul/li"
            main_page = MainPage(driver)
            main_page.open()
            
            time.sleep(2)

            main_page.login()
            time.sleep(2)

            wait = ws(driver, 10) #페이지가 열릴 때 까지 10초간 대기
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url

            time.sleep(2) 


            main_page.search_items('노트북')

            ws(driver,20).until(EC.presence_of_element_located((By.XPATH, ITEMS_XPATH)))
            items = driver.find_elements(By.XPATH, ITEMS_XPATH)

            item_name = parse.quote('노트북')
            assert len(items) > 0
            assert item_name in driver.current_url


            driver.save_screenshot('메인페이지_검색_성공.png')
        except NoSuchElementException as e:
            driver.save_screenshot('메인페이지_검색_실패_노서치.png')
            assert False

        except TimeoutException as e:
            driver.save_screenshot('메인페이지_검색_실패_노서치.png')
            assert False
        

    #검색결과 비교
    def test_compare_search(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)

            # 비로그인 상태 검색
            main_page.open()

            time.sleep(2)
            
            main_page.search_items('노트북')
            nologin_results = main_page.get_search_results()

            time.sleep(2)
            driver.back()
            
            # 로그인 상태 검색
            main_page.login()

            time.sleep(2)
            
            main_page.search_items('노트북')
            login_results = main_page.get_search_results()

            time.sleep(2)
            
            assert nologin_results == login_results, " 로그인/비로그인 검색 결과가 다릅니다!"
            print("로그인/비로그인 검색 결과가 동일합니다!")

            # 비교 결과 스크린샷 저장
            driver.save_screenshot('로그인_비로그인_결과비교성공.png')

        except Exception as e:
            print(f"❗테스트 실패: {e}")
            driver.save_screenshot('로그인_비로그인_결과비교실패.png')
            assert False