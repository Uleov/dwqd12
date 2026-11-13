requests = [
    {"phone": "89001112233", "email": "user1@ya.ru"},
    {"phone": "900", "email": ""}
]

def check_line(value):
    return len(value) == 11

def check_request(request):
    results = []
    for field in ("phone", "email"):
        results.append(check_line(request.get(field, "")))
    return all(results)

def process(requests):
    result = []
    for req in requests:
        if check_request(req):
            result.append(req)
    return result

print(process(requests))
