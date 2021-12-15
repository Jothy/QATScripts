import requests
root = "http://yourservernamehere/api"
token_url = root + "/get-token/"
resp = requests.post(token_url, {'username': 'user', 'password': 'password'})
token = resp.json()['token']
headers = {"Authorization": "Token %s" % token}

# first find the UnitTestCollection we want to perform
resp = requests.get(root + '/qa/unittestcollections/?unit__name__icontains=Unit 1&test_list__name__icontains=Simple API Example', headers=headers)
utc_url = resp.json()['results'][0]['url']

# prepare the data to submit to the API. Notice you don't need to submit a value for
# sum_of_two since it is calculated from number_1 and number_2
data = {
    'unit_test_collection': utc_url,
    'day': 0, # optional day=0, for TestLists, required for Test List Cycles (where 0 <= day < # of test lists in cycle)
    'in_progress': False,  # optional, default is False
    'include_for_scheduling': True,
    'work_started': "2018-07-6 10:00",
    'work_completed': "2018-07-6 11:00",  # optional
    'comment': "test list comment",  # optional
    'tests': {
        'number_1': {'value': 1, 'comment': "hello number 1"}, # comment is optional
        'number_2': {'value': 2, 'skipped': False},  # value is mandatory, skipped is optional
    },
    'attachments': []  # optional
}
resp = requests.post(root + "/qa/testlistinstances/", json=data, headers=headers)

print(resp.json())

