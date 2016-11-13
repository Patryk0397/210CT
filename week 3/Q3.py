def main():
    string = input("Please input a string: ")
    counter = 0
    ChangeString(string,counter)
    print (ChangeString(string,counter))

    
def ChangeString(string,counter):
    vowels = ['a','e','i','o','u']


    if counter < 5:
        for i in string:
            if i == vowels[counter]:
                string.remove(i)
                ChangeString(string,counter)
            else:
                counter += 1
                ChangeString(string,counter)
            counter += 1

        return string
                
                
    
main()
    
