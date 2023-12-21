#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Working with Open Street Maps for Ski Resorts
"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import osmnx as ox
import pandas as pd
import geopandas as gpd

tags = ["aerialway", "piste:difficulty", "piste:type", "gladed"]

ox.settings.useful_tags_way = tags

lifts = '["aerialway"~"chair_lift|station"]'
runs = '["piste:type"~"downhill"]'
place = "Bolton Valley Resort"

G1 = ox.graph_from_place(place, retain_all = True, custom_filter = lifts)
G2 = ox.graph_from_place(place, retain_all = True, custom_filter = runs)
G = nx.compose(G1,G2)

# G = ox.graph_from_place(place, retain_all = True, custom_filter = runs)

ox.plot_graph(G)
edge_attributes = ox.graph_to_gdfs(G, nodes=False).columns

#ec = ox.plot.get_edge_colors_by_attr(G, 'piste:difficulty', start=0, stop=1, na_color='none')
#fig, ax = ox.plot_graph(G, node_color=ec, node_size=5, edge_color="#333333", bgcolor="k")
#ox.elevation.add_edge_grades(G, add_absolute=True, precision=3)


stats = ox.basic_stats(G)
print(stats)
#%% 
#