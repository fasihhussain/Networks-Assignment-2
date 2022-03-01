import numpy as np
import matplotlib.pyplot as plt

from ER import ErdosRenyi

CONFIGURATIONS = [(1000, 0.01)]
TRIALS = 30

for n, p in CONFIGURATIONS:
    s_average_clustering_coefficient = 0
    s_average_path_length = 0
    degrees = []

    trial = 0
    while trial < TRIALS:
        try:
            G = ErdosRenyi(n, p)

            s_average_path_length += G.average_path_length()
            s_average_clustering_coefficient += G.average_clustering_coefficient()
            degrees.extend(G.degrees())

            trial += 1
        except:
            pass

    s_average_clustering_coefficient /= TRIALS
    s_average_path_length /= TRIALS

    prediction_average_path_lenght = np.log(n) / np.log((n - 1) * p)

    print(
        f"Average Clustering Coefficient (prediction = {p}): {round(s_average_clustering_coefficient, 4)}"
    )
    print(
        f"Average Path Length (prediction = {round(prediction_average_path_lenght, 4)}): {s_average_path_length}"
    )

    cnts, bins = np.histogram(degrees, bins="auto")
    cnts = list(map(lambda x: x / TRIALS, cnts))

    plt.bar(bins[:-1] + np.diff(bins) / 2, cnts, np.diff(bins))
    plt.title("Degree Distribution")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.axvline(
        x=(n - 1) * p, linewidth=2, color="r", linestyle="--", label="Predicted Mean"
    )
    plt.legend()
    plt.show()
    print("\n\n")
