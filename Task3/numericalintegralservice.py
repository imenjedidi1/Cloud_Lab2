from flask import Flask, jsonify  # type: ignore
import math

app = Flask(__name__)

# Numerical integration function
def numerical_integration(lower, upper, N):
    delta_x = (upper - lower) / N
    integral = 0.0
    for i in range(N):
        x_i_mid = lower + (i + 0.5) * delta_x
        f_x = abs(math.sin(x_i_mid))
        integral += f_x * delta_x
    return integral


#@app.route('/')
#def home():
#    return "Flask is running!"

    
#@app.route('/test', methods=['GET'])
#def test_route():
#    return "Test route is working!"


# Flask route for the microservice
@app.route('/numericalintegralservice/<lower>/<upper>', methods=['GET'])
def compute_integral_range(lower, upper):
    lower = float(lower)
    upper = float(upper)
    print(f"Accessed route with lower={lower}, upper={upper}")
    # Predefined N values
    N_values = [10, 100, 1000, 10000, 100000, 1000000]

    # Compute the integral for each N
    results = {}
    for N in N_values:
        integral = numerical_integration(lower, upper, N)
        results[N] = integral

    # Return the results as JSON
    return jsonify({
        "lower": lower,
        "upper": upper,
        "N_values": N_values,
        "results": results
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
