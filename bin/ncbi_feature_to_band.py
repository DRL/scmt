#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File      : ncbi_feature_to_band.py
Version   : 0.1
Author    : Dominik R. Laetsch, dominik.laetsch at gmail dot com 
Comments  : Doesn't work always on non-gene/non-tRNA features ... check
To do     : 
"""

from __future__ import division
import sys 
import os

class FeatObj():
    def __init__(self):
        self.type = ''
        self.start = ''
        self.stop = ''
        self.name = ''
        self.pseudo = 0 

    def add_coordinates(self, feat_start, feat_stop, feat_type):
        self.type = feat_type
        self.start = feat_start
        self.stop = feat_stop

def parse_ncbi_feature(feature_file):
    list_of_features = []
    featObj = FeatObj()
    with open(feature_file) as fh:
        for line in fh:
            if line.startswith(">"):
                pass
            elif line[0].isdigit():
                if (featObj.name):
                    list_of_features.append(featObj)
                featObj = FeatObj()
                feature_start, feature_stop, feature_type = line.rstrip("\n").split("\t")
                featObj.add_coordinates(feature_start, feature_stop, feature_type)
            else:
                if line:
                    field = line.rstrip("\n").lstrip(" ").lstrip("\t").split("\t")
                    if field[0] == 'product' or field[0] == 'gene' or field[0] == 'gene_desc':
                        featObj.name = field[1]
                    if field[0] == 'pseudo':
                        featObj.pseudo = 1
                    if field[0] == 'note':
                        if featObj.type == "misc_feature":
                            featObj.name = '222'
                        else:
                            featObj.name = 'repeat'
    list_of_features.append(featObj)
    return list_of_features

def write_bands(list_of_features, parent):
    print "# " + feature_file
    for feat in list_of_features:
        if not feat.type == "CDS": 
            if (feat.pseudo):
                feat.type = 'pseudogene' 
            print "band %s %s %s %s %s %s" % (parent, feat.name, feat.name, feat.start, feat.stop, feat.type) 

if __name__ == "__main__":
    
    __version__ = 0.1

    feature_file = sys.argv[1]

    parent = sys.argv[2]

    list_of_features = parse_ncbi_feature(feature_file)

    write_bands(list_of_features, parent) 
