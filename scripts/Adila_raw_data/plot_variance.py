#x calibration: 0.00625104736536741, y calibration: 0.00172870047390461, z calibration: 0.00461516436189413
import matplotlib.pyplot as plt
import sys
import statistics
import glob

files = ["sample1.txt", "sample2.txt", "sample3.txt"]
# files = glob.glob("sample*")

def plot(file_name, offset):
    x_calibrations = []
    y_calibrations = []
    z_calibrations = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            x = float(line.split(",")[0].split(" ")[-1])
            y = float(line.split(",")[1].split(" ")[-1])
            z = float(line.split(",")[2].split(" ")[-1])
            x_calibrations.append(x)
            y_calibrations.append(y)
            z_calibrations.append(z)
    variance = statistics.variance(x_calibrations) * pow(10, 6)
    plt.scatter(offset, variance, label=file_name+"_x_variance")
    variance = statistics.variance(y_calibrations) * pow(10, 6)
    plt.scatter(offset+4, variance, label=file_name+"_y_variance")
    variance = statistics.variance(z_calibrations) * pow(10, 6)
    plt.scatter(offset+8, variance, label=file_name+"_z_variance")

counter = 0
for file in files:
    plot(file, counter)
    counter += 1
plt.xlabel("calibration vairance")
plt.ylabel("calibration values")
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()
