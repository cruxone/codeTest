# codeTest

This repository contains two challenges, both solved using python. 

### Challenge #1: Unique permutations of a string

This script will output all unique permutations of a string. Simply run the script: 
```
python permutation.py apples
```
The only dependencies this program has it that python must be installed. 

### Challenge #2: Log Redaction

I am including the sample logs that were provided by the challenge as a gzip file. 
To run, simply run as you would any python script: 
```
python redactor.py /some/directory/ log1.gz log2.gz
```
An audit.log file with be placed where the script was ran, and will show the name of logs redacted, and line counts. 
This has been tested using mutliple files that when gunzipped are roughly 730mb per file and takes about 42 seconds per file of that size, while consuming about 5 mb of memory. 

### TODO: write this in go and post some generic performance differences. 
