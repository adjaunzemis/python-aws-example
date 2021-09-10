from flask import Flask

testApp = Flask(__name__)

@testApp.route('/')
def hello_world():
    return 'Hello world! WAATech is on the rise!'

@testApp.route('/andris')
def hello_andris():
    return 'Hello Andris, we\'ve been waiting for you...'

@testApp.route('/alex')
def hello_alex():
    return 'Hello Alex, we\'ve been waiting for you...'

@testApp.route('/wes')
def hello_wes():
    return 'Hello Wes, we\'ve been waiting for you...'
