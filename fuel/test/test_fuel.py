from Fuel import convert , gauge

def testConvert(  ) :
    assert convert( 1 / 4 ) == '25%'

def testGauge(  ) :
    assert gauge( 99 ) == 'F'