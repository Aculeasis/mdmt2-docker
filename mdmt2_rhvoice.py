#!/usr/bin/env python3

import os

import docker_starter as ds

NAME = 'mdmt2_rhvoice'
LAN_IP = ds.get_ip_address()
AARCH = ds.get_arch()

CFG = {
    'name': NAME,
    'image': 'aculeasis/mdmt2_rhvoice:{}'.format(AARCH),
    'docker_path': ds.WORK_DIR,
    'dockerfile': os.path.join(ds.WORK_DIR, 'Dockerfile_rhvoice.{}'.format(AARCH)),
    'data_path': os.path.join(ds.DATA_PATH, NAME),
    'restart': 'always',
    'p': {7999: 7999},
    'v': {
        'tts_cache': '/opt/mdmterminal2/tts_cache',
        'models': '/opt/mdmterminal2/resources/models',
        'cfg': '/opt/cfg'
    },
    'e': {'HOST_REAL_IP': LAN_IP},
}
if ds.OS == 'linux':
    CFG['any'] = [['--device', ' ', '/dev/snd'], ]

ds.DockerStarter(CFG)
