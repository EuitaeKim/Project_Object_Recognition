import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import re

from bs4 import BeautifulSoup
from tqdm import tqdm
import argparse

# 상호명, 주소 데이터 불러오기
df = pd.read_csv('3. ulsan_store_info.csv')

# selenium 실행
driver = webdriver.Chrome()

# 리뷰 url 탐색 및 df에 저장
for i, keyword in enumerate(df['업소명'].tolist()):
    print("이번에 찾을 키워드 :", i, f"/ {df.shape[0]} 행", keyword)
    
    try:
        naver_map_search_url = f'https://map.naver.com/v5/search/{keyword}/place'
        driver.get(naver_map_search_url)
        
        time.sleep(1)
        cu = driver.current_url
        
        res_code = re.findall(r"place/(\d+)", cu)
        final_url = 'https://pcmap.place.naver.com/restaurant/'+res_code[0]+'/review/visitor#'
        
        print(final_url)
        df['naver_map_url'][i]=final_url
        
    except IndexError:
        df['naver_map_url'][i]= ''
        print('none')

# url이 포함된 df 내보내기   
df.to_csv('4. ulsan_store_info_add_url_pre-pro.csv', encoding='utf-8-sig')


'''


위에까지 과정은 리뷰를 가져올 URL을 수집하는 부분이고
아래부터의 과정은 수집한 URL을 기반으로 본격적인 크롤링을 진행하는 부분입니다.


'''

# colab notebook에서 url이 없는 음식점을 제외시킨 df 불러오기
df = pd.read_csv('5. ulsan_store_review_raw_pre-pro.csv')

# 수집할 정보
rating_list = [] # 평점
user_review_id = {} # 유저 id
review_json = {} # 리뷰
image_json = {} # 이미지

# 리뷰 수집
for i in range(1800, len(df)):
    print('======================================================')
    print(str(i)+'번째 식당')
    
    driver.get(df['naver_map_url'][i])
    thisurl = df['naver_map_url'][i]
    time.sleep(2)
    # 더보기 버튼이 있을 시 다 누르기
    while True:
        try:
            time.sleep(1)
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            time.sleep(1)
            driver.find_element_by_css_selector('#app-root > div > div > div.place_detail_wrapper > div:nth-child(5) > div:nth-child(4) > div:nth-child(4) > div._2kAri > a').click()
            time.sleep(1)
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            time.sleep(1)
            
        except NoSuchElementException:
            print('-더보기 버튼 모두 클릭 완료-')
            break

    # 파싱
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    time.sleep(1)
    
    # 식당 구분
    restaurant_name = df['업소명'][i]
    print('식당 이름 : '+restaurant_name)
    
    user_review_id[restaurant_name] = {}
    review_json[restaurant_name] = {}
    image_json[restaurant_name] = {}
    
    try:
        restaurant_classificaton = soup.find_all('span',attrs = {'class':'_3ocDE'})[0].text
    except:
        restaurant_classificaton = 'none'
    print('식당 구분 : '+restaurant_classificaton)
    print('----------------------------------------------')
    
    try:
        one_review = soup.find_all('div', attrs = {'class':'_1Z_GL'})
        review_num = len(one_review) # 특정 식당의 리뷰 총 개수
        print('리뷰 총 개수 : '+str(review_num))
    
        # 리뷰 개수
        for i in range(len(one_review)):
            # user url
            user_url = one_review[i].find('div', attrs = {'class':'_23Rml'}).find('a').get('href')
            print('user_url = '+user_url)
            
            # user url로부터 user code 뽑아내기
            user_code = re.findall(r"my/(\w+)", user_url)[0]
            print('user_code = '+user_code)
            
            # review 1개에 대한 id 만들기 
            res_code = re.findall(r"restaurant/(\d+)", thisurl)[0]
            review_id = str(res_code)+"_"+user_code
            print('review_id = '+review_id)
            
            # rating, 별점
            rating = one_review[i].find('span', attrs = {'class':'_2tObC'}).text
            print('rating = '+rating)
            
            # date
            # 사진 리뷰 없음
            if len(one_review[i].find_all('span', attrs = {'class':'_3WqoL'})) == 5:
                date = one_review[i].find_all('span', attrs = {'class':'_3WqoL'})[2].text
            elif len(one_review[i].find_all('span', attrs = {'class':'_3WqoL'})) == 6:
                date = one_review[i].find_all('span', attrs = {'class':'_3WqoL'})[3].text
            else:
                date = ""
            print('date = '+date)
            
            # review 내용
            try : 
                review_content = one_review[i].find('span', attrs = {'class':'WoYOw'}).text
            except: # 리뷰가 없다면
                review_content = ""
            print('리뷰 내용 : '+review_content)
            
            # image 내용
            sliced_soup = one_review[i].find('div', attrs = {'class':'_1aFEL _2GO1Q'})

            if (sliced_soup != None):
                sliced_soup = sliced_soup.find('div',attrs={'class':'dRZ2X'})
                
                try:
                    img_url = 'https://search.pstatic.net/common/?autoRotate=true&quality=95&type=l&size=800x800&src='+re.findall(r'src=(.*jpeg)', str(sliced_soup))[0]
                except :
                    if (len(re.findall(r'src=(.*jpg)', str(sliced_soup)))!= 0):
                        img_url = 'https://search.pstatic.net/common/?autoRotate=true&quality=95&type=l&size=800x800&src='+re.findall(r'src=(.*jpg)', str(sliced_soup))[0]
                    elif (len(re.findall(r'src=(.*png)', str(sliced_soup)))!= 0):
                        img_url = 'https://search.pstatic.net/common/?autoRotate=true&quality=95&type=l&size=800x800&src='+re.findall(r'src=(.*png)', str(sliced_soup))[0]
                    else :
                        img_url = ""
            else:
                img_url = ""
                
            print('이미지 url : '+img_url)
            print('----------------------------------------------')
            print('\n')

            #리뷰정보
            # user_review_id
            user_review_id[restaurant_name][user_code] = review_id
            # review_json
            review_json[restaurant_name][review_id] = review_content
            # image_json
            image_json[restaurant_name][review_id] = img_url
            # rating_df_list
            naver_review = user_code, restaurant_name, rating, date
            rating_list.append(naver_review)
            
    except NoSuchElementException:
            none_review = "네이버 리뷰 없음"
            print(none_review)
            review_num = 0
            #리뷰정보 = restaurant_name, restaurant_classification, review_num, none_review
            
            # rating_df_list
            naver_review = user_code, restaurant_name, none_review, none_review
            rating_list.append(naver_review)
            
    print('\n')

# 수집한 리뷰 저장 및 내보내기 
rating_df = pd.DataFrame(rating_list)
rating_df.columns = ['UserID', 'ItemID', 'Rating', 'Timestamp']
rating_df.to_csv('rating9.csv', encoding='utf-8-sig')

import json
file_path = "user_review_id.json"
with open(file_path,'w') as outfile:
    json.dump(user_review_id, outfile)
    
file_path = "review.json"
with open(file_path,'w') as outfile:
    json.dump(review_json, outfile)

file_path = "image.json"
with open(file_path,'w') as outfile:
    json.dump(image_json, outfile)