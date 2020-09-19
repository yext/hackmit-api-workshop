import requests

# Set the URL
URL = 'http://m.mit.edu/apis/shuttles/routes/'

# Get the response
resp = requests.get(URL)

# Check for errors in receiving the response
if resp.status_code != 200:
    raise ApiError('Error: {}'.format(resp.status_code))

# Access data in the response
for route in resp.json():
	print('Title:', route['title'])
	print('Description:', route['description'])
	print('-----------------------------------')