# Simple-NLP

This is a very simple micromaterial created for the Oxford [Summer of Hacks](https://summerofhacks.io) [Language Hack Day](https://summerofhacks.io/#2019:3-language-hackday).

The aim is to give learners practice in doing a very simple NLP task: turning
text into its corresponding Part of Speech (POS) tags. These are things like
NNS (singular noun) and JJS (comparative adjective).

## learning objectives

- what is a POS tag, and how to get them from text
- count the total different types of POS tags in a text
- count the frequency of different POS tags in a text
- calculate the most common n-grams of POS tags in a text

## The activity

One big skeleton function has already been written, along with the test for it.
So to complete the activity, just fill in the functions and run the tests.
If the test passes, you did it! If not, try to fix the function so the test passes.

to run the test:
`python -m unittest`

## Possible steps:

### 1) Find out about POS tags

Here is a [list](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) of POS tags used in both nltk and spacy,
two popular NLP libraries in python. And [this](https://www.sketchengine.eu/pos-tags/) is a good explanation of POS tags and
what they're used for (though sketch engine doesn't use the Penn Treebank set of POS tags).

The [Wikipedia page](https://en.wikipedia.org/wiki/Part_of_speech) has a much more in-depth discussion of these, if you're interested.

### 2) Find out about turning text into a list of POS tags

For our purposes, it doesn't matter whether you use the NLTK POS tagger ([example](https://medium.com/@gianpaul.r/tokenization-and-parts-of-speech-pos-tagging-in-pythons-nltk-library-2d30f70af13b)) or the Spacy POS tagger ([example](https://spacy.io/usage/linguistic-features))

Basically, read in your data source, load the models, and pass in the text into the appropriate function. It might be a good
idea to write the output to a file for later analysis so you don't have to repeat this step multiple times.

### 3) Find out about counting n-grams

An n-gram means a set of things that show up together, with the "n" part meaning the number of things. For example, if we're
looking at POS tags, a 2-gram that shows up a lot might be "IN, DET" ("in a"), and a 3-gram that shows up a lot might be
"DT NNS IN" ("the NOUN of"). For a more detailed discussion, see the [Wikipedia](https://en.wikipedia.org/wiki/N-gram) page.

Follow the steps from #2, and see which 2-grams and 3-grams are the most frequent. If you want to use your own data source
(perhaps a web page or document from the file system), possibly even look for 4-grams or 5-grams.
