#!/bin/bash

src='/jakiro'
for file in `ls`
do
    filePath="$src/$file"
    if [ -a $filePath ]; then
      if [ -d $file ]; then
        rm -rf $file
        ln -s $filePath
      else
        rm $file
        ln -s $filePath $file
      fi
    fi
done

redis-server &

python manage.py runserver 0.0.0.0:5001
