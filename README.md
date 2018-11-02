## UI selenium test framework in Python.

End to end test of a purchase of a commercial product on a test website 
(http://automationpractice.com/index.php).

### Instructions to run

1. ###### Prerequisites
    
    install pipenv, docker, docker-compose

2. ###### Docker images
    Pull down the hub and node images from docker-hub by running docker-compose,  
    (Make sure docker (docker daemon) is running first):  
    run `docker-compose up`  
    Nodes (isolated browser VMs) will become activated and registered with the hub.

3. ###### Run e2e tests by running tox
    
    Go into virtualenv `pipenv shell`    
    Run tests with `tox -v firefox, chrome`
    To run specific browser type in terminal `tox -v -e firefox` or `tox -v -e chrome`
    
To run tests locally (not using docker) uncomment section "local" in setUpClass() 
method in EnvironmentSetup class. Disable (comment out) "remote" section. Download 
geckodriver and chromedriver and add their paths to each driver instance. Requires 
Python 3.


Things to improve:
- to remove redundant @property getter methods (and call locators directly from each page object)
- add WebdriverFactory class to deal with multiple browsers (instead of tox and env variable)
 master - for that need to change unittest to Pytest and use parameterization
- hide password in test credentials
- logs for chrome test don't show in docker-compose logs because of an error
- currently remote hub and nodes are located on localhost (demo purposes). To move them to
 an IP away from local machine. 
- set exception conditions so test run stops when exceptions are raised
 

