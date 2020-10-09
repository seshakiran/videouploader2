import boto3
s3 = boto3.client("s3")

def handler(event, context):
    evtHeaders = event.headers
    fileContent = event.body
    fullFileName = "test"# evtHeaders[0]
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
    return ("event headers are ", fullFileName)