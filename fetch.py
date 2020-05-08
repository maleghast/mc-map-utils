import sys
import json
import ftplib
from ftplib import FTP

secrets_response = json.loads(sys.argv[1])
secrets = json.loads(secrets_response['SecretString'])

server = secrets["server"] 
username = secrets["username"] 
password = secrets["password"]

filelist = []
filenames = []
target = ''

ftp = FTP(server)
ftp.login(username, password)
ftp.dir(filelist.append)

for line in filelist:
	filenames.append(line.split(" ")[-1])

for filename in filenames:
	if "backup" in filename:
		target = filename

with open('/home/ec2-user/backup.zip', 'wb') as fp:
	ftp.retrbinary('RETR {}'.format(target), fp.write)



