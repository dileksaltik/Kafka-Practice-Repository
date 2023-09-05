from confluent_kafka import Producer

def send_order_update(order_id, status):
    p = Producer({'bootstrap.servers': 'localhost:9092'})  # Replace with your Kafka server

    message = f'Order {order_id} status updated to {status}'
    p.produce('order-updates', key=order_id, value=message)
    p.flush()

# Example usage
send_order_update(12345, 'shipped')