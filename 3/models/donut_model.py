from transformers import DonutProcessor, VisionEncoderDecoderModel

def load_donut_model():
    processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base")
    model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base")
    return processor, model
