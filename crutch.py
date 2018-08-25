#!/usr/bin/env python3

import configparser
import os
import subprocess
import sys
import time

import main

# Реальный ip не определить из контейнера, можно добавить его через переменную окружения HOST_REAL_IP
# docker run -d -p 7999:7999 --device /dev/snd testme
# docker run -d -p 7999:7999 -e HOST_REAL_IP="192.168.1.198" --device /dev/snd testme

time.sleep(1)  # Пока rhvoice-rest.py запускается


def start():
    while main.main():
        pass
    sys.exit()


settings = os.path.join(os.path.join('/opt', 'cfg'), 'settings.ini')

if os.path.isfile(settings):
    start()

settings_ln = os.path.join(os.path.join('/opt', 'mdmterminal2'), 'settings.ini')

call = subprocess.run(['ip', 'route', 'show'], stdout=subprocess.PIPE)
host_ip = ''
for line in call.stdout.decode().split('\n'):
    if line.startswith('default'):
        host_ip = line.split(' ')[2]

rhvoice_here = os.path.isfile(os.path.join('/opt', 'rhvoice-rest.py'))
config = configparser.ConfigParser()
config['mpd'] = {'ip': host_ip}
config['log'] = {'file_lvl': 'info', 'print_lvl': 'crit', 'file': '/opt/cfg/mdmterminal.log'}
config['rhvoice'] = {'server': 'http://{}:8080'.format('127.0.0.1' if rhvoice_here else host_ip)}
config.add_section('Settings')
config['cache'] = {'tts_priority': 'rhvoice' if rhvoice_here else 'yandex'}
config.set('Settings', 'providertts', 'rhvoice' if rhvoice_here else 'google')
if 'HOST_REAL_IP' in os.environ:
    config.set('Settings', 'ip', os.environ['HOST_REAL_IP'])


with open(settings, 'w') as f:
    config.write(f)
os.symlink(settings, settings_ln)

start()

