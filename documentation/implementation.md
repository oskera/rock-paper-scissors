# Implementation

The project has been implemented as a Python project. It has been divided into two packages: logic and ui.

## Logic

Logic contains the classes and functions required to handle the rock-paper-scissors game, tries to store the actions and the AI itself. The AI uses Markov chains to calculate the most probable next action by the opponent and chooses a action to counter it. The AI consists of multiple AIs with fixed length. These Multi-AI chooses the action chosen by the AI that has the best winrate in recent history. The AIs use tries to find the opponent's most frequent action sequence.

## UI

UI is a very simple CLI.