import os

BASE_DIR = os.path.dirname(__file__) # c:\projects\myproject
# __file__ = c:\projects\myproject\config.py = 현재실행되는 파일의 경로를 반환
# os.path.dirname(__file__) = c:\projects\myproject\config.py 중 디렉토리명만(c:\projects\myproject) 가져오기

SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR, "pybo.db")) # sqlite:///c:\projects\myproject\pybo.db
SQLALCHMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"

print(SQLALCHEMY_DATABASE_URI.startswith("sqlite:///"))