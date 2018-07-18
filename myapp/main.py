import argparse
from .command1 import Command1
from .command2 import Command2


def main():
    parser = argparse.ArgumentParser(description='myapp')
    subparsers = parser.add_subparsers(help='sub-command help')

    sub_parser = subparsers.add_parser('command1', help='help for command1')
    sub_parser.set_defaults(func=command1)
    sub_parser.add_argument('--option1', required=False, help='help for option1')

    sub_parser = subparsers.add_parser('command2', help='help for command2')
    sub_parser.set_defaults(func=command2)
    sub_parser.add_argument('--option1', required=False, help='help for option1')
    sub_parser.add_argument('--option2', required=False, help='help for option2')

    parse_args = parser.parse_args()

    if hasattr(parse_args, 'func'):
        parse_args.func(parse_args)
    else:
        parser.print_help()


def command1(args):
    command = Command1(args)
    command.exec()


def command2(args):
    command = Command2(args)
    command.exec()
