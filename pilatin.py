vowel = ('a','e','i','o','u')
consonants = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
word = input('Enter sentence:\n')
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



print(sentence)