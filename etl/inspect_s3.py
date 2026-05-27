import boto3

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

bucket_name = "weather-data-lake"

response = s3.list_objects_v2(Bucket=bucket_name)

print("Arquivos encontrados:\n")

for obj in response.get("Contents", []):
    print(obj["Key"])