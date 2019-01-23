---
layout: default
---

# Machine learners are only as good as their training data

## Module Info

**_Format:_** Programming lab

**_Area:_** Machine learning

**_Technical Content:_** Using an ML library to apply decision trees and support vector machines

**_Ethical Content:_** Responsible data curation, understanding impacts of ML-made decisions on real people

## Overview


## Requirements

A computing environment with this software:
- Python
- numpy
- pandas

## Instructor preparation

Assign this reading to students:
- [Pro Publica COMPAS article](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)
- [Pro Publica methodology](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm) (sections "How we acquired data" and "How we defined recidivism")
- [Meaning of "Misdemeanor" (vs "Felony")](https://en.wikipedia.org/wiki/Misdemeanor)

Prepare a csv file with columns for the full names, first names, and last names of your students.  See [data/students.csv](data/students.csv) for an example that you can overwrite.

Run the [preproc.py](preproc.py) script.  This chooses a random sample of subjects from the included compas dataset, one subject per student in your class.  It then replaces the original names of the sampled subjects with your students' names.  Finally, it produces the following files:

- [data/sample.csv](data/sample.csv): The data for sampled, renamed subjects.
- [data/sample_anonymized_unlabeled.csv](data/sample_anonymized_unlabeled.csv): The sample data with names and labels (i.e., whether the subject was a recidivist) removed.  The first column is an ID number used to identify datapoints in lieu of names.
- [data/assignments.csv](data/assignments.csv): Randomly assigns each student one anonymous, unlabeled datapoint for them to label.

Using your method of choice (e.g., google sheet), distribute the anonymous, unlabeled data to the students, and tell each of them the ID that they were assigned to label.  They should choose a label (recidivist vs not) using their best guess, based on the features of the anonymous subject they were assigned.  Collect all of their responses into a new csv file with the same format but labels filled in.  See [data/sample_anonymized_labeled.csv](data/sample_anonymized_labeled.csv) for an example that you can overwrite.

Run the script [postproc.py](postproc.py).  This adds a new column to sample.csv called "recidivist guess" and populates it with the students' guesses for the labels.  The resulting data is saved to the file [data/training_data.csv](data/training_data.csv).

## Programming lab activity

