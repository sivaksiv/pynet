#!/usr/bin/env python

'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note).

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python

I. Re-using the IP address validation function created in Class #6,
exercise3; create a Python module that contains only this one ip
validation function.

    A. Modify this Python module such that you add a set of tests
into the module.  Use the __name__ == '__main__' technique to
separate the test code from the function definition.  In your test
code, check the validity of each of the following IP addresses
(False means it should fail; True means it should pass the IP
address validation).

    test_ip_addresses = {
        '192.168.1'     :   False,
        '10.1.1.'       :   False,
        '10.1.1.x'      :   False,
        '0.77.22.19'    :   False,
        '-1.88.99.17'   :   False,
        '241.17.17.9'   :   False,
        '127.0.0.1'     :   False,
        '169.254.1.9'   :   False,
        '192.256.7.7'   :   False,
        '192.168.-1.7'  :   False,
        '10.1.1.256'    :   False,
        '1.1.1.1'       :   True,
        '223.255.255.255':  True,
        '223.0.0.0'     :   True,
        '10.200.255.1'  :   True,
        '192.168.17.1'  :   True,
    }


    B. Execute this module--make sure all of the tests pass.

$ ./ex1_valid_ip.py

Testing 223.0.0.0 ................ ok
Testing 10.200.255.1 ............. ok
Testing 169.254.1.9 .............. ok
Testing 192.168.1 ................ ok
Testing 192.256.7.7 .............. ok
Testing 10.1.1. .................. ok
Testing 10.1.1.256 ............... ok
Testing 0.77.22.19 ............... ok
Testing 10.1.1.x ................. ok
Testing 241.17.17.9 .............. ok
Testing 1.1.1.1 .................. ok
Testing 192.168.17.1 ............. ok
Testing -1.88.99.17 .............. ok
Testing 223.255.255.255 .......... ok
Testing 192.168.-1.7 ............. ok
Testing 127.0.0.1 ................ ok


    C. Import this module into the Python interpreter shell.  Make
sure the test code does not execute.  Also test that you can still
correctly call the ip validation function.

$ python
...
>>> import ex1_valid_ip
>>> ex1_valid_ip.valid_ip('192.168.1.1')
True
>>> ex1_valid_ip.valid_ip('1.168.1.1')
True
>>> ex1_valid_ip.valid_ip('0.168.1.1')
False

'''

def valid_ip(ip_address):
    '''
    Check if the IP address is valid

    Return either True or False
    '''

    # Make sure IP has four octets
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False

    # convert octet from string to int
    for i, octet in enumerate(octets):

        try:
            octets[i] = int(octet)
        except ValueError:
            # couldn't convert octet to an integer
            return False


    # map variables to elements of octets list
    first_octet, second_octet, third_octet, fourth_octet = octets

    # Check first_octet meets conditions
    if first_octet < 1:
        return False
    elif first_octet > 223:
        return False
    elif first_octet == 127:
        return False

    # Check 169.254.X.X condition
    if first_octet == 169 and second_octet == 254:
        return False

    # Check 2nd - 4th octets
    for octet in (second_octet, third_octet, fourth_octet):
        if (octet < 0) or (octet > 255):
            return False


    # Passed all of the checks
    return True



# Technique to allow importable and executable code to coexist
if __name__ == '__main__':

    # Create a bunch of test cases
    test_ip_addresses = {
        '192.168.1'     :   False,
        '10.1.1.'       :   False,
        '10.1.1.x'      :   False,
        '0.77.22.19'    :   False,
        '-1.88.99.17'   :   False,
        '241.17.17.9'   :   False,
        '127.0.0.1'     :   False,
        '169.254.1.9'   :   False,
        '192.256.7.7'   :   False,
        '192.168.-1.7'  :   False,
        '10.1.1.256'    :   False,
        '1.1.1.1'       :   True,
        '223.255.255.255':  True,
        '223.0.0.0'     :   True,
        '10.200.255.1'  :   True,
        '192.168.17.1'  :   True,
    }

    print

    # Run the test cases
    for ip, expected_return in test_ip_addresses.items():

        func_test = valid_ip(ip)

        # Make the output format nicer
        dots_to_print = (25 - len(ip)) * '.'

        if func_test == expected_return:
            print "Testing %s %s %s" % (ip, dots_to_print, 'ok')
        else:
            print "Testing %s %s %s" % (ip, dots_to_print, 'failed')

    print
