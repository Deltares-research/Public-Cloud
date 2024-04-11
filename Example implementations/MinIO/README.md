# Hands-on training 11-04-2024

Amazon Web Services (AWS) is one of the main public cloud computing vendors. One of its core components is S3, the object storage service offered by AWS. With its impressive availability and durability, it has become the standard way to store videos, images, and data. You can combine S3 with other services to build infinitely scalable applications. S3 has a well-documented interface to communicate with data in S3.

MinIO is a scalable object-store that implements the S3 interface. It can be used to deploy S3-like environments in an on-premise environment, Kubernetes or
at other public cloud vendors. This ensures that communication with data stored in different object stores is similar in different data environments.

Boto3 is the name of the Python SDK for AWS. It allows you to directly create, update, and delete AWS resources from your Python scripts. For the purposes of
this training session we only look at the interaction with data in a MinIO bucket (which implements the AWS S3 interface).

> By the end of this course, you’ll:
> 
> * Be confident working with buckets and objects directly from your Python scripts

## Installation and setup

To install Boto3 on your computer, go to your terminal and run the following:

    pip install boto3

You’ve got the SDK. But, you won’t be able to use it right now, because it doesn’t know which AWS account it should connect to.

To make it run against your MinIO bucket, you’ll need to provide some valid credentials. 

If you already have an IAM user that has full permissions to S3, you can use that user’s credentials (their access key and their secret access key) without needing to create a new user. Otherwise, the easiest way to do this is to create a new AWS user and then store the new credentials.

At its core, all that Boto3 does is call MinIO APIs on your behalf. For the majority, Boto3 offers two distinct ways of accessing these abstracted APIs:

* Client: low-level service access
* Resource: higher-level object-oriented service access

You can use either to interact with S3.

To connect to the low-level client interface, you must use Boto3’s client(). You then pass in the name of the service you want to connect to, in this case, s3:

    import boto3
    s3_client = boto3.client('s3')

To connect to the high-level interface, you’ll follow a similar approach, but use resource():

    import boto3
    s3_resource = boto3.resource('s3')

In the FileIOExample.ipynb Jupyter Notebook you will be able to see how to connect succesfully to an existing MinIO bucket.

## How to create an access key

To create an access and secret key go to https://s3-console.deltares.nl/browser 

After logging in, go to "Access Keys" and click "Create Access Key".

Store your access and secret key somewhere safe.

## Machine Learning example

See an example on how to use data from MinIO / S3 in a machine learning environment.

## Docker container

To run a Docker container locally you need Docker Desktop installed: https://www.docker.com/products/docker-desktop/

Before building the container add your bucket name and credentials in the python script (/docker_example/upload_file_to_minio.py)

To build the container execute the following command:

    docker build -t s3-upload .

To run the container execute the following command:

    docker run s3-upload
