#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def create_collection(faces):

    client=boto3.client('rekognition')

    #Create a collection
    print('Creating collection:' + faces)
    response=client.create_collection(CollectionId=faces)
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')
    
def main():
    collection_id='faces'
    create_collection(collection_id)

if __name__ == "__main__":
    main()    