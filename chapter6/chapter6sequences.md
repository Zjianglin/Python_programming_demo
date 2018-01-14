# chapter 6 sequences

## 6.1 序列
序列是python提供的一种数据存储和访问机制，序列的各个元素在空间上连续存储，可以通过下标操作符加地址偏移量来访问，即`seq[index]`，python的下标是从0开始增长的。反向从`-1`到`·len(seq)`。同时，多个序列元素可以通过切片来得到。

python的序列包括：`字符串(str)`  `列表(list)`  `元组(tuple)`

**python序列支持的操作符有**：
序列操作符  | 作用
--- | ---
seq[index] | 获得序列seq下表为index的元素
seq[beg:end:step] | 切片，获得下表beg至end间隔step的元素集合
seq * expr | 返回seq 重复expr 次的新序列
seq1 + seq2  | 连接seq1和seq2，得到一个新的序列
obj `in` seq | 若元素obj在序列seq中，返回True，否则返回False
obj `not in` seq | 若元素obj不在seq中返回True，否则返回False
---
>注1: 切片索引的开始和结束索引值可以超过列表的长度
---
>注2：连接操作符`+`并不是最好或最快的，因为涉及到内存重新分配和元素构造。对`字符串`来说，把所有子串放在列表或可迭代对象里并调用`join`方法把所有的内容连接在一起，比较节省内存。 而对`列表`来说，调用`extend`方法将seq2中所有元素添加到seq1中；*当然要视情况而定，extend方法返回值为`None`*

**类型转换：**
工厂函数 | 作用
--- | ---
list(iter)  | 返回一个包含可迭代对象所有元素的列表
tuple(iter) | 返回一个包含可迭代对象所有元素的元组
str(obj)    | 返回obj对象字符串表示的结果 *a*
unicode(obj)| 把obj对象转换成unicode字符串 *b*
basestring()| python2中`str`和`unicode`工厂函数的父类，不能被实例化也不能被调用 *b*
---
>注a: python3使用`文本(text)`概念来表示unicode字符串，所有的文本都是unicode的，`encode`的Unicode字符串在python3中是`(二进制)数据[(binary)data]`,`str`表示文本，`bytes`表示数据。

>注b：内建`basestring`抽象类已经在python3中被移除


**序列的内建函数或工厂方法：**
BIFs/ FF  |  function
--- | ---
len(seq)                                   |  返回序列seq的元素个数
sorted(iteratble, key=None, reverse=False) | 返回一个可迭代对象所有元素升序排列的新列表
enumerate(iter[, start])                   | 返回一个enumerate对象(也是一个生成器)，该对象生成由iter每个元素索引index和元素值item组成的元组对，index从start开始递增，默认start为0
max(iter)、min(iter)                       | 返回序列的最大、最小元素
reversed(seq) | 返回一个seq序列元素反向访问的迭代器
zip(iter1 [,iter2 [...]])                  | **python2 返回一个元组列表，python3 返回一个zip对象(也是一个生成器)**，该对象生成的第i个元组由所有iter对象第i个元素组成，__next()__方法运行直到最短的iter对象元素穷尽。
sum(iter, start=0)                         | 返回序列所有元素和start的算数和
------


