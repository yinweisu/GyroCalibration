import matplotlib.pyplot as plt
import sys
import statistics
import glob
import numpy as np
import scipy.stats as stats


arg = "iphone*"
if len(sys.argv) > 1:
    arg = sys.argv[1]
files = sorted(glob.glob(arg))

def plot(file_name, offset):
    intervals = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            intervals.append(float(line.strip()))
    intervals.sort()
    imean = np.mean(intervals)
    istd = np.std(intervals)
    pdf = stats.norm.pdf(intervals, imean, istd)
    plt.plot(intervals, pdf, '-o', label=file_name)
    # plt.scatter([i for i in range(len(intervals))], intervals, label=file_name)

counter = 0
for file in files:
    plot(file, counter)
    counter += 1
plt.xlabel("interval vairance")
plt.legend()
plt.tight_layout()
plt.show()
