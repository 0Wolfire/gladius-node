import subprocess
import os
import sys
import requests
import json
from time import sleep
from shutil import copyfile



def setup_peer(node_name):
    # Create our config files config file
    copyfile("/vagrant/tests/test_files/gladius-controld.toml", "/gladius/gladius-controld.toml")
    copyfile("/vagrant/tests/test_files/gladius-networkd.toml", "/gladius/gladius-networkd.toml")

    # Start the controld in the background
    subprocess.Popen("/vagrant/build/gladius-controld >> /tmp/controld_%s.out 2>&1" % node_name,
                     env={"GLADIUSBASE": "/gladius"},
                     shell=True)

    # Wait for controld to start
    sleep(15)

    # Create an account
    url = "http://localhost:3001/api/keystore/account/create"
    data = '''{"passphrase":"password"}'''
    response = requests.post(url, data=data).text
    print "account response: " + response

    url = "http://localhost:3001/api/keystore/account/open"
    data = '''{"passphrase":"password"}'''
    response = requests.post(url, data=data).text
    print "unlock repsonse: " + response



if __name__ == "__main__":
    setup_peer(sys.argv[1])
