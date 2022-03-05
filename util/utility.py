import re
from exceptions import invalidpatternexception, invalidvalueexception

def matches_pattern(pattern, string):
    try:
        if not isinstance(pattern, re.Pattern):
            raise invalidpatternexception.InvalidPattern('invalid pattern: {}'.format(pattern))
        if not isinstance(string, str):
            raise invalidvalueexception.InvalidValue('invalid value: {}, expected string'.format(string))
    except invalidpatternexception.InvalidPattern as e:
        # log this
        # print(e)
        return
    except invalidvalueexception.InvalidValue as e:
        # log this
        return False
    except Exception as e:
        # log this
        # print(e)
        return 
    return pattern.match(string.replace(' ','')) and True or False 

def extract_from_pattern(pattern, string):
    try:
        if not isinstance(pattern, re.Pattern):
            raise invalidpatternexception.InvalidPattern('invalid pattern: {}'.format(pattern))
        if not isinstance(string, str):
            raise invalidvalueexception.InvalidValue('invalid value: {}, expected string'.format(string))
    except invalidpatternexception.InvalidPattern as e:
        # log this
        # print(e)
        return
    except invalidvalueexception.InvalidValue as e:
        # log this
        return
    except Exception as e:
        # log this
        # print(e)
        return 
    return pattern.search(string.replace(' ',''))

if __name__ == '__main__':
    RATE_PATTERN = re.compile(r'([1-5]\.[0-9])\/5')

    assert matches_pattern(RATE_PATTERN, 4.1) == False
    assert matches_pattern(RATE_PATTERN, '4.1') == False
    assert matches_pattern(RATE_PATTERN, None) == False
    assert matches_pattern(None, None) is None
    assert matches_pattern(None, '4.1/5') is None
    assert matches_pattern(RATE_PATTERN, '4.1/5') == True

    assert extract_from_pattern(RATE_PATTERN, 4.1) is None
    assert extract_from_pattern(RATE_PATTERN, '4.1') is None
    assert extract_from_pattern(RATE_PATTERN, None) is None
    assert extract_from_pattern(None, None) is None
    assert extract_from_pattern(None, '4.1/5') is None
    assert isinstance(extract_from_pattern(RATE_PATTERN, '4.1/5'), re.Match)
    assert extract_from_pattern(RATE_PATTERN, '4.1/5').group(1) == '4.1'
