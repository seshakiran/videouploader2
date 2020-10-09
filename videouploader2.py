def handler(event, context):
    evtHeaders = event.headers
    fileContent = event.Body
    return ("event headers are ", evtHeaders[0])