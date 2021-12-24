import requests
import pprint as pp
import pylab as pl
import numpy as np

#QAT+ demo site root and token
#"http://randlet.com/qatrack/api"\
#"eac2dae558ffedaaedcae401f80c3ba85d142f6a"

class QAT_API():
    connectionSuccess=None

    def __init__(self,root="https://canberra-staging.multileaf.ca/api",
                 token='754303d15f0cd9c49a8606a02a741eac5bf2d1c9'):
        print('Connecting to Multileaf... @:' ,root)
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

    def getUserEmails(self):
        auth = self.getAuthorization()
        resp = requests.get(self.root + '/auth/users', headers=auth)
        emails= resp.json()
        numEmails=np.size(emails['results'])
        emailList=[]
        for x in range(0,numEmails,1):
            emailList.append(emails['results'][x]['email'])
        return emailList

    def getTests(self):
        auth = self.getAuthorization()
        resp = requests.get(self.root + '/qc/tests', headers=auth)
        tests= resp.json()
        numTests=np.size(tests['results'])
        testNames=[]
        for x in range(0,numTests,1):
            testNames.append(tests['results'][x]['name'])
        return testNames

    def getTestFrequencies(self):
        auth = self.getAuthorization()
        resp = requests.get(self.root + '/qc/frequencies', headers=auth)
        frequencies= resp.json()
        numTests=np.size(frequencies['results'])
        testFrequencies=[]
        for x in range(0,numTests,1):
            testFrequencies.append(frequencies['results'][x]['name'])
        return testFrequencies


    def test(self):
        auth = self.getAuthorization()
        resp = requests.get(self.root , headers=auth)
        units = resp.json()
        return units


#use QAT+ demo site
# api=QAT_API()
# users=api.getUserNames()
# pp.pprint(users)


#headers=api.getHeaders()
#pp.pprint(headers)

# test=api.test()
# pp.pprint(test)

# users=api.getUserEmails()
# pp.pprint(users)

#units=api.getUnitNames()
#pp.pprint(units)

#pp.pprint(api.getUnitDetails('Brindabella'))



#classes=api.getVendorNames()
#pp.pprint(classes)






