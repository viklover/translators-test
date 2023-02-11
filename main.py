import sys

import sources
import translators

# LANGUAGES TARGET
languages = ['en', 'ru']

def main(args):
    
    for source in sources.variants:
        data = source.get(*args)

        for sentence in data:

            print(f'Sentence: {sentence}')

            for translator in translators.variants:

                print('-'*20)
                print(f'  {translator.get_name()}')
                print('  ' + '¯'*20)

                for lang in languages:
                    translation, seconds = translator.translate(sentence, dest=lang)
                    print(f'  {lang.upper()} - {round(seconds, 2)}s:\n  {translation}\n')
             
            print()


if __name__ == "__main__":
    main(sys.argv[1:])
