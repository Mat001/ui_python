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
    
    Go into virtualenv `pipenv shell` Make sure docker-compose is running.  
    Run tests with `python -m pytest -s -v`  
    This will run firefox tests in docker container.  
    To run specific browser run:  
    `python -m pytest -s -v --browser firefox-remote` for firefox in docker  
    `python -m pytest -s -v --browser chrome-remote` for chrome in docker  
    `python -m pytest -s -v --browser firefox-local` for local firefox  
    `python -m pytest -s -v --browser chrome-local` for local chrome  
    
    If `--browser` option is not specified test will default to firefox in docker.
    
    Tests in docker will run headlessly. For logs see docker-compose console.


Things to improve:
- to set all browsers in docker to run with one command
- to remove redundant @property getter methods (and call locators directly from each 
page object)
- hide password in test credentials (env var?)
- logs for chrome test don't show in docker-compose logs because of an error
- currently remote hub and nodes are located on localhost (demo purposes). To move them to
 an IP away from local machine. 
- set exception conditions so test run stops when exceptions are raised
- set functionality to easily toggle between running tests in docker (remotely) and locally
 

