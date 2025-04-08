import json

from paho import mqtt

BROKER_ADDRESS = "localhost"  # Change if needed
TOPIC = "sensors/health"





def on_message(client, userdata, msg):
    """
    Callback function to handle incoming messages.
    It decodes the payload, converts it to a dictionary, and prints the data.
    """
    try:
        message_str = msg.payload.decode('utf-8')
        data = json.loads(message_str)
        print("\nReceived a message:")
        #Group5_util.print_data(data)
    except Exception as e:
        print("Error decoding message:", e)

def main():
    # Create MQTT client instance using keyword arguments to avoid parameter conflicts
    client = mqtt.Client(client_id="Subscriber", callback_api_version=1)
    client.on_message = on_message

    client.connect(BROKER_ADDRESS)
    client.subscribe(TOPIC)
    print("Subscriber connected and subscribed to topic:", TOPIC)

    # Enter the network loop
    client.loop_forever()

if __name__ == '__main__':
    main()