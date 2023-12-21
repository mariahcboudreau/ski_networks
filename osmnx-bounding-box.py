import osmnx
import networkx as nx
import pdb
import matplotlib.pyplot as plt

## Bolton Valley Resort
featureGDF = osmnx.features.features_from_bbox(
    44.4272, 44.4080, -72.8244, -72.8712, 
    tags = {
        'landuse': 'winter_sports', 
        'sport': 'skiing', 
        'ele':True,
        'name': True
    }
)


nodeGDF = featureGDF.loc[('node')]
wayGDF = featureGDF.loc[('way')]


#nodes are irrelevant for our purposes and will be neglected. only ways are relevant.

waynotNAN = wayGDF[wayGDF['piste:type'].notna()]
bway = waynotNAN[waynotNAN['name'] == 'Broadway']

fig, ax = plt.subplots()
waynotNAN.plot(ax=ax, column='piste:type', cmap='OrRd')
fig.savefig('./test_piste.png')

figb, axb = plt.subplots()
bway.plot(ax=axb, cmap='OrRd')
figb.savefig('./test_broadway.png')

pdb.set_trace()

