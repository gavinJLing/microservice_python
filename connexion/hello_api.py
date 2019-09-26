# `hello_api.py` file contents

def say_hello(name=None):
    return {"message": "Hello {}, to my first python flask microservice API!".format(name or "you") }
