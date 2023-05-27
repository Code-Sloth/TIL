# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# Python
import os
from datetime import date

BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'
BRIGHT_END = '\033[0m'

"""
pip 명령어로 각 모듈 설치해 주세요
$ pip install beautifulsoup4
$ pip install selenium
$ pip install webdriver_manager
"""

h3_tags = []

# 폴더: YYMMDD
folder = str(date.today().strftime("%y%m%d"))

# 과제 폴더 경로
dirs_example = folder + '/'

# 드라이버 옵션
options = Options()
options.add_argument("headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 실라버스 url
url = 'https://syllaverse.com'
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
print(BRIGHT_BLUE + '\n===========실행 중===========' + BRIGHT_END)

# 페이지 로딩 대기(5초), 만약 5초 안에 로딩되면 바로 실행
driver.implicitly_wait(5)
driver.get(url)

# ID / PASSWORD / 로그인
# ID, PW에 입력 해 주세요
Email = 'djqmflsk@naver.com'
PW = 'alsdnr12@'

def login(driver):
    driver.find_element(By.ID, 'email').send_keys(Email)
    driver.find_element(By.ID, 'password').send_keys(PW)
    driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/main/form/button').click()

def move(driver):
    driver.find_element(By.XPATH, "//*[@id='app']/main/main/main/div[2]/main/section[2]/ul/li[3]/div[1]").click()

def makefile(driver):
    h3_tags = driver.find_elements(By.TAG_NAME, 'h3')
    os.makedirs(dirs_example, exist_ok=True)
    for i in range(len(h3_tags)):
        code = '<!DOCTYPE html>\n<html lang="en">\n<head>\n  <meta charset="UTF-8">\n  <meta http-equiv="X-UA-Compatible" content="IE=edge">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <title>Document</title>\n</head>\n<body>\n  \n</body>\n</html>'
        file_name = '0' + str(i+1) + '.html'
        write_file = code
        f = open(dirs_example + '/' + file_name, 'w', encoding='UTF-8')
        f.write(write_file)
    f.close()
    print(BRIGHT_GREEN + '파일 생성 완료' + BRIGHT_END)

try:
    login(driver)
    print(BRIGHT_GREEN + '로그인 성공' + BRIGHT_END)
    try:
        move(driver)
        print(BRIGHT_YELLOW + '과제 페이지 이동' + BRIGHT_END)
        try:
            makefile(driver)
        except:
            print('과제 폴더 생성 실패')
    except:
        print('과제 페이지 이동 실패')
except:
    print('로그인 실패')
finally:
    print(BRIGHT_RED + '===========종료 중===========' + BRIGHT_END)
    driver.quit()