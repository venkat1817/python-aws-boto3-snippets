'''
import boto3
region = 'us-east-1'
instance_id = 'i-00b37f75bbef19e9b'
session = boto3.Session(
    aws_access_key_id='AKIA3KLTVEVUFPF5BFMO',
    aws_secret_access_key='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',
    region_name=region
)

ec2_resource = session.resource('ec2')
instance = ec2_resource.Instance(instance_id)
def start_instance():
    instance.start()
    instance.wait_until_running()
    print(f"Instance {instance.id} has been started")
def stop_instance():
    instance.stop()
    instance.wait_until_stopped()
    print(f"Instance {instance.id} has been stopped")
# start_instance()
stop_instance()

'''
# import boto3

# region = 'us-east-1'
# instance_id = 'i-00b37f75bbef19e9b'

# session = boto3.Session(region_name=region)
# ec2_resource = session.resource('ec2')
# instance = ec2_resource.Instance(instance_id)

# def start_instance():
#     instance.start()
#     instance.wait_until_running()
#     print(f"Instance {instance.id} has been started")

# def stop_instance():
#     instance.stop()
#     instance.wait_until_stopped()
#     print(f"Instance {instance.id} has been stopped")

# # start_instance()
# stop_instance()
#!/usr/bin/python
import boto3
from decouple import config

session=boto3.session.Session(profile_name="default")

AWS_REGION = config('us-east-1')

ec2_con_re=session.resource(service_name="ec2",region_name=AWS_REGION)
my_inst=ec2_con_re.Instance(id="i-00b37f75bbef19e9b")
#print dir(my_inst)
my_inst.start()
#my_inst.stop()
