""" OpenAI module """

import os
import openai

def translate_text(text):
    """ Translate text """

    contents = [
        f"You are an expert English-to-{os.getenv('LANG_TO_TRANSLATE_STRING')} translator.\n",
        "The role of the translator is:\n",
        "- Always maintain the same structure provided.\n",
        "- If is presnet html tags, do not translate them.\n",
        "- Humanize the translated text.\n",
        "- Keep the tone of the original text.\n",
        "- Do not translate proper nouns.\n",
        "- If you can't translate or are unable to translate, write always |UNTRANSLATABLE|.\n",
        "- You are translating the texts of the Dyson Sphere Program video-game.\n",
        "- Do not translate the name of the video-game.\n",
        "- Do not translate the names of the technologies.\n",
        "- Do not translate the names of the planets.\n",
    ]

    string_content = "\n".join(contents)

    try:
        client = openai.OpenAI()
        user_content = f"Translate into {os.getenv('LANG_TO_TRANSLATE_STRING')}: {text}"
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": string_content},
                {"role": "user", "content": user_content}
            ],
        )

        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error translation: {e}")
        return text
