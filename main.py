import argparse

import source as sources
import translator as pytranslators


def main(source_name, args):

    source = sources.variants[source_name]
    source.set_args(args)

    sentences = source.get()

    for sentence in sentences:

        print(f'Sentence: {sentence}')

        for api in args.api:

            translator = pytranslators.get_by_api(api)

            print('-'*20)
            print(f'  {translator.get_name()}')
            print('  ' + '¯'*25)

            for lang in args.target:
                translation, seconds = translator.translate(sentence, dest=lang)
                print(f'  {lang.upper()} - {round(seconds, 2)}s:\n  {translation}\n')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='commands', description='choose a source of sentences')
    
    for source in sources.variants.values():
        source.setup_parser(subparsers, main)

    args = parser.parse_args()
    
    if not vars(args):
        parser.print_help()
    else:
        args.func(args)
