import subprocess
import re

def analyze_results(output):
    passed = re.search(r"(\d+) passed", output)
    failed = re.search(r"(\d+) failed", output)

    passed_count = int(passed.group(1)) if passed else 0
    failed_count = int(failed.group(1)) if failed else 0

    return passed_count, failed_count


def save_report(passed, failed):
    with open("reports/results.txt", "w") as f:
        f.write(f"Passed: {passed}\n")
        f.write(f"Failed: {failed}\n")


def run_tests():
    print("Running all tests...\n")

    result = subprocess.run(
        ["python", "-m", "pytest"],
        capture_output=True,
        text=True
    )

    output = result.stdout
    print(output)

    passed, failed = analyze_results(output)

    print("\nSummary:")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    # ✅ IMPORTANT: call it here
    save_report(passed, failed)


if __name__ == "__main__":
    run_tests()