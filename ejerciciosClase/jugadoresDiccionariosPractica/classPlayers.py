class Players():
    def winner(self, dictionary):
        winners = []
        for dictionaryKey in dictionary:
            if len(winners) == 0:
                winners.append(dictionaryKey)
            elif dictionary[winners[0]] < dictionary[dictionaryKey]:
                winners = [dictionaryKey]
            elif dictionary[winners[0]] == dictionary[dictionaryKey]:
                winners.append(dictionaryKey)
        return winners