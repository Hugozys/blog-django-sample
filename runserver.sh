#!/bin/bash
res= "1"
while [ "$res" != "0" ]
do
    sleep 1;
    python3 manage.py runserver 0:8000
    res="$?"
done

    
