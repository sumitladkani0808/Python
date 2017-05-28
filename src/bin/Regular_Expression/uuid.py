import re


def is_valid_uuid(uuid):
    # return bool(re.search(r'^[a-f\d]{8}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}$', uuid, re.IGNORECASE))
    return bool(re.search(r'''
        ^
        [a-f\d]{8} # 8 hexadecimal digits
        -
        [a-f\d]{4} # 4 hexadecimal digits
        -
        [a-f\d]{4} # 4 hexadecimal digits
        -
        [a-f\d]{4} # 4 hexadecimal digits
        -
        [a-f\d]{12} # 12 hexadecimal digits
        $
    ''', uuid, re.IGNORECASE | re.VERBOSE))

if __name__ == '__main__':
    print(is_valid_uuid('ecf3893a-435e-11e7-ba4c-507b9d9a31f6'))
