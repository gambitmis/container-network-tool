from flask import Flask,render_template,request,url_for,redirect
import socket,platform,os,psutil,multiprocessing
import datetime,pytz
import speedtest
import inspect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
  
