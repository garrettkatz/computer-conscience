---
layout: default
---

# Machine learners are only as good as their training data

This readme and supporting files can also be viewed directly in the github repository [here](https://github.com/garrettkatz/computer-conscience/tree/master/modules/ml/training). 

## Module Info

**_Format:_** Programming lab

**_Area:_** Machine learning

**_Technical Content:_** Basic data wrangling, training/testing, and regularization when applying an ML library to real-world data

**_Ethical Content:_** Understanding impacts of ML-made decisions, and manually labeled ML data, on real people.

## Overview

In this programming lab, students will use decision trees to predict recidivism, with a twist: their own names will appear in the training data, and they will also be involved in manually labeling the data as best they can before using the ground truth.  The lab uses the [compas dataset](https://github.com/propublica/compas-analysis) (the data is already copied in this repository for your convenience).  Leading up to the lab, students will read about the problem and the dataset, and they will participate in the manual data labeling.

## Requirements

A computing environment with this software:
- python
- numpy
- pandas
- scikit-learn
- ipython

## Instructor preparation

Assign this reading to students ahead of the lab:
- [Pro Publica COMPAS article](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)
- [Pro Publica methodology](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm) (sections "How we acquired data" and "How we defined recidivism")
- [Meaning of "Misdemeanor" (vs "Felony")](https://en.wikipedia.org/wiki/Misdemeanor)

Prepare a csv file with columns for the full names, first names, and last names of your students.  See [data/students.csv](https://github.com/garrettkatz/computer-conscience/blob/master/modules/ml/training/data/students.csv) for an example that you can overwrite.

Run the [preproc.py](https://github.com/garrettkatz/computer-conscience/blob/master/modules/ml/training/preproc.py) script.  This chooses a random sample of subjects from the included compas dataset, one subject per student in your class.  It then replaces the original names of the sampled subjects with your students' names.  Finally, it produces the following files:

- [data/sample.csv](https://github.com/garrettkatz/computer-conscience/blob/master/modules/ml/training/data/sample.csv): The data for sampled, renamed subjects.
- [data/sample_anonymized_unlabeled.csv](https://github.com/garrettkatz/computer-conscience/blob/master/modules/ml/training/data/sample_anonymous_unlabeled.csv): The sample data after removing names and labels (i.e., whether the subject was a recidivist).  The first column is an ID number used to identify datapoints in lieu of student names.
- [data/assignments.csv](https://github.com/garrettkatz/computer-conscience/blob/master/modules/ml/training/data/assignments.csv): Randomly assigns each student one anonymous, unlabeled datapoint for them to label.

Using your method of choice (e.g., google sheet), distribute the anonymous, unlabeled data to the students, and tell each of them the ID that they were assigned to label.  They should choose a label (recidivist vs not) using their best guess, based on the features of the anonymous subject they were assigned (age, number of prior convictions, etc.).  Collect all of their responses into a new csv file with the same format but labels filled in.  See [data/sample_anonymous_labeled.csv](https://github.com/garrettkatz/computer-conscience/blob/master/modules/ml/training/data/sample_anonymous_labeled.csv) for an example that you can overwrite.

Run the script [postproc.py](https://github.com/garrettkatz/computer-conscience/blob/master/modules/ml/training/postproc.py).  This adds a new column to sample.csv called "recidivist guess" and populates it with the students' guesses for the labels.  The resulting data is saved to the file [data/training_data.csv](https://github.com/garrettkatz/computer-conscience/blob/master/modules/ml/training/data/training_data.csv).

## Lab activity

The ipython notebook [lab.ipynb](https://github.com/garrettkatz/computer-conscience/blob/master/modules/ml/training/lab.ipynb) contains a number of exercises of increasing complexity in which students wrangle the training data and then train a decision tree classifier on it.  Each cell has a comment with instructions followed by a code solution.  Partially or completely erase the code as appropriate for your students' background.  Then distribute your version of the notebook during the programming lab session.

## Debrief

After the lab, you might consider soliciting a discussion and/or written response from the students, in which they reflect on their experience and thoughts while they worked with this data.

