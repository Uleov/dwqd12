def calc_cost(request):
    if not request:
        return 0
    if "ops" not in request:
        return 0
    ops = request["ops"]
    if ops <= 0:
        return 0
    if ops > 100:
        return ops * 2
    return ops

tests = [
    {},
    {"text": "no ops"},
    {"ops": -10},
    {"ops": 0},
    {"ops": 50},
    {"ops": 150}
]

for t in tests:
    print("input:", t, "-> result:", calc_cost(t))
