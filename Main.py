import requests
import pprint as pp
import pylab as pl
import numpy as np

#QAT+ staging server
root = "https://canberra-staging.multileaf.ca/api"
#Use token from QAT+
token='754303d15f0cd9c49a8606a02a741eac5bf2d1c9'

#Get access token using ID & password
def RetriveToken(root,user,password):
    token_url = root + "/get-token/"
    resp=requests.post(token_url, {'username': user, 'password': password})
    token = resp.json()['token']
    return token

def GetAuthorization(root,token):
    headers = {"Authorization": "Token %s" % token}
    return headers


def GetHeaders(root,token):
    headers = GetAuthorization(root,token)
    resp = requests.get(root, headers=headers).json()
    return resp

def GetUnitNames(root,token):
    auth = GetAuthorization(root, token)
    resp = requests.get(root + '/units/units', headers=auth)
    units = resp.json()
    numUnits=np.size(units['results'])
    unitNames=[]
    for x in range(0,numUnits,1):
        unitNames.append(units['results'][x]['name'])
    return unitNames

def GetUnits(root,token):
    auth = GetAuthorization(root, token)
    resp = requests.get(root + '/units/units', headers=auth)
    units = resp.json()
    return units['results']

def GetUnitUrl(root,token,unitName):
    pass



# headers=GetHeaders(root,token)
# pp.pprint(headers)

unitNames=GetUnitNames(root,token)
# pp.pprint(unitNames)
CTIdx=unitNames.index('LA4')
#print(CTIdx)

units=GetUnits(root,token)
pp.pprint(units[CTIdx])






# #get BB details
# resp = requests.get(root + '/units/units/7', headers=headers)
# BB_JSON=resp.json()
# #pp.pprint(BB_JSON)
#
# resp = requests.get(root + '/qa/testinstances', headers=headers)
# #pp.pprint(resp.json())
#
#
# url = root + '/qa/testinstances/'
# params = {
#     "unit_test_info__unit__name": "LA1",
#     "unit_test_info__test__name": "6X D(5cm)",
# }
#
# resp = requests.get(url, params, headers=headers)
# payload = resp.json()
# data = [(x['created'], x['value']) for x in payload['results']]
# #pp.pprint(data)
#
# outputs=[]
# print('-----------------------------------------------------')
# print('Data points found: ',np.shape(data))
# for x in range(0,np.shape(data)[0],1):
#     outputs.append((data[x][1]))
# pl.plot(outputs)
# ref=np.linspace(0,np.shape(data)[0],65)
# print(ref)
# pl.plot(ref,ref*0.0+1.0)
# pl.title('LA1:6X output trend (cGy)')
# pl.show()



