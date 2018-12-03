"""currency.py: Exchange rate conversion

__author__ = "HuChaoyuan"
__pkuid__  = "1800011776"
__email__  = "huchaoyuan@pku.edu.cn"
"""
from urllib.request import urlopen
currency_from=input()
currency_to=input()
amount_from=input()
def up(a):
    '''Selective uppercase strings and converted into a dictionary.
    a is the string to be selectively capitalized;
    return is a string that is selectively capitalized
    '''
    b = ''
    for i in range(len(a)):
        if str(a[i:i+4])=='true'or str(a[i:i+5])=='false':
            b=b+a[i].upper()
        else:
            b=b+a[i]
    return b
    pass
def exchange(currency_from, currency_to, amount_from):
    '''Export the desired exchange rate.
    Parameter currency_from: the currency on hand.
    Parameter currency_to: the currency to convert to.
    Parameter amount_from: amount of currency to convert.
    '''
    doc=urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    result=eval(up(jstr))["to"].split()[0]
    return(float(result))
    pass
def test_up():
    '''test up()'''
    assert(up('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }')==
           '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : True, "error" : "" }')
def test_exchange():
    '''test exchange()'''
    assert(exchange('USD','EUR','2.5')==2.1589225)
def testAll():
    """test all cases"""
    test_up()
    test_exchange()
    print("All tests passed")
testAll()
def main():
    print(exchange(currency_from, currency_to, amount_from))
if __name__ == '__main__':
    main()
