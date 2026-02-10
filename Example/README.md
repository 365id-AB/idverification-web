# 365id idverification SDK Example solution

This is a simple sample app written in python making use of the 365id id verification SDK.

this can either be started directly using python or by using the dockerfile provided.

## Run using python

### STEP 1

Update `credentials.py` with your credentials.

### STEP 2

```sh
# On macOS or Linux
python3 -m venv .venv
source .venv/bin/activate

# On Windows
py -3 -m venv .venv
# Command Prompt (CMD)
./.venv/Scripts/Activate.bat
# Powershell
./.venv/Scripts/Activate.ps1

# This common for all platforms
pip install -r requirements.txt
npm login
npm install @365id/id-verification
python sample_app.py
```

## Run using Docker

```sh
npm login
DOCKER_BUILDKIT=1 docker build --no-cache --secret id=npmrc,src=$HOME/.npmrc -t 365id/web-id-verification .
docker run --rm -it -p 5001:5001 365id/web-id-verification
```

## Run using Docker Compose

```sh
npm login
docker compose build --no-cache
docker compose up -d
```

### STEP 3

Follow [this link](http://localhost:5001) to the [Example](http://localhost:5001)