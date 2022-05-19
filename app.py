import os
from flask import Flask
from datetime import timedelta

app = Flask(__name__)
# 配置缓存的有效时间
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
# 配置 session_key 最好使用随机字符串
app.config['SECRET_KEY'] = os.urandom(24)

