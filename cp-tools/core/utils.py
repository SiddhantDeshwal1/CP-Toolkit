# utils.py
import logging

import httpx
from settings import LOGGING_ENABLED, REQUEST_TIMEOUT

# Setup Logging
if LOGGING_ENABLED:
    logging.basicConfig(level=logging.INFO)


def fetch_json(url):
    """Fetch JSON response from a URL."""
    try:
        response = httpx.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Request failed: {e}")
        return None


def convert_to_ist(utc_timestamp):
    """Convert UTC timestamp to IST."""
    from datetime import datetime, timedelta, timezone

    return datetime.fromtimestamp(utc_timestamp, timezone.utc) + timedelta(
        hours=5, minutes=30
    )
