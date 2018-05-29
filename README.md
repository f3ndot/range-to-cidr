# range-to-cidr
A stupid simple Python script to turn CSV of IP ranges to CIDR blocks in STDOUT

## Usage

Expects a headless CSV file with the first column to be the start IP in range, and second column to be end IP in range. Nirsoft's country IP lists are in this format: https://www.nirsoft.net/countryip/

```bash
pip install --user pipenv
pipenv run python range-to-cidr.py PATH_TO_CSV
```

## Example

```bash
$ echo "23.16.0.0,23.17.255.255," > test.csv
$ echo "23.29.192.0,23.29.223.255," > test.csv
$ echo "23.83.208.0,23.83.223.255," > test.csv
$ echo "23.83.224.0,23.83.255.255," > test.csv
$ echo "23.91.128.0,23.91.159.255," > test.csv
$ echo "23.91.160.0,23.91.191.255," > test.csv
$ pipenv run python range-to-cidr.py tests.csv
23.16.0.0/15
23.29.192.0/19
23.83.208.0/20
23.83.224.0/19
23.91.128.0/19
23.91.160.0/19
```
