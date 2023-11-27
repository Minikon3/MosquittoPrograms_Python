import paho.mqtt.publish as publish

# Указать адрес и порт брокера Mosquitto
broker_address = "your_address.com"
port = 1883

# Указать тему и сообщение
topic = "your_topic"
message = '{"example": 100}'

# Указать имя пользователя и пароль, если требуется
username = "your_key"
password = ""

# Опубликовать сообщение
publish.single(topic, message, hostname=broker_address, port=port, auth={'username': username, 'password': password})
