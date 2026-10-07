from ipaddress import ip_address
from urllib.parse import urlsplit


_SUSPICIOUS_KEYWORDS = (
    "login",
    "verify",
    "update",
    "secure",
    "bank",
    "account",
    "signin",
)


def _is_ip_address(hostname: str | None) -> bool:
    if not hostname:
        return False

    try:
        ip_address(hostname)
        return True
    except ValueError:
        return False


def extract_features(url: str) -> dict:
    try:
        parsed_url = urlsplit(url)
        hostname = parsed_url.hostname
        scheme = parsed_url.scheme.lower()
    except ValueError:
        hostname = None
        scheme = ""

    return {
        "url_length": len(url),
        "dot_count": url.count("."),
        "has_at": int("@" in url),
        "uses_https": int(scheme == "https"),
        "has_ip": int(_is_ip_address(hostname)),
        "has_suspicious_keyword": int(
            any(keyword in url.lower() for keyword in _SUSPICIOUS_KEYWORDS)
        ),
    }
