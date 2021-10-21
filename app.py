from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from flask_cors import CORS, cross_origin
import os
from Model import model
import pandas as pd

app = Flask(__name__, template_folder='Template')
cors = CORS(app)
Bootstrap(app)
"""
Routes
"""
# 서버 구성할 떄 아래에 있는 render~주소의 리턴 값을 보여주겠다
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # 파일 업로드 진행 시 정의
        uploaded_file = request.files['file']
        # 파일명이 None이 아닌 경우 Path 정의
        if uploaded_file.filename != '':
            # static에 업로드 파일을 저장
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            classes, probs = model.pred_image(image_path)

            review = pd.read_csv('/Users/et.kim/Desktop/project_6/Data/review_nam.csv')
            land_add = pd.read_csv('/Users/et.kim/Desktop/project_6/Data/Landmark_add.csv')
            add = land_add.loc[land_add['landmark'] == classes, 'add_summary_1'][0]
            add_full = land_add.loc[land_add['landmark'] == classes, 'add_full'][0]
            result = [classes, probs, image_path, add_full]
            # 파일명이 None이 아닐 경우 실행
            return render_template('result.html', result = result, review = review)
            # 기본으로 불러오는 것
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')