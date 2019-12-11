#!/usr/bin/env python3
import sys
import os

name = sys.argv[2]
repo_name = sys.argv[1]
print("on est dedans")
print(name)
print(repo_name)
os.system("docker rm -f " + name)
os.system("docker rmi -f " + repo_name)
os.system("docker pull " + repo_name)
os.system("/devops/script/docker_run_script")
