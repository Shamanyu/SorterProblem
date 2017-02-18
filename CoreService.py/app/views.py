from app import app
import requests

@app.route('/')
@app.route('/index')
def index():
  return "Core Service"

@app.route('/camera_sensor')
def camera_sensor():
  url = app.config['CONNECTION_PROTOCOL']+app.config['BARCODE_SERVICE_URL']+app.config['BARCODE_SERVICE_PORT']+app.config['BARCODE_SERVICE_ENDPOINT']
  headers = {}
  return str((requests.get(url, headers=headers)).json())

@app.route('/weight_sensor')
def weight_sensor():
  url = app.config['CONNECTION_PROTOCOL']+app.config['WEIGHT_SERVICE_URL']+app.config['WEIGHT_SERVICE_PORT']+app.config['WEIGHT_SERVICE_ENDPOINT']
  headers = {}
  return str((requests.get(url, headers=headers)).json())

@app.route('/arm_sensor')
def arm_sensor():
  url = app.config['CONNECTION_PROTOCOL']+app.config['ARM_SERVICE_URL']+app.config['ARM_SERVICE_PORT']+app.config['ARM_SERVICE_ENDPOINT']
  headers = {}
  return str((requests.get(url, headers=headers)).json())
