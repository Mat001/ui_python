## UI selenium test framework in Python.

### Instructions to run

1. ###### Prerequisites
    
    install pipenv, docker, docker-compose

2. ###### Docker images
    Pull down the hub and nodes images from docker-hub by running docker-compose,  
    (Make sure docker (docker daemon) is running first):  
    run `docker-compose up`  
    Nodes (isolated browser VMs) will become activated and registered with the hub.

3. ###### Run e2e tests by running tox
    
    Go into virtualenv `pipenv shell`    
    Run tests with `tox -v firefox, chrome`
    To run specific browser type in terminal `tox -v -e firefox` or `tox -v -e chrome`
    
To run tests locally (not using docker) uncomment section "local" in setUpClass() 
method in EnvironmentSetup class. Comment out "remote" section.

Download and add geckodriver and chromedriver paths to the driver instance. 


Things to improve:
- add WebdriverFactory class to deal with multiple browsers (instead of tox and env variable)
- hide password in test credentials
- logs for chrome test don't show in docker-compose logs because of an error
- currently remote hub and nodes are located on localhost (demo purposes). 
To move them to an IP away from local machine. 

