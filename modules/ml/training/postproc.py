import numpy as np
import pandas as pd

# Compile complete training data including student labels
sample = pd.read_csv("data/sample.csv", index_col=0)
sample_anonymous_labeled = pd.read_csv("data/sample_anonymous_labeled.csv", index_col=0)
assignments = pd.read_csv("data/assignments.csv")

for a in assignments.index:
    idx = assignments.loc[a, "ID to label"]
    sample.loc[idx, "recidivist guess"] = sample_anonymous_labeled.loc[idx, "recidivist"]

sample.to_csv("data/training_data.csv")

