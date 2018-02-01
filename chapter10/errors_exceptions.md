# Chapter 10 Errors and Exceptions

## 10.1 错误和异常

**错误**包括语法错误和逻辑错误，前者指的是程序代码结构上的错误，导致不能被解释器解释或编译器执行，后者指的是可能由于不完整或不合理输入导致的程序无法继续执行的错误。

**异常**指的是因为程序出现了错误而在正常控制流以外采取的行为。

## 10.2 python中的异常

* `SyntaxError`: 语法错误，python中唯一不在运行时发生的错误。
* `NameError`: 访问一个未声明的变量
* `IndexError`: 索引下标超出范围
* ...

## 10.3 检测和处理异常

```python
try:
    #task code
except Exception as err:
    #exceprtion tackle code
else:
    #(optional)
    # if the no exception occures in try-block,
    # then the else-block will be executed
finally:
    #(optional)
    #无论异常是否发生、是否捕获，finally子句都会执行
    #因此，finally子句通常用来维持一致的行为而无论异常是否发生。
```

## 10.4 上下文管理

预定义了清理动作，`with` 语句,仅能工作于支持上下文管理协议的对象，如文件对象`file`,线程锁对象`threading.Lock`等。效果类似`try-finally`语句。

```python
with open('demo.txt', 'w') as fout:
    for i in range(3):
        fout.write('line {} \n'.format(i))
        
with open('demo.txt', 'r') as fin:
    for line in fin:
        print(line)
        
line 0 
line 1 
line 2
```
## 10.5 触发异常

python解释器在程序执行期间遇到错误会触发错误。程序员也可以在代码中遇到不合理输入时等场景触发异常，使用`raise` 语句。


## 10.6 断言

断言是一句必须等价于布尔真的判定，若不为真，则触发断言错误`AssertionError`。

```python
>>> assert 1 == 1
>>> assert 1 == 2
-----------------------------------------------------
AssertionError     Traceback (most recent call last)
<ipython-input-41-a810b3a4aded> in <module>()
----> 1 assert 1 == 2
AssertionError: 

>>> assert 1 == 2, "Error occured!"
----------------------------------------------------------
AssertionError    Traceback (most recent call last)
<ipython-input-42-928e060080c0> in <module>()
----> 1 assert 1 == 2, "Error occured!"
AssertionError: Error occured!
```

## 10.7 标准异常
```python
BaseException
  --SystemExit
  --KeyboardInterrupt
  --Exception
    --all other stand exceptions
```

## 10.9 异常和sys模块

可以通过sys 模块中exc_info()函数获取异常信息

