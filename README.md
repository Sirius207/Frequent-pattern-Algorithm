# Frequent-pattern Algorithm

Algorithms for Frequent-pattern Mining

## Usage

### Find frequent pattern
```
python main.py --input data/sample.txt --output output.csv --minsup '2' --algorithm fp
```
- input: input data file name
- output: output file name
- minsup: minimum support
- algorithm: frequent pattern algorithm(fp or ap)


### Find association rules
```
python rules.py --minconfidence 0.2 --input patterns.csv --output rules.csv
```
- minconfidence: minimum confidence
- input: input data file name
- output: output file name


## Implementation
- [Apriori Algorithm](https://en.wikipedia.org/wiki/Apriori_algorithm)
- [FP Growth](https://en.wikibooks.org/wiki/Data_Mining_Algorithms_In_R/Frequent_Pattern_Mining/The_FP-Growth_Algorithm)

## Dataset
- [Kaggle: Random Shopping cart](https://www.kaggle.com/fanatiks/shopping-cart)
    - v1: original data
    - v2: [updated] filter duplicated items of each transaction
- IBM Quest Synthetic Data Generator

## Report
