import boto3 
import json
from fake_web_events import Simulation
from dotenv import load_dotenv
from os import getenv

load_dotenv('/.env')

client = boto3.client(
    'firehose',
    aws_access_key_id = getenv('AWS_ID'),
    aws_secret_access_key = getenv('AWS_KEY')
    )

def put_record (event: dict):
    data = json.dumps (event) + "\n" 
    response = client.put_record(DeliveryStreamName='ingestion_fake_web_events', Record={"Data": data})
    print(event)
    return response

simulation = Simulation(user_pool_size=100, sessions_per_day=100000) 
events = simulation.run(duration_seconds=3000)

for event in events:
    put_record(event)
