import exrex
import re

def regex_pattern(btchId1,regex_pattern1):
    # regex_pattern1 = r'^[a-zA-Z]{5}\d{4}[a-zA-Z]$'
    # regex_pattern1 = r'^[a-zA-Z0-9]{8,20}$'

    for btchId in btchId1:
        random_date_string = exrex.getone(regex_pattern1)
        btchId.text = str(random_date_string)
        # print(random_date_string)

    # if re.match(regex_pattern1, random_date_string):
    #     print('Regex matches')
    # else:
    #     print('Regex does not match')

# s1 = regex_pattern()

