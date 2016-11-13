r = raw_input("Enter your code, ya feel me: \n")
def isRespectable(code):
    respectableCode = {']':'[', ')':'(', '}':'{'}
    respected = []
    i = 0
    errors = []
    while i < len(code):
        char = code[i]
        if char in respectableCode.values():
            #print char
            respected.append((char, i))
        elif char in respectableCode.keys():
            if(len(respected) > 0):
                if respectableCode[char] == respected[len(respected) - 1][0]:
                    #print "Ran while char is ", char, "and respected[len(respected) - 1] is ", respected[len(respected) - 1]
                    respected.pop(len(respected) - 1)
                else:
                    #errors.append((lastPos, code[lastPos]))
                    #errors.append((respected[len(respected)-1], (char, i)))
                    #respected.pop(len(respected) - 1)
                    respected.append((char, i))
            else:
                respected.append((char, i))
        i += 1
    # TODO FIX
    if len(respected) > 0:
        i = 0
        while i < len(respected):
            if len(respected) > 0:
                errors.append((respected[i], respected[len(respected)-1]))
                respected.remove(respected[len(respected)-1])
            else:
                errors.append((respected[i], respected[i]))
            i += 1
    errors.append(code)
    return errors

def showMismatches(errored):
    errorLocs = []
    for tuple in errored:
        if tuple !=errored[len(errored)-1]:
            # add to array
            errorLocs.append("Error: Mismatched '" + str(tuple[0][0]) + "' (" +
                             str(tuple[0][1]) + ")" + " with '" + str(tuple[1][0]) + "' (" + str(tuple[1][1]) + ")")
    return errorLocs

def showMismatchLocs(errored):
    errorLocs = []
    i = 0
    string = errored[len(errored) - 1]
    while i < len(string):
        errorLocs.append(" ")
        i += 1
    j = 1
    for tuple in errored:
        if tuple !=errored[len(errored)-1]:
            errorLoc1 = tuple[0][1]
            errorLoc2 = tuple[1][1]
            errorLocs[errorLoc1] = j
            errorLocs[errorLoc2] = j
            j += 1
    return errorLocs

#TODO FIX Needs to show ^ and numbers corresponding to their errors
def showErrorLocs(errored):
    errorLocs = []
    i = 0
    string = errored[len(errored)-1]
    while i < len(string):
        errorLocs.append(" ")
        i += 1
    ax = 0
    while ax < len(errored)-1:
        errorLocs[errored[ax][0][1]] = "^"
        errorLocs[errored[ax][1][1]] = "^"
        ax += 1
    return errorLocs

# Turn an array to a string
def toString(var):
    string = ""
    for vals in var:
        string += str(vals)
    return string

''' Print Data '''
errored = isRespectable(r)
if len(errored) == 1:
    print "No errors found :)"
else:
    # Print errors
    print "" \
          "Errors:"
    print errored[len(errored)-1]
    print toString(showErrorLocs(errored))
    print toString(showMismatchLocs(errored))
    i = 1
    for mismatch in showMismatches(errored):
        print str(i) + ": " + mismatch
        i += 1
