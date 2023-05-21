from requests import request
import numpy as np
import json

def getReq(url) -> request:

    headersList = {
        "Accept": "*/*",
        "User-Agent":
          "Thunder Client (https://www.thunderclient.com)"
    }
    payload = ""
    return request("GET", url, data=payload,  headers=headersList)

def generateTickersfile():
    
    tickers_text = getReq('https://www.sec.gov/include/ticker.txt').text.split()
    tickers_array = np.array(tickers_text).reshape(-1,2)
    tickers = {}
    for ticker in tickers_array:
        tickers[ticker[0]] = zeros(ticker[1])
    with open("tickers.json", "w") as fp:
        fp.write(json.dumps(tickers))

def getCik() -> dict:
    with open("tickers.json", "r") as fp:
        return json.load(fp)

def get10K(stock) -> json:

    url = f'https://data.sec.gov/api/xbrl/companyfacts/CIK{getCik()[stock]}.json'
    return getReq(url).json()

def zeros (num) -> str:
   zeros_length=10-len(num)
   array_zeros=np.zeros(zeros_length,dtype=int)

   return ''.join(str(i) for i in array_zeros)+num

def getVal(form:dict, value:str, index:int) -> float:
  if value in form:
    for key in form[value]['units'].keys():
      return form[value]['units'][key][index]['val']/1e9
  else:
    return None

def findListValue(form, pista, index:int) -> dict:
  list = {}
  for key in form.keys():
    if key.lower().find(pista) > -1:
      if getVal(form, key, index) != None:
        list[key] = getVal(form, key, index)
  return list