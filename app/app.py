from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

rc = Counter("web_requests_total", "Total web requests", ["endpoint"])

@app.route('/')
def home():
    rc.labels(endpoint="/").inc()
    return "welcome to the monitoring app"

@app.route('/health')
def health():
    rc.labels(endpoint="/health").inc()
    return jsonify(status="UP")

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
