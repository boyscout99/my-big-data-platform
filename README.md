# My Big Data Platform, a Proof of Concept (work in progress)

This repository provides a design for a big data platform used for network data processing.

It is the result of my design and programming assignments for the course Big Data Platforms, 
which I followed at Aalto University during the Spring of 2021.

## What I used for this project

Apache Cassandra
 - for 
 
Apache Spark
 - for stream processing in near real-time
 - uses Spark Streaming for batch processing
 - uses Hadoop as scheduler
 
Apache Kafka
 - for 
 
Zookeeper
 - used to orchestrate Kafka brokers
 - brokers send metadata about them and their topics to Zookeeper nodes
 
Python
- to write most of the code
- libraries like cassandra.cluser, kafka, pyspark, csv, json

Docker containers
- for Kafka brokers
- for Zookeeper nodes
- for a cluster of Apache Cassandra nodes
- for Apache Spark workers and master node
- for the Apache Spark Streaming processor image because the JVM version of my machine was not the one I needed

## The structure
Picture of the design.

And brief explanation.

## How to navigate the folders

Links to other folders.
Inside [src]()
```
streaming-analysis
    ├── docker-compose.yml
    ├── kafka_consumer.py
    ├── kafka_producer.py
    ├── SparkProcessor
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   ├── spark_processor.py
    │   └── start_spark.sh

```
