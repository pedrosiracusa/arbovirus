# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
This script generates a kml file containing Aedes occurrence data.
Dataset available at http://datadryad.org/resource/doi:10.5061/dryad.47v3c

@author: Pedro
"""

import pandas as pd

from lxml import etree
from pykml.parser import Schema
from pykml.factory import KML_ElementMaker as KML


aegypti_data_url='http://datadryad.org/bitstream/handle/10255/dryad.88853/aegypti.csv?sequence=1'


# Read dataset from file
try: 
    dataset
    
except NameError:
    dataset = pd.read_csv(aegypti_data_url)    
    dataset = dataset[dataset.COUNTRY=='Brazil']


# File Skeleton
doc = KML.kml(
    KML.Document(
        KML.Name("Aedes occurrence")
           
    )
)


# Iterate through dataset and add placemarks for each occurrence
for i, row in dataset.iterrows():
    pm = KML.Placemark(
        KML.name(row.VECTOR),
        KML.description( 
            "id: %d\nLocation Type: %s\nYear: %s" % 
            (row.OCCURRENCE_ID, row.LOCATION_TYPE, row.YEAR)        
        ),
        KML.Point(
            KML.coordinates( "%f, %f" %(row.X, row.Y)  )        
        )
    )
    
    doc.Document.append(
        pm
    )


# Create the file
with open("aegypti_occurrences.kml", 'w') as f:
    f.write( etree.tostring( doc, encoding="unicode", pretty_print=True ) )
