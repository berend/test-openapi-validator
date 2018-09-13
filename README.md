# test-openapi-validator


Install requirements with
    
    $ pip install -r requirements.txt
    
Run example app with:

    $ python server.py
    
Do an example request with `curl`:

    curl -X POST \
    http://127.0.0.1:8080/cars \
    -H 'Content-Type: application/json' \
    -d '{"ps": 123}'
    
This should contain two errors.
