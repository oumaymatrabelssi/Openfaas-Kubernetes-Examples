import json
from influxdb import InfluxDBClient

host = 'localhost'
port = 8086
user = 'admin'
password = 'admin'
dbname = 'sensors'


def insert_to_influx(client):
                    json_body = [ {
                       "measurement": "humidity",
                       "tags":{
                          "device_id": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f",
                          "device_name": device},
                       "time": data['timestamp'],
                       "fields": {
                       "value": float(data['value']['humidity'])
                                }
                          }
                           ]
                    print(json_body)
                    client.write_points(json_body)                           
            



def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    client = InfluxDBClient(host, port, user, password, dbname)
    print("waiting to receive messages")
    # start the proton Container event loop with the DTEConsumer event handler
    return client

handle("")
