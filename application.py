from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello world! WAATech is on the rise!'

@application.route('/andris')
def hello_andris():
    return 'Hello Andris, we\'ve been waiting for you...'

@application.route('/alex')
def hello_alex():
    return 'Hello Alex, we\'ve been waiting for you...'

@application.route('/wes')
def hello_wes():
    return 'Hello Wes, we\'ve been waiting for you...'
