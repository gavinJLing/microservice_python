# microservice_python
A Python based microservice. To allow me to explore the Python language for micro service experiments.



### Goal
To create a collection of python based REST apis adopting a Car theme. To Query car related data 
As part of a wider desire to present a collection of AWS EC2 REST api's within a Terraformed AWS & Azure data fabric.
With SIEM leveraging Splunk escalation (via email or Slack). Adopting a car theme.


### Docs
Leverages Python _[Flask](https://flask-restful.readthedocs.io/en/latest/)_ api


### Installs & setup
This is a Python3 application, so install python3 & Pip package manager. Because this api uses Python libraries to do the heavy lifting, we will need to install these also. 

```
pip install flask
pip install connextion
pip install connexion[swagger-ui]
```

## Car Leads (searches) api



Servcie Interface
```
  ./flask/spec/lead_api.yaml
```

Service implementation code
```
  ./flask/lead.py
```

Server (Connexion & Flask Http framework provide REST webservices )
```
  .flask/servce.py
```
**Start the HTTPServer**
```
$ cd ./flask
$ python service.py


 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat

 * Debugger is active!
```

> __We've started an HTTP server that can listen for, and process web requests. The 'connexion' & 'flask' frameworks will handle all the heavy lifting such as:__
* Listen on port 8080
* Process service interface spec. `./flask/spec/lead_api.yaml`
* Map the request url path to a service interface & implementation handler
* Unmarshal the request from a byte stream sent by the client. 
* execute a handler method, passing in any unmarshalled request params, path variables or post'd object structures.
* marshal the response back on to the wire
* Establish an HTTP response code 
* Send the whole lot back to the original client. Because this is a synchonous web servcie (a.k.a REST Microservice)

__Leaving the service implementation code to accept inputs, process them according to the business logic and return a 'thing'. We are leveraging a lot of default behaviour here.__



## Review the Interface

With the HTTP server (above) running. Issue the following url in a browser, to explore the service interface. 

```
http://localhost:8080/api/ui
```
> * Click 'Lead operations' link to see the group of Lead related api operations.  
> * Click 'Leads' link to see details of the 'Leads' api operation.
> * Click 'Try ot out' and scroll down - the api ../api/leads was executed and its Request URL/ Response headers and body are revealed.


## Testing

With the HTTP server running, we can test the above service. Issue the following url in a browser.
``` 
http://localhost:8080/api/leads
```

From a command line tool like 'curl' issue the following cmd line:
```
$ curl http://127.0.0.1:8080/api/leads -v
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8080 (#0)
> GET /api/leads HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 694
< Server: Werkzeug/0.15.5 Python/3.7.3
< Date: Fri, 27 Sep 2019 16:55:19 GMT
< 
[
  {
    "description": "Audi R8 4.2 FSI V8 R Tronic quattro 2dr",
    "miles": 32500,
    "ref": "audi-r8-a",
    "registration": "AAAAAA",
    "timestamp": "2019-09-27 17:49:06",
    "value": 75500,
    "year": 2007
  },
  {
    "description": "Audi R8 4.2 V8 QUATTRO AUTO 500 BHP 2 DR COUPE ABT BODYSTYLING",
    "miles": 36950,
    "ref": "audi-r8-b",
    "registration": "BBBBBBB",
    "timestamp": "2019-09-27 17:49:06",
    "value": 54000,
    "year": 2008
  },
  {
    "description": "Audi R8 4.2 FSI V8 R Tronic quattro 2dr ",
    "miles": 40000,
    "ref": "audi-r8-c",
    "registration": "CCCCCC",
    "timestamp": "2019-09-27 17:49:06",
    "value": 65000,
    "year": 2009
  }
]
* Closing connection 0
```


**Well Done!** - youve just executed a python microservice.



 
