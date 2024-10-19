# ⚡ Kafka Cluster with Docker Compose

This project sets up an **Apache Kafka** cluster using Docker and Docker Compose. The cluster consists of multiple **controllers** and **brokers** to demonstrate the use of Kafka in a production-like environment with fault tolerance and scalability. It also includes examples of how to connect to Kafka from a Python application to send messages to a client.

## 📂 Project Structure

- **Controllers**: 🛠️ Handle Kafka metadata and leader election (**KRaft mode**).
- **Brokers**: 🗄️ Store data (messages) and handle client requests for message production and consumption.

## ✨ Features

- 🖥️ **Multiple Controllers**: 3 Kafka controllers (`controller-1`, `controller-2`, `controller-3`) for high availability.
- 📊 **Multiple Brokers**: 3 Kafka brokers (`broker-1`, `broker-2`, `broker-3`) to distribute and store messages.
- 🐳 **Dockerized Setup**: Easily start the entire cluster using Docker Compose.
- 🐍 **Python Kafka Producer Example**: Simple Python script to send messages to Kafka.

## 📋 Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/get-started) 🐳
- [Docker Compose](https://docs.docker.com/compose/install/) 🐙
- [Python 3.6+](https://www.python.org/downloads/) 🐍

## 🚀 Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/moiseshernandez27/Kafka-Python.git
cd kafka-docker-cluster
docker-compose up -d
```
This will spin up the following services:

3 Kafka Controllers (Ports: 9093)
3 Kafka Brokers:
Broker 1 (External Port: 29092)
Broker 2 (External Port: 39092)
Broker 3 (External Port: 49092)

###  Step 3: Check Status
You can check the status of the containers using:

```bash
docker ps

```

### Step 4:Produce Messages to Kafka with Python
First, install the Python Kafka client and then run the script:

```bash
pip install kafka-python
python kafka_producer.py
```
This will send a message to the Kafka topic my-topic.

## ⚙️ Configuration Details

Controllers: 🛠️ The controllers manage metadata and leader elections for Kafka. They communicate on port 9093.
Brokers: 🗄️ Kafka brokers handle messages and client requests. Each broker is exposed on a separate port:
Broker 1: External port 29092
Broker 2: External port 39092
Broker 3: External port 49092

## 📁 Files

docker-compose.yml: Defines the services (Kafka controllers and brokers) for the cluster.
kafka_producer.py: Python script for sending messages to Kafka.
