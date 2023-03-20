# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/aws_s3.ipynb.

# %% auto 0
__all__ = ['BUCKET_NAME', 's3_conn', 'S3_Connector']

# %% ../nbs/aws_s3.ipynb 1
import boto3
from io import BytesIO
from PIL import Image
import os

# %% ../nbs/aws_s3.ipynb 2
class S3_Connector:
    TEST_URL = "http://localstack:4566"
    
    def __init__(self, bucket_name):
        if os.getenv("USE_LOCALSTACK") == "1":
            self.s3 = boto3.client('s3', endpoint_url=S3_Connector.TEST_URL, aws_access_key_id="", aws_secret_access_key="")
            self.s3_resource = boto3.resource('s3', endpoint_url=S3_Connector.TEST_URL, aws_access_key_id="", aws_secret_access_key="")
            self.s3.create_bucket(Bucket=bucket_name)
        else:
            self.s3 = boto3.client('s3')
            self.s3_resource = boto3.resource('s3')
        self.bucket_name = bucket_name
        self.s3_bucket = self.s3_resource.Bucket(self.bucket_name)

    def move(self, dir_old, dir_new, file_name):
        " Moves an object to other directory"

        old_destination = f'{dir_old}/{file_name}'
        new_destination = f'{dir_new}/{file_name}'
        copy_source = {
                        'Bucket': self.bucket_name,
                        'Key': old_destination}
        self.s3.copy_object(CopySource=copy_source, Bucket=self.bucket_name, Key=new_destination)
        self.s3.delete_object(Bucket=self.bucket_name, Key=old_destination)

        return True

    def upload_img(self, img, dir, file_name, pil_image = False):
        " Uploads an image to specified directory"
        if pil_image:
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            self.s3.upload_fileobj(buffer, self.bucket_name, f'{dir}/{file_name}')
        else:
            self.s3.upload_fileobj(img, self.bucket_name, f'{dir}/{file_name}')

        return True

    def read_images(self, dir):
        " Reads images from S3 directory"

        imgs = []
        for img in self.s3_bucket.objects.filter(Prefix=dir):
            file_path = img.key
            if file_path.endswith('.png'):
                image_data = BytesIO()
                self.s3_bucket.download_fileobj(img.key, image_data)
                image = Image.open(image_data)

                # Insert file name
                image.filename = img.key.split('/')[-1]
                imgs.append(image)
        
        return imgs
    
    def count_objects(self, dir):
        " Counts objects in S3 directory"

        count_objects = self.s3_bucket.objects.filter(Prefix=dir)

        return len(list(count_objects)) -1


BUCKET_NAME = 'tflmhelloworldbucket'
s3_conn = S3_Connector(BUCKET_NAME)
