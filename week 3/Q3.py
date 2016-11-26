def removeVowels(counter=0):
    
    vowels = ['a','e','i','o','u']
    
    if counter < len(vowels):
        if vowels[counter] in word:
            word.remove(vowels[counter])
            removeVowels(counter)
        else:
            counter += 1
            removeVowels(counter)

        return(word)


if __name__ == '__main__':
    word = input('Word: ')
    word = list(word)

    removeVowels()
