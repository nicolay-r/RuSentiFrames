# RuSentiFrames 1.0

This lexicon describes sentiments and connotations conveyed with a predicate in a verbal or nominal form.

## Statistics

| Lexical Unit Type | v-1.0 |
|-------------------|-------|
| Verbs             | 2794  |
| Nouns             | 822   |
| Phrases           | 2401  |
| Other             | 49    |
| Unique Entries    | 6036  |
| Total Entries     | 6412  |

| Polarity      | Polarity | v-1.0 |
|:--------------|----------|-------|
| A0→A1         | POS      | 2252  |
| A0→A1         | NEG      | 2802  |
| author→A0     | POS      | 1178  |
| author→A0     | NEG      | 1571  |
| author→A1     | POS      | 1429  |
| author→A1     | NEG      | 815   |

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
