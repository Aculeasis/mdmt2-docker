#!/bin/bash

echo 'Setting trap PID $$'
trap cleanup INT TERM

cleanup() {
    echo 'stopping...'
    MAIN="$(pgrep 'python' -a | grep 'main.py' | awk '{print $1}')"
    kill -TERM "$MAIN"
    wait "$MAIN"
    pgrep 'python' | xargs -r kill -TERM
    wait
    echo 'stop'
    exit 0
}

if [ -f /usr/local/etc/RHVoice/RHVoice.conf ] && [ ! -L /usr/local/etc/RHVoice/RHVoice.conf ]; then
    if [ ! -f /opt/cfg/RHVoice.conf ]; then
        mv /usr/local/etc/RHVoice/RHVoice.conf /opt/cfg/RHVoice.conf
    fi
    ln -fs /opt/cfg/RHVoice.conf /usr/local/etc/RHVoice/RHVoice.conf
fi

if [ ! -L /etc/asound.conf ]; then
    touch /opt/cfg/asound.conf
    ln -fs /opt/cfg/asound.conf /etc/asound.conf
fi

if [ ! -L /opt/mdmterminal2/settings.ini ]; then
    touch /opt/cfg/settings.ini
    ln -fs /opt/cfg/settings.ini /opt/mdmterminal2/settings.ini
fi

if [ ! -f /opt/cfg/configured ]; then
    if [ -f /opt/asound.conf.h3 ]; then
        mv /opt/asound.conf.h3 /opt/cfg/asound.conf.h3
    fi

    if [ -f /opt/mdmterminal2/crutch.py ]; then
        python3 -u /opt/mdmterminal2/crutch.py
    fi

    touch /opt/cfg/configured
fi

if [ -f /opt/rhvoice-rest.py ]; then
    python3 /opt/rhvoice-rest.py & sleep 1
fi

if [ -f /opt/mdmterminal2/main.py ]; then
    python3 -u /opt/mdmterminal2/main.py &
fi

wait