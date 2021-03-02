# Udacity Data Streaming Nanodegree. Data Ingestion with Kafka

This repository contains learning materials & notes for
first chapter of [Udacity Data Streaming Nanodegree](https://www.udacity.com/course/data-streaming-nanodegree--nd029).

## Notes

### Docker & docker-compose
* Stop & rm containers
    ```bash
    docker-compose stop && docker-compose rm -fsv
    ```
### Using the CLI Kafka tools
* List Kafka topics
    ```bash
    kafka-topics.sh --list --zookeeper localhost:2181
    ```
* Create kafka topic
    ```bash
    kafka-topics.sh --create --topic "my-first-topic" --partitions 1 --replication-factor 1 --zookeeper localhost:2181
    ```
* Run producer 
    ```bash
    kafka-console-producer.sh --topic "my-first-topic" --broker-list localhost:9092
    ```
* Run consumer
    ```bash
    kafka-console-consumer.sh --topic "my-first-topic" --bootstrap-server localhost:9092 --from-beginning
    ```  