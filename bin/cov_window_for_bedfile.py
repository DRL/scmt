#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File      : cov_window_for_covfile.py
Version   : 0.1
Author    : Dominik R. Laetsch, dominik.laetsch at gmail dot com 
Desc      : 
To do     : TESTING
"""

from __future__ import division
import sys 
import argparse
import os
      
def parse_karyotype_file(karyotype_file):
    
    contigs = {}
    with open(karyotype_file) as fh:
        for line in fh:
            field = line.rstrip("\n").split(" ")
            contig = field[2]
            length = int(field[5])
            contigs[contig] = length
    return contigs

def parse_normalisation_file(normalisation_file, covfile):
    
    cov_file = os.path.basename(covfile)
    with open(normalisation_file) as fh:
        for line in fh:
            field = line.rstrip("\n").split("\t")
            dataset = field[0]
            norm_value = float(field[1])
            if dataset == cov_file:
                return norm_value
    return 1.0 

def parse_covfile(covfile, contigs):
    
    contig, pos, cov = '', 0, 0
    dict_of_contigs = {}
    with open(covfile) as fh:
        for line in fh:
            field = line.rstrip("\n").split("\t")
            contig = field[0]
            pos = int(field[1])
            cov = int(field[2])
            if not contig in dict_of_contigs:
                dict_of_contigs[contig] = [0] * contigs[contig]
            dict_of_contigs[contig][pos] = cov
    return dict_of_contigs 

def calculate_window_cov(dict_of_contigs, window, norm_value):
    start = 0
    stop = window
    for contig in sorted(dict_of_contigs):
        list_of_covs = dict_of_contigs[contig]
        print "# %s %s" % (contig, len(list_of_covs)) 
        #print list_of_covs
        while stop < len(list_of_covs):
            chunk = list_of_covs[start:stop]
            cov = (sum(chunk)/len(chunk)) * norm_value
            print "%s %s %s %s" % (contig, start, stop, round(cov, 2))
            #print chunk, len(chunk), len(list_of_covs)
            start += window
            stop += window
        #if start < len(list_of_covs) + 1:
        chunk = list_of_covs[start:stop]
        cov = sum(chunk)/len(chunk) * norm_value
        print "%s %s %s %s" % (contig, start, len(list_of_covs), round(cov, 2))
        #print chunk, len(chunk), len(list_of_covs)
        start = 0
        stop = window
        chunk = []

if __name__ == "__main__":
    
    __version__ = 0.1

    covfile = sys.argv[1]
    
    window = int(sys.argv[2])
    
    norm_value = 1.0

    karyotype_file = sys.argv[3] # this is needed to infer 0-cov positions
    
    try:
        normalisation_file = sys.argv[4]
        norm_value = parse_normalisation_file(normalisation_file, covfile)
    except:
        pass

    contigs = parse_karyotype_file(karyotype_file)

    dict_of_contigs = parse_covfile(covfile, contigs)

    calculate_window_cov(dict_of_contigs, window, norm_value)
