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


#################### Creating a session and getting the ec2 instance client
session = boto3.session.Session(region_name='ap-south-1')
ec2client = session.client('ec2')
###########################################################################


########################### Function Declaration section
'''
Function_Name = get_instanceIds_Stopped
arguments = tag and value
Description  = This function filter outs the instance with particular tags and instance state as stopped
'''
def get_instanceIds_Stopped(tag,value):
    response = ec2client.describe_instances(Filters=[{'Name':'tag:'+'Env','Values':['Demo_Lab']}])
    instancelist = []
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            if instance['State']['Name'] == 'stopped':
                instancelist.append(instance["InstanceId"])
    print instancelist,"InstanceList"
    return instancelist
def main():
    instancelist = get_instanceIds_Stopped('Demo_Lab','Env')
    for val in instancelist:
        res = ec2client.start_instances( InstanceIds=[val,],DryRun=False)
        print res,"res"
if __name__ == "__main__":
        main()
