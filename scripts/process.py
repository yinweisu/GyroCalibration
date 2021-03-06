#x calibration: 0.00625104736536741, y calibration: 0.00172870047390461, z calibration: 0.00461516436189413
import matplotlib.pyplot as plt
import sys
import statistics
import glob

files = glob.glob("iphone*")

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
    plt.scatter([offset for i in range(len(x_calibrations))], x_calibrations, label=file_name)
    plt.scatter([offset+4 for i in range(len(y_calibrations))], y_calibrations, label=file_name)
    plt.scatter([offset+8 for i in range(len(z_calibrations))], z_calibrations, label=file_name)

counter = 0
for file in files:
    plot(file, counter)
    counter += 1
plt.xlabel("calibration vairance")
plt.ylabel("calibration values")
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()
