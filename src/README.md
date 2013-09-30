pixmor

A simple library and CLI for processing massive amounts of video and image data.

Example, loading a video and performing structure-from-motion:

$ pixmor import EdinburghCastle.mp4 
$ ...imported as EdinburghCastle_0001

$ pixmor view -as video EdinburghCastle_0001

$ python recover_3d_points.py EdinburghCastle_0001 

$ pixmor view -as pointcloud 

$ pixmor export

$ pixmor query -as asciipoints

Where the meat of the matter is expressed in the following python file:

http://www.inf.ethz.ch/personal/chzach/
http://users.ics.forth.gr/~lourakis/sba/

#########################################

History:

I made this for stereo reconstruction - but now it seems awfully useful for everything else!

Example:

> from pixmor import store
> idx = store.import('/path/to/video.file')
> idx
> {}a
> def 

> job = idx.apply('LINE',findline) 
>  
> store.find('LINE')
>   idx1:  

Do this linearly - it takes...

Limits

Do this 

Dependencies:
	- Python 2.7.5 with opencv, numpy

	(On windows use:)


Data is organised into "VIEWS" representing the temporal-spatial realworld moment the pixel data was captured.

There can be any number of views

Views are uniquely identified by a [x,y,z,t,theta,rho]


