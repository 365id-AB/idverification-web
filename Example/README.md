# 365id idverification SDK Example solution

This is a simple sample app written in python making use of the 365id id verification SDK.

this can either be started directly using python or by using the dockerfile provided.

## Configuration

No source file needs to be edited. All settings are injected from the environment
and read by `credentials.py`:

| Variable | Description |
| --- | --- |
| `CLIENT_ID` | Your License Key client id |
| `CLIENT_SECRET` | Your License Key client secret |
| `WEB_SDK_TOKEN_URL` | Token endpoint (has a default) |
| `ALLOWED_ORIGIN` | Origin pattern the SDK is allowed to run on |
| `TRANSFER_DEVICE_DOMAIN_URL` | URL used when transferring to a second device |
| `FLASK_SECRET_KEY` | Flask session key (random per start if unset) |

Each variable can also be supplied as `<NAME>_FILE` pointing at a file that holds
the value, which is how Docker secrets are consumed.

### STEP 1

```sh
cp .env.example .env
# then fill in CLIENT_ID, CLIENT_SECRET, ALLOWED_ORIGIN and
# TRANSFER_DEVICE_DOMAIN_URL
```

`.env` is git-ignored, so your credentials stay out of the repo.

## Run using python

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
docker run --rm -it -p 5001:5001 --env-file .env \
  -e CLIENT_ID -e CLIENT_SECRET \
  365id/web-id-verification
```

## Run using Docker Compose

Everything comes from `.env`. `CLIENT_ID` and `CLIENT_SECRET` are passed in as
Docker secrets, so they reach the app as files under `/run/secrets/` rather than
as environment variables on the process.

The secrets are sourced from the environment rather than from files on disk,
which means this also works against a remote docker context (`docker context
use ...`), where a host path would not exist on the machine running the
container. Compose v2.23 or later is required for that.

```sh
npm login
docker compose build --no-cache
docker compose up -d
```

### STEP 3

Follow [this link](http://localhost:5001) to the [Example](http://localhost:5001)
