from bank import value

def testHello(  ) :
    assert value( 'Hello' ) == '$0'

def testElse(  ) :
    assert value( 'What is up' ) == '$100'