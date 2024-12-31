""" OpenAI module """

import os
import openai

def translate_text(text):
    """ Translate text """
    try:
        client = openai.OpenAI()
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Sei un traduttore esperto da inglese a {os.getenv('LANG_TO_TRANSLATE_STRING')}."},
                {"role": "system", "content": "Mantieni sempre la stessa struttura fornita."},
                {"role": "system", "content": "Umanizza il testo tradotto."},
                {"role": "system", "content": "Mantieni il tono del testo originale."},
                {"role": "system", "content": "Non tradurre i nomi propri."},
                {"role": "user", "content": f"Traduci in {os.getenv('LANG_TO_TRANSLATE_STRING')}: {text}"}
            ],
        )

        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error translation: {e}")
        return text