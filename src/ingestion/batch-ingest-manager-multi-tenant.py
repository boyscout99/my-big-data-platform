"""
This manager runs the client-id-batch-ingest-app.py 
based on the received client-id.
Schedules the running based on the updates on the
client-stagin-input-directory folder
"""

if __name__ == '__main__':
	
	print("### EXECUTING BATCH INGEST MANAGER ###")
	count = 0
	while count < 2:
		client_id = input("Enter your client ID (e.g. client-1): ")
		# Execute the ingest app of the client
		path_to_app = "./client-ingest-api/"+client_id+"-batchingestapp.py"
		#path_to_app = "./client-ingest-api/clientbatchingestapp.py"
		print(type(path_to_app))
		exec(open(path_to_app).read())
		count = count + 1
