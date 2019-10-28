# National Cyber Security Centre (NCSC)
## Cyber School Hub event


### Notes:
The service is deliberately crude. In an attempt to reveal aspect of security.

1.  The password is hardcoded and in the clear. Consider improvements that word improve on this...

>> - __Hard coding__. In the real world not even a static machine to machine technical account/password should be hard coded within the code. This is because the it makes the code brittle, but mainly the anybody with access to the source code repo, can see the password which negates its purpose. Passwords can be passed in the runtime code as an environment variable or resolved by querying a persisten store (db/Ldap etc). 
>> - __Authentication__ (I am me). Used to gain access to a system/service. Clear text password are weak authentication, Password is usually known to both client and server, communicated over some connection/transport. The transport can be intercepted and read (Man in the middle attack vector) Encryption and hashing are viable solutions. Both system require the client & server to understand the algorithm used and any key phrase required to encode/decode the password. Middle ware and API gateways can be used to determine the validity of the request. Removing the need to Authentication checks within the server code.
>> - __Authorisation__ (I have 'admin' authority). Used to determine the scope of your authority. Authorisation is different to Authentication. Authorissation is light weight security measure. JWT can be leverage to determine what you can and can't do within the server. JWTs are stateless authorisation tokens. Meaning that they are self contained and do not require a call to a persistent store in order to validate authority. They can't easily be changed and can be set to expire (TTL). The body payload of a JWT can contain app. specific data, and is base64 coded along with its meta data (alg., ttl etc) but also has a hashed value which means although the body can be easily read (base64 - decode) it can't be changed. It's effectively immutable, it can however be replayed within the life span of its ttl.




- Overview: What is going on, how & why. An example of intersystem communications.
    - Demostration of basic service. The Banner system.
- Server: REST Webservice - URL query parameters and HTTP security header
    - Password faults
        - Hard coded, clear text password
        - Unofficial HTTP header, lack of JWT or similar token
        - Crude static authentication check mechanism, requiring stateful password checking - negated by JWT.
    - Python Flask server coding framework for quick REST, header and Query param processing.
    - See [more...](server_banner.md)
