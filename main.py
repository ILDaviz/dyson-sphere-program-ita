""" Script translate texts """

import time
import openai
from dotenv import load_dotenv

def translate_text(text):
    """ Translate text """
    try:
        client = openai.OpenAI()
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Sei un traduttore esperto da inglese a italiano."},
                {"role": "system", "content": "Mantieni sempre la stessa struttura fornita."},
                {"role": "system", "content": "Umanizza il testo tradotto."},
                {"role": "user", "content": f"Traduci in italiano: {text}"}
            ],
        )

        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error translation: {e}")
        return text

def get_file_content():
    """ Get file content """

    files = [
        '1055/[outsource].txt',
        '1055/[user].txt',
        '1055/combat.txt',
        '1055/creation.txt',
        '1055/dictionary.txt',
        '1055/prototype.txt',
        #'1055/base.txt'
    ]

    for file in files:
        input_file = 'original/' + file
        output_file = 'translated/' + file
        enconding = 'utf-16 le'

        index = 0

        with open(input_file, "r", encoding=enconding) as file:
            total_lines = sum(1 for _ in file)

        open_file = open(input_file, "r", encoding=enconding)
        output_file = open(output_file, "w", encoding=enconding)

        with open_file as infile, output_file as outfile:
            for line in infile:
                parts = line.split("\t")
                if len(parts) >= 4:
                    english_text = parts[3].strip()
                    if english_text:
                        translated_text = translate_text(english_text)
                        time.sleep(1)
                        translated_text = translated_text.replace('\n', ' ')
                        parts[3] = translated_text
                        outfile.write("\t".join(parts) + "\n")
                    else:
                        outfile.write(line)
                else:
                    outfile.write(line)

                index = index + 1
                print(f"Translate {index}/{total_lines} string of file {input_file}!")

        print(f"File {input_file} is translated!")
    print('Translation completed!')

def main():
    """ Main function """
    load_dotenv()
    get_file_content()

if __name__ == "__main__":
    main()
