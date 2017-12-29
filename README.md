# 3intcomp

Save file in 3 int or even less

## Principle

We can use the randomness of irrational number for save large file into several bytes. Just save the irrational number (`a`), the starting decimal index (`b`), and the offset number (`c`). For example, sqaure 2 ~ 1.4142135623730951, and we have `a` = 2, `b` = 3, `c` = 10 to store `2135623730`.

## Limitation

This projection is not guarantee 1 to 1, so in a small range, the answer may not be found, and some target string pattern can be found multiple times.

## Beyond 3 int

1. We can reduce a int via specify the irrational number (`a`), or use some random generator.

2. We can also determine a pattern for escape, so the offset number (`c`) may also removed.

3. If both `1.` and `2.` is considered, then a file can be store in only 1 int, although the searching base is super large.

4. If the digits is overflow an integer, it can also be stored as a bytes string, i.e. store a file in a relatively short byte string.

## Use case

This method can use to transmit a large amount data between planets, or preserve data for a very long time with less cost.

## Demo

### Environment

- Python3.6

### Usage

```
python encode.py <FILENAME>
python decode.py <SEED> <START> <OFFSET>
```

For example

```
python encode.py demo/small_file.txt
python decode.py 0 60492 2
```

### Pseudo random generator

The repeat cycle in python pseudo random generator is `2 ** 19937 - 1`, so for certain demonstration, it's enough.
