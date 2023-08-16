import json
import boto3

def extract_volume_id(resource):
    resource_split = resource.split(":")
    volume_id = resource_split[-1].split("/")[-1]
    return volume_id

def lambda_handler(event, context):
    # TODO implement
    volume_arn = event["resources"][0]
    volume_id = extract_volume_id(volume_arn)
    print(volume_id)
    ec2_client = boto3.client("ec2")
    response = ec2_client.modify_volume(
        VolumeId = volume_id,
        VolumeType = 'gp3',
    )