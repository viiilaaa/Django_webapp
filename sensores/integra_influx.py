from influxdb_client import InfluxDBClient
from prueba import settings

def read_from_influx():
    try:
        client = InfluxDBClient(
            url=settings.INFLUXDB["URL"],
            token=settings.INFLUXDB["TOKEN"],
            org=settings.INFLUXDB["ORG"]
        )
        query = f'from(bucket:"{settings.INFLUXDB["BUCKET"]}") |> range(start: -1h)'
        query_api = client.query_api()
        tables = query_api.query(query)
        
        results = []
        for table in tables:
            for record in table.records:
                results.append({
                    "time": record.get_time(),
                    "value": record.get_value(),
                    "field": record.get_field(),
                    "measurement": record.get_measurement()
                })
        
        client.close()
        return results
    except Exception as e:
        return {"status": "error", "message": str(e)}
