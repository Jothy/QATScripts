import requests
import pprint as pp
import pylab as pl
import numpy as np

root = "https://canberra.multileaf.ca/api"
token_url = root + "/get-token/"
resp = requests.post(token_url, {'username': 'jselvaraj', 'password': 'Shiva_1234'})
token = resp.json()['token']

#print("Retrieved token: ",token)


headers = {"Authorization": "Token %s" % token}

resp = requests.get("https://canberra.multileaf.ca/api", headers=headers)
#pp.pprint(resp.json())
#print('***************************************************')

resp = requests.get(root + '/units/units', headers=headers)
#pp.pprint(resp.json())

#get BB details
resp = requests.get(root + '/units/units/7', headers=headers)
BB_JSON=resp.json()
#pp.pprint(BB_JSON)

resp = requests.get(root + '/qa/testinstances', headers=headers)
#pp.pprint(resp.json())


url = root + '/qa/testinstances/'
params = {
    "unit_test_info__unit__name": "LA1",
    "unit_test_info__test__name": "6X D(5cm)",
}

resp = requests.get(url, params, headers=headers)
payload = resp.json()
data = [(x['created'], x['value']) for x in payload['results']]
#pp.pprint(data)

outputs=[]
print('-----------------------------------------------------')
print('Data points found: ',np.shape(data))
for x in range(0,np.shape(data)[0],1):
    outputs.append((data[x][1]))
pl.plot(outputs)
ref=np.linspace(0,np.shape(data)[0],65)
print(ref)
pl.plot(ref,ref*0.0+1.0)
pl.title('LA1:6X output trend (cGy)')
pl.show()



