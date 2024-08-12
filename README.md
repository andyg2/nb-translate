# Batch Translator

A Python script to translate a list of words from English to multiple languages of your choice.

## Description

This script reads words from a text file named 'words_source.txt', translates each word to multiple specified languages, and saves the results into separate CSV files for each target language.

## Requirements

The script uses the `deep_translator` library for translation. You can install it using pip:

```bash
pip install deep_translator
```

## Usage

1. Create a file named 'words_source.txt' in the same directory as the script. Each line should contain one word to be translated.

2. Open the script and modify the `translated_languages` list to specify your desired target languages:

   ```python
   translated_languages = ['ceb', 'fil']  # Add or remove languages as needed
   ```

   You can find language codes here: [Google Translate Languages](https://cloud.google.com/translate/docs/languages)

3. Run the script:

   ```python
   python nb-translate.py
   ```

4. The script will process all given words and create separate CSV files for each target language with the naming convention `words_translated-{source_language}-{target_language}.csv`. Each CSV file will have two columns:
   - source
   - translation

5. You can open the generated CSV files with any spreadsheet application like Microsoft Excel or Google Sheets.

## Customization

By default, the script translates from English. If you want to change the source language, modify the following line in the script:

```python
source_language = 'en'
```

Replace 'en' with your desired source language code.

## Notes

- The translations may not be perfect, especially for compound words or technical terms. Words such as "ExpenseByMonth" may not be translated and will need manual translation.
- For manual translation or verification, you can use [Google Translate](https://translate.google.com/).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
