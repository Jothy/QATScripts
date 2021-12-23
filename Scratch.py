import requests
import pprint as pp


root = "https://canberra-staging.multileaf.ca/api"
token = "754303d15f0cd9c49a8606a02a741eac5bf2d1c9"
auth = {"Authorization": "Token %s" % token}
#print(auth)

# first find the UnitTestCollection we want to perform
resp = requests.get(root + '/qa/unittestcollections/?unit__name__icontains=LA4&test_list__name__icontains=Electron Energy', headers=auth)
utc_url = resp.json()['results'][0]['url']
pp.pprint(utc_url)

# prepare the data to submit to the API. Notice you don't need to submit a value for
# sum_of_two since it is calculated from number_1 and number_2

#YYYY-MM-DD HH:SS format (so 2021-12-1 1:00 is not valid)
data = {
    'unit_test_collection': utc_url,
    'in_progress': True,  # optional, default is False
    'work_started': "2021-12-17 12:00",
    'work_completed': "2021-12-17 13:00",  # optional
    'comment': "Testing waters 8...",  # optional
    'tests': {
        'set_baseline': {'value': 'No'},
        'E20': {'value':21.05, 'comment': "hello number 1"},
        'E16': {'value':17.2, 'comment': "hello number 1"},
        'E12': {'value':12.1, 'comment': "hello number 1"},
        'E9': {'value':9.05, 'comment': "hello number 1"},
        'E6': {'value':6.03, 'comment': "hello number 1"},
    },
    'attachments': []  # optional
}
#resp = requests.post(root + "/qa/testlistinstances/", json=data, headers=auth)

#pp.pprint(resp.json())




