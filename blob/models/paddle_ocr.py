from paddleocr import PaddleOCR

def load_paddle_ocr():
    return PaddleOCR(use_angle_cls=True, lang='en')
