#!/usr/bin/python
import boto3
import csv

iam_obj = boto3.resource('iam')
iam = boto3.resource('iam')

file_open = open('iam.userdetails.csv','w',newline='')
data_obj = csv.writer(file_open, delimiter=",")
data_obj.writerow([ 'user_name'])
for iam_user in iam_obj.users.all():
  data_obj.writerow([iam_user.name])
file_open.close()