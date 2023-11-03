import boto3
#import logging

session = boto3.session.Session(region_name='ap-south-1')
ec2client = session.client('ec2')

######### Variable declaration section
res = None
response = None
instancelist = None
session = None
ec2client = None
########################################

