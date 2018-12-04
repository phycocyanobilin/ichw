"""currency.py: To inplement currency exchange.

__author__ = "Xiang Yifan"
__pkuid__  = "1800011820"
__email__  = "1800011820@pku.edu.cn"
"""


short_name = ['AED','AFN','ALL','AMD','ANG','AOA','ARS','AUD',
              'AWG','AZN','BAM','BBD','BDT','BGN','BHD','BIF',
              'BMD','BND','BOB','BRL','BSD','BTC','BTN','BWP',
              'BYR','BZD','CAD','CDF','CHF','CLF','CLP','CNY',
              'COP','CRC','CUC','CUP','CVE','CZK','DJF','DKK',
              'DOP','DZD','EEK','EGP','ERN','ETB','EUR','FJD',
              'FKP','GBP','GEL','GGP','GHS','GIP','GMD','GNF',
              'GTQ','GYD','HKD','HNL','HRK','HTG','HUF','IDR',
              'ILS','IMP','INR','IQD','IRR','ISK','JEP','JOD',
              'JPY','KES','KGS','KHR','KMF','KPW','KRW','KWD',
              'KYD','KZT','LAK','LBP','LKR','LRD','LSL','LTL',
              'LVL','LYD','MAD','MDL','MGA','MKD','MMK','MNT',
              'MOP','MRO','MTL','MUR','MVR','MWK','MXN','MYR',
              'MZN','NAD','NGN','NIO','NOK','NPR','NZD','OMR',
              'PAB','PEN','PGK','PHP','PKR','PLN','PYG','QAR',
              'RON','RSD','RUB','RWF','SAR','SBD','SCR','SDG',
              'SEK','SGD','SHP','SLL','SOS','SRD','STD','SVC',
              'SYP','SZL','THB','YJS','TMT','TND','TOP','TRY',
              'TTD','TWD','TZS','UAH','UGX','USD','UYU','UZS',
              'VEF','VND','VUV','WST','XAF','XAG','XAU','XCD',
              'XDR','XOF','XPD','XPF','XPT','YER','ZAR','ZMK',
              'ZMW','ZWL']


def test_currency_from():
    '''to test whether the currency code to be exchanged is valid'''
    global currency_from1,test,test_result
    
    if currency_from1 in short_name :
        pass
    else :
        test_result = 'Error: Source currency code is invalid.'
        if test == 0:
            print(test_result)
            assert(False)

def test_currency_to():
    '''to test whether the currency code to be exchanged to is valid'''
    global currency_to1,test,test_result
    
    if currency_to1 in short_name :
        pass
    elif test_result == '' :
        test_result = 'Error: Exchange currency code is invalid.'
        if test == 0:
            print(test_result)
            assert(False)

def test_amount_from():
    '''to test whether the amount of currency to convert is valid'''
    global amount_from1,test,test_result
    
    test_amountisfloat = list(amount_from1)
    count_decimal_point = 0
    
    for i in test_amountisfloat:
        a_ascii = ord(i)
        
        if 48 <= a_ascii <= 57 :
            pass
        elif a_ascii == 46 :
            count_decimal_point += 1
        elif test_result == '' :
            test_result = 'Error: Currency amount is invalid.'
            if test == 0:
                print(test_result)
                assert(False)
                
    if count_decimal_point >= 2 and test_result == '':
        test_result = 'Error: Currency amount is invalid.'
        if test == 0:
            print(test_result)
            assert(False)
        
def exchange(currency_from,currency_to,amount_from): 
    '''to test and to get the currency in type float'''
    
    global exchange_result,test_result,currency_from1,currency_to1,amount_from1
    
    exchange_result,test_result = '',''
    currency_from1 = currency_from
    currency_to1 = currency_to
    amount_from1 = amount_from
    
    test_currency_from()       # have all the inputs tested to avoid invalid inputs
    test_currency_to()
    test_amount_from()

    if test_result == '':     #all the test pass and begin to get result
        from urllib.request import urlopen

        amount_from = float(amount_from)
    
        URL = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=%(c_from)s&to=%(c_to)s&amt=%(a_from)d' % \
                {'c_from':currency_from,'c_to':currency_to,'a_from':amount_from}
    
        doc = urlopen(URL)
        docstr = doc.read()
        doc.close()
        jstr = docstr.decode('ascii')

        exchange_result = jstr.split('"')     #analyze the string and get availible number
        exchange_result = exchange_result[7]
        exchange_result = exchange_result.split()
        exchange_result = exchange_result[0]
    
    
    
    if test_result != '':          #To finish the function 'test_exchange'
        return test_result
    else :
        return exchange_result
    


def to_choose():
    '''to choose to exchange currency or test the function'''
    
    choice = input('Do you want to exchange?(please input "yes" or "no" or "test it")   ')
     
    global currency_from1,currency_to1,amount_from1,test
    test = 0

    if choice == "yes":    #You want to exchange currency.The next step is input the parameter.
       
        currency_from = input('short name of your currency:')
        currency_to = input('short name of currency you want to exchange to:')
        amount_from = input('amount:')
        
        print('You will get:',exchange(currency_from,currency_to,amount_from),currency_to)  #To call the function 'exchange'
    
    elif choice == "no":
        pass
    
    elif choice == "test it":
        test_exchange()
    
    

def test_exchange():
    '''standard for test'''
    global test
    
    test = 1
    
    assert(exchange('EUR','CNY','15') == '119.01944141117' )
    assert(exchange('EUr','CNY','15') == 'Error: Source currency code is invalid.' )
    assert(exchange('EUR','CNy','15') == 'Error: Exchange currency code is invalid.' )
    assert(exchange('EUR','CNY','ASFs') == 'Error: Currency amount is invalid.' )
    assert(exchange('EUR','CNY','15.342.3') == 'Error: Currency amount is invalid.' )
    assert(exchange('MKD','MMK','15') == '434.65929035848' )
    assert(exchange('BAM','AUD','15.0') == '12.344196626392' )
    assert(exchange('BTN','NGN','15') == '75.904778502099' )
    assert(exchange('SBD','DKK','15') == '12.240312278571' )
    print('All pass!')

    
def main():
    to_choose()
    
    
if __name__ == '__main__':
    main()
