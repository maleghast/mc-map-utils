import sys
import os
import boto3
from datetime import date, timedelta

files = os.listdir(sys.argv[1])
destination_bucket = sys.argv[2]
backup_latest_stem = "backup-{}".format(date.today() - timedelta(days = 1))
target = ""

for file in files:
	if backup_latest_stem in file:
		target = file

s3 = boto3.client('s3')
s3.upload_file("{}/{}".format(sys.argv[1], target), destination_bucket, target)
