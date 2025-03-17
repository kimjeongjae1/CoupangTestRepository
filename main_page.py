from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from hide import EMAIL, PASSWORD
class MainPage:
    URL = "https://www.coupang.com"
    SEARCH_INPUT_ID = "headerSearchKeyword"


    #객체를 인스턴스화 시킬 때, 내가 원하는 설정으로 셋업을 하는 함수
    def __init__(self, driver: WebDriver): 
        self.driver = driver


    #쿠팡 웹 사이트 오픈 기능
    def open(self):
        self.driver.get(self.URL)

    #서치 기능 구현
    def search_items(self, item_name: str):
        search_input_box = self.driver.find_element(By.ID, self.SEARCH_INPUT_ID)
        search_input_box.send_keys(item_name)
        search_input_box.send_keys(Keys.ENTER)



    def click_LINK_TEXT(self, lick_text: str):
        login_button = self.driver.find_element(By.LINK_TEXT, lick_text)
        login_button.click()

    #로그인 기능 구현
    def login(self, email: str = EMAIL , password: str = PASSWORD ):
        # 로그인 페이지 이동
        self.open()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "로그인"))
        ).click()

        # 이메일 입력
        input_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='login-email-input']"))
        )
        input_email.send_keys(email)

        # 비밀번호 입력
        input_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='login-password-input']"))
        )
        input_password.send_keys(password)

        # 로그인 버튼 클릭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='memberLogin']/div[1]/form/div[5]/button"))
        ).click()


    #검색결과 비교
    def get_search_results(self, xpath: str = "//form//ul/li"):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return [item.text for item in self.driver.find_elements(By.XPATH, xpath)]