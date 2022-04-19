
from dataclasses import replace


class Players():
    def winner(self, dictionary):
        jumpFirstIteration = True
        winners = [""]
        for dictionaryKey in dictionary:
            if jumpFirstIteration == True:
                winners[0] = dictionaryKey
                jumpFirstIteration = False
            if dictionary[winners[0]] < dictionary[dictionaryKey]:
                winners[0] = dictionaryKey
        for dictionaryKey in dictionary:
            if dictionaryKey != winners[0]:
                if dictionary[winners[0]] == dictionary[dictionaryKey]:
                    winners.append(dictionaryKey)
        return winners
