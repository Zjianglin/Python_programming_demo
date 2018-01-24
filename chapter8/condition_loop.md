# Chapter 8 Condition and Loop

## 8.1 else 语句

1. `if ...(elif ...) else`
2. `while-else`, `for-else` 语句： 在循环中使用时，`else`子句只在循环正常完成后执行，即循环内`break`也会跳过循环对应的`else`块。

```python
 for i in range(3):
    if i > 1:
        print('break the for-loop!')
        break
    print(i)
else:
    print('else block!')
    
0
1
break the for-loop!
``` 
```python
for i in range(3):
    if i > 3:
        print('break the for-loop!')
        break
    print(i)
else:
    print('else block!')
    
0
1
2
else block!
```

## 8.2 迭代器

* 迭代器是一类具有`next()`方法的对象，可以为类序列对象提供一个类序列的接口，但是迭代器并不是通过索引来计数。用户或循环机制(如`for`语句)需要下一项数据时，可以调用迭代器的`next()`方法即可获得；不断调用直到条目全部取出，则迭代器会引发一个`StopIteration`异常，告诉外部调用者，迭代完成。

* `for`语句和`while`语句内部就是通过迭代器机制实现的。
* 迭代器的创建：对一个对象调用`iter()`方法可以返回一个迭代器。
```python
iter(iterable)
iter(callable, sentinel) #the callable is called until it returns the sentinel.
```
>**python3中，`iterator.next()`被重命名为`iterator.__next__()`，因此python3中迭代器的调用要使用内建函数`next()`: `next(it)`而不是`it.next()`。**

>```iter(function, sentinel) <--> next(iterator, sentinel)```,此时迭代器迭代返回完所有条目后,下一次调用捕获`StopIteration`异常，返回哨兵值`sentinel`而不是传播异常。

## 8.3 列表解析

列表解析可以用来动态地创建列表。

>```[expr for iter_val in iterable if cond_expr]```

`for`循环迭代`iterable`对象的所有条目，在此过程中会过滤/捕获满足条件表达式`cond_expr`的条目，应用`expr`的结果值作为生成序列的成员，组成最终列表。

```python
list(map(lambda x: x * 2, range(5)))
Out[42]: [0, 2, 4, 6, 8]

[x * 2 for x in range(5)]
Out[43]: [0, 2, 4, 6, 8]
```

## 8.4 生成器(generator)

生成器是一种返回迭代器的函数，每次调用(`for`/`while`循环中调用或通过`next()`内建函数调用)时会在`yield`关键字子句处“暂停”并返回结果，下一次调用时会在上次“暂停”的`yield`子句下一句开始执行，直到所有的值都`yield`完毕，下一次调用会触发一个`StopIteration`异常。

生成器的创建主要有两种:  生成器表达式 和 `yield`声明

1. 生成器表达式:
>`(expr for iter_var in iterable if cond_expr)`

与列表解析类似，区别在于将列表解析两端的`[]`换成了`()`，它并不真正创建条目列表，而是返回一个生成器，每次调用时返回下一个条目。因此，生成器表达式是内存使用更友好的结构。

```python
In [19]: l = [x * 2 for x in range(3)]

In [20]: l
Out[20]: [0, 2, 4]

In [21]: g = (x * 2 for x in range(3))

In [22]: g #g 是一个生成器对象
Out[22]: <generator object <genexpr> at 0x000001816682E8E0>

In [23]: next(g) #可以通过内建函数next()不断获得下一个值
Out[23]: 0

In [24]: next(g)
Out[24]: 2

In [25]: next(g)
Out[25]: 4

In [26]: next(g)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-26-5f315c5de15b> in <module>()
----> 1 next(g)

StopIteration:
In [29]: g = (x * 2 for x in range(3))
In [30]: for i in g:
    ...:     print(i, end=' ')
    ...:     
0 2 4 # for 循环才是生成器表达式迭代的正确打开方式
```

2. 生成器函数
> `yield` 声明

`yield`声明语句被用来定义一个生成器函数，该函数被调用时会返回一个生成器迭代器,生成器函数体是通过反复调用生成器的`next()`方法来执行的，每次`next()`调用时，遇到`yield`语句会返回，下一次调用时从上次返回的`yield`语句处接着执行，直到引发`StopIteration`异常为止。

以斐波那契数列求解为例：
```python
In [39]: def fib(n):
    ...:     a, b = 0, 1
    ...:     for i in range(n):
    ...:         yield b
    ...:         a, b = b, a+b
    ...:         

In [40]: fib(5)
Out[40]: <generator object fib at 0x00000181668D67D8>

In [41]: for i in fib(5):
    ...:     print(i, end=' ')
    ...:     
1 1 2 3 5 
```


