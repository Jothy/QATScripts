import requests
import pprint as pp
import pylab as pl
import numpy as np


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
        auth = self.getAuthorization()
        resp = requests.get(self.root, headers=auth).json()
        return resp

    def getUnitNames(self):
        auth = self.getAuthorization()
        resp = requests.get(self.root + '/units/units', headers=auth)
        units = resp.json()
        numUnits=np.size(units['results'])
        unitNames=[]
        for x in range(0,numUnits,1):
            unitNames.append(units['results'][x]['name'])
        return unitNames

    def getVendorNames(self):
        auth = self.getAuthorization()
        resp = requests.get(self.root + '/units/vendors', headers=auth)
        vendors = resp.json()
        numVendors = np.size(vendors['results'])
        vendorNames = []
        for x in range(0, numVendors, 1):
            vendorNames.append(vendors['results'][x]['name'])
        return vendorNames

    def getSiteNames(self):
        auth = self.getAuthorization()
        resp = requests.get(self.root + '/units/sites', headers=auth)
        sites = resp.json()
        numSites = np.size(sites['results'])
        siteNames = []
        for x in range(0, numSites, 1):
            siteNames.append(sites['results'][x]['name'])
        return siteNames

    def getUnitClasses(self):
        auth = self.getAuthorization()
        resp = requests.get(self.root + '/units/unitclasses', headers=auth)
        classes = resp.json()
        numClasses = np.size(classes['results'])
        classNames = []
        for x in range(0, numClasses, 1):
            classNames.append(classes['results'][x]['name'])
        return classNames

    def getUnits(self):
        auth = self.getAuthorization()
        resp = requests.get(self.root + '/units/units', headers=auth)
        units = resp.json()
        return units['results']

    def getUnitDetails(self,unitName):
        unitNames=self.getUnitNames()
        unitIdx=unitNames.index(unitName)
        unitDetails=self.getUnits()[unitIdx]
        return unitDetails

    def getUserNames(self):
        auth = self.getAuthorization()
        resp = requests.get(self.root + '/auth/users', headers=auth)
        users= resp.json()
        numUsers=np.size(users['results'])
        userNames=[]
        for x in range(0,numUsers,1):
            userNames.append(users['results'][x]['username'])
        return userNames

    def getUserGroups(self):
        auth = self.getAuthorization()
        resp = requests.get(self.root + '/auth/groups', headers=auth)
        groups= resp.json()
        numGroups=np.size(groups['results'])
        groupNames=[]
        for x in range(0,numGroups,1):
            groupNames.append(groups['results'][x]['name'])
        return groupNames


    def test(self):
        auth = self.getAuthorization()
        resp = requests.get(self.root + '/auth/groups', headers=auth)
        units = resp.json()
        return units




api=QAT_API()

#test=api.test()
#pp.pprint(test)

users=api.getUserGroups()
pp.pprint(users)

# units=api.getUnits()
# pp.pprint(units)

#pp.pprint(api.getUnitDetails('Brindabella'))

# headers=api.getHeaders()
# pp.pprint(headers)

# classes=api.getUnitClasses()
# pp.pprint(classes)






