# **Question-Generator-API** 

This project is a modification of **Sequence-to-Sequence Learning for Indonesian Automatic Question Generator (AQG)** (go to https://github.com/FerdiantJoshua/question-generator) so it generate question from a predetermined answers and have an API endpoint to generate question and answer grading. 
This project is a part of Knowledge Self-Evaluation System with Automatic Factoid Question Generator.
To know more about overall system : https://github.com/kariswr/Knowledge-Self-Evaluation-System.git

## How to Use

### API

To run the API, use `python src/api/api_endpoint.py` in the repository folder.

The API will run at http://localhost:5000.\
To Generate Question send a post request to http://127.0.0.1:5000/get-question with body as follows:

```
{
    "paragraph": "Dummy paragraph.",
    "answer": [["dummy", "answer1"], ["dummy","answer2"], ["last", "dummy", "answer"]]
}
```
To grade answer send a post request to  http://127.0.0.1:5000/get-score with body as follows:

```
{
    "input": "Dummy user input",
    "ground_truth": "Dummy correct answer",
    "case_sensitive": true,
    "character_based": false,
    "threshold": 85
}
```

