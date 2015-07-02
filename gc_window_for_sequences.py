#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File      : gc_window_for_sequences.py
Version   : 0.1
Author    : Dominik R. Laetsch, dominik.laetsch at gmail dot com 
Bugs      : 
To do     : 
"""

from __future__ import division
import sys 
import argparse
import os

class ContigObj():
    def __init__(self, header, seq):
        self.header = header
        self.seq = seq

    def print_gc_by_position(self, window):
        start = 0
        stop = start + window
        pos = 0
        print "# %s %s" % (len(self.seq), self.header)
        #while stop < window:
        #    subseq = self.seq[start:stop]
        #    #print start, stop, subseq
        #    #print self.get_gc_score(subseq)
        #    print "%s %s %s %s %s" % (self.header, pos, self.get_gc_score(subseq), len(self.seq), subseq)
        #    stop += 1
        #    pos += 1 
        while stop <= len(self.seq):
            subseq = self.seq[start:stop]
            #print start, stop, subseq
            #print self.get_gc_score(subseq)
            print "%s %s %s %s %s" % (self.header, pos, self.get_gc_score(subseq), len(self.seq), subseq)
            start += 1
            stop += 1
            pos += 1
        while start < len(self.seq):
            subseq = self.seq[start:stop]
            print "%s %s %s %s %s" % (self.header, pos, self.get_gc_score(subseq), len(self.seq), subseq)
            #print start, stop, subseq
            #print self.get_gc_score(subseq)
            start += 1
            pos += 1
    def get_gc_score(self, string):
        length = len(string)
        score = sum(scoring_table[i] for i in string)
        gc_content = score / length
        return round(gc_content,3)
        
def parse_fasta(infile):

    contigs, header, seq = {}, '', ''
    
    with open(infile) as fh:
        for line in fh:
            if line.startswith(">"):
                if (seq):
                    contigs[header] = ContigObj(header, seq)
                    header, seq = '', ''
                header = line.rstrip("\n").lstrip(">")
            else:
                seq += line.rstrip("\n")
        contigs[header] = ContigObj(header, seq)
    return contigs 

if __name__ == "__main__":
    
    __version__ = 0.1

    scoring_table = {
        'G':1.0, 'C':1.0, 'A':0.0, 'T':0.0,
        'S':1.0, 'W':0.0, 'R':0.5, 'Y':0.5, 
        'D':1/3, 'H':1/3, 'V':2/3, 'B':2/3,
        'M':0.5, 'K':0.5, 'N':0.5 
    }

    infile = sys.argv[1]

    contigs = parse_fasta(infile)

    for contig, contigObj in contigs.items():
        contigObj.print_gc_by_position(3)
