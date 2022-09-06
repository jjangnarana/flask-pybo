from pybo import db

"""
    모델 만들기
    질문 question
        속성 : id(고유),subject(제목),content(내용),create_date(작성일시) 

    답변 answer
        속성 : id(고유), question_id(질문id), content(답변내용), create_date(작성일시)
"""

quesiton_voter = db.Table(
    "question_voter",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), primary_key=True),
    db.Column("question_id", db.Integer, db.ForeignKey("question.id", ondelete="CASCADE"), primary_key=True)
)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user = db.relationship("User", backref=db.backref("question_set"))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship("User", secondary=quesiton_voter, backref=db.backref("question_voter_set"))
    """ 
        Question 클래스를 생성 하면서 db.Model을 상속 받아야 속성값 정의가 가능. db.Model 의 db는 __init__.py 에서 생성한 SQLALchemy 클래스 객체임
        db.Column(Only = DataType, *any)
        
        DataType 인수 정의
        db.Integer : 정수 숫자 타입
        db.String(int) : 인수(int) 갯수만큼 제한된 문자열 타입
        db.Text() : 제한없는 문자열 타입
        db.Datetime() : 날짜 및 시각 타입
    """

answer_voter = db.Table(
    "answer_voter",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), primary_key=True),
    db.Column("answer_id", db.Integer, db.ForeignKey("answer.id", ondelete="CASCADE"), primary_key=True)
)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id", ondelete="CASCADE")) # db.ForeignKey의 question.id = question테이블의 id 컬럼을 외래키로 지정, CASCADE = 종속하다
    question = db.relationship("Question", backref=db.backref("answer_set", cascade="all, delete-orphan"))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user = db.relationship("User", backref=db.backref("answer_set"))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship("User", secondary=answer_voter, backref=db.backref("answer_voter_set"))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

