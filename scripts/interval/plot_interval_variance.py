import matplotlib.pyplot as plt
import sys
import statistics
import glob

files = sorted(glob.glob("iphone*"))
arg = ""
if len(sys.argv) > 1:
    arg = sys.argv[1]

def plot(file_name, offset):
    intervals = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            intervals.append(float(line.strip()))
    variance = statistics.variance(intervals) * pow(10, 6)
    if arg == "variance":
        plt.scatter(offset, variance, label=file_name+"_variance")
    else:
        plt.scatter([i for i in range(len(intervals))], intervals, label=file_name)

counter = 0
for file in files:
    plot(file, counter)
    counter += 1
plt.xlabel("interval vairance")
plt.legend()
plt.tight_layout()
plt.show()
