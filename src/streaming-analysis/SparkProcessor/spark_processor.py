# spark-submit --master "spark://spark:7077" --packages  org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.4.6 pyspark_test.py
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
import logging
from kafka import KafkaProducer

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger("mini-batcher-application")
rootLogger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
consoleHandler.setLevel(logging.DEBUG)
rootLogger.addHandler(consoleHandler)

WINDOW_DURATION = 5
zookeeper_quorum = 'zookeeper:2181'
consumer_group_id = 'my-group-id'
topic_report = 'topic2'
#broker = 'kafka-1:9092'

# previous configuration spark://spark:7077
sc = SparkContext(appName="Pyspark_counter")
sc.setLogLevel("ERROR")

# get the messages from topic1 and publish on topic2
ssc = StreamingContext(sc, WINDOW_DURATION)
# create a kafka receiver and consume topic1 1 parition at a time
kafkaStream = KafkaUtils.createStream(ssc, zookeeper_quorum, consumer_group_id, {'topic1':1})

#producer = KafkaProducer(bootstrap_servers=['kafka-1:29092'],value_serializer=lambda x:dumps(x).encode('utf-8'))
#Reporting Services

def GetKafkaProducer():
    return KafkaProducer(bootstrap_servers = ['kafka:9092'])

def send_alert(timestamp, onuid, avg_speed):
    '''
    Sends the received message to the Kafka topic, using the KafkaProducer class. 
    '''
    #print("Sending on topic", topic_report)
    #print(f"key: {key}, count: {count}")
    producer = GetKafkaProducer()
    producer.send(topic_report, str.encode(f'TIMESTAMP: {timestamp, }ONUID: {onuid}, Avg. Speed: {avg_speed}'))
    producer.flush()
    return

def process_kafka_pending_messages(message):
    '''
    Processes the JSON message coming from the Kafka broker. 
    The data coming is in this format "data={'counter': j}". 
    '''
    rootLogger.info("========= Started Processing New RDD! =========")
    kafka_messages = message.collect()
    print("kafka_messages: ", kafka_messages)
    try:
        data = []
        for message in kafka_messages:
            # Processes the messages in the Kafka pipeline
            # Each message is inserteed in the data array
            data.append(json.loads(message))
            print("Data array: ", data)
        
        for item_string in data:
            print("Item_string: ", item_string)
            # For each string in data save the single item
            avg_speed = (item_string["speedin"]+item_string["speedout"])/2
            print("Processed item: avg speed = ", avg_speed)
            #print("Item in the array: ", item)
            # Here do the processing, e.g. add a letter
            rootLogger.info("Sending to broker...")
            send_alert(item_string["onuid"], avg_speed)
            
                
        rootLogger.info("========= Completed Processing of RDD! =========")
        rootLogger.info("========= Results =========")
        # printing the valresults:
        '''
        for key in node_avg_data:
        rootLogger.info(f"Node Name: {key}, Counter:{count} for window of {WINDOW_DURATION} seconds")
        send_alert(key, count)
	'''

    except Exception as e:
        rootLogger.error(f"Encountred exception while processing: {e}")
    
    rootLogger.info("========= Finish =========")
    
    return
    
if __name__ == '__main__':

   parsed = kafkaStream.map(lambda v: v[1])
   parsed.foreachRDD(process_kafka_pending_messages)

   ssc.start()
   ssc.awaitTermination()
