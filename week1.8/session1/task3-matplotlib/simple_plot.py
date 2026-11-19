
import matplotlib.pyplot as plt  # import library

x = [ k for k in range(10) ]  # create a range for the data
y = [ k*k for k in x ]      # create a simple function y=x^2

plt.plot(x,y)  # create a 2d plot

plt.xlabel('x')
plt.ylabel('y=x^2')  # annotate

  # display
plt.title("Simple Matplotlib Graph")
plt.annotate("Point (10, 100)",
  xy=(10, 100),
 xytext=(5, 200),

 arrowprops=dict(arrowstyle="->"))
plt.grid(True)
plt.legend()
plt.show()

# Test the example as is on the slides
# - Modify the data and the range
# - Plot in different ways
# Read matplotlib documentation
# - Test some other plotting functions
