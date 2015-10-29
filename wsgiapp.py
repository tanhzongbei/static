#coding:utf8
"""
Created on Jun 18, 2014

@author: ilcwd
"""
import logging.config
import logging
import os

import yaml


STATIC_PATH = '/home/xiaobei/git_tanzhongbei/monitor-service/monitor/static'


from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
application = Flask(__name__, static_url_path='')

@application.route('/static/<path:path>')
def send_js(path):
    return send_from_directory(STATIC_PATH, path)

if __name__ == "__main__":
    host, port = '0.0.0.0', 8080
    application.run(host, port, debug=True, use_reloader=False)
