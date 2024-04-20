# Weekly Report 5

## Hours spent

14 hours in total. Breakdown below:

| Amount | Description                                     |
| ------ | ----------------------------------------------- |
| 3      | Reading about tries                             |
| 3      | Experimenting tries                             |
| 5      | Writing code                                    |
| 2      | Making peer review                              |
| 1      | Writing documentation                           |

## What has been achieved this week?

I familiarized myself with tries. I wrote some experimental code (not submitted on github) implementing tries. I wrote the code for single n-AI, that uses Markov chains to play rock-paper-scissors.

## What have I learned?

I learned that you can infact use lists to make this project work. My current single AI uses a string to store previous actions made by the human player, and counts the occurences of certain sequences in O(n) time. While this is slower than using a trie, it is more memory efficient and makes for a more simple code structure in my opinion. However, I will update my code to use a trie next week, since I feel the point of this project is to make time efficient code.

## Problems encountered

I've struggled managing time to work on this project. I also struggled to figure out to implement tries without making the data structure convoluted. I agree a prefix tree is a good way to store a data, but I was struggling with how to make them useful. My original idea was to make a single trie in the Game-class that makes a new "word" for every sequence and sub sequence. For example if player played RPPS the tree should have following words: RPPS, PPS, PS, S. In the next week's version I'm planning to make a more simple structure, where n-AI (AI, with memory of n length) has a trie that has n-length words and their occurences. For example 2-AI would have following words in its trie: RR, RP, RS, PR, PP, PS, SR, SP, SS. This however would mean that same data is stored multiple times.

## What's next?

Multi-AI, data structure rework, UI
