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
git clone https://github.com/yourusername/kafka-docker-cluster.git
cd kafka-docker-cluster
