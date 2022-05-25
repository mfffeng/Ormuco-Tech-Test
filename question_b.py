#!/usr/bin/python3

import re

# Returns the larger version string
def ver_compare(ver1: str, ver2:str) -> str:
    # Only doing at max three period separated components without further specifications,
    # since it's rare to have more than three components in version numbers
    v1 = re.match(r"^(?P<major>\d+\.)?(?P<minor>\d+\.)?(?P<mod>\d+)", ver1)
    v2 = re.match(r"^(?P<major>\d+\.)?(?P<minor>\d+\.)?(?P<mod>\d+)", ver2)
    group1, group2 = v1.groups(), v2.groups()
    for i in range(min(len(group1), len(group2))):
        if group1[i] is None or group2[i] is None:
            continue
        # Strip the period and cast to int for comparison
        comp1 = int(group1[i][:-1]) if group1[i][-1] == "." else int(group1[i])
        comp2 = int(group2[i][:-1]) if group2[i][-1] == "." else int(group2[i])
        if comp1 == comp2:
            continue
        return ver1 if comp1 > comp2 else ver2
    if len(group1) == len(group2):
        return "Same Version"
    # Assume that "123.45.67" > "123.45"
    elif len(group1) > len(group2):
        return ver1
    else:
        return ver2

if __name__ == "__main__":
    print(ver_compare("1.23.456", "6.1.14"))
    print(ver_compare("1.23.456", "1.23.456"))
    print(ver_compare("1.23.456", "1.23"))
    print(ver_compare("1", "3"))


