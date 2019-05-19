from random import random

class Adaline:

  def __init__(self):
    self.w = [random() for i in range(8)]
    self.alpha = 0.3 # Best value

  def set_x(self, x):
    x = x.zfill(8)
    self.x = [float(i) for i in x]
    self.x.reverse()
    self.x = x
  
  def set_y(self, y):
    self.y = y

  def print_me(self):
    print("Neuron:")
    for i in range(len(self.w)):
      print('w[{i}]={w}'.format(i=i, w=self.w[i]))

  def sum(self):
    sum = 0
    for i in range(len(self.w)):
      sum += float(self.x[i]) * float(self.w[i])
    return sum

  def calc_y(self):
    return self.sum()

  def update(self, error):
    for i in range(len(self.w)):
      self.w[i] += float(self.alpha) * float(error) * float(self.x[i])