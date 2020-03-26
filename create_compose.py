import os
import configparser

Config = configparser.ConfigParser()
Config.read("settings.ini")

nickname = Config.get('General', 'nickname')
token = Config.get('General', 'token')
userlist = Config.get('General', 'userlist')
graylog = Config.get('General', 'graylog')


def main():
    with open('docker-compose.yaml', 'w+') as fi:
        fi.write("""version: '3'
  services:""")
        with open(userlist) as f:
            for line in f:
                channel = line.strip()
                fi.write("""  
    %s:
      image: twitchreader:latest
      environment:
        USERNAME: %s
        OATH_KEY: %s
        CHANNEL_NAME: %s
      logging:
        driver: "gelf"
        options:
          gelf-address: "%s"
          tag: "%s" \n""" % (channel, nickname, token, channel, graylog, channel))


if __name__ == '__main__':
    main()
