import json
from models.donut_model import load_donut_model
from models.paddle_ocr import load_paddle_ocr
from PIL import Image

processor, model = load_donut_model()
ocr = load_paddle_ocr()

def extract_text(image_path):
    try:
        image = Image.open(image_path)
        inputs = processor(image, return_tensors="pt")
        outputs = model.generate(**inputs)
        text = processor.batch_decode(outputs, skip_special_tokens=True)[0]
        return text
    except Exception as e:
        print(f"Donut failed, fallback to OCR: {e}")
        result = ocr.ocr(image_path, cls=True)
        return " ".join([line[1][0] for line in result[0]])

def postprocess_to_json(raw_text):
    # TODO: подключить LLM для извлечения ключевых полей
    return {
        "document_type": "unknown",
        "raw_text": raw_text,
        "fields": {
            "account_number": "...",
            "date": "...",
            "amount": "..."
        }
    }

if __name__ == "__main__":
    doc = extract_text("data/sample_statement.jpg")
    structured = postprocess_to_json(doc)
    print(json.dumps(structured, indent=2, ensure_ascii=False))
