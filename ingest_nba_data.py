import boto3
import os


local_path = "/mnt/c/Users/julio/Desktop/nba/all_seasons.csv"



bucket_name = "nbadataa"
s3_key = "nba_players.csv" 


s3 = boto3.client("s3")


try:
    s3.upload_file(local_path, bucket_name, s3_key)
    print(f" Upload concluido: {local_path} -> s3://{bucket_name}/{s3_key}")
except Exception as e:
    print(" Erro ao enviar para o S3:", e)
