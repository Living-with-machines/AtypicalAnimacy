<div align="center">
    <h1>Living Machines:<br>
      A Study of Atypical Animacy</h1>
</div>
 
<p align="center">
    <a href="https://github.com/Living-with-machines/AtypicalAnimacy/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg">
    </a>
    <br/>
</p>

This repository provides underlying code and materials for the paper 'Living Machines: A Study of Atypical Animacy' (COLING2020).

## Table of contents

* [Installation](https://github.com/Living-with-machines/AtypicalAnimacy/#installation)
* [Directory structure](https://github.com/Living-with-machines/AtypicalAnimacy/#directory-structure)
* [Description of the codes](https://github.com/Living-with-machines/AtypicalAnimacy/#description-of-the-codes)
* [Datasets and resources](https://github.com/Living-with-machines/AtypicalAnimacy/#datasets-and-resources)
* [Evaluation results](https://github.com/Living-with-machines/AtypicalAnimacy/#evaluation-results)
* [Citation](https://github.com/Living-with-machines/AtypicalAnimacy/#citation)
* [Acknowledgements](https://github.com/Living-with-machines/AtypicalAnimacy/#acknowledgements)
* [License](https://github.com/Living-with-machines/AtypicalAnimacy/#license)

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

:warning: We have noticed that, in some machines, `fasttext` installation crashes. In this case, installing it at the end via `conda` seems to work: `conda install -c conda-forge fasttext`.

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

## Datasets and resources

Run `code/setup.ipynb` to download and prepare the data and resources used in the experiments.

#### _Stories_ dataset
Dataset described in Tables 1 and 3 of the paper, generated from the animacy dataset annotated in:
  > Jahan, Labiba, Geeticka Chauhan, and Mark Finlayson. "A new approach to animacy detection." In Proceedings of the 27th International Conference on Computational Linguistics, pp. 1-12. 2018.

Run `code/setup.ipynb` to download it and convert it to the format used in our experiments.
  
#### _19thC Machines_ dataset
Atypical animacy dataset, described in Tables 2 and 3 of the paper, annotated by us, based on nineteenth-century sentences in English extracted from an [open dataset of nineteenth-century books digitized by the British Library](https://data.bl.uk/digbks/db14.html). Run `code/setup.ipynb` to download it and convert it to the format used in our experiments.

#### Language models
Nineteenth-century BERT and Word2vec English models trained on the [_19thC BL Books_](https://data.bl.uk/digbks/db14.html) dataset can be downloaded from [Zenodo](https://zenodo.org/record/4782245). For more information, you can read [this paper](https://arxiv.org/abs/2105.11321) and look at [its Github repository](https://github.com/Living-with-machines/histLM).

If you use these models, please cite:
```
Hosseini, Kasra, Kaspar Beelen, Giovanni Colavizza, and Mariona Coll Ardanuy. "Neural Language Models for Nineteenth-Century English." arXiv preprint arXiv:2105.11321 (2021).
```

```
@article{hosseini2021neural,
  title={Neural Language Models for Nineteenth-Century English},
  author={Hosseini, Kasra and Beelen, Kaspar and Colavizza, Giovanni and Coll Ardanuy, Mariona},
  journal={arXiv preprint arXiv:2105.11321},
  year={2021}
}
```

## Evaluation results

The evaluation results of our experiments (partially reported in Table 5 of the paper) can be found [in this file](https://github.com/Living-with-machines/AtypicalAnimacy/blob/main/evaluation.md).

## Citation

```
Mariona Coll Ardanuy, Federico Nanni, Kaspar Beelen, Kasra Hosseini, Ruth Ahnert, Jon Lawrence, Katherine McDonough, Giorgia Tolfo, Daniel CS Wilson and Barbara McGillivray. "Living Machines: A study of atypical animacy." In Proceedings of the 28th International Conference on Computational Linguistics (COLING), pp. 4534--4545. 2020.
```

```
@inproceedings{coll-ardanuy-etal-2020-living,
    title = "Living Machines: A study of atypical animacy",
    author = "Coll Ardanuy, Mariona  and
      Nanni, Federico  and
      Beelen, Kaspar  and
      Hosseini, Kasra  and
      Ahnert, Ruth  and
      Lawrence, Jon  and
      McDonough, Katherine  and
      Tolfo, Giorgia  and
      Wilson, Daniel CS  and
      McGillivray, Barbara",
    booktitle = "Proceedings of the 28th International Conference on Computational Linguistics (COLING)",
    year = "2020",
    address = "Barcelona (Online)",
    publisher = "International Committee on Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.coling-main.400",
    pages = "4534--4545",
}
```

## Acknowledgements

Work for this paper was produced as part of [Living with Machines](http://livingwithmachines.ac.uk/). This project, funded by the UK Research and Innovation (UKRI) Strategic Priority Fund, is a multidisciplinary collaboration delivered by the Arts and Humanities Research Council (AHRC), with The Alan Turing Institute, the British Library and the Universities of Cambridge, East Anglia, Exeter, and Queen Mary University of London. This work was also supported by The Alan Turing Institute under the EPSRC grant EP/N510129/1.

## License

- The source codes are licensed under MIT License.
- Copyright (c) 2020 The Alan Turing Institute, British Library Board, Queen Mary University of London, University of Exeter, University of East Anglia and University of Cambridge.
- The [atypical animacy dataset](https://bl.iro.bl.uk/work/ns/323177af-6081-4e93-8aaf-7932ca4a390a) hosted on the British Library Research Repository is licensed under CC0 1.0 Universal Public Domain.
