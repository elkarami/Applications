# Installation de l'API googletrans
# pip install google_trans_new

import googletrans
print (googletrans.LANGUAGES)
from google_trans_new import google_translator

texte = "La Vie Se change, reste à jour"

trans = google_translator()

dt = trans.detect(texte)
print(dt) # Affiche: ['fr', 'french']

# traduction du texte du français à l'anglais
translated = trans.translate(texte, lang_src = 'fr', lang_tgt = 'en')

print(translated) # affiche: Life is changing, stay up to date 