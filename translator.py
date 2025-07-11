from deep_translator import GoogleTranslator

def translate_to_english(text, source='auto'):
    if not text.strip():
        return ""

    translated_text = []
    try:
        paragraphs = text.split('\n')
        for para in paragraphs:
            para = para.strip()
            if para:
                translated_para = GoogleTranslator(source=source, target='en').translate(para)
                translated_text.append(translated_para)
        return '\n'.join(translated_text)
    except Exception as e:
        print(f"Translation Error: {e}")
        return ""
