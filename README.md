# TwitchChatReader
Read twitch chats

This application is a a ingester for twitch chat of a channel.

This application use websocket to watch a channel on the twitch server and use docker-compose with gelf driver to send stout to graylog.

Requirements.
1. Python 3
2. Docker
3. Docker-compose

How to:
1. copy settings.ini.example to settings.ini.
2. Set username to your twitch username.
3. Set OATH token for your username, can be generated here: https://twitchapps.com/tmi/.
4. Set name of the list to use, it will loop the file to generate a compose file.
5. Set graylog as the the url where to deliver stout
6. run bash build.sh
   1. this will build chatlogger to a docker image
   2. creates a compose file
   3. and run composefile