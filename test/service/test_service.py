

def create_post(request):
    title = request.data.get('title')
    body = request.data.get('body')

    data = {
        "title": title,
        "body": body
    }
    return data