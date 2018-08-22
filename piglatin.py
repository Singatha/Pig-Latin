""" Name: Xhanti Singatha
    Date: 12 December 2016 
                           """

def to_pig_latin(word):
    vowel = ('a','e','i','o','u')
    consonants = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')    
    sentence = word.split()
    counter = 0 
    for item in sentence:
        letter = ''
        counter1 = 0
        for element in item:
            if element in vowel and letter == '':
                sentence[counter] = item+'way'
                counter += 1
                break
            
            elif element in consonants:
                letter += element
                counter1 += 1
            
            elif element in vowel and letter != '':
                b = len(item)-counter1
                sentence[counter] = item[counter1:]+'a'+letter+'ay'
                counter += 1 
                break   
            
            
    for i in sentence:
        print(i,end=" ")

def to_english(word):
    vowel = ('a','e','i','o','u')
    consonants = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
    sentence = word.split()
    
    counter = 0
    for i in sentence:
        letter = '' 
        if i[:-4:-1] == 'yaw':
            sentence[counter] = i[0:len(i)-3]
            counter += 1
            
        else:
            a = i[0:len(i)-2]
            for j in a[::-1]:
                if j in consonants:
                    letter += j
                else:
                    break
                    
            sentence[counter] = letter[::-1]+i[0:len(i)-(len(letter)+3)]
            counter += 1
    for i in sentence:
        print(i,end=" ")
        
def main():
    user_input = input("(E)nglish or (P)ig Latin ?\n")
    if user_input == 'E':
        user_input1 = input('Enter an English sentence:\n')
        print('Pig-Latin:')
        to_pig_latin(user_input1)
        
    else:
        user_input2 = input('Enter a Pig Latin sentence:\n')
        print('English:')
        to_english(user_input2)
        
        
main()
        
    