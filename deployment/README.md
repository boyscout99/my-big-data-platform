# Deployment guide

> Development environment: Ubuntu 20.04LTE Virtual Machine with 4Gb RAM, 100 Gb memory, 2 CPUs at 2.40GHz

Docker version: 20.10.12

Cassandra image version: latest

docker-compose version: 1.29.2

Python version: 3.8.10

pip version: 20.0.2

cassandra-driver version: 3.25.0

## Install the requirements

1. Update packages `apt update`
2. Install Docker Engine `curl -fsSL https://get.docker.com -o get-docker.sh; sudo sh get-docker.sh`
3. Install docker-compose `sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`, and `sudo chmod +x /usr/local/bin/docker-compose`
4. Install Python version 3 `sudo apt install python3.8.10`
5. Install pip `apt install pip`
6. Install the Python library cassandra-driver `pip install cassandra-driver`

## Using Cassandra as a Docker container

**mysimbdp-coredms** is implemented as a cluster of Cassandra two Docker containers: _code_cassandra1_1_ and _code_cassandra2_1_. To create the cluster refer to the /code folder in the repository.

## How to work with virtual environment
**MacOS/Linux - Method 1**
```
sudo apt-get install python3-venv
cd project-vaccine-distribution             # Move to the project root folder
python3 -m venv venv                        # Create a virtual environment 
source venv/bin/activate                    # Activate the virtual environment
(venv) $                                    # You see the name of the virtual environment in the parenthesis.
```
