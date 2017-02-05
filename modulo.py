#!/usr/bin/env python

import sys

usage="""
Example run script do demonstrate gnu-parallel.

for i in {10..20};do %s $i;done

parallel --bar %s ::: {10..20}


"""%(sys.argv[0], sys.argv[0])




def isMod(m):
    return [x for x in xrange(100000000) if x%m==0]

if __name__ == "__main__":
    if len(sys.argv)<2:
        print usage
        sys.exit(0)
    print len(isMod(int(sys.argv[1])))
