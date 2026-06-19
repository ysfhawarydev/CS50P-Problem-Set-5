def main(  ) :
    greeting = input( "Greeting: " )
    print( value( greeting ) )


def value( greeting ) :
    if greeting.startswith( "Hello" ) :
        return '$100'

    elif greeting.startswith( 'H' ) :
        return '$20'

    else :
        return '$0'
    

if __name__ == '__main__' :
    main(  )