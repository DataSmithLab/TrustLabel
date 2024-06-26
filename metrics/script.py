import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def generate_histogram(column, repo):
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.figure(figsize=(10, 2))

    # file_path = f"{repo}_prototype.csv"
    # if label == "component":
    file_path = f"{repo}_both_prototypes_v2.csv"

    df = pd.read_csv(file_path, encoding='gbk')

    df_filtered = df[df[column] != 'N/A'].dropna(subset=[column])

    bin_boundaries = np.linspace(0, 100, num=11)

    hist_values, bin_edges = np.histogram(df_filtered[column], bins=bin_boundaries)

    # Assumes the repo metric value is the last row
    aim = df_filtered.tail(1)[column].values[0]
    if aim is None:
        aim = 0.01

    for i, (start, end) in enumerate(zip(bin_boundaries, bin_boundaries[1:])):
        # print(start, end)
        width = end - start
        # print(hist_values)
        height = hist_values[i] / 5
        if start <= aim and end > aim:
            rect = plt.Rectangle((start, 0), width, height, color='blue', fill=True, alpha=0.7)
        else:
            rect = plt.Rectangle((start, 0), width, height, color='grey', fill=True, alpha=0.7)
        plt.gca().add_patch(rect)

    plt.ylim(0, 100)
    plt.xlim(0, 100)
    ax = plt.gca()
    ax.yaxis.set_visible(False)
    # ax.xaxis.set_visible(False)
    ax.tick_params(labelbottom=False)   
    ax.set_xlabel("Trustworthiness $\longrightarrow$", fontsize=14)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    save_path = f"./images/{repo}/{column}.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight', pad_inches=0.1)
    plt.close()


### Trustee label
histograms = ['maintenance', 'contribution', 'popularity', 'code_quality']

# roughViz = [23.9, 18.0, 36.8, 18.0]
for index, column in enumerate(histograms):
    generate_histogram(column, 'roughViz')

# twopasswords = [15.8, 0.0, 7.5, 3.9]
for index, column in enumerate(histograms):
    generate_histogram(column, 'twopasswords')

# voice_listener = [11.1, 7.6, 8.8, 10.7]
for index, column in enumerate(histograms):
    generate_histogram(column, 'voice_listener')


### Component label
histograms = ['community_activity_and_integrity_component', 'maintenance_and_goodwill_component', 'code_quality_component']

# roughViz = [20.025, 24.825, 12.35]
for index, column in enumerate(histograms):
    generate_histogram(column, 'roughViz')

# twopasswords = [2.467, 15.775, 3.0]
for index, column in enumerate(histograms):
    generate_histogram(column, 'twopasswords')

# voice_listener = [8.267, 11.075, 9.7]
for index, column in enumerate(histograms):
    generate_histogram(column, 'voice_listener')
