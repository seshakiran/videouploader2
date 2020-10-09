def handler(event, context):
    evtHeaders = event.headers
    fileContent = event.Body
    fullFileName = evtHeaders[0]
    return ("event headers are ", evtHeaders[0])