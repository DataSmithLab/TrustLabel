import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.figure(figsize=(10, 4))

file_path = "prototype_normalized_metrics.csv"
df = pd.read_csv(file_path, encoding='gbk')


def generate_histogram(column, value):
    df_filtered = df[df[column] != 'N/A'].dropna(subset=[column])

    bin_boundaries = np.linspace(0, 10, num=11)

    hist_values, bin_edges = np.histogram(df_filtered[column], bins=bin_boundaries)

    aim = value

    if aim is None:
        aim = 0

    for i, (start, end) in enumerate(zip(bin_boundaries, bin_boundaries[1:])):
        width = end - start
        height = hist_values[i]
        if start < aim <= end:
            rect = plt.Rectangle((start, 0), width, height, color='lightcoral', fill=True, alpha=0.7)
        else:
            rect = plt.Rectangle((start, 0), width, height, color='lightblue', fill=True, alpha=0.7)
        plt.gca().add_patch(rect)
        plt.ylim(0, max(hist_values) * 1.15)

    plt.xlim(0, 10)
    plt.gca().yaxis.set_visible(False)
    plt.gca().xaxis.set_visible(False)
    
    save_path = f"./markdown/images/nithincvpoyyil_voice_listener_v2/{column}.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight', pad_inches=0.5)
    plt.close()


metrics = ['maintenance', 'contribution', 'popularity', 'code_quality', 'issues_maintenance', 'code_maintenance', 'community_documentation', 'maintainer_history', 'contributor_participation', 'code_contribution', 'contributor_growth', 'stars_and_watches', 'forks', 'project_maturity', 'downstream_dependents', 'dependencies_health', 'testing_quality', 'review_coverage', 'community_activity_and_integrity']
roughViz = [2.782916666666667,0.1555555555555555,0.3637499999999999,2.2522222222222217,2.0,5.0,1.7966666666666669,2.335,0.3666666666666667,0.06,0.04,0.15,0.03,1.275,None,6.646666666666666,0.02,0.65,0.11]
twopasswords = [0.67,None,0.14125,2.2222222222222223,None,None,1.6900000000000002,0.99,None,None,None,None,None,0.565,None,6.666666666666667,None,0.52,0.11]
voicelistener = [0.8395833333333333,0.7055555555555556,0.51875,2.0477777777777777,None,None,1.5333333333333334,1.825,2.106666666666667,0.01,None,None,None,2.075,None,6.1433333333333335,None,0.52,0.11]

for index, metric in enumerate(metrics):
    generate_histogram(metric, voicelistener[index])
