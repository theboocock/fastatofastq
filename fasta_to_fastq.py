#!/usr/bin/env python
# Copyright (c) 2014 JAMES BOOCOCK james.boocock@otago.ac.nz
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
#(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, 
#merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
#LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR 
#IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



import argparse
import sys
import random

bases = ['A','T','C','G']

def is_base(b):
    if b in "ATCG":
        return True
    return False

def get_random_base():
    """ Returns a random base to replace the old bases

    """
    return random.choice(bases)

def get_sequence_and_quality(sequence,quality_char):
    """ Returns the sequence and quality strings after filtering to remove Ns is done
    """
    quality_scores_n = chr(33)
    sequence = sequence.upper()
    quality_scores = [quality_char if is_base(o) else quality_scores_n for o in sequence]
    sequence = [get_random_base() if o not in bases else o for o in sequence]
    return (''.join(sequence),''.join(quality_scores))

def fasta_to_fastq(fasta_file, quality_score):
    quality_char=chr(quality_score)
    with open(fasta_file,'r') as fasta:
        while True:
            header=fasta.readline()
            sequence = fasta.readline()
            if not header or not sequence:
                break
            sample = header.strip().split('>')[1]
            (sequence,quality_score) = get_sequence_and_quality(sequence.strip(),quality_char)
            print "@"+sample
            print sequence
            print "+"
            print quality_score
parser = argparse.ArgumentParser(description="Fasta to Fastq annotation")
parser.add_argument('fasta_file', help="Fasta input file")
parser.add_argument('--quality',dest="quality",help="Quality of the bases",type=int,default=40)
args = parser.parse_args()
fasta_to_fastq(fasta_file=args.fasta_file,quality_score=args.quality) 


