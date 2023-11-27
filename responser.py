import paho.mqtt.publish as publish

# Указать адрес и порт брокера Mosquitto
broker_address = "your_address.com"
port = 1883

# Указать тему и сообщение
response_topic = "your_topic"
response_message = '{"example":"0;255;0"}'

# Указать имя пользователя и пароль, если требуется
username = "your_key"
password = ""

# Опубликовать сообщение
publish.single(response_topic, response_message, hostname=broker_address, port=port, auth={'username': username, 'password': password})
