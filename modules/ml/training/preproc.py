import numpy as np
import pandas as pd

students = pd.read_csv("data/students.csv")
compas = pd.read_csv("data/compas-scores-two-years-violent.csv", index_col=0)

# filter out bad data as per Pro Publica's methodology
keep = \
    (compas["days_b_screening_arrest"] <= +30) & \
    (compas["days_b_screening_arrest"] >= -30) & \
    (compas["is_recid"] != -1) & \
    (compas["c_charge_degree"] != "O") & \
    (compas["score_text"] != "N/A")
compas = compas.loc[keep,:]

# choose a random subset of compas subjects, one per student
sampler = np.random.choice(compas.shape[0], size=students.shape[0], replace=False)

# replace compas subset with student names
sample = compas.iloc[sampler,:].copy()
sample[["name","first","last"]] = students.values # values to ignore different pandas indexes

# select columns to use for training data and assign more descriptive names
columns = {
    "name": "full name",
    "first": "first name",
    "last": "last name",
    "compas_screening_date": "risk assessment date",
    "sex": "gender",
    "dob": "date of birth",
    "age": "age",
    "race": "race",
    "juv_fel_count": "number of juvenile felonies",
    "juv_misd_count": "number of juvenile misdemeanors",
    "juv_other_count": "number of other juvenile crimes",
    "priors_count": "number of prior convictions",
    "c_charge_degree": "degree of charge (felony/misdemeanor)",
    # "c_charge_desc": "description of charge",
    "is_recid": "recidivist",
    # "r_charge_degree": "degree of recidivism charge",
    # "r_charge_desc": "description of recidivism charge",
    # "is_violent_recid": "violent recidivist",
    "decile_score.1": "recidivism risk score",
    # "v_decile_score": "violent recidivism risk score",
}
sample = sample[columns.keys()]
sample = sample.rename(columns = columns)
sample.to_csv("data/sample.csv")

# Prepare anonymized, unlabeled data for students to label
sample_anonymous_unlabeled = sample.drop(columns=[
    "full name", "first name", "last name",
    "recidivism risk score"])
sample_anonymous_unlabeled["recidivist"] = -1
sample_anonymous_unlabeled.to_csv("data/sample_anonymous_unlabeled.csv", index_label="id")

# Assign each student one anonymized subject to label
assignments = students.copy()
assignments["ID to label"] = np.random.permutation(sample.index.values)
assignments.to_csv("data/assignments.csv")

