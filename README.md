# 이미지 객체인식 기술을 활용한 앱 애플리케이션 구축
*발표 및 발표 자료에서 앱을 웹으로 잘못 기입하였습니다. 이 점 참고 부탁드립니다.*

## 폴더 구조

**데이터 파일은 개인정보 이슈가 있을 수 있어 업로드하지 않았음을 참고 부탁드립니다** 

- **data** <br> 
    ㄴㅡ 1.train_labels_fold.csv <br>
    ---> Cross Validation 활용을 위해 이미지 별 1~5까지 무작위로 라벨을 부여한 파일 <br>
    ㄴㅡ 2.ulsan_landmark_add.csv <br>
    ---> 울산에 위치한 랜드마크의 이름, 주소 데이터를 담은 파일 <br>
    ㄴㅡ 3.ulsan_store_info.csv <br>
    ---> 울산에 위치한 음식점의 상호명, 주소 데이터를 담은 파일 <br>
    ㄴㅡ 4.ulsan_store_info_add_url_pre-pro.csv <br>
    ---> **data** 3번 파일에 네이버 플레이스 URL을 추가하고 URL이 없는 음식점을 삭제한 파일 <br>
    ㄴㅡ 5.ulsan_store_review_raw_pre-pro.csv <br>
    ---> **data** 4번 파일의 URL을 활용하여 수집한 평점, 리뷰 데이터 원본 파일 <br>
    ㄴㅡ 6.ulsan_store_review_raw_pre-pro_address.csv <br>
    ---> **data** 5번 파일에 음식점 별 주소지를 추가한 파일 <br>

- **review_crawling** <br>
    ㄴㅡ 1. ulsan_store_info_concat.ipynb <br>
    ---> 울산에 위치한 음식점의 상호명, 주소 데이터를 하나로 통합하는 파일(구 별로 나눠져있던 파일을 하나로 통합) <br>
    ㄴㅡ 2. web_crawling.py <br>
    ---> **data** 3번 파일을 활용하여 리뷰 URL를 수집하고, 이후 URL 별 리뷰, 평점 데이터를 수집하는 파일 <br>
    ㄴㅡ 3. review_concat_add_Info.ipynb <br>
    ---> **data** 5번 파일을 **data** 3번 데이터와 통합하는 파일 <br>
    ㄴㅡ 4. text_pre-pro.ipynb <br>
    ---> **data** 6번 파일의 리뷰 텍스트 전처리를 진행하는 파일 <br>
    
- **model** <br>
    ㄴㅡ 1. Image_load_eda_resize.ipynb <br>
    ---> 울산 랜드마크 이미지를 불러와 EDA 및 전처리를 진행하는 파일 <br>
    ㄴㅡ 2. Image_pre-pro_modeling_eval.ipynb <br>
    ---> 이미지를 2차 전처리하고 딥러닝 모델을 구축하여 학습 및 성능평가 진행. 진행 완료 후 모델 및 requirments.txt 저장 <br>
    ㄴㅡ model.py <br>
    ---> **model** 2번의 딥러닝 모델을 가져와 이미지 분류 예측을 진행하고 결과값을 도출하는 파일 <br>
    ㄴㅡ model.h5 <br>
    ---> **model** 2번의 딥러닝 모델 구조 및 파라미터 값을 저장한 파일 <br>
    
- **Template** <br>
    ㄴㅡ base.html, index.html, result.html, upload.html <br>
    ---> HTML 구축을 위한 파일 <br>

- **requirements.txt** <br>
    ---> 로컬 및 클라우드 환경에서 사용한 패키지 모음

- **app.py**
    ---> 어플리케이션 구축 파일
