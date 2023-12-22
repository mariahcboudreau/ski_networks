import geopandas as gpd
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import pdb
import json
import warnings
import pickle


'''
Extracts properties by ID of the trail, and writes out to a csv file 
using the index, the name, and the grooming/gladed status  as well as 
to a pickle object.

'''

#-----header with document paths

base = "./ski_networks"
input_skifolder = os.path.join(base, "ski-data")



#----------helper fns -------




#--------- run code---------

runspath = os.path.join(input_skifolder, 'intermediate_runs.geojson')

picklepath = os.path.join(base, 'intermediate_runs.pickle')
if not os.path.exists(picklepath): 
        
    runs = gpd.read_file(runspath)
    
    with open(picklepath, 'wb') as f: 
        pickle.dump(runs, f)

else: 
    with open(picklepath, 'rb') as f: 
        runs = pickle.load(f)
    
    
    
outpath = os.path.join(base, 'trail_status.csv')
outpickle = os.path.join(base, 'trail_status.pickle')
outdata = runs[['name', 'gladed', 'grooming', 'difficulty']]

pdb.set_trace()

outdata.to_csv(outpath, header=True, index=True)
with open(outpickle, 'wb') as f: 
    pickle.dump(outpickle, f)

pdb.set_trace()

#gladed is either true or null
#grooming is going to be a column and it gives string responses
#if grooming is null, print null or something similar