
from .base import Source

from argparse import ArgumentParser, _SubParsersAction

class Input(Source):

    def __init__(self) -> None:
        super().__init__('Input')

        self.sentence = None

    def setup_parser(self, subparsers: _SubParsersAction, func):

        parser: ArgumentParser = subparsers.add_parser('translate', help='translate your sentence')
        parser.add_argument('sentence', type=str)
        parser.set_defaults(func=lambda args: func('translate', args))

        return super().setup_parser(parser)

    def set_args(self, args):
        self.sentence = args.sentence

    def get(self):
        return [self.sentence]
