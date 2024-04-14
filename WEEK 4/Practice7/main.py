def printinfo( argl, *vartuple):
    #THis is test
    print ("Output is: ")
    print (argl)
    for var in vartuple:
        print (var)
        return;
printinfo( 10 );
printinfo( 70, 60, 50 );