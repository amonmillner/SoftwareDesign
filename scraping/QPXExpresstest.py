### QPXExpresstest.py ###

## Script for experimenting and testing the QPX Express API. This API deals with airfare search and return.

from authenticate import authtokens
import requests, time, json

qpxin = '{"request":{"passengers":{"adultCount":1},"slice":[{"origin":"BOS","destination":"LAX","date":"2014-11-05"},      {"origin":"LAX","destination":"BOS","date":"2014-11-10"}]}}'
headers = {'content-type': 'application/json'}

qpxlink = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key='+authtokens['qpxgoogle']


r = requests.post(qpxlink, data = qpxin, headers = headers)
print r.url
print r.json()



# params = {'ai': '', 'p': '', 'do': 'y', 'ft': 'rt', 'ns': 'y', 'cb': 'e', 'pa': 1, 'l1': 'MKE', 't1': 'a', 'df': 'us1', 'd1': '11/24/2014', 'depart_flex': 'exact', 'r1': 'n', 'l2': 'BOS', 't2': 'a', 'd2': '11/30/2014', 'return_flex': 'exact', 'r2': 'n', 'b': ''}

# kayakurl = 'http://www.kayak.com/s/search/air'

# r = requests.get(kayakurl, params = params)
# print r.url

# print r.text.encode('utf-8')