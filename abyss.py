#!/usr/bin/env python
# Run ABySS for Spearmint
# Code written by Shaun Jackman @sjackman - extended to two parameters by Laura Gutierrez Funderburk
# config.json file written by Shaun Jackman @sjackman - extended to two parameters by Laura Gutierrez Funderburk

import csv
import os
import shlex
import subprocess

# Run ABySS
def main(job_id, params):
    k = params['k']
    s = params['s']
    subprocess.call(shlex.split("make k=%d s=%d" % (k, s)))
    max_n50 = 0
    with open("results/200k/k%d/s%d/hsapiens-scaffolds.fac.tsv" % (k, s)) as csvfile:
        csvfile.readline()
        csvreader = csv.reader(csvfile, delimiter="\t")
        for row in csvreader:
            n50 = int(row[5])
            max_n50 = max(max_n50, n50)
    print "k=%d\ts=%d\tN50=%d" % (k, s, n50)
    return -max_n50

if __name__ == "__main__":
	main(None, {"k": 40, "s": 1000})
