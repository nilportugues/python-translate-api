import googletrans


def execute(dto):
    # Read data
    text = dto.get("text", "")

    translator = googletrans.Translator()
    result = translator.detect(text)

    return True, {
        "language": result.lang,
        "confidence": result.confidence
    }

