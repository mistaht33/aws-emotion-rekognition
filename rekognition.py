import boto3

BUCKET_NAME = 'some-bucket'
AWS_ACC_KEY_ID = ''
AWS_SECRET_ACC_KEY = '+mpYwx2W'
REGION = 'us-east-1'

if __name__ == '__main__':
    s3 = boto3.client('s3',
                      aws_access_key_id=AWS_ACC_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACC_KEY,
                      region_name=REGION)
    all_objects = s3.list_objects(Bucket=BUCKET_NAME)
    for objects in all_objects.get('Contents'):
        file = objects.get('Key')
        rekognition = boto3.client('rekognition',
                                   aws_access_key_id=AWS_ACC_KEY_ID,
                                   aws_secret_access_key=AWS_SECRET_ACC_KEY,
                                   region_name=REGION)
        rekognition_response = rekognition.detect_faces(
            Image={'S3Object': {'Bucket': BUCKET_NAME, 'Name': file}},
            Attributes=['ALL'])
        for item in rekognition_response.get('FaceDetails'):
            print(f'{file} has been detected to have emotion: {item.get("Emotions")[0]["Type"]}')