## 6.2 字符串
字符串是python最基本的数据类型之一，字符串是一种直接量或标量，这意味着python解释器在处理字符串时是把它当做单一值并且不会包含其他python类型，同时字符串是不可变类型，不能对字符串对象进行复制操作(即有字符串`s='test'`,则`s[2]='C'`会引发错误），改变一个字符串的元素就要新建一个新的字符串。 字符串是由独立的字符组成的，支持下表读访问和切片操作顺序地访问。

**字符串和操作符**

1. 字符串支持比较操作符: `>`,`<`,`==`, `!=`;作比较时，字符串是按照对应字符的ASCII值大小来比较的；若len(s1) < len(s2)且两个字符串的前len(s1)个字符均相同，则较长的字符串S2更大。
2. 序列操作符切片（`[]，[beg:end:step]`）;索引访问时index超过字符串最大元素数会引发错误。支持`顺序索引`和`反向索引`。
3. 连接操作符（`+`）： 运行时连接可用连接操作符`+`和字符串格式化操作符`%`， 如`'%s %s' % (str1, str2)`等。也可以在编译时字符串连接，即在源码中把几个字符串连在一起写，以此来构建新的字符串，如`>>> foo = "hello" 'world'` 得到的foo的值为`'helloworld'`。可以把一个长的字符串分成几部分来写，这样跨行也不用加反斜杠。
4. python2中讲一个普通字符串和unicode字符串连接，得到的新的字符串是unicode字符串。
5. 只适用于字符串的操作符：格式化操作符`%`, 原始字符串操作符`r/R`，unicode字符串操作符`u/U`；原始字符串中所有字符都是字面意义的，没有转移字符或不可打印字符。格式化操作符在python3中被抛弃，并在将来会移除,python3中用`format()`函数来实现字符串格式化。python3中不再用`u'...'`来表示unicode文本了，因为python3中文本/字符串默认是unicode的。


## 6.3 列表（list）
列表是python中一种基本的内建序列数据类型，提供了下表或切片方式来访问单个或某一块连续的元素；与字符串的`只能由字符组成且不可变`不同，列表的元素可以是任何数据类型，一个列表实例对象可以包含不同数据类型的元素，而且列表对象是可变的，可以通过`append,pop,insert,extend,sort`等方法增加或减少列表对象元素，以及改变元素的排列顺序。

1. 列表的创建和赋值、访问、修改：可以由方括号`[]`括起来 一组元素组成或由工厂方法`list(iter)`创建。
```python 
>>> l1 = []
>>> l2 = [None, 1, 'Hello']
>>> l3 = list(['hello', 'world', 3.14, 15])
>>> print(l1)
[]
>>> print(l2)
[None, 1, 'Hello']
>>> print(l3)
['hello', 'world', 3.14, 15]
>>> l2[1] = 233
>>> print(l2)
[None, 233, 'Hello']
```
2. 标准操作符: `<`, `>`, `!=`, `==`, 列表比较时，两个列表对应位置的元素分别比较，直到有一方胜出。**python3不支持不同数据类型对象的比较，而python2支持.**
```python
python 2.7.13
>>> l2 = [None, 1, 'Hello']
>>> l3 = list(['hello', 'world', 3.14])
>>> l2 < l3
True
>>> l4 = [None, 1, 'Fun']
>>> l2 < l4
False
```

```python 
python 3.6.3
>>> l2 = [None, 1, 'Hello']
>>> l3 = list(['hello', 'world', 3.14])
>>> l2 < l3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'NoneType' and 'str'
>>> l4 = [None, 1, 'Fun']
>>> l2 < l4
False
```

3. 序列操作符: `[]`, `[start:end:step]`, `+`, `*`， `in`, `not in`

`+` 可以将两个序列连接成一个新的序列，`extend`可以在一个列表的末尾添加列表2的所有元素，返回值为`None`。连接两个列表时推荐使用`list.extend`方法,该方法效果与`+=`相同。 
```python
pyhon 3.6.3
>>> l2
[None, 1, 'Hello']
>>> l3
['hello', 'world', 3.14]
>>> l2 + l3    #连接操作符
[None, 1, 'Hello', 'hello', 'world', 3.14]
>>> l2.extend(l3)
>>> print(l2)
[None, 1, 'Hello', 'hello', 'world', 3.14]
>>> l2 = [None, 1, 'Hello']
>>> l3
['hello', 'world', 3.14]
>>> l2 += l3
>>> print(l2)
[None, 1, 'Hello', 'hello', 'world', 3.14]

>>> l2 * 2  # 重复操作符
[None, 1, 'Hello', 'hello', 'world', 3.14, None, 1, 'Hello', 'hello', 'world', 3.14]
>>> [x for x in range(5)]   #列表解析
[0, 1, 2, 3, 4]
```

4. **`可以改变对象值的可变类型的方法是没有返回值的，如list.extend()等`**。


## 6.4 元组
与列表非常类似，元组也是python中的一种基本的序列数据类型。但是与列表不同，元组一旦创建就不可以改变,是一个**不可变类型**，意味着其通过`hash`算法得到的值总是一个值，因此元组可以作为字典的`key`。

1. 元组对象本身是不可变的，但是元组中可变元素对象是可变的。
```python
>>> t = (1, 2, [1, 5], 'hello')
>>> t[2] = [1, 5, 6, 7]     #元组本身是不可变的
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> for i in t: print(id(i))
...
1773428896
1773428928
2318474194312
2318474188984
>>> t[2].extend([6, 7])   #元组中可变元素对象是可变的。
>>> t
(1, 2, [1, 5, 6, 7], 'hello')
>>> for i in t: print(id(i))
...
1773428896
1773428928
2318474194312 #可以看到元组第二个元素的对象id没有改变
2318474188984
```

2. 所有多对象的、逗号分隔的、没有明确用类型符号定义的元素都是元组类型。如
```python
>>> 'abc', 123, 'hello'
('abc', 123, 'hello')
>>> x, y = 1, 2
>>> x, y
(1, 2)
```
3. 出了有符号封装的,所有函数返回的多对象数据都是元组类型。

## 6.5 浅拷贝和深拷贝
1. **浅拷贝**实际上是新建了一个类型与原对象相同、其内容是原对象元素的引用。序列类型对象的默认拷贝类型是浅拷贝，主要方式有：`完全切片操作[:]`；`利用工厂函数，如list(), tuple()等`； `使用copy模块的copy函数`。
```python
>>> l1 = ['name', [1, 2, 3]]
>>> l2 = l1     #浅拷贝
>>> for i in l1: print(id(i))
...
2318441769872
2318474202120
>>>
>>>
>>> for i in l2: print(id(i))
...
2318441769872
2318474202120
>>> l1
['Changed', [1, 2, 3]]
>>> l2
['Changed', [1, 2, 3]]
```

2. **深拷贝**是指创建一个与原对象类型相同的新的容器对象，包含原有对象元素全新拷贝的引用。需要`copy.deepcopy()`函数。
```python
>>> import copy
>>> l3 = copy.deepcopy(l1)  #深拷贝
>>> for i in l1: print(id(i))
...
2318474189432
2318474202120
>>> for i in l3: print(id(i))
...
2318474189432
2318474193800
>>> l1 [0] = 'Hello'
>>> l1
['Hello', [1, 2, 3]]
>>> l3
['Changed', [1, 2, 3]]
```
*可以看出执行深拷贝后新的容器对象的元素id发生了改变，第一个字符串的id没有改变，原因是对于整型和字符串这类不可变对象，python会很高效地缓存它们.这会导致我们认为python应该新建对象时，它实际上并没有新建。*

3. 非容器类型(如数字、字符串、其他“原子”类型对象，如代码、xrange对象等)没有被拷贝一说,浅拷贝是用完全切片操作来实现的；
4. 如果元组变量只包含原子类型对象，对它的深拷贝将不会进行.