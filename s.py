import re
from util.utility import matches_pattern, extract_from_pattern
RATE_PATTERN = re.compile(r'([1-5]\.[0-9])\/5')

# print(matches_pattern(re.compile(r'[1-5]\.[0-9]\/5'),'4.1/5'))
# print(isinstance('h', re.Pattern))
# print(matches_pattern(RATE_PATTERN, None))
# print(extract_from_pattern(RATE_PATTERN, '4.1/5').group(1))
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
