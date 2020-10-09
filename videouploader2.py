def handler(event, context):
    evtHeaders = event.headers;
    return {"event headers are ", evtHeaders}