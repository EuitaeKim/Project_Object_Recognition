from sqlalchemy.orm import relationship, backref
from flask_app import db
from datetime import datetime

class Rand_id(db.Model) :
    __tablename__ = 'rand_id'
    id = db.Column(db.Integer(), primary_key = True)
    name_rand = db.Column(db.String(), nullable = False, unique = True)

    def __repr__(self):
        return f"ID:{self.id}, 지역:{self.name_rand}"

class Res_id(db.Model) :
    __tablename__ = 'res_id'
    id = db.Column(db.Integer(), primary_key = True)
    name_res = db.Column(db.String(), nullable = False)

    def __repr__(self):
        return f"ID:{self.id}, 음식점 명:{self.name_res}"

class Rand(db.Model) :
    __tablename__ = 'rand'
    id = db.Column(db.Integer(), primary_key = True)
    id_geo = db.Column(db.Integer(), db.ForeignKey('rand_id.id'), nullable = False)
    name_rand = db.Column(db.String(), nullable = False)
    Type1 = db.Column(db.Text())
    Type2 = db.Column(db.Text())
    add = db.Column(db.Text(), nullable = False)
    randmark_1 = db.relationship('Rand_id', backref = 'rand', cascade = 'all, delete')

    def __repr__(self):
        return f"ID(지역):{self.id_geo}, 랜드마크 명:{self.name_rand}, 카테고리 1:{self.Type1}, 카테고리 2:{self.Type2}, 주소:{self.add}"

class Res(db.Model) :
    __tablename__ = 'res'
    id_geo = db.Column(db.Integer(), db.ForeignKey('rand_id.id'), nullable = False)
    id_res = db.Column(db.Integer(), db.ForeignKey('res_id.id'), primary_key = True)
    loc_street = db.Column(db.Text())
    add = db.Column(db.Text(), nullable = False)
    res_url = db.Column(db.Text())
    review_url = db.Column(db.Text())
    randmark_2 = db.relationship('Rand_id', backref = 'res', cascade = 'all, delete')
    restaurant_1 = db.relationship('Res_id', backref = 'res', cascade = 'all, delete')

    def __repr__(self):
        return f"ID(지역):{self.id_geo}, ID(음식점):{self.id_res}, 도로명:{self.loc_street}, 주소:{self.add}, 음식점 url:{self.res_url}, 리뷰 url:{self.review_url}"

class Res_review(db.Model) :
    __tablename__ = 'res_review'
    id = db.Column(db.Integer(), primary_key = True)
    id_res = db.Column(db.Integer(), db.ForeignKey('res_id.id'), nullable = False)
    Timestamp = db.Column(db.DateTime(), default = datetime.today())
    Rating = db.Column(db.Text(), nullable = False)
    review = db.Column(db.Text())
    restaurant_2 = db.relationship('Res_id', backref = 'res_review', cascade = 'all, delete')

    def __repr__(self):
        return f"ID(음식점):{self.id_res}, 작성시간:{self.Timestamp}, 평점:{self.Rating}, 리뷰:{self.review}"