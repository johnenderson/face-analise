import boto3
import json

client = boto3.client('rekognition')
s3 = boto3.resource('s3')

def detecta_faces():
    faces_detectadas=client.index_faces(
        CollectionId='faces',
        DetectionAttributes=['DEFAULT'],
        ExternalImageId='TEMPORARIA',
        Image={
             'S3Object': {
                 'Bucket': 'fa-img-jes-alura',
                 'Name': '_analise.jpg',
            },
        },
    )
    return faces_detectadas()

faces_detectadas = detecta_faces()
print(json.dumps(faces_detectadas, indent=4))