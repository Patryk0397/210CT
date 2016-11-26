def removeVowels(counter=0):
    
    vowels = ['a','e','i','o','u']
    
    if counter < len(vowels):
        if vowels[counter] in word:
            word.remove(vowels[counter])    #remove the vowel from word
            removeVowels(counter)           #looks for another instance of this vowel
        else:
            counter += 1
            removeVowels(counter)

        return(word)


if __name__ == '__main__':
    word = input('Word: ')
    word = list(word)

    removeVowels()
