from app import app
import random

@app.route('/')
@app.route('/index')
def index():
  return "Barcode service"

@app.route('/barcode')
def get_barcode():
  return str(random.randint(1, 10000))
