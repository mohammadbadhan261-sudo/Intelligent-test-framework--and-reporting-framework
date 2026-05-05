from flask import Flask, render_template, redirect, url_for, jsonify
import subprocess
import threading
import os

app = Flask(__name__)

TEST_RUNNING = False


def run_tests_background():
    global TEST_RUNNING
    TEST_RUNNING = True

    process = subprocess.Popen(
        ["python", "framework/run_tests.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output, error = process.communicate()

    # Save logs
    with open("reports/logs.txt", "w") as f:
        f.write(output)
        if error:
            f.write("\nERRORS:\n" + error)

    TEST_RUNNING = False


def read_results():
    try:
        with open("reports/results.txt", "r") as f:
            lines = f.readlines()

        passed = lines[0].split(":")[1].strip()
        failed = lines[1].split(":")[1].strip()
        flaky = lines[2].split(":")[1].strip()

        return passed, failed, flaky
    except:
        return "0", "0", "Unknown"


def read_logs():
    if os.path.exists("reports/logs.txt"):
        with open("reports/logs.txt", "r") as f:
            return f.read()
    return "No logs yet."


@app.route("/")
def home():
    passed, failed, flaky = read_results()
    return render_template("index.html", passed=passed, failed=failed, flaky=flaky)


@app.route("/run")
def run():
    if not TEST_RUNNING:
        thread = threading.Thread(target=run_tests_background)
        thread.start()
    return redirect(url_for("home"))


@app.route("/status")
def status():
    return jsonify({"running": TEST_RUNNING})


@app.route("/logs")
def logs():
    return jsonify({"logs": read_logs()})


if __name__ == "__main__":
    app.run(debug=True)