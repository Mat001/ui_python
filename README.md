## UI selenium test framework in Python.

### Instructions to run

1. ###### Prerequisites
    
    install pipenv, docker, docker-compose

2. ###### Docker images

    Pull down the hub and nodes from docker-hub:
        Make sure docker (docker daemon) is running.
        `docker pull selenium/hub selenium/node-chrome selenium/node-firefox`
    Bring up the hub and the nodes by running `docker-compose up`.
        This will activate them and register the nodes (remote browser VMs) with the hub.

3. ###### Run e2e tests by running tox
    
    Go into virtualenv `pipenv shell`    
    Run tests with `tox -v firefox, chrome`
    To run specific browser type in terminal `tox -v -e firefox` or `tox -v -e chrome`
    
To run tests locally (not using docker) uncomment section "local" in setUpClass() 
method in EnvironmentSetup class. Comment out "remote" section.

Download and add geckodriver and chromedriver paths to the driver instance. 


Things to improve:
- hide password in test credentials
- logs for chrome test don't show in docker-compose logs because of an error
- currently remote hub and nodes are located on localhost (demo purposes). 
To move them to an IP away from local machine. 

