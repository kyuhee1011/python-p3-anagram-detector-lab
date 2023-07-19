class Anagram:
    def __init__(self, word): 
        self.word=word
    def match (self, list):
        newList=[]
        new_match_word=[letter for letter in self.word]
        for word in list:
            if sorted ([letter for letter in word])==sorted (new_match_word):
                newList.append(word)
        return newList
