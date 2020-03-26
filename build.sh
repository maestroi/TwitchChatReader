docker build -t twitchreader .
python3 create_compose.py
docker-compose build
docker-compose up -d