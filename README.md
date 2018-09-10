mdmT 2 docker
====
[![Docker Pulls](https://img.shields.io/docker/pulls/aculeasis/mdmt2.svg?label=mdmt2)](https://hub.docker.com/r/aculeasis/mdmt2/) [![Docker Pulls](https://img.shields.io/docker/pulls/aculeasis/mdmt2_rhvoice.svg?label=mdmt2_rhvoice)](https://hub.docker.com/r/aculeasis/mdmt2_rhvoice/)

Готовые образы и докерфайлы для [mdmTerminal 2](https://github.com/Aculeasis/mdmTerminal2)

mdmTerminal 2 - форк [mdmPiTerminal](https://github.com/devoff/mdmPiTerminal), голосового терминала для MajorDoMo. Он полностью совместим с [MDM VoiceAssistant](https://github.com/lanket/mdmPiTerminalModule)

Быстрый старт
====
Запуск\обновление из хаба:

-  mdmTerminal 2: `./mdmt2.py --upgrade`
-  mdmTerminal 2 + rhvoice-rest: `./mdmt2_rhvoice.py --upgrade`

Полное описание [тут](https://github.com/Aculeasis/docker-starter)

### Переменные окружения
Новый контейнер можно запустить со следующими переменными (через -e):
- **HOST_REAL_IP**. Сообщает контейнеру локальный ip хоста, сам он его узнать не может. Этот ip будет проговаривать терминал до настройки, больше он ни на что не влияет. Если не задать будет что-то вроде 172.17.0.2
- **ASOUND**. Использует преднастроенный asound.conf, доступно только `-e ASOUND="h3"`. Может помочь если rhvoice-rest заикается.
- **RHVOICE**. Задает полный адрес сервера rhvoice-rest и включает его как TTS. Можно установить и для образов с rhvoice-rest, но не нужно.
- **HOST_INTERNAL_IP**. Сообщает контейнеру адрес хоста в сети докера. В линуксе сам определит, а вот в винде можно указать `host.docker.internal`, если версия докера 18.03 и выше.

Пример, все сразу: `docker run -d -p 7999:7999 --device /dev/snd -e HOST_REAL_IP="192.168.2.102" -e ASOUND="h3" -e RHVOICE="http://192.168.2.101:8080" aculeasis/mdmt2:arm64v8`

### Автозапуск
Включить автозапуск демона `systemctl enable docker.service`

По умолчанию контейнеры не запускаются автоматически, например после ребута. Самый простой вариант добавить к `docker run` `--restart unless-stopped` или обновить существующий контейнер `docker update --restart unless-stopped <container name>`.

Образы mdmTerminal 2
====
- aarch64 `docker run -d -p 7999:7999 --device /dev/snd aculeasis/mdmt2:arm64v8`
- armv7l `docker run -d -p 7999:7999 --device /dev/snd aculeasis/mdmt2:arm32v7`
- x86_64 `docker run -d -p 7999:7999 --device /dev/snd aculeasis/mdmt2:amd64`

Образы mdmTerminal 2 + rhvoice-rest
====
- aarch64 `docker run -d -p 7999:7999 --device /dev/snd aculeasis/mdmt2_rhvoice:arm64v8`
- armv7l `docker run -d -p 7999:7999 --device /dev/snd aculeasis/mdmt2_rhvoice:arm32v7`
- x86_64 `docker run -d -p 7999:7999 --device /dev/snd aculeasis/mdmt2_rhvoice:amd64`

Примечания
====
- В образах нет mpd, его нужно установить на хосте `sudo apt install mpd`
- Для работы с аудио контейнеру пробрасывается /dev/snd. Вероятно вы не сможете запустить несколько контейнеров\терминалов - snowboy постоянно использует микрофон
- rhvoice-rest тут не доступен за пределами контейнера. Конечно, лучше использовать для него отдельный образ: mdmTerminal 2 + [rhvoice-rest](https://github.com/Aculeasis/rhvoice-rest)
- mdmTerminal 2 имеет больше настроек чем оригинальный mdmPiTerminal, не все из них доступны через MDM VoiceAssistant - редактируйте settings.ini
- Чтобы не терять данные при обновленях, нужно вынести на хост (через -v): `/opt/mdmterminal2/tts_cache`, `/opt/mdmterminal2/resources/models` и `/opt/cfg`

Ссылки
====
- mdmTerminal 2 - https://github.com/Aculeasis/mdmTerminal2
- rhvoice-rest - https://github.com/Aculeasis/rhvoice-rest
- MDM VoiceAssistant - https://github.com/lanket/mdmPiTerminalModule
- MajorDoMo - https://github.com/sergejey/majordomo

