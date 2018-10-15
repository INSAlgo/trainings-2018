# Handling Input/Output in Python 3

Exercices include :

* How to fetch data from the standard input stream (single line inputs, multi line inputs, single values, arrays, formatted inputs...) ;

* How to format and send data to the standard output stream ;

* How to use input and output redirection in a Linux environment to easily test your programs.

* Some Python tricks we will show you during the lesson

## Basic I/O manipulations

### Exercice 1 - "Simon Says"

Write a program that, given a sentence S, prints it back preceded by "Simon Says: "
S is an alphanumeric string, which may also contain spaces and punctuation marks

Input : a single line, containing the sentence S

Output : a single line, containing the modified sentence

#### Example
##### Input

```
I love INSAlgo ! ;)
```

##### Output

```
Simon Says: I love INSAlgo ! ;)
```

### Exercice 2 - Multiplication

Write a program that, given two integers A and B, prints back the result of A*B

Input :
* on the first line, a single integer A
* on the second line, a single integer B

Output : on one line, a single integer, the result of A*B

#### Example
##### Input

```
5
8
```

##### Output

```
40
```

### Exercice 3 - Multiplication (2)

Same exercice as before, but now, A and B are on the same line, and separated by a space

Input : on one line, two space separated integers A and B

Output : on one line, a single integer, the result of A*B

#### Example
##### Input

```
5 8
```

##### Output

```
40
```

### Exercice 4 - Multiplication (3)

Same exercice as before, but now you must multiply more than 2 integers

Input :
* on the first line, a single integer N, the number of integers to multiply
* on the second line, N space separated integers I1, I2, ..., IN, the integers to multiply

Output : on one line, a single integer, the product of I1*I2*...*IN

#### Example
##### Input

```
4
5 6 2 1
```

##### Output

```
60
```

### Exercice 5 - Multiplication (4)

Same exercice, but now the N integers are on separate lines

Input :
* on the first line, a single integer N, the number of integers to multiply
* on the N following lines, a single integers Ii, the i-th integer to multiply

Output : on one line, a single integer, the product of I1*I2*...*IN

#### Example
##### Input

```
4
5
6
2
1
```

##### Output

```
60
```

## Interlude : A bit of Linux I/O redirection

This knowledge can come in useful when you want to test / debug your program locally before you submit it

### Prerequisite

Consider this program :

```python
print(input())
```

It shouldn't come as a surprise for you that this program prints directly on the standard output the first line it gets from the standard input. Write this program in a Python file that you can name custom_cat.py

### Exercice 1 - Custom cat

Use standard input redirection and custom_cat.py to display in your shell the first line of a file of your choice

```bash
python3 ./custom_cat.py < input_file
```

### Exercice 2 - Custom copy

Use standard input and output redirection and custom_cat.py to copy the first line of a file of your choice to another file

```bash
python3 ./custom_cat.py < input_file > output_file
```

## Advanced I/O manipulations

### Exercice 1 - Multiplication (5)

Same exercice as before, but now the N integers are on a single line and separated by the two characters ', '

Input :
* on the first line, a single integer N, the number of integers to multiply
* on the second line, N integers I1, I2, ..., IN, the integers to multiply, separated by ', ' (a comma followed by a space)

Output : on one line, a single integer, the product of I1*I2*...*IN

#### Example
##### Input

```
4
5, 6, 2, 1
```

##### Output

```
60
```

### Exercice 2 - Pattern

Write a program that, given one integer I, prints on I+2 lines the following pattern : xxIxxAxx where I is the given integer, and A is an integer such as A = I+2

Input : on one line, a single integer 0 <= I <= 8

Output : on I+2 lines, the pattern xxIxxAxx such as A = I+2

#### Example
##### Input

```
5
```

##### Output

```
xx5xx7xx
xx5xx8xx
xx5xx9xx
xx5xx10xx
xx5xx11xx
xx5xx12xx
xx5xx13xx
```

### Exercice 3 - Precision

Write a program that, given N integers, prints their mean value with a precision of exactly 10^-10

Input : on one line, N space separated integers I1, I2, ..., IN

Output : the mean value, with the given precision

#### Example
##### Input

```
5 2 3
```

##### Output

```
3.3333333333
```

### Exercice 4 - Histogram

Write a program that, given N integers between 1 and 5, prints an histogram of how many times the numbers from 1 to 5 appeared

Input : on one line, N space separated integers I1, I2, ..., IN such as 1 <= Ii <= 5

Output : on the 5 following lines, as many 'X' characters as the corresponding number appeared in the input

#### Example
##### Input

```
1 5 1 2 4 4 5 4 4 1 2
```

##### Output

```
XXX
XX

XXXX
XX
```
