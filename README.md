<div align="center">
    <h1>Living Machines:<br>
      A Study of Atypical Animacy</h1>
</div>
 
<p align="center">
    <a href="https://github.com/Living-with-machines/DeezyMatch/blob/master/LICENSE">
        <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg">
    </a>
    <br/>
</p>

This repository provides underlying code and materials for the paper 'Living Machines: A Study of Atypical Animacy' (COLING2020).

## Table of contents

* [Installation](https://github.com/Living-with-machines/AtypicalAnimacy/tree/master#installation)
* [Directory structure](https://github.com/Living-with-machines/AtypicalAnimacy/tree/master#directory-structure)
* [Description of the codes](https://github.com/Living-with-machines/AtypicalAnimacy/tree/master#description-of-the-codes)
* [Description of the datasets](https://github.com/Living-with-machines/AtypicalAnimacy/tree/master#description-of-the-datasets)
* [Evaluation results](https://github.com/Living-with-machines/AtypicalAnimacy/tree/master#evaluation-results)
* [Citation](https://github.com/Living-with-machines/AtypicalAnimacy/tree/master#citation)
* [Acknowledgements](https://github.com/Living-with-machines/AtypicalAnimacy/tree/master#acknowledgements)
* [License](https://github.com/Living-with-machines/AtypicalAnimacy/tree/master#license)

## Installation

* Refer to [Anaconda website and follow the instructions](https://docs.anaconda.com/anaconda/install/).

* Create a new environment:

```bash
conda create -n py37animacy python=3.7
```

* Activate the environment:

```bash
conda activate py37animacy
```

* Clone AtypicalAnimacy repository:

```bash
git clone https://github.com/Living-with-machines/AtypicalAnimacy.git
```

* Install the requirements:

```bash
cd /path/to/my/AtypicalAnimacy
pip install -r requirements.txt
```

* Allow the newly created `py37animacy` environment to show up in the notebooks:

```bash
python -m ipykernel install --user --name py37animacy --display-name "Python (py37animacy)"
```

* Run the `code/setup.ipynb` notebook, one cell at a time.


## Directory structure

In our code, we assume the following directory structure:

```bash
AtypicalAnimacy/
├── code/
├── data/
├── experiments/
├── models/
│   ├── classifiers/
│   └── language_models/
│       ├── bert_models/
│       └── fastai/
└── resources/
```

## Description of the codes

### Data processing
To get the data to the right format, run these notebooks in the following order:
1. `code/process_stories_dataset.ipynb`
2. `code/process_machines19thC_dataset.ipynb`

### Masking approach

To apply the masking approach, run the following notebook:
* `code/masking_approach.ipynb`

### Classification approach

To train the classifiers, run the following notebooks:
* `code/train_bert_classifier.ipynb`
* `code/train_svm_classifiers.ipynb`

To apply the classifiers on new data, run the following notebook:
* `code/classification_approach.ipynb`

### Sequential tagging approach
To train and evaluate the LSTM classifier, run the following notebook:
* `code/train_LSTM_seq_classifiers.ipynb`

## Description of the datasets

Experiments are performed on two different datasets:
* _Stories_ dataset: generated from the animacy dataset created in 
  > Jahan, Labiba, Geeticka Chauhan, and Mark Finlayson. "A new approach to animacy detection." In Proceedings of the 27th International Conference on Computational Linguistics, pp. 1-12. 2018.
  Run `code/setup.ipynb` to download it and convert it to the format used in our experiments.
* _19thC Machines_ dataset: Atypical animacy dataset, annotated by us, based on nineteenth-century sentences in English extracted from an open dataset of nineteenth-century books digitized by the British Library (available [here](https://data.bl.uk/digbks/db14.html), DOI [10.21250/db14](https://doi.org/10.21250/db14), British Library Labs, 2014). This dataset contains 598 sentences containing mentions of machines. Each sentence has been annotated according to the animacy and humanness of the machine in the sentence. You can download the annotated dataset used in our experiments [here](https://bl.iro.bl.uk/work/ns/323177af-6081-4e93-8aaf-7932ca4a390a).

  A publication containing the guidelines of the dataset is **coming soon**.

## Evaluation results

[In this file](https://github.com/Living-with-machines/AtypicalAnimacy/blob/develop/evaluation.md) you can find the evaluation results of our experiments (partially in Table 5 of the paper).

## Citation

```
Mariona Coll Ardanuy, Federico Nanni, Kaspar Beelen, Kasra Hosseini, Ruth Ahnert, J. Lawrence, Katherine McDonough, Giorgia Tolfo, Daniel C. Wilson and Barbara McGillivray. "Living Machines: A study of atypical animacy." In Proceedings of the 28th International Conference on
Computational Linguistics (COLING2020).
```

```
@inproceedings{collardanuy2020living,
    title = "Living Machines: A study of atypical animacy",
    author = "Mariona Coll Ardanuy and Federico Nanni and Kaspar Beelen and Kasra Hosseini and Ruth Ahnert and Jon Lawrence and Katherine McDonough and Giorgia Tolfo and Daniel CS Wilson and Barbara McGillivray",
    booktitle = "Proceedings of the 28th International Conference on Computational Linguistics (COLING 2020)",
    year = "2020",
    publisher = "Association for Computational Linguistics",
}
```

## Acknowledgements

Work for this paper was produced as part of [Living with Machines](http://livingwithmachines.ac.uk/). This project, funded by the UK Research and Innovation (UKRI) Strategic Priority Fund, is a multidisciplinary collaboration delivered by the Arts and Humanities Research Council (AHRC), with The Alan Turing Institute, the British Library and the Universities of Cambridge, East Anglia, Exeter, and Queen Mary University of London. This work was also supported by The Alan Turing Institute under the EPSRC grant EP/N510129/1.

## License

- The source codes are licensed under MIT License Copyright (c) 2020 Living with Machines.
- The datasets hosted on [zenodo](xxxxxx) **TODO:FIX PATH** are licensed under CC-BY-4.0.
