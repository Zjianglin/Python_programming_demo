# chapter 7 Dict and Set

## 1 Dict

字典是一个键(key) 映射到 值(value)的"键值对"集合，键必须是可哈希的，值可以是任何数据类型。

1.1 字典的创建: 工厂函数dict(),{}， {k:v, ...}
```python
>>> d1 = {}
>>> d2 = {'a': 1, 'b': 2}
>>> d3 = dict([('a', 1), ('b', 2)])
>>> d1
{}
>>> d2
{'a': 1, 'b': 2}
>>> d3
{'a': 1, 'b': 2}
```

1.2 字典的访问: `d[key] -> value; d.get(key[, v]); dict.setdefault(k[,v])`

```python
>>> d2['a']
1
>>> for k in d2:
...     print('key={}, value={}'.format(k , d2[k]))
...
key=a, value=1
key=b, value=2
>>> d2.get('a')
1
>>> d2.get('c') #dict.get()访问一个不存在的key，返回None
>>> d2.get('c', 'new value') # 或返回get设置的默认参数v
'new value'
>>> d2
{'a': 1, 'b': 2}
>>> d2.setdefault('c', 'new value') 
'new value'
>>> d2
{'a': 1, 'c': 'new value', 'b': 2}
>>> d2.setdefault('c', 'value new')
'new value'
>>> d2
{'a': 1, 'c': 'new value', 'b': 2}
```
>D.setdefault(k[,v]) -> D.get(k, v), also set D[k]=v if k not in D

1.3 字典的更改: `d[k]=v; dict.update();` 

```python
>>> d2['c'] = 3 #update an item
>>> d2['b'] = 4 #update an item
>>> d2['e'] = 5 #add an item
>>> d2
{'a': 1, 'c': 3, 'b': 4, 'e': 5}
>>> d2.update(a=12) 
>>> d2
{'a': 12, 'c': 3, 'b': 4, 'e': 5}
>>> d2.update({'a':13, 'b': 2, 'f':666})
>>> d2 #D.update() 可以更新或添加新的条目 
{'a': 13, 'c': 3, 'b': 2, 'e': 5, 'f': 666}
```

1.4 删除字典的元素和字典: `del D[k]; D.clear()`

```python
>>> d2
{'a': 13, 'c': 3, 'b': 2, 'e': 5, 'f': 666}
>>> del d2['f']  #delete an item
>>> d2
{'a': 13, 'c': 3, 'b': 2, 'e': 5}
>>> d2.clear() #clear the dict, i.e. delete all the items
>>> d2
{}
```

1.5 字典支持的运算符: 
*  `in`/`not in`可以判断某个键是否在字典中，python2中`D.has_key(k)`效果一样但是不推荐后者。
* 比较运算符:`>, <, ==, !=`。大小比较运算符(`> / <, >= / <=`)在python2中支持，在python3中不支持。在python2中，两个字典比较算法: **首先比较两个字典的大小，然后是键，最后是键对应的值**

1.5 字典支持的内建方法
* `D.keys(), D.values()` ，分别返回字典D的所有键和值。在python2中，这两个函数返回一个列表，而python3中返回一个提供字典键(或值)s的视图(view)的类似集合的对象
* `D.items()`，python2中返回一个字典中所有键值对的列表，python3中返回一个提供字典D的所有条目视图的j集合样对象(set-like object)。
* `D.iterkeys(), D.itervalues(), D.iteritems()`， python2中返回一个字典D的键(值、条目)的迭代器。python3中删去了这几个内建函数
* `D.pop(k[, v])` 删除字典D中指定键，返回对应的值或默认值。若k不存在且未指定默认值，则会引发异常错误。
* `D.popitem()`，删除一个条目，*python3中似乎是删除最后添加的条目，而python2中的顺序不固定。具体机制没有仔细研究。*
* `D.copy()`, 返回字典的一个**浅拷贝**

1.6 字典的键： 必须是**可哈希的**,所有不可变类型都是可哈希的，所以都可以作为字典的键，例如数字、字符串。
* 值相同的数字b表示相同的键。例如整数`1`和浮点数`1.0`表示相同的键，因为它们d额哈希值是相同的。
* 有些可变类型是可哈希的，如实现了特殊方法`__hash__()`的类。
* 元组是不可变类型，但是用元组做有效键时有限制，只有元组中只包含像数字和字符串这类不可变类型的元素时才可以作为z字典中有效的值。


## 2 集合

集合对象是一组无序排列的可哈希的值,因此集合的元素都可以作为字典的键。python的集合对象包括两种：`可变集合(set)`和`不可变集合(frozenset)`。

