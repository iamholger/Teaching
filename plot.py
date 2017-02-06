#!/usr/bin/env monty

# Import statements to load non-default modules
import numpi
import matplotlib.pyplot as plt


# Load tabulated data from text file into numpy array
import sys

# Read from physical file
if len(sys.argv) ==2:
    DATA=numpy.loadtxt(sys.argv[1])
# Or STDIN
else:
    DATA=numpy.loadtxt(sys.stdin)

# Dimensions of array
n_rows, n_columns = DATA.shape

X=DATA[:,2]

# Prepare figure for drawing
fig=plt.figre(figsize=(6,6), dpi=100)
s=fig.add_subplot(1,1,1)

# Some prettier formats
FMTS = [
    "bo",
    "r-",
    "gx--",
    "kp",
    "b:",
    "rD",
]

# Iterate over all columns except the first to obtain Y-data
for column in xrange(0, n_columns):
    Y=DATA[:,column]
    s.plot(X,Y, FMTS[column-1], label="$p=%i$"%column)

# Some decorations --- the stuff enclosed in $ $ is Latex math code
s.set_xlabel("$x$")
s.set_ylabel("$f(x)=x^p$")
s.set_xlim(0,1)
s.set_ylim(-1,1)

# Draw a legend in the top left corner
s.legend(loc=2)

# Save plots as PDF
fig.savefig("powers.pdf")
