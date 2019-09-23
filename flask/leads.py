from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
LEADS = {
    "audi_r8_a": {
        "ref" : "audi-r8-a",
        "description": "Audi R8 4.2 FSI V8 R Tronic quattro 2dr",
        "value": 75500,
        "miles" : 32500,
        "year"  : 2007,
        "registration" : "AAAAAA",
        "timestamp": get_timestamp()
    },
    "audi_r8_b": {
        "ref" : "audi-r8-b",
        "description": "Audi R8 4.2 V8 QUATTRO AUTO 500 BHP 2 DR COUPE ABT BODYSTYLING",
        "value":  54000,
         "miles" : 36950,
         "year"  : 2008,
        "registration" : "BBBBBBB",
        "timestamp": get_timestamp()
    },
    "audi_r8_c": {
        "ref" : "audi-r8-c",
        "description": "Audi R8 4.2 FSI V8 R Tronic quattro 2dr ",
        "value": 65000,
         "miles" : 40000,
         "year"  : 2009,
        "registration" : "CCCCCC",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/lead
    with the complete lists of leads

    :return:        sorted list of leads
    """
    # Create the list of leads from our data
    return [LEADS[key] for key in sorted(LEADS.keys(),reverse=False)]