#!/bin/bash
function myfunc() { echo $X $Y $*; }
X=1
Y=a
myfunc # will be 1 a
myfunc x # will be 1 a x
myfunc $X # will be 1 a 1
X=2 myfunc $X # will be 2 a 1
X=2 Y=b myfunc $X # will be 2 b 1
