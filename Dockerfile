FROM python:3.8-alpine
# Change workdir
WORKDIR . /chatlogger
# Copy files
COPY . .
# Run Chatlogger.
CMD [ "python", "./chatlogger/chat_logger.py" ]
