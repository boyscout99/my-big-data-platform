# Running the code described in the Report

> NOTE! For testing purposes there is only one Zookeeper and one Kafka broker, in production replicate both as clisters of at least three nodes.

## Part 1 - The ingestion with the ingest manager

1. Place yourself in the folder /code/streaming-analysis and type `docker-compose up zookeeper` to start the Zookeeper service, wait some minutes and then `docker-compose up kafka` to start the kafka broker, then `docker-compose up spark` to start the Apache Spark, and once this latter is ready `docker-compose up --scale spark-worker=2 spark-worker` to start the two Spark workers. 
2. Start the Kafka producer with `python3 kafka_producer.py`
3. Start the streaming application **tenantstreamapp** with `docker-compose up stream-processor`, which will call the service `spark_processor.py` in the folder /SparkProcessor
4. Then start the Kafka consumer with `python3 kafka_consumer.py` which will receive the analyzed stream in real-time.
