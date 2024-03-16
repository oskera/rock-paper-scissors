# Specifications

## What does it do?

The project is a [rock paper scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors) AI. It plays the game against a human opponent and adapts its strategy against the opponent in real time based on the previous plays from the opponent.

## Algorithm

The algorithm used in the project is [Markov chains](https://en.wikipedia.org/wiki/Markov_chain).

## Time complexity and memory

The probability tables used by the algorithm are to be stored in either a hash table or two dimensional array (matrix). If stored in a hash table, the values can be updated and read in linear time O(1). If stored in a matrix, the said matrix would have 3 columns (one for each rock, paper and scissors) and n rows, where n=3^m (or 9^m, if also considering the outcomes of the previous games) and m is the amount of games the algorithm considers for deciding the probabilities of next input.

## Language

The programming language used in the project is Python. I can peer review projects written in either Python or Java.

## Other stuff

I'm a student in Computer Science Bachelor program (Tietojenkäsittelytieteen kandidaatti (TKT)). The project was inspired by this [paper](https://arxiv.org/pdf/2003.06769.pdf). This and everything else related to the document will be written in English, but I can peer review projects written in either English or Finnish.
