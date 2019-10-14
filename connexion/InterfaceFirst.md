# Interface First - Microservice
A Python based microservice, where OpenAPI (Swagger) is used to describe a micro service. The microservice application leverages a coding framework (connexion) to provide the REST api heavy lifting, leaving the business logic implementation to you. 



### Connexion 

```
pip install flask
pip install connextion
pip install connexion[swagger-ui]
```

## Hello World example

An example of minimal [interface first](interfacefirst.md) appraoch to creating a microservice.
The api for a basic hello world service is provided by the OpenAPI spec. (formally 'Swagger') `hello_api.yaml` where the service request / response, operations, query params, url path varialbes etc are defined. The break down of the api yaml file can be found [here](helloopenapi.md) if its not obvious.

The api describes a `/greeting` service endpoint. Where the client (browser) call would be `http://{host}:{port}/greeting`
__Notice__ the `operationId` which is OpenApi specific. It provides a hint to the implmenation of the service.

So far we have not considered the business logic (implemenation) of the service. Which will be written in python code. 
The ojective is to write the least amount of code required to implement the described api. which can be seen in 'hello_api.py`

As you will see its fairly terse.  By leveraging the 'Connexion' framework which builds upon 'flask'  to provide boiler plate code for the complexities of web services handling. All we nee to do is implement the 'handler' aspect of the micro service implmentation. As hinted at by the service interface .yaml 'operartionId:' hinted at above.

Within a file called 'hello_api.py' paste the code snippet below and save.

```
# `hello_api.py` file contents
def say_hello(name=None):
    return {"message": "Hello {}, to my first python flask microservice API!".format(name or "you") }
```

So we have 2 files:
* Service interface spec. `hello_api.yaml`
* Service implementation code `hello_api.py`

## Execute the microservice
Execute the following command line to start an HTTP server and bind our service spec. to our implementation. Ready for testing.

```
$ connexion run hello_api.yaml -v
```
Whats happening?

> __We've started an HTTP server that can listen for, and process web requests. The 'connexion' & 'flask' frameworks will handle all the heavy lifting such as:__
* Listen on a port
* Map the request url path to a service interface & implementation handler
* Unmarshal the request from a byte stream sent by the client. 
* execute a handler method, passing in any unmarshalled request params, path variables or post'd object structures.
* marshal the response back on to the wire
* Establish an HTTP response code 
* Send the whole lot back to the original client. Because this is a synchonous web servcie (a.k.a REST Microservice)

__Leaving the service implementation code to accept inputs, process them according to the business logic and return a 'thing'. We are leveraging a lot of default behaviour here.__


## Testing

With the HTTP server running, we can test the above service. FRom a browser or commandline tool issue the following url
``` 
http://localhost:5000/greeting?Gavin
```

The server shown process the request and issue a response to the client in the form of a json object:
```
{
  "message": "Hello Gavin, to my first python flask microservice API!"
}
```

From a command line tool like 'curl' issue the following cmd line:
```
$ curl localhost:5000/greeting?name=gavin -v

*   Trying ::1...
* TCP_NODELAY set
* Connection failed
* connect to ::1 port 5000 failed: Connection refused
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET /greeting?name=Gavin HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 75
< Server: Werkzeug/0.15.5 Python/3.7.3
< Date: Thu, 26 Sep 2019 06:51:45 GMT
< 
{
  "message": "Hello Gavin, to my first python flask microservice API!"
}
* Closing connection 0
```


**Well Done!** - youve just executed a python microservice.

