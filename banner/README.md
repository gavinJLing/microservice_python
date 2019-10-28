# National Cyber Security Centre (NCSC)
## Cyber School Hub event
### Discuss aspects of web service security:
With 80 year9-10 (aged 13-15) London school students:  Example client server with basic header security & CORS


## banner
This simple server project written in Python using the popular flask package. To act as a basic REST service to various clients within this overall project.

### Before you start
This is a python3 project, which requires Python3 to be installed together with its package download manager `pip`. I would suggest that you look at a Python environment manager. They allow you to support various flavours of python (python2 & python3).


### Get the code
Download the code from the cloud repository.
```
$ git clone {url}/microservice_python
$ cd microservice_python
```

### Install Dependancies
```
$ pip3 install -r requirements.txt
```

### Run the server
```
$ ./bannerserver.py
```
The expected response would be:
```
 * Serving Flask app "bannerserver" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 742-324-475

```



### Test the server

see [Testing the service](test_bannerserver.md)

## The talk...
Aspects discussed with the students.

- Overview: What is going on, how & why. An example of intersystem communications.
    - Demostration of basic service. The Banner system. (see above test
- Server: REST Webservice - URL query parameters and HTTP security header
    - [Password faults](server_banner.md)
        - Hard coded, clear text password
        - Unofficial HTTP header, lack of JWT or similar token
        - Crude static authentication check mechanism, requiring stateful password checking - negated by JWT.
- Client: OS tools (curl), use of URL Query params & authentication headers
    - Use of Curl OS Man page
    - Use of --verbose switch to reveal interaction
    - Visualisation of TLS handshaking for HTTPS comms to Google.
    - See [more...](client_curl.md)
- Client: Python Flask, simple client coding and HTTP header passing
    - See [more...](client_python.md)
- Client: Chrome Browser direct
    - Use of Chrome Developer tools
    - Use of Modify Headers plugin to inject Authentication header (for testing)
    - See [more...](client_browser.md)
- Client: Web Client, JavaScript AJAX aysnc. server call, security header passing
    - JavaScript sandbox, errors and pre flight 'options' check
    - CORS violation - why this is happening
    - Server changes to overcome CORs (bad)
    - See [more...](client_webappAjax.md)
- Client: PostMan
    - See [more...](client_postman.md)
- Interactive Terminal attachment to invoke REST api.
    - See [more...](client_terminal_mac.md)
- HTTP Headers and Response codes
    - See [more...](headers_ResponseCodes.md)
