# Braille Gun

QUICK! You're an Automated Combustion Mechanic for the rebel forces. Your task is to build an autonomous robot to burn files containing classified material. The only problem is that the rebellion was too carried away making self-driving X-Wings to allocate you any cameras. You'll have to use the braille indentations labelling each file.

Your droids can sense the following information from the identifiers: the number of raised dots in a row and number of raised dots in a column. Write a program that, given the number of raised dots per row/column, identify whether this file could be classified. There may be cases where a reading is ambiguous, but you should burn any file that might be classified - you **really** can't have these secrets getting out! 

Below is a braille numbering guide:

```
0  1  2  3  4  5  6  7  8  9
01 10 10 11 11 10 11 11 10 01
11 00 10 00 01 01 10 11 11 10
00 00 00 00 00 00 00 00 00 00
```

1 corresponds to a raised dot, 0 to an unraised dot.

## Input
 - First line: 2 space separated integers: *N*: the number of digits in this number, and *S*: the "classified" identifier
 - Second line: 3 space separated integers: x0 x1, x2 the number of raised dots in the first, second, and third rows.
 - Row *i* of the next *N* lines: 2 space separated integers: number of raised dots in the first and second column of the *i*th digit

Note: *S* may have leading zeroes.

## Output

"yes"/"no", whether to burn this file.

## Sample

### Input
```
10 0123456789
14 11 0
1 2
1 0
2 0
1 1
1 2
1 1
2 1
2 2
2 1
1 1
```

### Output
```
yes
```