"""Shared X API authentication — macOS Keychain + OAuth1."""

import subprocess

import requests
from requests_oauthlib import OAuth1


def get_keychain_secret(service: str, account: str = "stikman28") -> str:
    """Retrieve a secret from macOS Keychain."""
    result = subprocess.run(
        ["security", "find-generic-password", "-a", account, "-s", service, "-w"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to retrieve '{service}' from Keychain: {result.stderr.strip()}")
    return result.stdout.strip()


def get_auth() -> OAuth1:
    """Create OAuth1 auth using Keychain credentials (fir-risk-publisher app)."""
    return OAuth1(
        get_keychain_secret("X_PUBLISH_CONSUMER_KEY"),
        get_keychain_secret("X_PUBLISH_CONSUMER_SECRET"),
        get_keychain_secret("X_PUBLISH_ACCESS_TOKEN"),
        get_keychain_secret("X_PUBLISH_ACCESS_TOKEN_SECRET"),
    )


def get_user_id(auth: OAuth1) -> str:
    """Get the authenticated user's X user ID."""
    resp = requests.get("https://api.x.com/2/users/me", auth=auth)
    if resp.status_code != 200:
        raise RuntimeError(f"Failed to get user ID: {resp.status_code} {resp.text}")
    return resp.json()["data"]["id"]
