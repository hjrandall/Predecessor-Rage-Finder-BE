# Predecessor-Rage-Finder-BE
This is the back end for the rage finder web app we are making

mongo db credentials
username = Developer
password = QjeAr4lwRkKYsiBW

in order to get the database set up in your local environment follow these steps

*first make sure you have downloaded python*
    in the command line type        python -v
    if it shows a version you are set.
    if it does not show there is a version go to https://www.python.org/downloads/windows/ to download python

*second you will download fastapi* 
    in the command line type                                    pip install fastapi

*third you will need to install uvicorn*
    in the command line type                                    pip install uvicorn

*fourth you will need to install mongo db*
    in the command line type                                    python -m pip install pymongo

*You are now all set to start up the server locally!*
    to run the server locally, in the command line type         python .\main.py

For running the the be on the server you need to run    setsid python3 main.py then pres ctr d to disconect it from the terminal
run ps aux to see background programms
to stop run kill <pid>