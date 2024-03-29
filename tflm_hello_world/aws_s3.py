# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/aws_s3.ipynb.

# %% auto 0
__all__ = ['BUCKET_NAME', 's3_conn', 'S3_Connector']

# %% ../nbs/aws_s3.ipynb 1
import boto3
from io import BytesIO
from PIL import Image
import os
import tarfile

# %% ../nbs/aws_s3.ipynb 2
class S3_Connector:
    "Class for accessing files on S3. If the environment variable USE_LOCALSTACK is set to 1, localstack will be used instead of AWS."
    TEST_URL = "http://localstack:4566"
    
    def __init__(self, bucket_name:str):
        if os.getenv("USE_LOCALSTACK") == "1":
            self.s3 = boto3.client('s3', endpoint_url=S3_Connector.TEST_URL, aws_access_key_id="", aws_secret_access_key="")
            self.s3_resource = boto3.resource('s3', endpoint_url=S3_Connector.TEST_URL, aws_access_key_id="", aws_secret_access_key="")
            self.s3.create_bucket(Bucket=bucket_name)
        else:
            self.s3 = boto3.client('s3')
            self.s3_resource = boto3.resource('s3')
        self.bucket_name = bucket_name
        self.s3_bucket = self.s3_resource.Bucket(self.bucket_name)

    def move(self, dir_old:str, dir_new:str, file_name:str):
        " Moves an object to other directory"

        old_destination = f'{dir_old}/{file_name}'
        new_destination = f'{dir_new}/{file_name}'
        copy_source = {
                        'Bucket': self.bucket_name,
                        'Key': old_destination}
        self.s3.copy_object(CopySource=copy_source, Bucket=self.bucket_name, Key=new_destination)
        self.s3.delete_object(Bucket=self.bucket_name, Key=old_destination)

        return True

    def upload_img(self, img, dir:str, file_name:str, pil_image = False):
        " Uploads an image to specified directory. `img` is a file-like object, unless pil_image is True in which case it's a Pillow Image."
        if pil_image:
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            self.s3.upload_fileobj(buffer, self.bucket_name, f'{dir}/{file_name}')
        else:
            self.s3.upload_fileobj(img, self.bucket_name, f'{dir}/{file_name}')

        return True

    def read_images(self, dir : str):
        " Reads images from S3 directory `dir`"

        imgs = []
        for img in self.s3_bucket.objects.filter(Prefix=dir):
            file_path = img.key
            if file_path.endswith(('jpg', 'png')):
                image_data = BytesIO()
                self.s3_bucket.download_fileobj(img.key, image_data)
                image = Image.open(image_data)

                # Insert file name
                image.filename = img.key.split('/')[-1]
                imgs.append(image)
        
        return imgs
    
    def count_objects(self, dir : str):
        " Counts objects in S3 directory `dir`"

        count_objects = self.s3_bucket.objects.filter(Prefix=dir)

        if os.getenv("USE_LOCALSTACK") == "1":
            return len(list(count_objects)) -1
        else:
            return len(list(count_objects))
    
    def upload_tar_file(self, tar_file : str):
        " Uploads tar.gz file to S3 storage"

        with open(f'{tar_file}', 'rb') as tar:
            self.s3.upload_fileobj(tar, self.bucket_name, tar_file)
    
    def download_tar_file(self, tar_file: str):
        " Donwloads tar.gz file from S3 storage"        

        tmp_dir = f'temp/{tar_file}'
        extract_dir = f'temp/'

        if os.getenv("USE_LOCALSTACK") == "1":
            self.create_tar_archive('data.tar.gz', 'data')
            self.upload_tar_file('data.tar.gz')
            self.create_tar_archive('data2.tar.gz', 'data2')
            self.upload_tar_file('data2.tar.gz')
            self.s3.download_file(self.bucket_name, tar_file, tmp_dir)
        else:
            self.s3.download_file(self.bucket_name, tar_file, tmp_dir)

        with tarfile.open(tmp_dir, 'r:gz') as tar:
            tar.extractall(path=extract_dir)
    
    def create_tar_archive(self, output_filename, dataset):
        """Creates a tar.gz archive from a folder."""
        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(dataset, arcname=os.path.basename(dataset))



BUCKET_NAME = 'tinymldatasets'
s3_conn = S3_Connector(BUCKET_NAME)
    
