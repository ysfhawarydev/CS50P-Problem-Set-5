def main(  ) :
    word = input( "Input: " )
    print( 'Output: ' , end = '' )
    print( shorten( word ) )


def shorten( word ) :
    result = ''
    for i in word :
        if i.lower( ) not in [ "a" , "e" , "i" , "o" , "u" ] :
            result += i

    return result


if __name__ == '__main__' :
    main(  )