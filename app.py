import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

from feature_extraction import extract_features


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "random_forest.pkl"

FEATURE_ORDER = [
    "url_length",
    "dot_count",
    "has_at",
    "uses_https",
    "has_ip",
    "has_suspicious_keyword",
]


@st.cache_resource
def load_model():
    with MODEL_PATH.open("rb") as file:
        return pickle.load(file)


def main():
    st.set_page_config(
        page_title="PhishGuard AI",
        page_icon="🛡️",
        layout="centered",
    )

    st.title("PhishGuard AI")
    st.write("Machine Learning Based Phishing URL Detection")

    url = st.text_input(
        "Enter a URL",
        placeholder="https://example.com",
    )

    if st.button("Analyze URL", type="primary"):
        if not url.strip():
            st.warning("Please enter a URL.")
            return

        try:
            clean_url = url.strip()
            features = extract_features(clean_url)
            model = load_model()

            feature_vector = pd.DataFrame(
                [[features[name] for name in FEATURE_ORDER]],
                columns=FEATURE_ORDER,
            )

            prediction = int(model.predict(feature_vector)[0])

            st.subheader("Prediction")

            if prediction == 1:
                st.error("⚠️ Phishing")
            else:
                st.success("✅ Safe")

            with st.expander("Extracted Features"):
                for name in FEATURE_ORDER:
                    st.write(f"**{name}:** {features[name]}")

        except Exception as exc:
            st.error(f"Unable to analyze the URL: {exc}")


if __name__ == "__main__":
    main()
