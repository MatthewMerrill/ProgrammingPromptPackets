# Towers

Given a list of towers uniquely identified by a single letter, print the towers in increasing size. If two towers share a size, order by id.

## Input

First line of input contains *N*, the number of towers. The *i*'th of the next *N* lines contain a single integer defining the height of the *i*'th tower to print followed by the identification letter.

## Output

N towers of asterisks, sorted as described. Under each tower, print its id letter.

## Constraints

No more than 26 towers, each of height ranging from 0 to 20. All identifiers are unique and consist of a single uppercase letter.

## Sample
```
5       |     *
2 A     |     *
2 B     |     *
2 C     |  ****
1 D     | *****
5 E     | DABCE
```

