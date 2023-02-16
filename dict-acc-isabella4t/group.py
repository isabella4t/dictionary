
def form(theline):
    stag1 = theline.strip('\n.,!?-:; "')
    stag2 = stag1.strip("'")
    line = stag2.lower()
    return line

def group():
    words = {} # an empty dictionary
    with open('The-Last-Question.txt', 'r') as f: # opens the file for reading
        for x in f:
            x = form(x)
            newlist = x.split(' ') ##splits into different words
            for item in newlist:
                finwo = form(item) ##i dont know how to strip characters in long strings
                wordlen = len(finwo)
                if wordlen in words:

                    if finwo in words[wordlen]:
                        pass
                    else:
                        words[wordlen].append(finwo)
                elif wordlen == 0:
                    pass
                else:
                    words[wordlen] = [finwo]

                # INSERT GROUPING CODE HERE
                #
    return words
print(group())

def questf():
    quest = {} # an empty dictionary
    with open('The-Last-Question.txt', 'r') as f:
        for m in f:
            m = m.strip('\n')
            newlist = m.split(' ') ## we have words, now need to define a sentence
            for i in range(len(newlist)):
                if newlist[i] = '.':
                    x = i ##this is where question begins
                elif newlist[i] = '?':
                    y = i
                    return
            
