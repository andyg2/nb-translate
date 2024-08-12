from deep_translator import GoogleTranslator
import csv 
import os.path
import sys 

source_language = 'en'
translated_languages = ['ceb', 'fil']  # Add or remove languages as needed
header = ['source', 'translation']
input_file = 'words_source.txt'

if not os.path.exists(input_file):
    sys.exit('Input file not found!')

print("Processing words...")
count = sum(1 for line in open('words_source.txt'))

for target_language in translated_languages:
    output_file = f'words_translated-{source_language}-{target_language}.csv'
    
    print(f"\nTranslating to {target_language}...")
    with open(output_file, 'w', encoding='utf-8', newline='') as w:
        writer = csv.writer(w, delimiter=',')
        writer.writerow(header)
        w.flush()
        
        with open('words_source.txt') as f:
            for c, line in enumerate(f, 1):
                word = line.strip()
                print(f"{c}/{count}", end='\r')
                
                translate = GoogleTranslator(source=source_language, target=target_language).translate(word)
                data = [word, translate]
                writer.writerow(data)
                w.flush()
    
    print(f"\nTranslation to {target_language} complete. Results saved in {output_file}")

print("\nAll translations complete.")
