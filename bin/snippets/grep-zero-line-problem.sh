#!/bin/bash

echo "hello" | grep -v "bye" 
echo $? # will be 0
echo | grep -v "bye" 
echo $? # will be 0
emptyfile=emptyfile
rm $emptyfile || true
touch $emptyfile
cat $emptyfile | grep -v "bye" 
echo $? # will be -1
