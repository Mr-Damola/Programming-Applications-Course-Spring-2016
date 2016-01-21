#import numpy and matlibplots module


#generate array of x values from 0 to 6pi

#calculate y values for sin wave

#calculate y values for cosine wave

#plot x and y values for both functions 

#set dashed line for sine wave and solide line for cosine wave

#add legend


#leave comment here with your information
#Name:Goodness Fowora
#Date:January 20th, 2016

import numpy
import matplotlib.pyplot as plt
plt.rcdefaults()
from numpy import sin, cos, pi

x = numpy.linspace(0,6*pi,999999)
sin_line=sin(x)
cos_line=cos(x)

plt.gca().set_color_cycle(['blue','red'])
plt.plot(x, cos_line)
plt.plot(x, sin_line, '--', linewidth=2)
plt.ylabel("Y-Axis")
plt.xlabel("Angles")
plt.legend(('cos(x)','sin(x)'))
plt.title('Plot of sin(x) and cos(x) from 0 to 6pi')

plt.show()

