from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flaskext.markdown import Markdown

import config

naming_convention = {
    "ix" : "ix_%(column_0_label)s",
    "uq" : "uq_%(table_name)s_%(column_0_name)s",
    "ck" : "ck_%(table_name)s_%(column_0_name)s",
    "fk" : "fk_%(table_name)s_%(column_0_name)s",
    "pk" : "pk_%(table_name)s_%(column_0_name)s"
}

db = SQLAlchemy()
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    """
       __name__ = pybo = 실행된 모듈 이름 = 실행되는 최초의 모듈일 경우 __main__ 이 반환 
    """

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else: 
        migrate.init_app(app, db)
    from . import models

    # Blueprint
    from .views import main_views, question_views, answer_views, auth_views
    """ 
        from .views 중 . 은 현재 모듈의 경로 즉 'pybo' 폴더를 뜻함.
         즉 .views 는 'pybo\views' 폴더를 뜻 함.
        from .views import main_views 'pybo\views' 폴더내의 'main_views' 모듈(main_views.py) 을 import 한다는 뜻.
    """
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    
    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # markdown
    Markdown(app, extensions=['nl2br', 'fenced_code'])

    return app

