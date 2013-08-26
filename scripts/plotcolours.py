import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

data = np.genfromtxt(open("colours.txt","rb"),delimiter="\t")
hue = data[:,0]
count = data[:,1]
hsv = np.dstack((hue/180.0,np.ones(180),np.ones(180)))
rgb = hsv_to_rgb(hsv)
colours=['#%02x%02x%02x' % tuple(c*255) for c in rgb[0]]

plt.bar(hue,count,color=colours,edgecolor=colours)
plt.xlim(0,180)
plt.xlabel('Hue')
plt.ylabel('Total Pixel Count')
plt.show()
