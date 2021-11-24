# PoC for the Risteys pipeline

## Description

This repository is a proof-of-concept/demo of the refactored Risteys pipeline. The goal is to enable the following features:

- both FinnGen and FinRegistry data can be processed 
- the same analysis pipeline can be applied to both FinnGen and FinRegistry data
- more tests can be easily implemented 

The Risteys pipeline can be split into two pipelines: the **data pipeline** and the **analysis pipeline**. The data pipeline includes scripts for loading and preprocessing datasets. Project-specific scripts are usually required to load and preprocess the data, and therefore many of the scripts associated with the data pipeline are stored in `risteys_pipeline` subdirectories `finngen` and `finregistry`. The output data format of the two data pipelines should match. The analysis pipeline is the same for the two datasets and includes scripts such as `mortality_analysis.py` and `survival_analysis.py`. Project-specific analysis scripts can also be implemented and stored in the project subdirectories if needed.

Tests are stored in the `test` directory. Tests are used to validate data, assert the correctness or the analysis, detect bugs, and get confidence on the outputs. In Risteys, test cases might include e.g. verifying that the requirement for the minimum number of individuals is met or checking that the two data pipelines produce data in the same format.

Possible challenges include harmonizing the output of the data pipeline for the two datasets and accounting for the different computing environment requirements.

In this demo,  the lung.csv dataset from the `lifelines` Python package is used. The dataset can be downloaded here: https://github.com/CamDavidsonPilon/lifelines/blob/master/lifelines/datasets/lung.csv

## Setup

The requirements are listed in the `environment.yml`. The required Python packages can be installed as follows.

```
conda env create -f environment.yml
conda activate risteys-pipeline-poc
```

## For developers

The `config.py` script is used for storing paths to the data.

The `risteys_pipeline` is a local Python package. Functions can be imported and used as follows.

```
from risteys_pipeline.mortality_analysis import mortality_analysis
from risteys_pipeline.finngen.load_data import load_finngen_data
```

Tests are implemented using `pytest`. The tests can be run from the project root as follows.

```
python -m pytest test
```
