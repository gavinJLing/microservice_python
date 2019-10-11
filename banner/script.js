// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest()

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://localhost:5000/banner/helloworld?font=thick', true)

request.onload = function() {
  const bannerDiv = document.createElement('BannerHere')
  bannerDiv.setAttribute('class', 'container')
}

// Send request
request.send()