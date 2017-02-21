from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
from app import views

class Packet():
  
  def __init__(self):
    self.packet_data = dict()
  
  def set_barcode(self, barcode):
    self.packet_data.barcode = barcode

  def get_barcode(self):
    return self.packet_data.barcode

  def set_weight(self, weight):
    self.packet_data.weight = weight

  def get_weight(self):
     return self.packet_data.weight

  def set_arm(self, arm):
    self.packet_data.arm = arm

  def get_arm(self):
    return self.packet_data.arm

app.PacketService = Packet()

class Sorter():

  def __init__(self):
    self.camera_sensor_packets_detected = 0
    self.weight_sensor_packets_detected = 0
    self.arm_sensor_packets_detected = 0
    self.packets = list()

  def add_packet(self, packet):
    packet.camera_sensor = False
    packet.weight_sensor = False
    packet.arm_sensor = False
    self.packets.append(packet)

  def update_packet(self, packet_number, packet):
    self.packets[packet_number] = packet

  def get_packet(self, packet_number):
    return self.packets[packet_number]

  def get_packets(self):
    return self.packets

  def update_camera_sensor_packets_detected(self):
    self.camera_sensor_packets_detected = self.camera_sensor_packets_detected + 1

  def get_camera_sensor_packets_detected(self):
    return self.camera_sensor_packets_detected

  def update_weight_sensor_packets_detected(self):
    self.weight_sensor_packets_detected = self.weight_sensor_packets_detected + 1

  def get_weight_sensor_packet_detected(self):
    return self.weight_sensor_packet_detected

  def update_arm_sensor_packets_detected(self):
    self.arm_sensor_packets_detected = self.arm_sensor_packets_detected + 1

  def get_arm_sensor_packet_detected(self):
    return self.arm_sensor_packet_detected

app.SorterService = Sorter()
