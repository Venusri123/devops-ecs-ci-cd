#!/usr/bin/env python3
#webhook Test
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Welcome to DevOps ECS CI/CD Flask App")

@app.route("/health")
def health():
    return jsonify(status="UP")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


