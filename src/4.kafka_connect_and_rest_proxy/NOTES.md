### Kafka-connect & Kafka REST Proxy

* View connector-plugins
    ```bash
    curl http://localhost:8083/connector-plugins | python -m json.tool
    ```
* Create connector 
    ```bash
    curl -X POST -H 'Content-Type: application/json' -d '{
    "name": "first-connector",
    "config": {
        "connector.class": "FileStreamSource",
        "tasks.max": 1,
        "file": "/var/log/journal/confluent-kafka-connect.service.log",
        "topic": "kafka-connect-logs"
      }
    }' \
    http://localhost:8083/connectors
    ```
* List connectors
    ```bash
    curl http://localhost:8083/connectors | python -m json.tool
    ```

* Detailing connectors
    ```bash
    curl http://localhost:8083/connectors/first-connector | python -m json.tool
    ```  
* Pausing connectors
    * To pause:
    ```bash
    curl -X PUT http://localhost:8083/connectors/first-connector/pause
    ```
    * To restart:
    ```bash
    curl -X POST http://localhost:8083/connectors/first-connector/restart
    ```
  
* Delete connectors
    ```bash
    curl -X DELETE http://localhost:8083/connectors/first-connector
    ```

### Exercise 4.3
* Download connectors from [confluent](https://docs.confluent.io/5.5.1/connect/managing/install.html])
* Put them under [jars](/jars) directory
* Run `exercise4.3.py` to create kafka connect source
* Check status
    ```bash
    curl http://localhost:8083/connectors/clicks-jdbc | python -m json.tool
    curl http://localhost:8083/connectors/clicks-jdbc/status | python -m json.tool
    ```
* Consume records from the topc
    ```bash
    kafka-console-consumer.sh --topic "solution3.clicks" --bootstrap-server localhost:9092 --from-beginning
    ```

### Glossary
* Kafka Connect - A web server and framework for integrating Kafka with external 
data sources such as SQL databases, log files, and HTTP endpoints.
* JAR - Java ARchive. Used to distribute Java code reusably in a library format under a single file.
* Connector - A JAR built on the Kafka Connect framework which integrates to an external 
system to either source or sink data from Kafka
* Source - A Kafka client putting data into Kafka from an external location, such as a data store
* Sink - A Kafka client remove data from Kafka into an external location, such as a data store
* JDBC - Java Database Connectivity. A Java programming abstraction over SQL database interactions.
* Task - Responsible for actually interacting with and moving data within a Kafka connector. 
One or more tasks make up a connector.
* Kafka REST Proxy - A web server providing APIs for producing and consuming from Kafka, as well as 
fetching cluster metadata.
