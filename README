# Summary
Simple class based util that converts an integer to its Roman Numeral equivalent.

# Limitations
Only goes up to 5000 because then it gets weird.

# All the fun you can have!
```
>>> from romannumerals import RomanNumeral
>>> numeral = RomanNumeral(3)
>>> numeral.numeral
'III'
```

```
>>> from romannumerals import RomanNumeral
>>> numeral = RomanNumeral(333)
>>> numeral.numeral
'CCCXXXIII'
```

```
>>> from romannumerals import RomanNumeral
>>> numeral = RomanNumeral(4821)
>>> numeral.numeral
'MVDCCCXXI'
```

```
>>> from romannumerals import RomanNumeral
>>> for i in range(0, 50):
...     if i % 2 == 0:
...         numeral = RomanNumeral(i)
...         print('{}: {}'.format(i, numeral.numeral))
...
0:
2: II
4: IV
6: VI
8: VIII
10: X
12: XII
14: XIV
16: XVI
18: XVIII
20: XX
22: XXII
24: XXIV
26: XXVI
28: XXVIII
30: XXX
32: XXXII
34: XXXIV
36: XXXVI
38: XXXVIII
40: XL
42: XLII
44: XLIV
46: XLVI
48: XLVIII
```

```
>>> for i in range(0, 50):
...     if i % 2 == 1:
...         numeral = RomanNumeral(i)
...         print('{}: {}'.format(i, numeral.numeral))
...
1: I
3: III
5: V
7: VII
9: IX
11: XI
13: XIII
15: XV
17: XVII
19: XIX
21: XXI
23: XXIII
25: XXV
27: XXVII
29: XXIX
31: XXXI
33: XXXIII
35: XXXV
37: XXXVII
39: XXXIX
41: XLI
43: XLIII
45: XLV
47: XLVII
49: XLIX
```
