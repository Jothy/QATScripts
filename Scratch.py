import requests
import pprint as pp


root = "https://canberra-staging.multileaf.ca/api"
token_url = root + "/get-token/"
resp = requests.post(token_url, {'username': 'jselvaraj', 'password': 'Shiva_1234'})
token = resp.json()['token']
auth = {"Authorization": "Token %s" % token}
#print(auth)

# first find the UnitTestCollection we want to perform
resp = requests.get(root + '/qa/unittestcollections/?unit__name__icontains=LA4&test_list__name__icontains=RPM QA', headers=auth)
utc_url = resp.json()['results'][0]['url']
pp.pprint(utc_url)

# prepare the data to submit to the API. Notice you don't need to submit a value for
# sum_of_two since it is calculated from number_1 and number_2
data = {
    'unit_test_collection': utc_url,
    'in_progress': False,  # optional, default is False
    'work_started': "2021-12-15 11:00",
    'work_completed': "2021-12-15 12:00",  # optional
    'comment': "Testing waters...",  # optional
    'tests': {
        'rpm_trilogy_done': {'value':True, 'comment': "hello number 1"}, # comment is optional
    },
    'attachments': []  # optional
}
resp = requests.post(root + "/qa/testlistinstances/", json=data, headers=auth)

print(resp)

