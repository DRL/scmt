#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File      : mtDNA_blast_analysis.py
Version   : 0.1
Author    : Dominik R. Laetsch, dominik.laetsch at gmail dot com 
Bugs      : 
To do     : 
"""

from __future__ import division
import sys 
import argparse
import os


def parse_blastfile(blastfile):
    with open(blastfile) as fh:
        for line in fh:
            field = line.rstrip("\n").split("\t")
            query = 

if __name__ == "__main__":
    
    __version__ = 0.1

    blastfile = sys.argv[1]

    name = {
        'gi|5869814|emb|AJ249395.1|' : 'Gp1',
        'gi|108885493|gb|DQ631911.1|' : 'Gp2',
        'gi|108885494|gb|DQ631912.1|' : 'Gp3',
        'gi|108885496|gb|DQ631913.1|' : 'Gp4',
        'gi|108885497|gb|DQ631914.1|' : 'Gp5',
        'gi|129562017|gb|EF193005.1|' : 'Gr1',
        'gi|129562010|gb|EF462976.1|' : 'Gr2',   
        'gi|129562012|gb|EF462977.1|' : 'Gr3',
        'gi|197239848|gb|EF462978.2|' : 'Gr4',
        'gi|129562014|gb|EF462979.1|' : 'Gr5',
        'gi|129562015|gb|EF462980.1|' : 'Gr6',
        'gi|129562016|gb|EF462981.1|' : 'Gr7'
         }

    data = parse_blastfile(blastfile)
