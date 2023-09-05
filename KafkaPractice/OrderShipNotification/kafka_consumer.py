from confluent_kafka import Consumer, KafkaError

def process_order_update(message):
    print(f'Received order update: {message.value()}')

def listen_to_order_updates():
    c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'my-group', 'auto.offset.reset': 'earliest'})
    c.subscribe(['order-updates'])

    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
        else:
            process_order_update(msg)
            
# Example usage
listen_to_order_updates()