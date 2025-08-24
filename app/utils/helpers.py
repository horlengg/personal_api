from flask import request
from urllib.parse import urlparse

def get_client_ip():
    """Return the real client IP address from a Flask request object."""
    if request.headers.get("X-Forwarded-For"):
        # Handles proxies/load balancers (first IP is the client)
        ip = request.headers.get("X-Forwarded-For").split(",")[0].strip()
    else:
        ip = request.remote_addr
    return ip


def is_localhost(url: str) -> bool:
    parsed = urlparse(url)
    hostname = parsed.hostname
    
    if hostname is None:
        return False
    
    return hostname in ("localhost", "127.0.0.1", "0.0.0.0") or hostname.startswith("127.")