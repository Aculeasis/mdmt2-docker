mdmT 2 docker
====
Готовые образы и докерфайлы для [mdmTerminal 2](https://github.com/Aculeasis/mdmTerminal2)

mdmTerminal 2 - форк [mdmPiTerminal](https://github.com/devoff/mdmPiTerminal), голосового терминала для MajorDoMo. Он полностью совместим с [MDM VoiceAssistant](https://github.com/lanket/mdmPiTerminalModule)

### Переменные среды
Новый контейнер можно запустить со следующими переменными (через -e):
- **HOST_REAL_IP**. Сообщает контейнеру локальный ip хоста, сам он его узнать не может. Этот ip будет проговаривать терминал до настройки, больше он ни на что не влияет. Если не задать будет что-то вроде 172.17.0.2
- **ASOUND**. Использует преднастроенный asound.conf, доступно только `-e ASOUND="h3"`. Может помочь если rhvoice-rest заикается.
- **RHVOICE**. Задает полный адрес сервера rhvoice-rest и включает его как TTS. Можно установить и для образов с rhvoice-rest, но не нужно.

Пример, все сразу: `docker run -d -p 7999:7999 --device /dev/snd -e HOST_REAL_IP="192.168.2.102" -e ASOUND="h3" -e RHVOICE="http://192.168.2.101:8080" aculeasis/mdmt2:arm64v8`

### VOLUME
При запуске хосту будет доступен /opt/cfg контейнера со следующими файлами:
- settings.ini - Настройки mdmTerminal 2. Создается вместе с контейнером
- RHVoice.conf - Настройки RHVoice, для образов с rhvoice-rest
- asound.conf - Настройки ALSA
- mdmterminal.log - Логи терминала

См. `docker volume`

Образы mdmTerminal 2
====
Для aarch64:

`docker run -d -p 7999:7999 --device /dev/snd aculeasis/mdmt2:arm64v8`

Для x86_64

`docker run -d -p 7999:7999 --device /dev/snd aculeasis/mdmt2:amd64`


Образы mdmTerminal 2 + rhvoice-rest
====
Для aarch64:

`docker run -d -p 7999:7999 --device /dev/snd aculeasis/mdmt2_rhvoice:arm64v8`

Для x86_64

`docker run -d -p 7999:7999 --device /dev/snd aculeasis/mdmt2_rhvoice:amd64`

Примечания
====
- В образах нет mpd, его нужно установить на хосте `sudo apt install mpd`
- Образы для armv7l отсутствуют, их можно собрать самостоятельно из *.arm32v7 файлов.
- Для работы с аудио контейнеру пробрасывается /dev/snd. Вероятно вы не сможете запустить несколько контейнеров\терминалов - snowboy постоянно использует микрофон
- rhvoice-rest тут не доступен за пределами контейнера. Конечно, лучше использовать для него отдельный образ: mdmTerminal 2 + [rhvoice-rest](https://github.com/Aculeasis/rhvoice-rest)
- mdmTerminal 2 имеет больше настроек чем оригинальный mdmPiTerminal, не все из них доступны через MDM VoiceAssistant - редактируйте settings.ini
- TTS кэш хранится внутри контейнера (/opt/mdmterminal2/tts_cache).

Ссылки
====
- mdmTerminal 2 - https://github.com/Aculeasis/mdmTerminal2
- rhvoice-rest - https://github.com/Aculeasis/rhvoice-rest
- MDM VoiceAssistant - https://github.com/lanket/mdmPiTerminalModule
- MajorDoMo - https://github.com/sergejey/majordomo

