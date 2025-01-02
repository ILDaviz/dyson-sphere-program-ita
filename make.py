""" Script translate texts """

import os
import time
from dotenv import load_dotenv
from src.files_map import get_files
from src.openai import translate_text

def get_file_content():
    """ Get file content """

    files = get_files()

    if not os.path.exists('translated/' + os.getenv('LANG_TO_TRANSLATE')):
        os.makedirs('translated/' + os.getenv('LANG_TO_TRANSLATE'))

    for file in files:
        input_file = 'original/' + file
        output_file = 'translated/' + os.getenv('LANG_TO_TRANSLATE') + '/' + file
        encoding = 'utf-16 le'

        if not os.path.exists(input_file):
            print(f"Updated file {input_file} does not exist, skipping.")
            continue

        index = 0

        with open(input_file, "r", encoding=encoding) as file:
            total_lines = sum(1 for _ in file)

        open_file = open(input_file, "r", encoding=encoding)
        output_file = open(output_file, "w", encoding=encoding)

        with open_file as infile, output_file as outfile:
            for line in infile:
                parts = line.split("\t")
                if len(parts) >= 4:
                    text_to_translate = parts[3].strip()
                    if text_to_translate:
                        translated_text = translate_text(text_to_translate)
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
