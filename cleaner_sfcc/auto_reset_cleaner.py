#!/usr/bin/env python3

import os
import requests

id = os.environ["CLIENT_ID_SFCC"]
pw = os.environ["CLIENT_PW_SFCC"]

r = requests.get("http://localhost:9250/blacklist/save/", auth=(id, pw))

stop_docker_sfcc_clean = "docker rm -f sfcc_clean"
run_docker_sfcc_clean = "docker run -p 9250:9250 --name sfcc_clean -e CLIENT_ID_SFCC -e CLIENT_PW_SFCC -d khsadira/sfcc_clean:latest"


os.system(stop_docker_sfcc_clean)
os.system(run_docker_sfcc_clean)
