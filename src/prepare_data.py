arab_quran = "../data/raw_data/arab_quran.txt"
eng_quran = "../data/raw_data/english_quran.txt"

import re
'''
Con esto se consigue que palabras que son la misma,
pero escritas con variantes gráficas, se traten igual.
'''
from camel_tools.morphology.analyzer import DEFAULT_NORMALIZE_MAP as normalizer

'''
Elimina los diacríticos árabes (ḥarakāt), es decir,
las marcas cortas de vocalización y otros símbolos fonéticos.

Así evitamos que los diacríticos interfieran en el análisis
(la mayoría de modelos entrenados de CAMeL Tools usan texto sin diacríticos, y si usamos otros modelos esto puede ayudar).
'''
from camel_tools.utils.dediac import dediac_ar

print(normalizer.map_string("بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ"))

# Arabic Quran normalization
with open(arab_quran, "r", encoding="utf-8") as f:
    arabic_lines = f.readlines()
    arabic_lines = [dediac_ar(normalizer.map_string(line)) for line in arabic_lines]
    with open("../data/cleaned_data/cleaned_arab_quran.txt", "w", encoding="utf-8") as out_f:
        out_f.writelines("".join(arabic_lines))

# English Quran normalization
def normalize_english(text: str) -> str:
    text = text.lower()
    # elimninar lo que no son letras ni espacios (\s)
    text = re.sub(r"[^a-z\s]", " ", text)
    # limpiar espacios múltiples
    text = re.sub(r"\s+", " ", text).strip()
    return text

print(normalize_english("1|1|In the name of Allah, the Entirely Merciful, the Especially Merciful."))

with open(eng_quran, "r", encoding="utf-8") as f:
    english_lines = f.readlines()
    english_lines = [normalize_english(line) for line in english_lines]
    with open("../data/cleaned_data/cleaned_english_quran.txt", "w", encoding="utf-8") as out_f:
        out_f.writelines("\n".join(english_lines))