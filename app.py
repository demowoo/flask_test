#coding:utf-8
__author__ = 'demowu'

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

if __name__ == '__main__':
    print app.config['MAIL_FROM_EMAIL']
    app.run()
