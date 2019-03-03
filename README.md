# python3-tcpip
파이썬 3 기반의 TCP/IP 활용, 에이콘출판
This is the code repository for [Python Data Structures and Algorithms](https://www.packtpub.com/application-development/python-data-structures-and-algorithm?utm_source=github&utm_medium=repository&utm_campaign=9781786467355), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## 이 책에 관하여
Data structures allow you to organize data in a particular way efficiently. They are critical to any problem, provide a complete solution, and act like reusable code. 
In this book, you will learn the essential Python data structures and the most common algorithms.
## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.

Chapter 12 and 13 does not have any code file

The code will look like the following:
```
def dequeue(self):
    if not self.outbound_stack:
        while self.inbound_stack:
            self.outbound_stack.append(self.inbound_stack.pop())
    return self.outbound_stack.pop()
```

The code in this book will require you to run Python 2.7.x or higher. Python's default interactive environment can also be used to run the snippets of code. In order to use other third-party libraries, pip should be installed on your system.

## Related Products
* [Learning Functional Data Structures and Algorithms](https://www.packtpub.com/application-development/learning-functional-data-structures-and-algorithms?utm_source=github&utm_medium=repository&utm_campaign=9781785888731)

* [Learning JavaScript Data Structures and Algorithms [Video]](https://www.packtpub.com/web-development/learning-javascript-data-structures-and-algorithms-video?utm_source=github&utm_medium=repository&utm_campaign=9781782175698)

* [Java 9 Data Structures and Algorithms](https://www.packtpub.com/application-development/java-9-data-structures-and-algorithms?utm_source=github&utm_medium=repository&utm_campaign=9781785889349)

