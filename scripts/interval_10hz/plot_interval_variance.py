import matplotlib.pyplot as plt
import sys
import statistics
import glob
import numpy as np
import scipy.stats as stats
import seaborn as sns

arg = "iphone*"
if len(sys.argv) > 1:
    arg = sys.argv[1]
files = sorted(glob.glob(arg))
# sns.set_palette(sns.color_palette("hls", 20))

if len(sys.argv) > 1:
    arg = sys.argv[1]

# Need to create as global variable so our callback(on_plot_hover) can access
fig = plt.figure()
plot = fig.add_subplot(111)

def on_plot_hover(event):
    # Iterating over each data member plotted
    for curve in plot.get_lines():
        # Searching which data member corresponds to current mouse position
        if curve.contains(event)[0]:
            print("over %s" % files[int(curve.get_gid())])

def plotting(file_name, offset):
    intervals = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            intervals.append(float(line.strip()))
    intervals.sort()
    imean = np.mean(intervals)
    istd = np.std(intervals)
    pdf = stats.norm.pdf(intervals, imean, istd)
    plot.plot(intervals, pdf, '-o', label=file_name, gid=offset)

counter = 0
for file in files:
    plotting(file, counter)
    counter += 1

plt.xlabel("interval values")
plt.ylabel("pdf of normal distribution")
plt.legend()
plt.tight_layout()
fig.canvas.mpl_connect('motion_notify_event', on_plot_hover)
plt.show()
