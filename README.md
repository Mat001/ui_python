## UI selenium test framework in Python.

End to end test of a purchase of a commercial product on a test website 
(http://automationpractice.com/index.php).

### Instructions to run

1. ###### Prerequisites
    
    install pipenv, docker, docker-compose  
    Requires Python >= 3.6.

2. ###### Docker images
    Pull down the hub and node images from docker-hub by running docker-compose,  
    (Make sure docker (docker daemon) is running first):  
    run `docker-compose up`  
    This will activate nodes (isolated browser VMs) and register them with the hub.

3. ###### Run tests
    
    Go into virtualenv `pipenv shell`    
    Run tests with `python -m pytest -s -v`  
    To run specific browser in docker comment out appropriate browser in "driver" fixture 
    in webdriver_factory.py file (for local browsers set correct path to geckodriver 
    and chromedriver).   
    Tests will run headlessly in docker container. For logs see docker-compose console.
    
To run tests locally (not using docker) uncomment Firefox or Chrome in section "locally" 
in "driver" fixture in test_application_flow.py file. Disable (comment out) "remote" 
section. Download geckodriver and chromedriver and add their paths to each driver 
instance. Then run `python -m pytest -v -s`


Things to improve:
- to remove redundant @property getter methods (and call locators directly from each page object)
- hide password in test credentials (env var?)
- logs for chrome test don't show in docker-compose logs because of an error
- currently remote hub and nodes are located on localhost (demo purposes). To move them to
 an IP away from local machine. 
- set exception conditions so test run stops when exceptions are raised
- set functionality to easily toggle between running tests in docker (remotely) and locally
 

