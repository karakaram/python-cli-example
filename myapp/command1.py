import boto3
import logging

logger = logging.getLogger(__name__)


class Command1(object):
    def __init__(self, opts):
        self.opts = opts
        self.ec2 = boto3.client('ec2', region_name='ap-northeast-1')

    def exec(self):
        response = self.ec2.describe_instances(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': ['my-alb-asg']
                },
                {
                    'Name': 'instance-state-name',
                    'Values': ['running', 'stopped']
                }
            ],
        )
        for reservations in response['Reservations']:
            for instances in reservations['Instances']:
                logger.info(instances['InstanceId'])
