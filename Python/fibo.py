def fibonaci(argx):
    arg = int(argx)
    print arg
    if arg<4:
        print "invalid argument"
    prevTerm,currentTerm = 1,1
    print prevTerm,
    terms = 2
    while(terms<=arg):
        print currentTerm,
        prevTerm,currentTerm = currentTerm,prevTerm+currentTerm
        terms = terms + 1

