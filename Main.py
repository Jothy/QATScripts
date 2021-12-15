import requests
import pprint as pp
import pylab as pl
import numpy as np

#QAT+ staging server
root = "https://canberra-staging.multileaf.ca/api"
#Use token from QAT+
token='754303d15f0cd9c49a8606a02a741eac5bf2d1c9'

class QAT_API():
    connectionSuccess=None

    def __init__(self,root="https://canberra-staging.multileaf.ca/api",
                 token='754303d15f0cd9c49a8606a02a741eac5bf2d1c9'):
        self.root=root
        self.token=token

    #Get access token using ID & password
    def getToken(self,root,user,password):
        token_url = root + "/get-token/"
        resp=requests.post(token_url, {'username': user, 'password': password})
        token = resp.json()['token']
        return token

    def getAuthorization(self):
        auth = {"Authorization": "Token %s" % self.token}
        return auth

    def getHeaders(self):
        headers = self.getAuthorization(self.root,self.token)
        resp = requests.get(root, headers=headers).json()
        return resp

    def getUnitNames(self):
        auth = self.getAuthorization(self.root,self.token)
        resp = requests.get(self.root + '/units/units', headers=auth)
        units = resp.json()
        numUnits=np.size(units['results'])
        unitNames=[]
        for x in range(0,numUnits,1):
            unitNames.append(units['results'][x]['name'])
        return unitNames

    def getVendorNames(self,root,token):
        auth = self.getAuthorization(self.root,self.token)
        resp = requests.get(root + '/units/vendors', headers=auth)
        vendors = resp.json()
        numVendors = np.size(vendors['results'])
        vendorNames = []
        for x in range(0, numVendors, 1):
            vendorNames.append(vendors['results'][x]['name'])
        return vendorNames

    def getSiteNames(self,root,token):
        auth = self.getAuthorization(self.root,self.token)
        resp = requests.get(root + '/units/sites', headers=auth)
        sites = resp.json()
        numSites = np.size(sites['results'])
        siteNames = []
        for x in range(0, numSites, 1):
            siteNames.append(sites['results'][x]['name'])
        return siteNames

    def getUnitClasses(self,root,token):
        auth = self.getAuthorization(self.root,self.token)
        resp = requests.get(root + '/units/unitclasses', headers=auth)
        classes = resp.json()
        numClasses = np.size(classes['results'])
        classNames = []
        for x in range(0, numClasses, 1):
            classNames.append(classes['results'][x]['name'])
        return classNames


    def getUnits(self,root,token):
        auth = self.getAuthorization(self.root,self.token)
        resp = requests.get(root + '/units/units', headers=auth)
        units = resp.json()
        return units['results']

    def getUnitDetails(self,unitName):
        pass

api=QAT_API()
print(api.root)
print(api.token)

#headers=GetHeaders(root,token)
#pp.pprint(headers)

#classes=GetUnitClasses(root,token)
#pp.pprint(classes)

# unitNames=GetUnitNames(root,token)
# # pp.pprint(unitNames)
# CTIdx=unitNames.index('LA4')
# units=GetUnits(root,token)
# pp.pprint(units[CTIdx])





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



