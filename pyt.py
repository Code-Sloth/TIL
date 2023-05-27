# BeautifulSoup
from bs4 import BeautifulSoup
import requests
# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# 실습 폴더 리스트 생성
folder_practice = []
folder_example = []

# 상위 폴더: YYMMDD
# 하위 폴더: 1_example / 1_practice
# folder = str(date.today().strftime("%y%m%d"))
folder = 'test'
example = '1_example'
practice = '2_practice'

# 예제 / 실습 폴더 경로
dirs_example = folder + '/' + example
dirs_practice = folder + '/' + practice

# line 49: 창 화면 O / line 50: 창 화면 X / line 51: 불필요한 메시지 제거
options = Options()
# options.add_experimental_option("detach", True)
options.add_argument("headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 실라버스 url
url = 'https://syllaverse.com/courses/17/s/15/curriculum/2023-01-18/contents/153/assignments/107'
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# 1920 x 1080 기준 창 화면 시작 좌표
driver.set_window_position(960,10)
print(BRIGHT_BLUE + '\n===========실행 중===========' + BRIGHT_END)

# 페이지 로딩 대기(5초), 만약 5초 안에 로딩되면 바로 실행
driver.implicitly_wait(5)
driver.get(url)

# ID / PASSWORD / 로그인
# ID, PW에 입력 해 주세요
Email = 'djqmflsk@naver.com'
PW = 'alsdnr12@'
driver.find_element(By.ID, 'email').send_keys(Email)
driver.find_element(By.ID, 'password').send_keys(PW)
driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/main/form/button').click()
print(BRIGHT_GREEN + '로그인 성공' + BRIGHT_END)

try:
    # 예제 페이지 이동 후 로딩시간 대기
    driver.find_element(By.XPATH, "//span[contains(text(), '예제')]").click()
    print(BRIGHT_YELLOW + '예제 페이지 이동' + BRIGHT_END)
    
    # 테이블 접근
    table = driver.find_element(By.XPATH, '//*[@id="app"]/main/main/main/div[2]/main/section/div/div/section/p/table')
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    rows = tbody.find_elements(By.TAG_NAME, 'tr')
    for index, value in enumerate(rows):
        # 예제문제 번호 / 이름 / 주소
        num = value.find_elements(By.TAG_NAME, 'td')[0].text    
        name = value.find_elements(By.TAG_NAME, 'td')[1].text    
        address = value.find_elements(By.TAG_NAME, 'td')[2].text    
        folder_example.append([num, name, address])
    print(BRIGHT_GREEN + '예제 테이블 리스트 생성 완료' + BRIGHT_END)

    # 대시보드 이동 후 로딩시간 대기
    driver.find_element(By.XPATH, "//span[contains(text(), '대시보드')]").click()
    print(BRIGHT_YELLOW + '메인 페이지 이동' + BRIGHT_END)

    try:
        # 실습 페이지 이동 후 로딩시간 대기
        driver.find_element(By.XPATH, "//span[contains(text(), '실습')]").click()
        print(BRIGHT_YELLOW + '실습 페이지 이동' + BRIGHT_END)
        
        # 테이블 접근
        table = driver.find_element(By.XPATH, '//*[@id="app"]/main/main/main/div[2]/main/section/div/div/section/p/table')
        tbody = table.find_element(By.TAG_NAME, 'tbody')
        rows = tbody.find_elements(By.TAG_NAME, 'tr')
        for index, value in enumerate(rows):
            # 실습문제 번호 / 이름 / 주소
            num = value.find_elements(By.TAG_NAME, 'td')[0].text
            name = value.find_elements(By.TAG_NAME, 'td')[1].text
            address = value.find_elements(By.TAG_NAME, 'td')[2].text
            folder_practice.append([num, name, address])
        print(BRIGHT_GREEN + '실습 테이블 리스트 생성' + BRIGHT_END)

        # 예제 파일
        os.makedirs(dirs_example, exist_ok=True)
        for i in folder_example:            
            # ex) '1234_덧셈.py' 파일 생성 / 파일 안에 ex) '# 1234 덧셈 <문제링크>' 작성   
            code = "\nimport sys\nsys.stdin = open('" './'+ dirs_example + '/' + str(i[0]) + "_input.txt', 'r')" + '\n' + 'input = sys.stdin.readline' + '\n\n'
            file_name = i[0] + '_' + i[1] + '.py'
            write_file = '# ' + i[0] + ' ' + i[1] + ' ' + i[2] + code
            f = open(dirs_example + '/' + file_name, 'w', encoding='UTF-8')
            f.write(write_file)            
        f.close()
        print(BRIGHT_GREEN + '예제 파일 생성 완료' + BRIGHT_END)

        # 실습 파일
        os.makedirs(dirs_practice, exist_ok=True)
        for i in folder_practice:
            # ex) '5678_뺄셈.py' 파일 생성 / 파일 안에 ex) '# 5678 뺄셈 <문제링크>' 작성
            code = "\nimport sys\nsys.stdin = open('" './'+ dirs_practice + '/' + str(i[0]) + "_input.txt', 'r')" + '\n' + 'input = sys.stdin.readline' + '\n\n'
            file_name = i[0] + '_' + i[1] + '.py'
            write_file = '# ' + i[0] + ' ' + i[1] + ' ' + i[2] + code
            f = open(dirs_practice + '/' + file_name, 'w', encoding='UTF-8')
            f.write(write_file)
        f.close()
        print(BRIGHT_GREEN + '실습 파일 생성 완료' + BRIGHT_END)    
        
        # input 파일 생성
        print(BRIGHT_YELLOW + '예제 input 파일 생성 중' + BRIGHT_END)
        for i in folder_example:
            url = i[2]
            driver.get(url)
            input_file_name = i[0] + '_input.txt'
            sample = driver.find_element(By.ID, 'sample-input-1').text
            f = open(dirs_example + '/' + input_file_name, 'w')
            f.write(sample)
        f.close()
        print(BRIGHT_GREEN + '예제 input 파일 생성 완료' + BRIGHT_END)

        print(BRIGHT_YELLOW + '실습 input 파일 생성 중' + BRIGHT_END)
        for i in folder_practice:
            url = i[2]
            driver.get(url)
            input_file_name = i[0] + '_input.txt'
            sample = driver.find_element(By.ID, 'sample-input-1').text
            f = open(dirs_practice + '/' + input_file_name, 'w')
            f.write(sample)
        f.close()
        print(BRIGHT_GREEN + '실습 input 파일 생성 완료' + BRIGHT_END)

        print('예제 O / 실습 O')

        print(BRIGHT_RED + '===========종료 중===========' + BRIGHT_END)
    except:
        # 예제 파일 생성
        os.makedirs(dirs_example, exist_ok=True)
        for i in folder_example:
            # ex) '1234_덧셈.py' 파일 생성 / 파일 안에 ex) '# 1234 덧셈 <문제링크>' 작성
            code = "\nimport sys\nsys.stdin = open('" './'+ dirs_example + '/' + str(i[0]) + "_input.txt', 'r')" + '\n' + 'input = sys.stdin.readline' + '\n\n'
            file_name = i[0] + '_' + i[1] + '.py'
            write_file = '# ' + i[0] + ' ' + i[1] + ' ' + i[2] + code
            f = open(dirs_example + '/' + file_name, 'w', encoding='UTF-8')
            f.write(write_file)
        f.close()
        print(BRIGHT_GREEN + '예제 파일 생성 완료' + BRIGHT_END)        

        print(BRIGHT_YELLOW + '예제 input 파일 생성 중' + BRIGHT_END)
        for i in folder_example:
            url = i[2]
            driver.get(url)
            input_file_name = i[0] + '_input.txt'
            sample = driver.find_element(By.ID, 'sample-input-1').text
            f = open(dirs_example + '/' + input_file_name, 'w')
            f.write(sample)
        f.close()
        print(BRIGHT_GREEN + '예제 input 파일 생성 완료' + BRIGHT_END)

        print('예제 O / 실습 X')

        print(BRIGHT_RED + '===========종료 중===========' + BRIGHT_END)
except:
    try:
        # 실습 페이지 이동 후 로딩시간 대기
        driver.find_element(By.XPATH, "//span[contains(text(), '실습')]").click()
        print(BRIGHT_YELLOW + '실습 페이지 이동' + BRIGHT_END)
        
        # 테이블 접근
        table = driver.find_element(By.XPATH, '//*[@id="app"]/main/main/main/div[2]/main/section/div/div/section/p/table')
        tbody = table.find_element(By.TAG_NAME, 'tbody')
        rows = tbody.find_elements(By.TAG_NAME, 'tr')
        for index, value in enumerate(rows):
            # 실습문제 번호 / 이름 / 주소
            num = value.find_elements(By.TAG_NAME, 'td')[0].text
            name = value.find_elements(By.TAG_NAME, 'td')[1].text
            address = value.find_elements(By.TAG_NAME, 'td')[2].text
            folder_practice.append([num, name, address])
        print(BRIGHT_GREEN + '실습 테이블 리스트 생성' + BRIGHT_END)

        # 실습 파일 생성
        os.makedirs(dirs_practice, exist_ok=True)
        for i in folder_practice:
            # ex) '5678_뺄셈.py' 파일 생성 / 파일 안에 ex) '# 5678 뺄셈 <문제링크>' 작성
            
            code = "\nimport sys\nsys.stdin = open('" './'+ dirs_practice + '/' + str(i[0]) + "_input.txt', 'r')" + '\n' + 'input = sys.stdin.readline' + '\n\n'
            file_name = i[0] + '_' + i[1] + '.py'            
            write_file = '# ' + i[0] + ' ' + i[1] + ' ' + i[2] + code
            f = open(dirs_practice + '/' + file_name, 'w', encoding='UTF-8')
            f.write(write_file)
        f.close()
        print(BRIGHT_GREEN + '실습 파일 생성 완료' + BRIGHT_END)        

        print(BRIGHT_YELLOW + '실습 input 파일 생성 중' + BRIGHT_END)
        for i in folder_practice:
            url = i[2]
            driver.get(url)
            input_file_name = i[0] + '_input.txt'
            sample = driver.find_element(By.ID, 'sample-input-1').text
            f = open(dirs_practice + '/' + input_file_name, 'x')
            f.write(sample)
        f.close()
        print(BRIGHT_GREEN + '실습 input 파일 생성 완료' + BRIGHT_END)

        print('예제 X / 실습 O')

        print(BRIGHT_RED + '===========종료 중===========' + BRIGHT_END)
    except:
        print('예제 X / 실습 X')
        print(BRIGHT_RED + '===========종료 중===========' + BRIGHT_END)
    
finally:
    driver.quit()