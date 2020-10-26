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

## Installation

* Refer to [Anaconda website and follow the instructions](https://docs.anaconda.com/anaconda/install/).

* Create a new environment for DeezyMatch

```bash
conda create -n py37animacy python=3.7
```

* Activate the environment:

```bash
conda activate py37animacy
```

* Allow the newly created `py37animacy` environment to show up in the notebooks:

```bash
python -m ipykernel install --user --name py37animacy --display-name "Python (py37animacy)"
```


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

## Citation

## Get in touch

## Acknowledgements

Work for this paper was produced as part of [Living with Machines](http://livingwithmachines.ac.uk/). This project, funded by the UK Research and Innovation (UKRI) Strategic Priority Fund, is a multidisciplinary collaboration delivered by the Arts and Humanities Research Council (AHRC), with The Alan Turing Institute, the British Library and the Universities of Cambridge, East Anglia, Exeter, and Queen Mary University of London. This work was also supported by The Alan Turing Institute under the EPSRC grant EP/N510129/1.

## License

- The source codes are licensed under MIT License Copyright (c) 2020 Living with Machines.
- The datasets hosted on [zenodo](xxxxxx) **TODO:FIX PATH** are licensed under CC-BY-4.0.
