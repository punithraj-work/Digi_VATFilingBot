from cgitb import text
import json
import requests
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

import numpy as np
import pandas as pd

def gettaxcisedata(p1,p2,p3):
    # if p1=="1":
    #     # hostname = "https://api.taxcise.ae/get-declarations?projectName=Taxcise - Al Fakher"   #input("Enter end point: ")   #sys.argv[1] #
    #     # hostname="https://api.taxcise.ae/get-declarations?projectName=Taxcise - Al Fakher&apiKey=bede40550d49e09933f8f2c5393d02f63d6b294871"
    #     hostname="https://api.taxcise.ae/get-declarations?projectName=Taxcise - Al Fakher&isAgent=false&apiKey=bede40550d49e09933f8f2c5393d02f63d6b294871"
    # elif p1=='2':
    #     # hostname = "https://api.taxcise.ae/get-declarations?projectName=Taxcise - Stienweg Sharaf"   #input("Enter end point: ")   #sys.argv[1] #
    #     # hostname="https://api.taxcise.ae/get-declarations?projectName=Taxcise - Stienweg Sharaf&apiKey=bede40550d49e09933f8f2c5393d02f63d6b294871"
    #     hostname="https://api.taxcise.ae/get-declarations?projectName=Taxcise%20-%20Stienweg%20Sharaf&isAgent=true&apiKey=bede40550d49e09933f8f2c5393d02f63d6b294871"
    # else:
    #     hostname="https://api.taxcise.ae/get-declarations?projectName=Taxcise - Al Fakhama&isAgent=false&apiKey=bede40550d49e09933f8f2c5393d02f63d6b294871"
    
    linkname = p3
    hostname=f"https://api.taxcise.ae/get-declarations?{linkname}&isAgent=false&apiKey=bede40550d49e09933f8f2c5393d02f63d6b294871"
    # print(hostname)

    '''
    #jsonbody
    #jsonrbody = open("D:\\Punith\\Python\\API CALL\\JsonBody.json", "r")
    # jsonrbodyp = input("Enter jsonbody path") #sys.argv[2] #
    # jsonrbody = open(jsonrbodyp, "r")
    # requestbody = json.loads(jsonrbody.read())
    # print(requestbody)
    ''' 

    #Headerfilepath
    # headerpath = input("Headers path") #sys.argv[3] #
    # headerdet = open(headerpath, "r")
    headerinfo = p2 #json.loads(headerdet.read())
    # print(headerinfo)
    # print(headerinfo)


    #x = requests.post(hostname, json = requestbody, headers = {"SECRETKEY" : "Profitley@sipl", "REQUESTTYPE" : "Products"})
    # x = requests.post(hostname, headers = headerinfo)
    # x = requests.get(hostname, headers= headerinfo)
    # x = requests.get(hostname, headers = {"Authorization":p2})
    x = requests.get(hostname)

    #Convert the response into json format 
    json_resp = x.json()   

    #Dump the json response into the variable , Indent is used for spacing for better readability
    jsondumpfile = json.dumps(json_resp, indent=4)  
    #print(jsondumpfile)

    
    #write the json data to a json file
    #jsonrespfile = open("D:\\Punith\\Python\\API CALL\\APIresponse.json", "w")

    # if p1=="1":
    #     jsonrespfilep = "Taxcise Alfakhar.json" #input("response body path") #sys.argv[4] #
    # elif p1=='2':
    #     jsonrespfilep = "Taxcise Steinweg.json" #input("response body path") #sys.argv[4] #
    # else:
    #     jsonrespfilep = "Taxcise Al Fakhama.json" #input("response body path") #sys.argv[4] #

    jsonrespfilep = "Taxcise.json"
    
    # print(jsonrespfilep)
    jsonrespfile = open(jsonrespfilep, "w")
    jsonrespfile.write(jsondumpfile)
    jsonrespfile.close()

    
    return jsonrespfilep

def countdecl(jsonfilename,jsonformname,ftaperiod,secnn,clientname):
    declarationc=0
    declarationcsec2=0
    valuex=0.00
    valuexsec2=0.00
    # print(ftaperiod)

    if ftaperiod=="0":
         periodm=""
    else:
        periodm=ftaperiod[0]
    
    if ftaperiod=="0":
         periody=""
    else:
        periody=ftaperiod[1]
    
    '''
    search_word = 'status'
    with open("Taxcise Steinweg.json", "r") as f:
        data = f.read()
        total = data.count(search_word)

    print(total)
    '''
    # search_word = jsonformname
    taxcisejsonf=open(jsonfilename, 'r')
    taxcisejsonf=json.loads(taxcisejsonf.read())
    # taxcisejsonf=taxcisejsonf.read()
    # total = taxcisejsonf.count(search_word)
    for decl in taxcisejsonf['data']:
        if decl['Declaration']==jsonformname and decl['PeriodMonth']==periodm and decl['PeriodYear']==periody:

            if secnn=='sec2' and (clientname=='1' and decl['TRN']!='100000189900007' or clientname=='2' and decl['TRN']!='100000685600007' or clientname=='3' and decl['TRN']!='100000234300007'):
                declarationcsec2=declarationcsec2+1
                if jsonformname!="EX203C - Transfer of Ownership":
                    values2 = float(decl['TotalExciseTaxValue'])
                    values2 = round(values2,2)
                    valuexsec2 = valuexsec2+values2
            elif secnn=='sec1' and (clientname=='1' and decl['TRN']=='100000189900007' or clientname=='2' and decl['TRN']=='100000685600007' or clientname=='3' and decl['TRN']=='100000234300007'):
                declarationc=declarationc+1
                # print(decl['DeclarationNumber'])
                if jsonformname!="EX203C - Transfer of Ownership":
                    value = float(decl['TotalExciseTaxValue'])
                    value = round(value,2)
                    valuex = valuex+value

    # print(total)
    return declarationc,valuex,declarationcsec2,valuexsec2

# authkey={'Authorization':'1000.f1311f04a69e2c583868cfe8be138189.365a7c99eda24377b82a6981e9ebd811'}
# gettaxcisedata("2",authkey)


# def testf():
#     a=2
#     b=5
#     c=a+b
#     return a,b,c

# op=testf()
# print(op[0],op[1],op[2])


# def funcdatarecon(pjsonfile,p201s1FTA,p202as1FTA,p202as2FTA,p202bs1FTA,p203as1FTA,p203as2FTA,p203bs1FTA,p203bs2FTA,p203cs1FTA,p203cs2FTA,p203cs3FTA,p203deds1FTA):