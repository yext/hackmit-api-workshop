const fetch = require('node-fetch');

// Set the URL
var URL = 'http://m.mit.edu/apis/shuttles/routes/'

fetch(URL)
	// Convert response to JSON object
	.then(response => {
		return response.json();
	})
	// Access data in the response
	.then(routes => {
		routes.forEach((route) => {
			console.log('Title:', route.title)
			console.log('Description:', route.description)
			console.log('-----------------------------------')
		})
	})
