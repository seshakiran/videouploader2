import boto3
import json
s3 = boto3.client("s3")


def handler(event, context):
    movieID = event["headers"]["movieid"])
    movieName = event["headers"]["moviename"])
    uploaderName = event["headers"]["uploadername"])
    fullFilename = movieID + "_" + movieName + "_" + uploadername
    try:
        data = s3.put_object(
            Bucket="movilti-user-reviews",
            Key=fullFileName,
            Body=fileContent,
            Metadata={}
        )
    except BaseException as e:
        print(e)
        raise(e)
    return ("File successfully uploaded ", fullFileName)