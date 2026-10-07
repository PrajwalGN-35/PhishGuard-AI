import re
from urllib.parse import urlsplit


_IPV4_PATTERN = re.compile(
    r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}"
    r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
)
_SUSPICIOUS_KEYWORDS = ("login", "verify", "update", "secure", "bank", "account", "signin")


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
        "has_ip": int(bool(hostname and _IPV4_PATTERN.fullmatch(hostname))),
        "has_suspicious_keyword": int(
            any(keyword in url.lower() for keyword in _SUSPICIOUS_KEYWORDS)
        ),
    }