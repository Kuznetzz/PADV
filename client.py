import socket
from argparse import ArgumentParser
import yaml
from datetime import datetime
import json


parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str, required=False,
    help='Sets config file path')

args = parser.parse_args()
config = {
    'host': 'localhost',
    'port': 8000,
    'buffersize': 1024
}

if args.config:
    with open(args.config)as file:
        config.update(yaml.load(file, Loader=yaml.Loader))

host, port = config.get('host'), config.get('port')

try:
    sock = socket.socket()
    sock.connect((host, port))
    print('Client was started')

    action = input('Enter action:')
    data = input('Enter data:')

    request = {
        'action': action,
        'time': datetime.now().timestamp(),
        'data': data
    }

    str_request = json.dumps(request)

    sock.send(str_request.encode())
    print('Client send data')

    b_responce = sock.recv(config.get('buffersize'))
    print(f'Server send data {b_responce.decode()}')

except KeyboardInterrupt:
    print('Client shutdown')
