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

def duplicate_reads(sam_file,read_depth):
    with open(sam_file) as f:
        output = f.read()
        print read_depth * output
    

parser = argparse.ArgumentParser(description="Duplicate reads in Sam")
parser.add_argument('sam_file', help="Sam input file")
parser.add_argument('-N',dest="read_depth",help="Number of Times to duplicate each read",type=int,default=60)
args = parser.parse_args()
duplicate_reads(sam_file=args.sam_file,read_depth=int(args.read_depth)) 
q

