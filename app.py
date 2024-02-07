from flask import Flask
import psutil
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "data": "Connected Successfully!"
    }, 200

@app.route("/ping")
def Ping():
    return {
        "data": "Ok"
    }, 200

@app.route("/healthz")
def getDiskUsage():
    hdd = psutil.disk_usage("/")

    return {
        "Total": hdd.total,
        "Used": hdd.used,
        "Free": hdd.free,
        "System": platform.system(),
        "Version": platform.release(),
    }, 200

if __name__ == "__main__":
    app.run(debug=True)