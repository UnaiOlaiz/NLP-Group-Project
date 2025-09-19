arab_quran = "data/arab_quran.txt"
eng_quran = "data/english_quran.txt"

import re

def normalize_arabic(text: str) -> str:
    # eliminar diacríticos
    text = re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED]", "", text)
    text = text.replace("ـ", "")  # tatweel
    
    # unificar grafías
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "و", text)
    text = re.sub("ئ", "ي", text)
    text = re.sub("ة", "ه", text)
    
    # mantener solo caracteres árabes + espacio
    text = re.sub(r"[^\u0600-\u06FF\s]", " ", text)
    
    # limpiar espacios múltiples
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

print(normalize_arabic("بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ"))

with open(arab_quran, "r", encoding="utf-8") as f:
    arabic_lines = f.readlines()
    arabic_lines = [normalize_arabic(line) for line in arabic_lines]
    with open("data/cleaned_arab_quran.txt", "w", encoding="utf-8") as out_f:
        out_f.writelines("\n".join(arabic_lines))