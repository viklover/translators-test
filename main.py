import sys

import source as sources
import translator as translators

# LANGUAGES TARGET (AFTER ENGLISH)
languages = ['ru']

def main(args):
    
    for source in sources.variants:
        data = source.get(*args)

        for sentence in data:

            print(f'Sentence: {sentence}')

            for translator in translators.variants:

                print('-'*20)
                print(f'  {translator.get_name()}')
                print('  ' + '¯'*25)

                translation_en, seconds = translator.translate(sentence, dest='en')
                print(f'  EN - {round(seconds, 2)}s:\n  {translation_en}\n')

                for lang in languages:
                    translation, seconds = translator.translate(translation_en, source='en', dest=lang)
                    print(f'  {lang.upper()} - {round(seconds, 2)}s:\n  {translation}\n')

            print()


if __name__ == "__main__":
    main(sys.argv[1:])
