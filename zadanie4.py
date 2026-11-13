workers = {
    "Ivan": ["repair", "cleaning"],
    "Anna": ["delivery"]
}

def check_data(request):
    if not request.get("text"):
        return "error: empty request"
    if request.get("amount", 0) <= 0:
        return "error: bad amount"
    return "ok"

def find_worker(kind, workers):
    for name in workers:
        if kind in workers[name]:
            return name
    return None

def notify(worker, req_id):
    print("notify", worker, "about request", req_id)

def save_to_journal(journal, req_id, worker):
    journal.append({"id": req_id, "status": "accepted", "worker": worker})

tests = [
    {"text": "", "amount": 100, "kind": "repair", "id": 1},
    {"text": "fix", "amount": -50, "kind": "repair", "id": 2},
    {"text": "paint", "amount": 200, "kind": "build", "id": 3},
    {"text": "fix", "amount": 300, "kind": "repair", "id": 4}
]

journal = []

for req in tests:
    status = check_data(req)
    if status != "ok":
        print(status)
        continue

    worker = find_worker(req.get("kind"), workers)
    if worker is None:
        print("error: no worker")
        continue

    notify(worker, req["id"])
    save_to_journal(journal, req["id"], worker)
    print("accepted")

print("journal:", journal)
