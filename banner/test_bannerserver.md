# National Cyber Security Centre (NCSC)
## Cyber School Hub event


## Test the BANNER server
Ensure that you are within the folder where the server has been downloaded, and all its dependancies have been resolved...
```
$ cd microservice_python
$ pip3 install -r requirements.txt
```

Run the server
```
$ ./bannerserver.py
```

The expected response would be:
```
 * Serving Flask app "bannerserver" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 742-324-475

```

### Testing the server (banner service)
Testing the server is simple achieved by invoking the REST endpoint URL from the operating system command prompt using basic comms tools like `curl`. Open a command window and type the following command.  

Optionally add `--verbose` to see more details of the communication that is is occurring between the client (`curl`) and the server (`bannerserver.py`)
```
$ curl "localhost:5000/banner/hello" -H "password:stumpylongnose"
```

The expected response would be:
```
|         |    |                            |        |
|---.,---.|    |    ,---.    . . .,---.,---.|    ,---|
|   ||---'|    |    |   |    | | ||   ||    |    |   |
`   '`---'`---'`---'`---'    `-'-'`---'`    `---'`---'
```

Well done! You have downloaded, started and tested teh Banner micro service.



### Futher tests

- add the `--verbose` command line option
- Change the password e.g. `Stumpy Long Nose'
- Change the header  e.g. `-H "PassWord:stumpylongnose"
- Change the format (URL query parameter) to `JSON`, `HTML` or `xxxx` , remove it altogether

e.g.

```
$ curl "localhost:5000/banner/hello world" -H "password:stumpylongnose"
$ curl "localhost:5000/banner/hello%20world" -H "password:stumpylongnose"
$ curl "localhost:5000/banner/hello%20world?format=HTML" -H "password:stumpylongnose"
$ curl "localhost:5000/banner/hello%20world?format=PLAIN&font=graffiti" -H "password:stumpylongnose"
$ curl "localhost:5000/banner/hello%20world?format=PLAIN&font=graffiti" -H "password:Stumpy Long Nose"
$ curl "localhost:5000/banner/hello%20world?format=PLAIN&font=graffiti" -H "PassWord:stumpylongnose"
$ curl "localhost:5000/banner/hello%20world?format=PLAIN&font=graffiti" -H "Pass Word:stumpylongnose"
```
