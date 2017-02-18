from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
from app import views

class Packet():
  
  def __init__():
    self.packet_data = dict()
  
  def set_barcode(barcode):
    self.packet_data.barcode = barcode

  def get_barcode():
    return self.packet_data.barcode

  def set_weight(weight):
    self.packet_data.weight = weight

  def get_weight():
     return self.packet_data.weight

  def set_arm(arm):
    self.packet_data.arm = arm

  def get_arm():
    return self.packet_data.arm

class Sorter():

  def __init__():
    self.camera_sensor_id = 0
    self.weight_sensor_id = 0
    self.arm_sensor_id = 0
    self.packets = list()

  def add_packet(packet):
    packet.camera_sensor = False
    packet.weight_sensor = False
    packet.arm_sensor = False
    self.packets.append(packet)

  def get_packets():
    return self.packets
