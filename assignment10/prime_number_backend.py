from flask import Flask
import json

app = Flask(__name__)

@app.route('/prime_number/<number>')
def prime_number(number):
    number = int(number)

    if number < 2:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    return json.dumps({
        "Number": number,
        "isPrime": is_prime
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)