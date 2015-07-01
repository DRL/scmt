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

class RibbonObj():
    def __init__(self, query, subject, pid, qstart, qstop, sstart, sstop, evalue, bitscore):
        self.query = query
        self.subject = subject
        self.pid = pid
        self.qstart = qstart
        self.qstop = qstop
        self.sstart = sstart
        self.sstop = sstop
        self.evalue = evalue
        self.bitscore = bitscore
        self.rbbh = 0

def parse_blastfile(blastfile):

    data = []
    
    with open(blastfile) as fh:
        for line in fh:
            field = line.rstrip("\n").split("\t")
            query = name[field[0]]
            subject = name[field[1]]
            pid = float(field[2])
            qstart = int(field[6])
            qstop = int(field[7])
            sstart = int(field[8])
            sstop = int(field[9])
            evalue = float(field[10])
            bitscore = int(field[11]) 
            
            if (query == subject) and (qstart == sstart) and (qstop == sstop):
                pass # no hits to self
            else:
                if evalue <= THRESHOLD:
                    ribbon = RibbonObj(query, subject, pid, qstart, qstop, sstart, sstop, evalue, bitscore)
                    if (data):
                        for prev_ribbon in data:
                            if (prev_ribbon.query == ribbon.subject) and (prev_ribbon.subject == ribbon.query) and (prev_ribbon.qstart == ribbon.sstart) and (prev_ribbon.sstart == ribbon.qstart) and (prev_ribbon.qstop == ribbon.sstop)and (prev_ribbon.sstop == ribbon.qstop):
                                prev_ribbon.rbbh = 1 
                                ribbon.rbbh = 1 
                        if ribbon.rbbh == 0:
                            data.append(ribbon)    
                    else:
                        data.append(ribbon)
    return data 

def write_ribbons(data):
    # chr1 start1 end1 chr2 start2 end2 [options]
    for ribbon in sorted(data, key=lambda x: (x.query, x.subject, x.qstart)):
        colour = ''
        if ribbon.evalue == 0.0:
            colour = 'vvvvdgrey'
        elif ribbon.evalue <= 1e-100:
            colour = 'vdgrey'
        elif ribbon.evalue <= 1e-50:
            colour = 'lgrey'
        else:
            colour = 'vvvvlgrey' 
        print "%s %s %s %s %s %s color=%s" % (ribbon.query, ribbon.qstart, ribbon.qstop, ribbon.subject, ribbon.sstart, ribbon.sstop, colour)

if __name__ == "__main__":
    
    __version__ = 0.1

    blastfile = sys.argv[1]

    THRESHOLD = 0.0
    
    name = {
        'gi|5869814|emb|AJ249395.1|' : 'Gp1_AJ249395',
        'gi|108885493|gb|DQ631911.1|' : 'Gp2_DQ631911',
        'gi|108885494|gb|DQ631912.1|' : 'Gp3_DQ631912',
        'gi|108885496|gb|DQ631913.1|' : 'Gp4_DQ631913',
        'gi|108885497|gb|DQ631914.1|' : 'Gp5_DQ631914',
        'gi|129562017|gb|EF193005.1|' : 'Gr1_EF193005',
        'gi|129562010|gb|EF462976.1|' : 'Gr2_EF462976',   
        'gi|129562012|gb|EF462977.1|' : 'Gr3_EF462977',
        'gi|197239848|gb|EF462978.2|' : 'Gr4_EF462978',
        'gi|129562014|gb|EF462979.1|' : 'Gr5_EF462979',
        'gi|129562015|gb|EF462980.1|' : 'Gr6_EF462980',
        'gi|129562016|gb|EF462981.1|' : 'Gr7_EF462981'
         }

    data = parse_blastfile(blastfile)

    write_ribbons(data)

    #for ribbon in sorted(data, key=lambda x: x.pid, reverse=True):
    #    print ribbon.__dict__
