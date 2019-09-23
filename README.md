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






 
