# Infotflproject


## Installation
- Make sure to install python version _**3.6**_
- Make sure to install java SDK version _**8**_
    - earlier versions wont work and later versions require an additional command to start the server
- Download the Stanfort CoreNLP package from the url given below
    - We used version 3.9.2. More important is that the wrapper version matches with the CoreNLP version
    - https://stanfordnlp.github.io/CoreNLP/index.html
- Extract the CoreNLP from the zip and store folder in a place you can find
- Use pip to install the wrapper to the CoreNLP
    - `pip install stanfordcorenlp`
    - Make sure it's the same version as the CoreNLP
    - With `pipenv` installed you could also run `pipenv install`

## Start up 
- In the commandline go to the folder where you unpacked the CoreNLP
- Run the following command to start the CoreNLP
    - `java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000`
    - If you change the port number also change the port number in the code otherwise it won't work
- Run `main.py` to start the program
    - From the commandline `python main.py`
    - With pipenv `pipenv run python main.py`



## Download stanfort core nlp package
https://stanfordnlp.github.io/CoreNLP/index.html

## Link to the python wrapper repository

https://github.com/Lynten/stanford-corenlp

## Command to run core nlp serve

`java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000`
