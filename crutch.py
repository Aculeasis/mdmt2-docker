#!/usr/bin/env python3

import configparser
import os
import subprocess
from shutil import copyfile

"""
Реальный ip не определить из контейнера, можно добавить его через переменную окружения HOST_REAL_IP
docker run -d -p 7999:7999 --device /dev/snd testme
docker run -d -p 7999:7999 --device /dev/snd -e HOST_REAL_IP="192.168.1.198" -e ASOUND="h3" \
aculeasis/mdmt2_rhvoice:arm64v8
"""


def sound_fix(name):
    path = os.path.join('/opt', 'cfg')
    dst = os.path.join(path, 'asound.conf')
    src = os.path.join(path, '{}.{}'.format(dst, name.lower()))
    if os.path.isfile(src):
        copyfile(src, dst)


def get_host_ip():
    if 'HOST_INTERNAL_IP' in os.environ:
        return os.environ['HOST_INTERNAL_IP']
    # docker>=18.03 https://docs.docker.com/docker-for-windows/networking/#use-cases-and-workarounds
    # ip = 'host.docker.internal'
    ip = '172.17.0.1'
    call = subprocess.run(['ip', 'route', 'show'], stdout=subprocess.PIPE)
    for line in call.stdout.decode().split('\n'):
        if line.startswith('default'):
            ip = line.split(' ')[2]
    return ip


host_ip = get_host_ip()
settings = os.path.join(os.path.join('/opt', 'cfg'), 'settings.ini')
rhvoice_here = os.path.isfile(os.path.join('/opt', 'rhvoice-rest.py')) or 'RHVOICE' in os.environ
rhvoice = os.environ.get('RHVOICE', 'http://127.0.0.1:8080') if rhvoice_here else 'http://{}:8080'.format(host_ip)
config = configparser.ConfigParser()
config['mpd'] = {'ip': host_ip}
config['log'] = {'file_lvl': 'info', 'print_lvl': 'crit', 'file': '/opt/cfg/mdmterminal.log'}
config['rhvoice-rest'] = {'server': rhvoice}
config.add_section('Settings')
config['cache'] = {
    'tts_priority': 'rhvoice-rest' if rhvoice_here else 'yandex',
    'tts_size': 0 if rhvoice_here else 100
}
config.set('Settings', 'providertts', 'rhvoice-rest' if rhvoice_here else 'google')
if 'HOST_REAL_IP' in os.environ:
    config.set('Settings', 'ip', os.environ['HOST_REAL_IP'])

with open(settings, 'w') as f:
    config.write(f)

if 'ASOUND' in os.environ:
    sound_fix(os.environ['ASOUND'])

