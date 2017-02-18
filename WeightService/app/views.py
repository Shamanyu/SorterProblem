from app import app
import random

@app.route('/')
@app.route('/index')
def index():
  return "Weight service"

@app.route('/weight')
def get_weight():
  return str(random.randint(1, 10000))
