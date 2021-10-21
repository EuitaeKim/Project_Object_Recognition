# 이미지 객체인식 기술을 활용한 앱 애플리케이션 구축
*발표 및 발표 자료에서 앱을 웹으로 잘못 기입하였습니다. 이 점 참고 부탁드립니다.*

## File Directory

**데이터 파일은 개인정보 이슈가 있을 수 있어 업로드하지 않았음을 참고 부탁드립니다** 

- **data** <br> 
    ㄴㅡ 1.train_labels_fold.csv <br>
    ---> CV를 위해 이미지 별 라벨을 부여한 파일(1~5,무작위) <br>
    
    ㄴㅡ 2.ulsan_landmark_add.csv <br>
    ---> 울산 랜드마크의 이름,주소 데이터 파일 <br>
    
    ㄴㅡ 3.ulsan_store_info.csv <br>
    ---> 울산 음식점의 상호,주소 데이터 파일 <br>
    
    ㄴㅡ 4.ulsan_store_info_add_url_pre-pro.csv <br>
    ---> **data 3번** 파일에 리뷰 URL을 추가하고, 없는 음식점은 삭제한 파일 <br>
    
    ㄴㅡ 5.ulsan_store_review_raw_pre-pro.csv <br>
    ---> **data 4번** 파일의 URL로 수집한 평점,리뷰 원본 파일 <br>
    
    ㄴㅡ 6.ulsan_store_review_raw_pre-pro_address.csv <br>
    ---> **data 5번** 파일에 음식점 주소지 추가한 파일 <br><br>

- **review_crawling** <br>
    ㄴㅡ 1. ulsan_store_info_concat.ipynb <br>
    ---> 울산 음식점의 상호,주소 데이터를 통합하는 파일(구 별로 나뉘어져있던 파일 통합) <br>
    
    ㄴㅡ 2. web_crawling.py <br>
    ---> **data 3번** 파일로 URL를 수집하고, 이를 활용해 리뷰,평점 데이터를 수집하는 파일 <br>
    
    ㄴㅡ 3. review_concat_add_Info.ipynb <br>
    ---> **data 5번** 파일과 **data 3번** 파일을 통합하는 파일 <br>
    
    ㄴㅡ 4. text_pre-pro.ipynb <br>
    ---> **data 6번** 파일의 텍스트 전처리를 진행하는 파일 <br><br>
    
- **model** <br>
    ㄴㅡ 1. Image_load_eda_resize.ipynb <br>
    ---> 울산 랜드마크 이미지를 불러와 EDA 및 전처리를 진행하는 파일 <br>
    
    ㄴㅡ 2. Image_pre-pro_modeling_eval.ipynb <br>
    ---> 이미지의 2차 전처리, 딥러닝 모델의 구축,학습,성능평가 진행. 이후 모델과 requirments.txt를 저장 <br>
    
    ㄴㅡ model.py <br>
    ---> **model 2번** 의 모델을 가져와 예측을 진행하고 결과를 반환하는 파일 <br>
    
    ㄴㅡ model.h5 <br>
    ---> **model 2번** 의 모델 구조 및 파라미터 값을 저장한 파일 <br><br>
    
- **Template** <br>
    ㄴㅡ base.html, index.html, result.html, upload.html <br>
    ---> HTML 구축을 위한 파일 <br><br>

- **requirements.txt** <br>
    ---> 로컬&클라우드 환경에서 사용한 패키지 (통합) <br><br>

- **app.py** <br>
    ---> 어플리케이션 구축 파일 <br>
