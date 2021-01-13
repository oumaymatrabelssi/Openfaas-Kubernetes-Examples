import json
from influxdb import InfluxDBClient

host = 'localhost'
port = 8086
user = 'admin'
password = 'admin'
dbname = 'sensors'


def insert_to_influx(client):
                    json_body = [ {
                       "measurement": "Temperature",
                       "tags":{
                          "device_id": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f",
                          "device_name": "device1"},
                       "time": "1610467532",
                       "fields": {
                       "value": "8")
                                }
                          }
                           ]
                    print(json_body)
                    client.write_points(json_body)                           
            



client = InfluxDBClient(host, port, user, password, dbname)
print("waiting to receive messages")
print(client)
