#!/usr/bin/python3

import base64
import json
from pathlib import Path

path = Path(__file__).parent

config_file = open(str(path.joinpath('v2ray/config/config.json')), 'r', encoding='utf-8')
config = json.load(config_file)

caddy = open(str(path.joinpath('caddy/Caddyfile')), 'r', encoding='utf-8').read()

uuid = config['inbounds'][0]['settings']['clients'][0]['id']
domain = caddy[:caddy.find(' {')]

j = json.dumps({
    "v": "2", "ps": domain, "add": domain, "port": "443", "id": uuid, "aid": "0", "net": "ws", "type": "none",
    "host": domain, "path": "/ws", "tls": "tls"
})

print("vmess://" + base64.b64encode(j.encode('ascii')).decode('ascii'))
