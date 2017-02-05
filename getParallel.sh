#!/bin/bash

wget http://ftp.gnu.org/gnu/parallel/parallel-20170122.tar.bz2
tar xjf parallel-20170122.tar.bz2
cd parallel-20170122
./configure --prefix=$HOME/Software
make
make install
echo "All done, now set environment variable by doing"
echo "export PATH=\$HOME/Software/bin:\$PATH"
