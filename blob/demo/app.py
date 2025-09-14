import streamlit as st
from app.pipeline import extract_text, postprocess_to_json
import json
import tempfile

st.title("🏦 OCR для банковских документов (MVP)")
uploaded_file = st.file_uploader("Загрузите документ (jpg/png/pdf)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.image(tmp_path, caption="Загруженный документ", use_column_width=True)
    raw_text = extract_text(tmp_path)
    result = postprocess_to_json(raw_text)

    st.subheader("Извлеченный JSON")
    st.json(result)
