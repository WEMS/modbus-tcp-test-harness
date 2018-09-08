from pymodbus.client.sync import ModbusTcpClient
import time


def process_values_file(file_handle, args):
    client = ModbusTcpClient(host=args.host, port=args.port)

    for line in file_handle:
        value = line.strip()
        print('Writing value: {}'.format(value))
        client.write_register(args.register, value)
        time.sleep(args.interval)
