'''Determine whether a one-to-one character mapping exists from one string, s1, to another string, s2.
For example, given ​s1 = abc​ and ​s2 = bcd,​ print "​true" into stdout​ since we can map each character in "abc" to a character in "bcd".
Given ​s1 = foo​ and ​s2 = bar,​ print "f​ alse"​ since the character ‘o’ cannot map to two characters.
But given ​s1 = bar a​ nd ​s2 = foo​, print "true​"​ since each character in "bar" can be mapped to a character in "foo".'''

def isIsomorphic(s1: str, s2: str) -> bool:
    return len(set(zip(s1, s2))) == len(set(s1))

test_case1 = isIsomorphic("abc", "bcd")
print(test_case1)

test_case2 = isIsomorphic("foo", "bar")
print(test_case2)

test_case3 = isIsomorphic("bar", "foo")
print(test_case3)
