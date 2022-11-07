# How to run the code

## Part 1 - The ingestion with the ingest manager

1. Place yourself in the folder /code/ and type `docker-compose up` to create the cluster of Cassandra nodes
2. Wait a couple of minutes to let the nodes configure automatically and discover each other. Open another terminal and enter a container with `docker exec -it <container-name> bash` and type `nodetool status` to see if all nodes have joined the network.
3. Open a third terminal and go again within the code directory. Run the ingest manager with `python3 batch-ingest-manager.py` which calls the clientbatchingestapp.py to ingest its data in **coredms**.
5. In the terminal where the container is running check that the data is actually stored in the database. Type `cqlsh`, then `USE networkdata; SELECT * FROM device_by_onuid` and it will show the stored data.

### Ingestion for different tenants

1. Run the ingest manager with `python3 batch-ingest-manager-multi-tenant.py` which calls the `<client-id>-batchingestapp.py` to ingest its data in **coredms**.
2. When the manager is run, it asks for the client-ID. For example, for the first client type 'client-1' and then for the second 'client-2'
3. In the terminal where the container is running check that the data is actually stored in the database. Type `cqlsh`, then `USE networkdata_<client_id>; SELECT * FROM device_by_onuid_<client_id>` and it will show the stored data.


## Part 2 - The streaming analysis

1. Place yourself in the folder /code/streaming-analysis and type `docker-compose up zookeeper` to start the Zookeeper service, wait some minutes and then `docker-compose up kafka` to start the kafka broker, then `docker-compose up spark` to start the Apache Spark, and once this latter is ready `docker-compose up --scale spark-worker=2 spark-worker` to start the two Spark workers. 
2. Start the Kafka producer with `python3 kafka_producer.py`
3. Start the streaming application **tenantstreamapp** with `docker-compose up stream-processor`, which will call the service `spark_processor.py` in the folder /SparkProcessor
4. Then start the Kafka consumer with `python3 kafka_consumer.py` which will receive the analyzed stream in real-time.
5. The Spark UI can be accessed at the address of the stream-processor container at port 4040. Check its IP with `docker network inspect stream-processing` -> most importantly: PySpark and the Spark image have to be of the same version, in this case 2.4.6
