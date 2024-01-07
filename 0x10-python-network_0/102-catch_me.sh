#!/bin/bash
# script that was a fun effort in breaking to http protocols on holberton servers
curl -s -L -X PUT -d "user_id=98" -H "Origin: H" 0.0.0.0:5000/catch_me
