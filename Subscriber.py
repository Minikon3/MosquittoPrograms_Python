import paho.mqtt.client as mqtt

# Замените на ваши учетные данные и хост ThingsBoard
THINGSBOARD_HOST = "your_address.com"
THINGSBOARD_PORT = 1883
ACCESS_TOKEN = "your_key"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Подписываемся на топики RPC-запросов
    client.subscribe("v1/devices/me/rpc/request/+") #пример подписки на топик

def on_message(client, userdata, msg):
    print("Received message on topic: " + msg.topic)
    print("Message payload: " + msg.payload.decode())

# Создаем MQTT-клиента
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)

# Назначаем обработчики событий
client.on_connect = on_connect
client.on_message = on_message

# Подключаемся к ThingsBoard
client.connect(THINGSBOARD_HOST, THINGSBOARD_PORT, 60)

# Запускаем бесконечный цикл для прослушивания сообщений
client.loop_forever()
