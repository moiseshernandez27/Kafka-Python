from confluent_kafka import Consumer, KafkaException, KafkaError  # type: ignore
from fastapi import FastAPI  # type: ignore

app = FastAPI()

# Kafka consumer configuration
conf = {
    'bootstrap.servers': 'localhost:29092',  # Same broker configuration
    'group.id': 'my_group',  # Define your consumer group
    'auto.offset.reset': 'earliest',  # Start from the earliest message
}

@app.get("/consume")
async def consume_all_kafka():
    # Create a new Consumer instance for each request
    consumer = Consumer(conf)
    topic = 'test_topic'
    consumer.subscribe([topic])
    
    messages = []
    try:
        for _ in range(10):  # Limit to 10 messages (adjust as needed)
            msg = consumer.poll(1.0)  # Poll messages with a timeout of 1 second
            if msg is None:
                break  
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(msg.error())
            # Append the message to the list
            messages.append({
                'key': msg.key().decode('utf-8') if msg.key() else None,
                'value': msg.value().decode('utf-8') if msg.value() else None,
                'topic': msg.topic(),
                'partition': msg.partition(),
                'offset': msg.offset()
            })
    except KafkaException as e:
        print(f"Kafka error: {e}")
    finally:
        consumer.close() 

    return {"messages": messages}

@app.get("/test")
async def show_test_message():
    return {"message": "this is a test"}
