# 365id idverification SDK Example solution

This is a simple sample app written in python making use of the 365id id verification SDK.

this can either be started directly using python or by using the dockerfile provided.

## Run using python

```sh
# On macOS or Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
npm install @365id/id-verification
python sample_app.py

# On Windows
py -3 -m venv .venv
./.venv/Scripts/Activate.bat
pip install -r requirements.txt
npm install @365id/id-verification
python sample_app.py
```

## Run using Docker

```sh
DOCKER_BUILDKIT=1 docker build --no-cache --secret id=npmrc,src=$HOME/.npmrc -t 365id/web-id-verification .
docker run --rm -it -p 5001:5001 365id/web-id-verification
```
