import  time
from    selenium        import  webdriver
from    selenium.webdriver.common.action_chains import  ActionChains
from    bs4             import  BeautifulSoup
# req = requests.get(url)
# req = requests.get(url, verify=False) SSL 오류가 발생하는 경우 회피 방법


# 크롤링 대상 사이트 리스트
# - Yes24 : https://www.yes24.com/Product/Category/MonthWeekBestSeller?categoryNumber=001
# - 교보문고 : https://product.kyobobook.co.kr/bestseller/total?period=003#?page=1&per=20&period=003&ymw=&bsslBksClstCode=A
# - 알라딘 : https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&BestType=MonthlyBest


# DB에 필요한 데이터 순서
# 도서
# isbn
# title
# onlinePrice
# 작가
# author
# 출판사
# publisher
# 판매처
# store
# 판매순위
# store_rank

driver = webdriver.Chrome()

def yes24_crawling():
    # Yes24 크롤링
    url = "https://www.yes24.com/Product/Category/MonthWeekBestSeller?categoryNumber=001"


    driver.get(url)
    time.sleep(2)

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    books = soup.select('.info_row.info_name')

    # 예스24의 월간 베스트24의 데이터 수집
    # 판매처별 순위를 넣기위한 temp
    temp =1
    for i in books:
        url = 'https://www.yes24.com' + i.select_one('.gd_name')['href']
        driver.get(url)
        time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        # 각 책의 데이터 크롤링
        isbn = soup.select_one('.tb_nor.tb_vertical > .b_size > tr:nth-of-type(3) > td').get_text()
        title = soup.select_one('.gd_name').get_text()
        onlinePrice = soup.select_one('.nor_price').get_text()
        author = soup.select_one('.gd_auth > a').get_text()
        publisher = soup.select_one('.gd_pub > a').get_text()
        store = '1'
        store_rank = temp
        temp += 1

        print(isbn)
        print(title)
        print(onlinePrice)
        print(author)
        print(publisher)
        print(store)
        print(store_rank)
        print('=================')


def kyobo_crawling():
    # 교보문고 크롤링
    url = "https://product.kyobobook.co.kr/bestseller/total?period=003#?page=1&per=20&period=003&ymw=&bsslBksClstCode=A"


    driver.get(url)
    time.sleep(2)

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    books = soup.select('.auto_overflow_contents')

    # 교보문고의 월간 베스트20의 데이터 수집
    # 판매처별 순위를 넣기위한 temp
    temp =1
    for i in books:
        url = i.select_one('.auto_overflow_inner > a')['href']
        driver.get(url)
        time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        # 각 책의 데이터 크롤링
        isbn = soup.select_one('.tbl_row_wrap > .tbl_row > tbody > tr > td').get_text()
        title = soup.select_one('.prod_title').get_text()
        onlinePrice = soup.select_one('.prod_price_box > .prod_price > .price > .val').get_text()
        author = soup.select_one('.prod_author_box.auto_overflow_wrap > .auto_overflow_contents > .auto_overflow_inner > .author > a').get_text()
        publisher = soup.select_one('.prod_info_text.publish_date > a').get_text()
        store = '2'
        store_rank = temp
        temp += 1

        print(isbn)
        print(title)
        print(onlinePrice)
        print(author)
        print(publisher)
        print(store)
        print(store_rank)
        print('=================')


def aladin_crawling():
    # 알라딘 크롤링
    url = "https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&BestType=MonthlyBest"


    driver.get(url)
    time.sleep(1)
    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    books = soup.select('.bo3')
    # books = soup.select('.ss_book_box > table > tbody > tr > td:nth-of-type(3) > table > tbody > tr:nth-of-type(1) > td:nth-of-type(1) > .ss_book_list:nth-of-type(1) > ul > li:nth-of-type(2)')
    # books = soup.select('.ss_book_box > .ss_book_list') 실패

    # 알라딘의 월간 베스트50의 데이터 수집
    # 판매처별 순위를 넣기위한 temp
    temp =1
    for i in books:
        url = i['href']
        print(url)
        driver.get(url)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 3000);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(3000, 6000);")
        time.sleep(1)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        # 각 책의 데이터 크롤링
        print(soup.select_one('.conts_info_list1 > ul > li:nth-of-type(1)').get_text())
        if soup.select_one('.conts_info_list1 > ul > li:nth-of-type(1)').get_text() == '양장본':
            isbn = soup.select_one('.conts_info_list1 > ul > li:nth-of-type(5)').get_text().split()[2]
        else:
            isbn = soup.select_one('.conts_info_list1 > ul > li:nth-of-type(4)').get_text().split()[2]
        title = soup.select_one('.Ere_bo_title').get_text()
        onlinePrice = soup.select_one('.Ere_fs24').get_text()
        author = soup.select_one('.tlist > ul > li:nth-of-type(3) > a').get_text()
        try: 
            element = soup.select_one('.introduction_nopic')
            if element is not None:
                author_detail = element.get_text()
        except AttributeError:
            try:
                element = soup.select_one('.introduction > div:nth-child(1) > a')
                if element is not None:
                    author_detail = element.get_text()
            except AttributeError:
                element = soup.select_one('.introduction')
                if element is not None:
                    author_detail = element.get_text()
        
        # try:
        #     author_detail = soup.select_one('.introduction_nopic').get_text()
        # except:
        #     try:
        #         author_detail = soup.select_one('.introduction > div:nth-child(1) > a').get_text()
        #     except:
        #         author_detail = soup.select_one('.introduction').get_text()
        if '(옮긴이)' in soup.select_one('.tlist > ul > li:nth-of-type(3)').get_text():
            publisher = soup.select_one('.tlist > ul > li:nth-of-type(3) > a:nth-of-type(3)').get_text()
        else:
            publisher = soup.select_one('.tlist > ul > li:nth-of-type(3) > a:nth-of-type(2)').get_text()

        store = '3'
        store_rank = temp
        temp += 1

        print(isbn)
        print(title)
        print(onlinePrice)
        print(author)
        print(author_detail)
        print(publisher)
        print(store)
        print(store_rank)
        print('=================')


# yes24_crawling()
# kyobo_crawling()
aladin_crawling()
# 크롬드라이버 종료
driver.quit() 