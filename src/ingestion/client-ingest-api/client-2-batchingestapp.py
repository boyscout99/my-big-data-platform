import logging
import os
import csv
import time
from datetime import datetime
from cassandra.cluster import Cluster

logging.basicConfig(level=logging.INFO)

def cassandra_connection():
	"""
	Connection object for Cassandra
	:return: session, cluster
	"""
	cluster = Cluster(['localhost'], port=9042)
	session = cluster.connect()
	session.execute("""
		CREATE KEYSPACE IF NOT EXISTS networkdata_client_2
		WITH REPLICATION =
		{ 'class' : 'SimpleStrategy', 'replication_factor' : 2 };
	""")
	time.sleep(5)
	session.set_keyspace('networkdata_client_2')
	#session.execute("""USE networkdata;""")
	session.execute("""
		CREATE TABLE IF NOT EXISTS device_by_onuid_client_2 (
		time text,
		provincecode text,
		ifindex text,
		onuid text,  
		speedin text, 
		speedout text,
		PRIMARY KEY (onuid)
		);
	""")
	return session, cluster

def remove_columns(row):
	"""
	Data wrangling function: creates a new row without redundant information
	input: row -> output: new_row
	"""
	# Get each value from row
	columns = row.split(',')
	provincecode = columns[0]
	deviceid = columns[1]
	ifindex = columns[2]
	frame = columns[3]
	slot = columns[4]
	port = columns[5]
	onuindex = columns[6]
	onuid = columns[7]
	time = columns[8]
	speedin = columns[9]
	speedout = columns[10].strip() #remove \n
	#print("Input row:\n", columns)
	date = datetime.strptime(time, "%d/%m/%Y %H:%M:%S")
	timestamp = datetime.timestamp(date)
	new_row = f'{timestamp}, {provincecode}, {ifindex}, {onuid}, {speedin}, {speedout}'
	#print("Output row:\n", new_row)
		
	return new_row


def ingest_file(path_to_csv):
	"""
	Use cqlsh method COPY to import a csv file into the database
	The data is present in the mounted volume.
	"""
	host = 'localhost'
	keyspace_name = 'networkdata_client_2'
	table_name = 'device_by_onuid_client_2'
	keys_order = '(time, provincecode, ifindex, onuid, speedin, speedout)'
	print("Keys order: ", keys_order)
	file_path = path_to_csv
	command = f"cqlsh {host} -k {keyspace_name} -e \"COPY {table_name} {keys_order} FROM '{file_path}' WITH DELIMITER=',' AND HEADER=TRUE;\""
	print("Command: ", command)
	os.system(command)
	
	return

def read_file(dir_path, path_to_proc_csv):
	# Open the file containing the data to ingest
	f = open(dir_path, "r")
	data = f.readlines()
	new_f = open(path_to_proc_csv, "a")
	count = 0
	for row in data:
		if count > 0:
			new_row = remove_columns(row)
			# write row
			new_f.write(f'{new_row}\n')
		if count == 0:
			count = count + 1
	# Close the files
	new_f.close()
	f.close()
		
	return 1


if __name__ == "__main__":

	logging.info('Not callable')
	print('Getting Cassandra session')    
	session, cluster = cassandra_connection()
	print('Reading data to process for client-2 ...')
	path_to_csv = './client-ingest-api/client-2-staging-input-directory/unproc-data-client-2.csv'
	path_to_proc_csv = './client-ingest-api/client-2-staging-input-directory/processed-data/proc-data-client-2.csv'
	read_file(path_to_csv, path_to_proc_csv)
	print('Data wrangling performed. New file created.')
	ingest_file(path_to_proc_csv)
	print('Ingested processed data for client-2.')





