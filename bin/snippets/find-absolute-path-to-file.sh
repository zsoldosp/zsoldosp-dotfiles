#!/bin/bash
# http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in
pushd . > /dev/null
cd `dirname $0`
SOURCE=`basename $0`
while [ -h "$SOURCE" ] ; do SOURCE="$(readlink "$SOURCE")"; done
cd `dirname $SOURCE`
SOURCE=`pwd`
popd > /dev/null
echo $SOURCE
echo `dirname $SOURCE`

