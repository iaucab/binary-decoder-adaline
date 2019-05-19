from adaline import Adaline
import dataset

adaline = Adaline()

print("Training....")

m_error = 1
iteration = 0
while m_error > 0.00000000000000001 and iteration < 30000:

  m_error = 0

  for data in dataset.mini_random_test_data:
    adaline.set_x(data.x)
    adaline.set_y(data.y)

    y = adaline.calc_y()
    e = data.y - y
    adaline.update(e)

    iteration += 1
    m_error += e if e > 0 else -e

  m_error = m_error / len(dataset.mini_random_test_data)

print()
print("Training completed")
print("Dataset size:", len(dataset.mini_random_test_data))
print("Number of iterations", iteration)
adaline.print_me()
print()

while True:
  x = input("Enter an 8-bit binary number: ")
  adaline.set_x(x)
  y = adaline.calc_y()
  print("Result:", y)
  print()
