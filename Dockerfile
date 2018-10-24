# see this: https://qxf2.com/blog/preparing-a-docker-image-for-running-selenium-tests/
# see: https://www.blazemeter.com/blog/how-to-run-selenium-tests-in-docker
# see firefox image from dockerhub: https://hub.docker.com/r/selenium/standalone-firefox/

# TODO NOT WORKING - CONSIDER PULLING FROM DOCKERHUB or invest time to build own (make sure geckodriver is included,
# TODO browser,...)

FROM python:3.6-alpine

# maybe I'll need to specify ENV var for password here?

WORKDIR /

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Firefox browser to run the tests
RUN apt-get install -y firefox

# GeckoDriver v0.23
RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.23-linux64.tar.gz" -O /tmp/geckodriver.tgz \
    && tar zxf /tmp/geckodriver.tgz -C /usr/bin/ && rm /tmp/geckodriver.tgz

# create symlink to geckodriver (to the PATH)
RUN ln -s /usr/bin/geckodriver && chmod 777 /usr/bin/geckodriver

COPY . .

CMD [ "python", "-m", "unittest", "discover" ]



# have a script to tell Docker to download sel;enium image
# then run the image


# SEE THIS blogpost: https://www.blazemeter.com/blog/how-to-run-selenium-tests-in-docker
