#!/usr/bin/env python


def f(x, power):
    return x**power

from numpy import linspace
X=linspace(0,1,100)

Y_1=[f(x, 1) for x in X]
Y_2=[f(x, 2) for x in X]
Y_3=[f(x, 3) for x in X]
Y_4=[f(x, 4) for x in X]
Y_5=[f(x, 5) for x in X]

import sys

if len(sys.argv) == 2:
    with open(sys.argv[1], "w") as f:
	for i in xrange(len(X)):
	    f.write("%f %f %f %f %f %f\n"%(X[i], Y_1[i], Y_2[i], Y_3[i], Y_4[i], Y_5[i]))
    print "Data written to file %s"%sys.argv[1]

else:
    for i in xrange(len(X)):
        sys.stdout.write("%f %f %f %f %f %f\n"%(X[i], Y_1[i], Y_2[i], Y_3[i], Y_4[i], Y_5[i]))


