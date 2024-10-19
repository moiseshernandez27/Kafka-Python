from confluent_kafka import Producer # type: ignore
#from faker import Faker
#fake = Faker()
##Te next step is to consume data from faker using a web interface
# Kafka producer configuration
conf = {
    'bootstrap.servers': 'localhost:29092',  # Ensure this matches your broker's advertised listener
}

# Create Producer instance
producer = Producer(**conf)

# Delivery report callback
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Produce a message
topic = 'test_topic'
producer.produce(topic, key='key1', value='Message 1', callback=delivery_report)
producer.produce(topic, key='key2', value='Message 2', callback=delivery_report)

# Wait for all messages to be delivered and then clear the object 
producer.flush()