import subprocess
import re

def run_pytest():
    result = subprocess.run(
        ["python", "-m", "pytest", "-q"],
        capture_output=True,
        text=True
    )
    return result.stdout


def analyze_results(output):
    passed = re.search(r"(\d+) passed", output)
    failed = re.search(r"(\d+) failed", output)

    passed_count = int(passed.group(1)) if passed else 0
    failed_count = int(failed.group(1)) if failed else 0

    return passed_count, failed_count


def detect_flaky_tests():
    print("\nChecking for flaky tests...\n")

    results = []

    for i in range(3):  # run tests 3 times
        print(f"Run {i+1}...")
        output = run_pytest()
        passed, failed = analyze_results(output)
        results.append((passed, failed))

    return results


def save_report(passed, failed, flaky=False):
    with open("reports/results.txt", "w") as f:
        f.write(f"Passed: {passed}\n")
        f.write(f"Failed: {failed}\n")
        f.write(f"Flaky Detected: {flaky}\n")


def run_tests():
    print("Running all tests...\n")

    output = run_pytest()
    print(output)

    passed, failed = analyze_results(output)

    print("\nSummary:")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    # detect flaky behavior
    results = detect_flaky_tests()

    flaky = len(set(results)) > 1  # if results differ → flaky

    if flaky:
        print("\n⚠️ Flaky tests detected!")
    else:
        print("\n✅ No flaky tests detected")

    save_report(passed, failed, flaky)


if __name__ == "__main__":
    run_tests()