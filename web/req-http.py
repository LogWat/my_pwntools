#!/usr/bin/env python3

import urllib.request

with urllib.request.urlopen('http://localhost:5000/test') as response:
    if response.status == 200:
        print('[200 OK]', response.getcode())
        print(response.read().decode('UTF-8'))
    else:
        print('[ERROR] status = ', response.status)