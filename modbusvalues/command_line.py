import argparse
from modbusvalues.writer import process_values_file


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def main():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument(
        '--source', '-s',
        help='Source path of values to read in'
    )

    arg_parser.add_argument(
        '--register', '-r',
        help='Register to write values to',
    )

    arg_parser.add_argument(
        '--interval', '-i',
        default=1,
        help='Interval in seconds to wait between writing values'
    )

    arg_parser.add_argument(
        '--host',
        default='127.0.0.1',
        help='Host IP address of the Modbus device'
    )

    arg_parser.add_argument(
        '--port',
        default=502,
        help='Port of the host Modbus device'
    )

    arg_parser.add_argument(
        '--verbose', '-v',
        type=str2bool,
        nargs='?',
        const=True,
        default=False
    )

    args = arg_parser.parse_args()

    try:
        with open(args.source, 'r') as fh:
            process_values_file(fh, args)

    except IOError as exc:
        print('Error:', exc.strerror)
        exit(1)


if __name__ == '__main__':
    main()
