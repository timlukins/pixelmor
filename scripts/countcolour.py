import cv
import cv2
import numpy as np

def mapper(key, value):
  # Read in the data and decode...
  imgbytes = np.fromstring(value,dtype='uint8') 
  imarr = cv2.imdecode(imgbytes,cv2.CV_LOAD_IMAGE_COLOR) 
  im = cv.fromarray(imarr) 
  # Convert and split data to get hue... 
  hsv = cv.CreateImage(cv.GetSize(im),8,3)
  hue = cv.CreateImage(cv.GetSize(im),8,1)
  cv.CvtColor(im,hsv,cv.CV_BGR2HSV)
  cv.Split(hsv, hue, None, None, None)
  # Calculate colour (hue) histogram...
  hue_bins = 180 
  hue_range = [0,180] # nb. opencv hue range
  hist = cv.CreateHist([hue_bins], cv.CV_HIST_ARRAY, [hue_range], 1) 
  cv.CalcHist([hue],hist,0,None)
  # Yeild count of colour... 
  for h in range(hue_bins):
    yield int(h),cv.QueryHistValue_1D(hist,h) 

def reducer(key, values):
  # Simply sum up the values per colour...
  yield key,sum(values)

if __name__ == "__main__":
  import dumbo
  dumbo.run(mapper, reducer, combiner=reducer)