1. 集合的创建： `{}`，工厂函数,`set(), frozenset()`
```python
In [12]: s1 = {1, 2, 3, 3, 2, 1}
In [13]: s2 = set([1, 2, 3, 3, 2, 1])
In [14]: s3 = frozenset([1, 2, 3, 3, 2, 1])
In [15]: s1
Out[15]: {1, 2, 3}
In [16]: s2
Out[16]: {1, 2, 3}
In [17]: s3
Out[17]: frozenset({1, 2, 3})
```
2. 集合的访问： `in`
```python
In [18]: for i in s1: print(i)
1
2
3

In [19]: 2 in s1
Out[19]: True

In [20]: 45 in s1
Out[20]: False
```
3. 集合的更改: `set.add()`, `set.remove()`, `set.discard()`
```python
In [21]: s1
Out[21]: {1, 2, 3}

In [22]: s1.add(4)

In [23]: s1.add(3)

In [24]: s1
Out[24]: {1, 2, 3, 4}

In [25]: s1.remove(2)

In [26]: s1
Out[26]: {1, 3, 4}
In [27]: s1.remove(5)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-2-a33ec7cafce9> in <module>()
----> 1 s1.remove(5)

KeyError: 5

In [28]: s1.discard(5) #S.discard(e)是S.remove(e)的友好版本,当e在S中时，从S中删去e。
```
4. 集合的删除： `del`
```python
In [27]: del s1

In [28]: s1
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-28-519f03d7d7d9> in <module>()
----> 1 s1

NameError: name 's1' is not defined
``` 
5. 集合支持的操作符、函数/方法总结表

<style>tableth:first-of-type{
    width:120px;
}</style>
函数/方法名  |  等价运算符  | 说明
--- | --- | ---
len(s) | -- | 返回集合基数：集合S中元素个数
set(iter) | -- | 可变集合工厂函数:根据可迭代对象iter创建一个可变集合
frozenset(iter)| -- | 不可变集合工厂函数: 根据可迭代对象iter创建一个不可变集合
-- | obj `in` s | 成员测试：当obj在集合s中时返回True，否则False
-- | obj `not in` s | 非成员测试： 当obj不在集合s中时返回True, 否则False
-- | s `==` t | 等价测试：测试集合s和t是否有相同的元素
-- | s `!=` t | 非等价测试
-- | s `<` t | (严格意义的)子集测试：s != t 且`s`中的元素都在`t`中
s.issubset(t) | s `<=` t | (非严格意义的)子集测试：`s`中的元素都在`t`中
-- | s `>` t | (严格意义的)超集测试: s != t 且`t`中所有元素都在`s`中
s.issuperset(t) | s `>=` t | (非严格意义的)超集测试：t中所有元素都在s中
s.union(t) | s `|` t | 并集操作：返回一个包含`s`和`t`中所有元素的集合
s.intersection(t) | s `&` t | 交集操作：返回一个包含`s`和`t`共有的元素集合
s.difference(t) | s `-` t | 差分操作：返回一个集合，该集合元素在`s`中但不在`t`中
s.symmetric_difference(t) | s `^` t | 对称差分操作(XOR)：返回一个集合，该集合中元素仅在t或仅在s中出现，但不是`s`和`t`共有的元素
s.copy() | -- | 返回集合`s`的一个**浅拷贝**
**以下仅用于可变集合** | -- | --
s.union_update(t) | s `|=` t | 并集更新s，将t中的成员添加到s中
s.intersection_update(t) | s `&=` t | 交集更新s：保留s和t共有的元素
s.difference_update(t) | s `-=` t | 差修改: s中保留仅在`s`而不在`t`中的元素
s.symmetric_difference_update(t) | s `^=` t | 对称差分修改操作：s中b保留仅属于s或仅属于t中的元素
s.add(e) | -- | 增加元素e
s.remove(e) | -- | 从s中删除元素e，若e不存在则引发异常错误
s.discard(e)| -- | remove的友好版本，若e在s中，则从s中删去e
s.pop() | -- | 移除并返回s中的任一个元素
s.clear() | -- | 移除s中的所有元素 

>>两个集合进行并、交、差分、对称差分等操作时，如果连个操作数是相同类型(都是可变集合或都是不可变集合)，则
运算结果的类型还是原集合类型；若两个操作数集合类型不同，则运算结果的类型与左侧操作数集合类型相同。
```python
s2 = frozenset([1, 2,  3, 4])

s1 = set([3, 4, 5, 6])

s1 & s2
Out[25]: {3, 4}

s2 & s1
Out[26]: frozenset({3, 4})

s1 & s1
Out[27]: {3, 4, 5, 6}

s2 & s2
Out[28]: frozenset({1, 2, 3, 4})
```