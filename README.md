[mdmT 2 docker](https://github.com/Aculeasis/mdmt2-docker)
===

[![Docker Pulls](https://img.shields.io/docker/pulls/aculeasis/mdmt2.svg?label=mdmt2)](https://hub.docker.com/r/aculeasis/mdmt2/)

Готовые docker-образы и докерфайлы для [mdmTerminal 2](https://github.com/Aculeasis/mdmTerminal2)

```bash
docker run -d \
  --name=mdmt2 \
  --device /dev/snd \
  -p 7999:7999 \
  -v /path/to/tts_cache:/opt/mdmterminal2/tts_cache `#optional` \
  -v /path/to/models:/opt/mdmterminal2/resources/models `#optional` \
  -v /path/to/cfg:/opt/cfg `#optional` \
  --restart unless-stopped \
  aculeasis/mdmt2:latest
```
Поддерживаемые архитектуры:
| Architecture | Available | Tag |
| :----: | :----: | ---- |
| x86-64 | ✅ | amd64 |
| arm64 | ✅ | arm64v8 |
| armhf | ✅ | arm32v7 |

Для автоматического обновления можно использовать [Watchtower](https://github.com/containrrr/watchtower).

### Переменные окружения
Новый контейнер можно запустить со следующими переменными (через -e):
- **HOST_REAL_IP**. Сообщает контейнеру локальный ip хоста, сам он его узнать не может. Этот ip будет проговаривать терминал до настройки, больше он ни на что не влияет. Если не задать будет что-то вроде `172.17.0.2`.
- **ASOUND**. Использует преднастроенный asound.conf, доступно только `-e ASOUND="h3"`. Может помочь если rhvoice-rest заикается.
- **RHVOICE**. Задает полный адрес сервера rhvoice-rest и включает его как TTS.
- **HOST_INTERNAL_IP**. Сообщает контейнеру адрес хоста в сети докера. В линуксе должен определить сам, в винде можно указать `host.docker.internal`, если версия докера 18.03 и выше.

Ссылки
====
- [mdmTerminal2](https://github.com/Aculeasis/mdmTerminal2)
- [rhvoice-rest](https://github.com/Aculeasis/rhvoice-rest)
- [MDM VoiceAssistant](https://github.com/lanket/mdmPiTerminalModule)
- [MajorDoMo](https://github.com/sergejey/majordomo)

