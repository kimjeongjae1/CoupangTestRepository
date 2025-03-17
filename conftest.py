import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 전역변수로 index 관리
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/91.0"
]
agent_index = 0

@pytest.fixture(scope="function")
def driver():
    global agent_index

    # User-Agent 순환 선택
    selected_agent = user_agents[agent_index]
    print(f"🛠️ 현재 User-Agent: {selected_agent}")

    # 다음 실행 때 다른 User-Agent 쓰게 index 조정
    agent_index = (agent_index + 1) % len(user_agents)

    # 크롬 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={selected_agent}")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # 드라이버 생성
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"Referer": "https://www.coupang.com/"}})
    driver.execute_cdp_cmd("Network.clearBrowserCache", {})
    driver.delete_all_cookies()

    # 대기 시간 설정
    driver.implicitly_wait(5)
    
    yield driver
    driver.quit()
