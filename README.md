# Coupang TestCase작성 실습 소개



---


## Summary        

**Selenium** 및 **Pytest** 를 이용하여, <br>
[쿠팡 홈페이지](https://www.coupang.com/?src=1042016&spec=10304903&addtag=900&ctag=HOME&lptag=%EC%BF%A0%ED%8C%A1&itime=20250314141813&pageType=HOME&pageValue=HOME&wPcid=17366935701840614859101&wRef=www.google.com&wTime=20250314141813&redirect=landing&gclid=&mcid=22df332209914a15bd15cbb7f888cdaf&network=g "Overview" ) 오픈부터, 검색, 로그인 등 <br>
<U>**사용자가 반복해야 하는 테스트**</U> 들을 자동화 하는 스크립트를 짜는 프로젝트 입니다.


 

---   


## Skill INFO      
<img src=image/pngwing.com.png height=50 widht=50>
- Python <br>
<br>
<img src=image/seleniumlogo.png height=50 widht=50>
- Selenium <br>
<br>
<img src=image/Pytestlogo.png height=50 widht=50>
- Pytest <br>

---
***
---

##  Code Example
# 홈페이지 오픈, 로그인, 회원가입, 마이쿠팡, 장바구니 자동화 검증


        def test_click_lick_text(self, driver:WebDriver):
        try:
            time.sleep(2)

            main_page = MainPage(driver)
            main_page.open()
            
            time.sleep(2)

            wait = ws(driver, 10) #페이지가 열릴 때 까지 10초간 대기
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url
            
            main_page.click_LINK_TEXT('로그인')

            assert "login" in driver.current_url
            driver.save_screenshot('메인페이지_로그인_성공.jpg')

            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url


            time.sleep(2)
            main_page.click_LINK_TEXT('회원가입')
            assert "memberJoinFrm" in driver.current_url
            driver.save_screenshot('메인페이지_회원가입_성공.jpg')

            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url


            time.sleep(2)
            main_page.click_LINK_TEXT('장바구니')
            assert "cartView" in driver.current_url
            wait.until(EC.url_contains("cartView"))
            driver.save_screenshot('메인페이지_장바구니_성공.jpg')

            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url

            #비로그인 이므로 마이쿠팡 클릭 시 로그인으로 가야함
            time.sleep(2)
            main_page.click_LINK_TEXT('마이쿠팡')
            assert "login" in driver.current_url
            driver.save_screenshot('메인페이지_장바구니_성공.jpg')

            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url

        except NoSuchElementException as e:
            driver.save_screenshot('메인페이지_링크텍스트_실패_노서치.jpg')
            assert False

        except TimeoutException as e:
            driver.save_screenshot('메인페이지_링크텍스트_실패_노서치.jpg')
            assert False


---   

##  빌드 환경
~~Eclipse~~ <br>
**Visual Studio Code**  <br>
**Pytest 8.3.5** <br>