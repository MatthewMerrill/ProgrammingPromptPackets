# Dew While

You are a gnome working at a dew factory (you ride a gnu to work, but that's beside the point). When you arrive at the factory, perform the following task:

1. You insert the number of the day (an integer) into the dew machine.
2. After 1 minute, you receive back another integer number.
2. If the number is not multiple of 5, you insert the number back into the machine and go to step 2.
3. If the number is a multiple of 5, you get to go home.

Your gnome family having your favorite meal for dinner tonight (mushroom pizza!), in *T* minutes. Given the first number of the machine *X* and assuming it takes 5 minutes to commute home, will you get back home in time for dinner?

Your boss has leaked to you that the machine performs the following mathematical operation to generate the next number:

```
f(x) =
  if x is a multiple of 7: floor((x - 7) / 2)
  else: 2x - 1
```

If you started with the number 11, you would visit numbers:
```
11 21 7 0
```

After 3 minutes of waiting for the machine and a 5 minute commute home, you would arrive home in time for any T >= 8.


## Input

First line contains *N*, the number of cases to process.
Each of the *N* cases contains two space-separated integers, *X* and *T*.

## Output

One "yes"/"no" per line, one line per case corresponding with whether you'll make it home in time for dinner.

## Constraints

All inputs will fit in a 16 bit signed integer.

## Sample

```
5             | yes
11 8          | no
11 7          | no
16 30         | yes
16379 13      | no
-1998 6       | 
```

