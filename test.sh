#!/bin/bash

a="test.log"
while [[ -f $a ]];
do
sleep 1;
size=`ls -lrt $a | cut -d " " -f 5`
echo $size
if [ $size -ge 1024 ];
then
logrotate  /etc/logrotate.d/test;
fi
done
