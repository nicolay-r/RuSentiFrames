# RuSentiFrames 2.0

This lexicon describes sentiments and connotations conveyed with a predicate in a verbal or nominal form.
Checkout reference section for details in related paper.

## Structure

The structure of the frames includes:

1. **Role designation:** A0 is an argument exhibiting features of a Prototypical Agent, and
A1 is a Theme (as in PropBank)

2. **Dimentions:**
* the attitude of the author of the text
towards mentioned participants;
*  positive or negative sentiment between
participants;
* positive or negative effects to participants;
* positive or negative mental states of
participants related to the described
situation.

## Statistics

> To be added.

## Format Description

The lexicon presented in JSON format.

Below is an example of the frame ```выйграть```:
```
"0_4": {
    "title": [
        "выиграть",
        "получить приз" ],
    "variants": [
        "выиграть",
        "выигрывать" ],
    "comment": "comment",
    "roles": {
        "a0": "победитель",
        "a1": "побежденный",
        "a2": "приз",
        "a3": "область, сфера, в которой одержана победа" },
    "frames": {
        "polarity": [
            [ "a1", "a0", "neg", 1.0 ],
            [ "a0", "a2", "pos", 1.0 ],
            [ "a1", "a2", "neg", 0.7 ],
            [ "a0", "a3", "pos", 1.0 ],
            [ "a1", "a3", "pos", 1.0 ] ],
        "value": [
            [ "a0", "a2", 1.0 ],
            [ "a1", "a2", 1.0 ] ],
        "effect": [
            [ "a0", "+", 1.0 ],
            [ "a1", "-", 1.0 ] ],
        "state": [
            [ "a0", "pos", 1.0 ],
            [ "a1", "neg", 1.0 ] ]
    }
}
```

Where keys denotes as follows:

```title``` -- list of possible frame titles.

```variants``` -- list of possible variants appeared in text.

```roles``` -- is a dictonary of participants (keys) with the related description.

```frames``` -- is a dictionary of parameters, which describes a frame in following directions:
* ````polarity```` -- positive or negative sentiment between
participants;
* ````value```` -- the attitude of the author of the text
towards mentioned participants;
* ````effect```` -- positive or negative effects to participants;
* ````state```` -- positive or negative mental states of
participants related to the described
situation.

## Collection Reader ![](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

Folder `reader` contains a collection reader (source file parsers), written in Python-3.6.

Please refer to [read.py](read.py), as it provides an example of how this collection could be parsed/readed. 

## Prior Releases

[RuSentiFrames-1.0](https://github.com/nicolay-r/RuSentiFrames/tree/v1.0)

## References

```
@article{loukachevitch2020sentiment,
  title={Sentiment Frames for Attitude Extraction in Russian},
  author={Loukachevitch, Natalia and Rusnachenko, Nicolay},
  booktitle={Proceedings of International Conference on 
             Computational Linguistics and Intellectual 
             Technologies Dialogue-2020},
  year={2019}
}
```
