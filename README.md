# named-entities-recognition-italiano

Script python per estrarre entità nominate da testi in italiano

# Install

## Reqirements

- pip 23 or later
- python 3.x

## Install instructions

Create a Virtual Environment

```shell
python3 -m env venv
```

Activate it

```shell
source env/bin/activate
```

Install dependencies with pip:

```shell
pip install -r requirements.txt
```

Be aware that the large language model is about 500mb.

# How to use

activate the virtual environment.

Call the script passing three parameters:

1. the input csv filename
2. the header of the column containing the text
3. the output csv filename
4. the model that sould be used: "sm" (small) or "lg" (large)

example:

```shell
python3 input.csv text_field output.csv lg
```
