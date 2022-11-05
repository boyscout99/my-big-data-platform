# My Big Data Platform, a Proof of Concept (work in progress)

This repository provides a design for a big data platform used for network data processing.

It is the result of my design and programming assignments for the course Big Data Platforms, 
which I followed at Aalto University during the Spring of 2021.

## What I used for this project
Python
- to write most of the code
- libraries like pandas, 

Docker containers
- dockercompose files for
- 
The project includes Python, Docker, Apache Cassandra, Apache Spark, Apache Kafka, Zookeeper.

## The structure
Picture of the design.

And brief explanation.

## How to navigate the folders

Links to other folders.
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
    └── unproc-data-client-1.csv
```
