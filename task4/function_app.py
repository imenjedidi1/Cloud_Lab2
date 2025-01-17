import azure.functions as func
import json
import math

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="numericalintegralfunction")
def numericalintegralfunction(req: func.HttpRequest) -> func.HttpResponse:
    # Predefined values for testing
    lower = 0
    upper = math.pi
    n_values = [10, 100, 1000, 10000, 100000, 1000000]

    # Perform your numerical integration logic here
    results = {}
    for n in n_values:
        dx = (upper - lower) / n
        integral = sum(math.sin(lower + i * dx) * dx for i in range(n))
        results[str(n)] = integral

    response = {
        "lower": lower,
        "upper": upper,
        "n_values": n_values,
        "results": results
    }

    return func.HttpResponse(json.dumps(response), status_code=200, mimetype="application/json")
