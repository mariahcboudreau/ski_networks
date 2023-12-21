#!/usr/bin/env python3
"""
	This script has a variety of utility functions for handling geojson ski
	resort data, such as filtering results by their operating/abandoned status,
	their geographic region, or whether they have a name defined.

	The geojson file includes several entries without location data, and others
	without names, so it takes some finagling to get only relevant entries.

	If you run this script it'll print the name of Vermont ski resorts, as an
	example usage.
"""
import geopandas as gpd
import json

def filterState(df, state):
	ldf = filterHasLocation(df)
	return ldf.loc[ldf["location"].apply(lambda r: r["iso3166_2"] == state)]

def filterOperating(df):
	return df.loc[df["status"] == "operating"]

def filterAbandoned(df):
	return df.loc[df["status"] == "abandoned"]

def filterHasName(df):
	return df.loc[df["name"].notnull()]

def filterHasLocation(df):
	return df.loc[df["location"].notnull()]

def loadDefaultFile():
	# There are two "engines" for geopandas to read files.
	# It'll use 'fiona' by default if available, otherwise 'pyogrio'
	# but on my system I got a segmentation fault parsing the geojson
	# file with fiona, so pyogrio it is.
	return gpd.read_file("ski_areas.geojson", engine = 'fiona')

if __name__ == "__main__":
	df = loadDefaultFile()
	resorts = filterHasName(filterState(df, "US-VT"))
	for name in resorts["name"]:
		print(name)

	print("done")