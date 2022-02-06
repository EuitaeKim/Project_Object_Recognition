# package import
import logging
import os

import tensorflow as tf
from tensorflow.keras.models import load_model

import cv2
from sklearn.utils import shuffle
import numpy as np

# 랜드마크 명을 숫자로 바꾸기 때문에 이를 다시 되돌리기 위한 함수 작성
def get_classlabel(class_code):
    labels = {0:'5D입체영상관', 1:'남구국민체육센터', 2:'뉴코아아울렛울산점', 3:'대현체육관', 4:'동구국민체육센터', 5:'매곡산업단지',
              6:'명촌어린이도서관', 7:'문수국제양궁장', 8:'문수힐링피크닉장', 9:'북구청소년문화의집', 10:'석계서원',
              11:'농소1동도서관', 12:'롯데백화점울산점', 13:'문수월드컵경기장', 14:'성남청소년문화의집', 15:'세이브존울산점',
              16:'꽃바위문화관', 17:'덕신1차시장', 18:'도로교통공단', 19:'목련암', 20:'문수야구장',
              21:'동구평생학습관', 22:'박제상유적', 23:'언양알프스시장', 24:'언양종합상가시장', 25:'옥골시장',
              26:'남구문화원', 27:'동축사', 28:'등억온천단지', 29:'롯데마트진장점', 30:'박상진의사송정역사공원',
              31:'곰장어골목', 32:'국립재난안전연구원', 33:'롯데마트울산점', 34:'만정헌', 35:'삼일사',
              36:'성남프라자', 37:'야음상가시장', 38:'약사동제방유적전시관', 39:'에너지경제연구원', 40:'옥골샘도서관'}
    
    return labels[class_code]

# 이미지 파일 읽기
def read_image(image_path) :
    image = tf.io.read_file(image_path)

    return tf.image.decode_jpeg(image, channels = 3)

# 이미지 전처리
def preprocess_input(image, target_size, augment = False) :
    image = tf.image.resize(
        image, target_size, method='bilinear')
    image = tf.cast(image, tf.uint8)
    image = tf.cast(image, tf.float32)
    image /= 255.

    return image

# 이미지 예측
def pred_image(image_path):
    # 코랩에서 학습한 모델 불러오기
    model = load_model('/Users/et.kim/Desktop/flask_app/model_ml/model.h5', custom_objects=None, compile=True)

    # 이미지를 받아 읽기 및 전처리 진행
    image = read_image(image_path)
    image = preprocess_input(image, (150, 150))
    image = np.reshape(image, (1, 150, 150, 3))

    # 이미지를 모델에 넣어 라벨 값 별 확률을 구한 후
    # 가장 큰 확률 값과 라벨 값을 도출
    pred_prob = model.predict(image)
    probs_argsort = tf.argsort(pred_prob, direction='DESCENDING')

    # 하나의 값을 특정
    probs = pred_prob[0][probs_argsort][0]
    classes = get_classlabel(np.argmax(pred_prob))
    
    return classes, probs