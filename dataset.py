from random import random

class Data:
  def __init__(self, x, y = None):    
    self.x = x
    self.y = y


all_test_data = [Data(bin(i)[2:].zfill(8), i) for i in range(256)]

random_test_data = [
  Data(bin(i)[2:].zfill(8), i) for i in range(256) if random() < 0.5
]

mini_random_test_data = [
  Data(bin(i)[2:].zfill(8), i) for i in range(256) if random() < 0.25
]