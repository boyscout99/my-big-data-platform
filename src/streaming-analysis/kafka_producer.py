'''
This producer emulates an OLT producing streaming data
and publishing it on a Kafka broker.

Pseudocode:

  open the file
    read each line of the file
      split the line on the comma (csv)
      get the value for each column
        save ifindex, onuid, speedin, speedout
        insert timestamp time.now()
      publish this information on topic1 in the form of a dictionary
      do this every second
'''
import time
from json import dumps
from kafka import KafkaProducer

# create the Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

def read_file(dir_path, path_to_csv):
    # Open the file containing the data to ingest
    f = open(dir_path, "r")
    data = f.readlines()
    for row in data:
        
    f.close()	
    return 1
    
def 

# message in JSON format
message = {
    'provincecode': 'HKD',
    'deviceid':'2222771642618',
    'ifindex':'6828878457269',
    'frame': 1,
    'slot': 1,
    'port': 13 ,
    'onuindex': 20,
    'onuid':'222277164261810113020',
    'time':'01/08/2019 11:38:33',
    'speedin': 2992,
    'speedout': 2947,
}


# publishing on topic1
for j in range(9999):
    print("Sending message: ", message)
    producer.send('topic1', value=message)
    sleep(1)
