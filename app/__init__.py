WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from flask import Flask

app = Flask(__name__)

app.config.from_object(__name__)
from app import views
