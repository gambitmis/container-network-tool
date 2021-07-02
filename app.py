from flask import Flask,render_template,request,url_for,redirect
import socket,platform,os,psutil,multiprocessing
import datetime,pytz
import speedtest
import inspect

ver = os.environ['version']
release = os.environ['releases']

def getHostnameAndIpAddr():
    try:
        hostName = socket.gethostname()
        hostIP = socket.gethostbyname(hostName)
        return hostName, hostIP
    except:
        hostName = "Error"
        hostIP = "Error"
        return hostName, hostIP

def getNow():
    try:
        tz_th = pytz.timezone('Asia/Bangkok')
        now_utc = datetime.datetime.now(tz=pytz.UTC)
        now_th = now_utc.astimezone(tz_th)
    except:
        print("Error can not get time for now")
    return now_th,now_utc

def getFlaskEnv(req):
    try:
        flask_env = {
            "remoteAddr":req['REMOTE_ADDR'],
            "userAgent":req['HTTP_USER_AGENT']
        }
    except:
        print("Error can not get Flask env")
    return flask_env

app = Flask(__name__)

@app.route("/")
def hello_world():
    hostname,ipaddr = getHostnameAndIpAddr()
    now_th,now_utc = getNow()
    flask_env = getFlaskEnv(request.environ)
    return "<p>Time:\"{}\"**** Hostname:\"{}\"**** CONTAINER_IP:\"{}\"**** REQUEST_IP:\"{}\"**** version:\"{}-{}\" </p>".format(now_th,hostname,ipaddr,flask_env['remoteAddr'],ver,release)
  
