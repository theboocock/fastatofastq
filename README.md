fasta_to_fastq
==============

`python fasta_to_fastiq --quality (default :60)  fasta_input.`


Approach
========

Takes a fasta file and converts it fastq at the quality you specify.

Any positions that have something other than ATCGatcg are converted to a random base
and given a quality score of zero.
