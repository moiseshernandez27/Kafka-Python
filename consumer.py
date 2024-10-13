from confluent_kafka import Consumer, KafkaException, KafkaError

# Kafka consumer configuration
conf = {
    'bootstrap.servers': 'localhost:29092',  # Same broker configuration
    'group.id': 'my_group',  # Define your consumer group
    'auto.offset.reset': 'earliest',  # Start from the earliest message
}

# Create Consumer instance
consumer = Consumer(**conf)

# Subscribe to the topic
consumer.subscribe(['test_topic'])

# Poll for new messages
try:
    while True:
        msg = consumer.poll(1.0)  # Poll for messages with a 1-second timeout
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition
                continue
            else:
                raise KafkaException(msg.error())
        print(f"Received message: {msg.value().decode('utf-8')} from topic: {msg.topic()}")

except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    consumer.close()
