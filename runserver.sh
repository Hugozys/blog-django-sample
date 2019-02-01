#!/bin/bash
sed -i /code/blog/settings/__init__.py -e "s:from \.production:#from \.production:"
sed -i /code/blog/settings/__init__.py -e "s:#from \.development:from .development:"

res= "1"
while [ "$res" != "0" ]
do
    sleep 1;
    python3 manage.py runserver 0:8000
    res="$?"
done

    
