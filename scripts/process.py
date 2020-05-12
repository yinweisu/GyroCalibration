#x calibration: 0.00625104736536741, y calibration: 0.00172870047390461, z calibration: 0.00461516436189413
import matplotlib.pyplot as plt
import sys

file_name_1 = sys.argv[1]
file_name_2 = sys.argv[2]

def plot(file_name, figure_num, calibration_num):
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
    if calibration_num == 1:
        plt.scatter([0 for i in range(len(x_calibrations))], x_calibrations, label=file_name+"_x")
    elif calibration_num == 2:
        plt.scatter([1 for i in range(len(x_calibrations))], y_calibrations, label=file_name+"_y")
    else:
        plt.scatter([2 for i in range(len(x_calibrations))], z_calibrations, label=file_name+"_z")


plot(file_name_1, 1, 1)
plot(file_name_2, 2, 1)
plot(file_name_1, 1, 2)
plot(file_name_2, 2, 2)
plot(file_name_1, 1, 3)
plot(file_name_2, 2, 3)
plt.xlabel("calibrations")
plt.ylabel("calibration values")
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()