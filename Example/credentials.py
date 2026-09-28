"""Configuration for the 365id WEB Id Verification SDK example app.

Every value is injected from the environment, so nothing has to be edited in
the source code. Two sources are supported, checked in this order:

1. ``<NAME>_FILE`` - path to a file holding the value. This is what Docker
   Compose uses: a secret declared in ``docker-compose.yml`` is mounted at
   ``/run/secrets/<name>``.
2. ``<NAME>`` - the value directly in an environment variable.

When running without Docker, export the variables yourself or put them in a
``.env`` file next to this one (see ``.env.example``).
"""

import os
from pathlib import Path


def _load_dotenv(path: Path) -> None:
    """Load ``KEY=value`` pairs from a .env file into the environment.

    Lets the app run with plain ``python sample_app.py``, without Docker
    Compose to supply the environment. Blank lines, comments and lines
    without ``=`` are skipped, and surrounding quotes are stripped from the
    value. Existing environment variables win, so an exported variable or a
    Docker secret is never overwritten by the file.

    Args:
        path: The .env file to read. A missing file is not an error.
    """
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


_load_dotenv(Path(__file__).parent / ".env")


def get_config(name: str, default: str | None = None) -> str:
    """Return a configuration value from the environment.

    Sources are checked in order:

    1. ``<name>_FILE`` - a path to a file holding the value, which is how
       Docker secrets are mounted (``/run/secrets/<secret>``). The contents
       are stripped of surrounding whitespace.
    2. ``<name>`` - the value directly in an environment variable. An empty
       variable counts as unset, so a blank entry in .env falls back to the
       default.
    3. `default`, when one was given.

    Args:
        name: Name of the environment variable, e.g. ``"CLIENT_ID"``.
        default: Value to use when neither source provides one. Omit it to
            make the setting required.

    Returns:
        The resolved configuration value.

    Raises:
        RuntimeError: No source provided a value and there is no `default`.
        OSError: ``<name>_FILE`` is set but the file cannot be read.
    """
    file_path = os.environ.get(f"{name}_FILE")
    if file_path:
        return Path(file_path).read_text(encoding="utf-8").strip()

    value = os.environ.get(name)
    if value:
        return value

    if default is not None:
        return default

    raise RuntimeError(
        f"Missing configuration: set {name} or {name}_FILE. "
        "See .env.example and docker-compose.yml."
    )


# --- Credentials (your License Key), injected as Docker secrets ---------------
client_id = get_config("CLIENT_ID")
client_secret = get_config("CLIENT_SECRET")

# --- Endpoint and payload settings -------------------------------------------
web_sdk_token_url = get_config(
    "WEB_SDK_TOKEN_URL",
    "https://global-customer-frontend.365id.com/api/v1/websdktoken",
)
allowed_origin = get_config("ALLOWED_ORIGIN")
transfer_device_domain_url = get_config("TRANSFER_DEVICE_DOMAIN_URL")

# --- Flask ---------------------------------------------------------------
flask_secret_key = get_config("FLASK_SECRET_KEY", os.urandom(32).hex())
