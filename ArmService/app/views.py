from app import app
import random

@app.route('/')
@app.route('/index')
def index():
  return "Arm service"

@app.route('/arm')
def get_arm():
  return str(random.randint(1, 10))
