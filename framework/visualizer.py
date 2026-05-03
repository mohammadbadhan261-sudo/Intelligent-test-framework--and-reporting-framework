import matplotlib.pyplot as plt

def read_results():
    with open("reports/results.txt", "r") as f:
        lines = f.readlines()

    passed = int(lines[0].split(":")[1].strip())
    failed = int(lines[1].split(":")[1].strip())

    return passed, failed


def plot_results(passed, failed):
    labels = ['Passed', 'Failed']
    values = [passed, failed]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Test Results")
    plt.xlabel("Test Status")
    plt.ylabel("Number of Tests")

    plt.savefig("reports/graph.png")
    plt.show()


if __name__ == "__main__":
    passed, failed = read_results()
    plot_results(passed, failed)