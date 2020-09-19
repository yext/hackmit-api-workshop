# ...

# Set the URL and parameters
URL = 'http://m.mit.edu/apis/shuttles/vehicles/'
PARAMS = {
	'agency': 'mit',
	'routes': 'tech',
}

# Get the response
resp = requests.get(url = URL, params = params)

# ...

###############################################################

# Set the URL with parameters inside
URL = 'http://m.mit.edu/apis/shuttles/vehicles?agency=mit&routes=tech'

# Get the response
resp = requests.get(URL)

# ...