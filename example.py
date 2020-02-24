import pysfmov # import the module

filename = './data/rec.sfmov' #set the path and the filename

data = pysfmov.get_data(filename) # get data from sfmov file
meta_data = pysfmov.get_meta_data(filename) # get meta data from sfmov file