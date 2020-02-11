from bs4 import BeautifulSoup
import json
import requests
import urllib.request
import time
import re
import datetime

f = open("input.txt", "r") #reads an input file containing text
stime = datetime.datetime.now() #starts timer
part1 = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" #google base endpoint 
part2 = "" #text to be queried
part3 = "&inputtype=textquery&region=in&fields=formatted_address,geometry,name" #google endpoint parameters
key = "input_your_google_key_here" #your google key
for x in f: #loop for each line of text in the text file
    part2 = x
    url = part1+part2+part3+key
    try:
        response = requests.get(url) #submits the request
        time.sleep(0.8) 

        y = json.loads(response.text)
        if (y['status'] == 'ZERO_RESULTS'): #error handling for no result returned from google
            out = open("results_fp.txt", "a", encoding="utf-8") #opens the output file
            out.write("No result from Google\n") #writes result to output file
            out.close()
        elif (y['status'] == 'INVALID_REQUEST'): #error handling for invalid request returned from google
            out = open("results_fp.txt", "a", encoding="utf-8") #opens the output file
            out.write("No result from Google-INV\n") #writes result to output file
            out.close()
        else: 
            for i in range(len(y['candidates'])): #read the content
                if re.findall('merchant_name',y['candidates'][i]['name']): #find the matching merchant name in this case
                    tmp1 = y['candidates'][i]['name'] #get merchant name from google
                    tmp2 = y['candidates'][i]['formatted_address'] #get address from google
                    tmp3 = y['candidates'][i]['geometry']['location']['lat'] #get latitude from google
                    tmp4 = y['candidates'][i]['geometry']['location']['lng'] #get longitude from google
                    final = str(tmp1)+","+str(tmp2)+"|"+str(tmp3)+","+str(tmp4)+'\n' #combine string
                    out = open("results_fp.txt", "a", encoding="utf-8") #opens the output file
                    out.write(final) #writes result to output file
                    out.close()
                    break
                elif i+1 == (len(y['candidates'])) and not y['candidates'][i]['name']=='merchant_name': #reached end of array and no result matched
                    out = open("results_fp.txt", "a", encoding="utf-8")
                    out.write("No matching result\n")
                    out.close()
                    break
                elif i+1 == (len(y['candidates'])) and y['candidates'][i]['name']=='merchant_name': #handle end of array with matched result
                    tmp1 = y['candidates'][i]['name']
                    tmp2 = y['candidates'][i]['formatted_address']
                    tmp3 = y['candidates'][i]['geometry']['location']['lat']
                    tmp4 = y['candidates'][i]['geometry']['location']['lng']
                    final = str(tmp1)+","+str(tmp2)+"|"+str(tmp3)+","+str(tmp4)+'\n'
                    out = open("results_fp.txt", "a", encoding="utf-8")
                    out.write(final)
                    out.close()
                    break
                else:
                    continue
    except:
        print("Error")
        out = open("results_fp.txt", "a", encoding="utf-8")
        out.write("Error\n")
        out.close()
        continue
etime = datetime.datetime.now() #ends timer
print(stime)
print(etime)
f.close() 
