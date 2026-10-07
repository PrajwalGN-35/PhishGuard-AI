from __future__ import annotations

import importlib.util
from pathlib import Path

import joblib
import numpy as np
import streamlit as st

FEATURE_FILE = Path("feature_extraction.py")
MODEL_PATH = Path("models/random_forest.pkl")
FEATURE_NAMES = [
    "url_length",
    "dot_count",
    "has_at",
    "uses_https",
    "has_ip",
    "has_suspicious_keyword",
]


def load_feature_extractor():
    if not FEATURE_FILE.exists():
        raise FileNotFoundError(
            "Missing dependency: feature_extraction.py from Member 2 is not available on this branch. "
            "Fetch origin/feature/features before testing the full prediction flow."
        )

    spec = importlib.util.spec_from_file_location("member2_features", FEATURE_FILE)
    if spec is None or spec.loader is None:
        raise ImportError("Unable to load the feature extractor module.")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "extract_features"):
        raise AttributeError("The feature extractor does not define extract_features(url).")

    return module


def normalize_prediction(model, value):
    label_value = str(value).strip().lower()
    if label_value in {"0", "safe", "legitimate", "legit", "not_phishing", "benign"}:
        return "SAFE"
    if label_value in {"1", "phishing", "malicious", "fraudulent"}:
        return "PHISHING"

    classes = getattr(model, "classes_", None)
    if classes is not None:
        for candidate in classes:
            current = str(candidate).strip().lower()
            if "phish" in current or "mal" in current or "fraud" in current:
                return "PHISHING"
            if "safe" in current or "legit" in current or "benign" in current or "normal" in current:
                return "SAFE"

    return "SAFE" if int(value) == 0 else "PHISHING"


def feature_vector_from_result(result):
    if isinstance(result, dict):
        values = {name: result.get(name, 0) for name in FEATURE_NAMES}
    elif isinstance(result, (list, tuple)) and len(result) == len(FEATURE_NAMES):
        values = {name: result[idx] for idx, name in enumerate(FEATURE_NAMES)}
    else:
        raise ValueError(
            "extract_features(url) returned an unexpected format. "
            "Expected exactly six values in the required feature order."
        )
    return values


st.set_page_config(page_title="PhishGuard AI", page_icon="🛡️")

st.title("PhishGuard AI")
st.caption("Machine Learning Based Phishing URL Detection")

url_input = st.text_input("Enter a URL", placeholder="https://example.com")

if st.button("Analyze"):
    if not url_input or not url_input.strip():
        st.warning("Please enter a URL.")
    else:
        try:
            feature_module = load_feature_extractor()
            extracted = feature_module.extract_features(url_input)
            feature_values = feature_vector_from_result(extracted)

            if not MODEL_PATH.exists():
                st.error(
                    "Missing dependency: models/random_forest.pkl from Member 3 is not available on this branch. "
                    "Fetch origin/feature/models before running the trained model."
                )
                st.stop()

            model = joblib.load(MODEL_PATH)
            feature_array = np.asarray([feature_values[name] for name in FEATURE_NAMES], dtype=float).reshape(1, -1)
            prediction = model.predict(feature_array)[0]
            result_label = normalize_prediction(model, prediction)

            st.subheader("Prediction")
            st.markdown(f"Prediction: {result_label}")

            st.subheader("Extracted Features")
            st.write(
                {
                    "URL Length": feature_values["url_length"],
                    "Dot Count": feature_values["dot_count"],
                    "@ Present": feature_values["has_at"],
                    "HTTPS": feature_values["uses_https"],
                    "IP Address": feature_values["has_ip"],
                    "Suspicious Keyword": feature_values["has_suspicious_keyword"],
                }
            )

        except Exception as exc:  # pragma: no cover - streamlit error surface
            st.error(f"Unable to process the URL: {exc}")
