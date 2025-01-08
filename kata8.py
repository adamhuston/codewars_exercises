def pig_it(text):
    print(text)
    result=""
    for word in text.split():
        
        
        if word.isalpha():
            if word[-2:] == "ay":
                result = result + " " + word
            else: 
                word = word[1:] + word[0] + 'ay'
                result = result + " " + word
        else:
            fixable = ""
            fix = list(word)
            for i in range(len(fix)):
                if fix[i].isalpha():
                    fixable = fixable + fix[i]
                else:
                    holdit = fix[i]
            fixable = fixable[1:] + fixable[0] + 'ay' + holdit
            result = result + " " + fixable

    return result

print(pig_it('igPay atinlay siay oolcay'))
print(pig_it('Jamey\'s beard is weird!'))