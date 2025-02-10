# 0x02. C++ - Headers and Libraries

## Project Information
* **Weight:** 1
* **Duration:** 2 days
* **Auto QA review available**

## Resources
Read or watch:
* [C++ Headers and Libraries](https://www.learncpp.com/cpp-tutorial/header-files/)
* [Standard Template Library (STL)](https://www.geeksforgeeks.org/the-c-standard-template-library-stl/)
* [Creating Custom Headers](https://www.learncpp.com/cpp-tutorial/header-guards/)
* [Header Guard/Include Guards](https://en.wikipedia.org/wiki/Include_guard)
* [Using C++ Libraries](https://www.modernescpp.com/index.php/c-core-guidelines-programming-with-the-standard-library)
* [Namespace in C++](https://www.geeksforgeeks.org/namespace-in-c/)

## Learning Objectives
By the end of this project, you should be able to explain:
- How to create and use header files
- Understanding of include guards
- How to use standard libraries effectively
- Working with STL containers and algorithms
- Creating and managing custom libraries
- Proper header file organization

## Tasks

### 0. Hello STL
**Mandatory**

Create a program that uses vectors from STL to store and manipulate integers.

Requirements:
* Use `vector<int>` to store numbers
* Implement functions to: add, remove, and display elements
* Must use STL algorithms for sorting and searching
* Create appropriate header file

```cpp
int main(void)
{
    VectorManipulator vm;
    vm.addNumber(5);
    vm.addNumber(10);
    vm.addNumber(3);
    vm.displayNumbers();
    vm.removeNumber(10);
    vm.displayNumbers();
    return (0);
}
```

Expected output:
```
Numbers: 3 5 10
Numbers: 3 5
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `0-vector_ops.cpp`, `vector_ops.h`

### 1. String Library
**Mandatory**

Create a custom string manipulation library with basic operations.

Requirements:
* Create header file with string operation declarations
* Implement functions for:
  - String reversal
  - Counting vowels
  - Converting to uppercase
* Must not use standard string methods

```cpp
int main(void)
{
    StringOps str;
    cout << str.reverse("Hello") << endl;
    cout << str.countVowels("OpenAI") << endl;
    cout << str.toUpper("hello world") << endl;
    return (0);
}
```

Expected output:
```
olleH
3
HELLO WORLD
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `1-string_ops.cpp`, `string_ops.h`

### 2. Math Operations
**Mandatory**

Create a mathematical operations library with complex calculations.

Requirements:
* Create a header file with math operation declarations
* Implement functions for:
  - Factorial calculation
  - Prime number checking
  - GCD calculation
* Handle edge cases and errors

```cpp
int main(void)
{
    MathOps math;
    cout << math.factorial(5) << endl;
    cout << math.isPrime(17) << endl;
    cout << math.gcd(48, 18) << endl;
    return (0);
}
```

Expected output:
```
120
true
6
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `2-math_ops.cpp`, `math_ops.h`

### 3. Stack Implementation
**Mandatory**

Implement a generic stack class using templates.

Requirements:
* Create a header file with template class definition
* Implement push, pop, peek operations
* Include bounds checking
* Use templates for any data type

```cpp
int main(void)
{
    Stack<int> s;
    s.push(1);
    s.push(2);
    s.push(3);
    cout << s.peek() << endl;
    s.pop();
    cout << s.peek() << endl;
    return (0);
}
```

Expected output:
```
3
2
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `3-stack.cpp`, `stack.h`

### 4. Queue with Priority
**Mandatory**

Create a priority queue implementation using STL containers.

Requirements:
* Use STL containers internally
* Implement enqueue and dequeue operations
* Support priority levels
* Create comprehensive header file

```cpp
int main(void)
{
    PriorityQueue pq;
    pq.enqueue("Task1", 2);
    pq.enqueue("Task2", 1);
    pq.enqueue("Task3", 3);
    cout << pq.dequeue() << endl;
    cout << pq.dequeue() << endl;
    return (0);
}
```

Expected output:
```
Task3
Task1
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `4-priority_queue.cpp`, `priority_queue.h`

### 5. Smart Array
**Mandatory**

Create a smart array class that manages memory automatically.

Requirements:
* Implement dynamic array with automatic resizing
* Include bounds checking
* Implement copy constructor and assignment operator
* Use RAII principles

```cpp
int main(void)
{
    SmartArray arr;
    arr.add(1);
    arr.add(2);
    arr.add(3);
    cout << arr.get(1) << endl;
    arr.remove(1);
    cout << arr.size() << endl;
    return (0);
}
```

Expected output:
```
2
2
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `5-smart_array.cpp`, `smart_array.h`

### 6. Date Library
**Mandatory**

Create a comprehensive date manipulation library.

Requirements:
* Create a Date class with various operations
* Include validation for dates
* Implement date arithmetic
* Support different date formats

```cpp
int main(void)
{
    Date d1(2024, 2, 8);
    d1.addDays(5);
    cout << d1.toString() << endl;
    cout << d1.daysBetween(Date(2024, 2, 1)) << endl;
    return (0);
}
```

Expected output:
```
2024-02-13
12
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `6-date.cpp`, `date.h`

### 7. Logger Library
**Mandatory**

Implement a logging system with different log levels.

Requirements:
* Support multiple log levels (INFO, WARNING, ERROR)
* Include timestamp in logs
* Support file and console output
* Thread-safe implementation

```cpp
int main(void)
{
    Logger log("app.log");
    log.info("Application started");
    log.warning("Low memory");
    log.error("Division by zero");
    return (0);
}
```

Expected output:
```
[2024-02-08 10:15:30] INFO: Application started
[2024-02-08 10:15:30] WARNING: Low memory
[2024-02-08 10:15:30] ERROR: Division by zero
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `7-logger.cpp`, `logger.h`

### 8. Memory Pool
**Mandatory**

Create a memory pool allocator for efficient memory management.

Requirements:
* Implement fixed-size block allocation
* Include memory recycling
* Thread-safe operations
* Memory leak prevention

```cpp
int main(void)
{
    MemoryPool<int> pool(10);
    int* p1 = pool.allocate();
    int* p2 = pool.allocate();
    *p1 = 5;
    *p2 = 10;
    cout << *p1 << " " << *p2 << endl;
    pool.deallocate(p1);
    return (0);
}
```

Expected output:
```
5 10
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `8-memory_pool.cpp`, `memory_pool.h`

### 9. Binary Tree
**Mandatory**

Implement a binary tree template class with various operations.

Requirements:
* Create template class for any data type
* Implement insertion, deletion, searching
* Include tree traversal methods
* Balance checking

```cpp
int main(void)
{
    BinaryTree<int> tree;
    tree.insert(5);
    tree.insert(3);
    tree.insert(7);
    tree.inorderTraversal();
    cout << tree.search(3) << endl;
    return (0);
}
```

Expected output:
```
3 5 7
true
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `9-binary_tree.cpp`, `binary_tree.h`

### 10. Hash Table
**Mandatory**

Create a hash table implementation with collision handling.

Requirements:
* Implement hash table with chaining
* Include rehashing functionality
* Support generic keys and values
* Handle collisions effectively

```cpp
int main(void)
{
    HashTable<string, int> ht;
    ht.insert("one", 1);
    ht.insert("two", 2);
    cout << ht.get("one") << endl;
    ht.remove("one");
    cout << ht.contains("one") << endl;
    return (0);
}
```

Expected output:
```
1
false
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `10-hash_table.cpp`, `hash_table.h`

### 11. Expression Parser
**Mandatory**

Create a mathematical expression parser and evaluator.

Requirements:
* Support basic arithmetic operations
* Handle parentheses and operator precedence
* Include error handling
* Support variables and constants

```cpp
int main(void)
{
    ExpressionParser parser;
    cout << parser.evaluate("2 + 3 * 4") << endl;
    cout << parser.evaluate("(2 + 3) * 4") << endl;
    return (0);
}
```

Expected output:
```
14
20
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `11-expression_parser.cpp`, `expression_parser.h`

### 12. Network Library
**Mandatory**

Implement a basic networking library for TCP/IP communication.

Requirements:
* Create socket wrapper classes
* Support both client and server operations
* Include error handling
* Support asynchronous operations

```cpp
int main(void)
{
    TCPServer server(8080);
    server.start();
    TCPClient client;
    client.connect("localhost", 8080);
    client.send("Hello");
    string response = client.receive();
    cout << response << endl;
    return (0);
}
```

Expected output:
```
Connection established
Message received: Hello
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `12-network.cpp`, `network.h`


### 10. Even Number Checker
**Mandatory**

Write a function that finds all multiples of 2 in a list.

Requirements:
* Function prototype: `bool* findEvenNumbers(int arr[], int size)`
* Return a new array with true/false values
* The new array should have the same size as the original
* Use dynamic memory allocation
* Handle empty arrays

```cpp
int main(void)
{
    int numbers[] = {0, 1, 2, 3, 4, 5, 6};
    int size = 7;
    bool* results = findEvenNumbers(numbers, size);

    for(int i = 0; i < size; i++) {
        cout << numbers[i] << " "
             << (results[i] ? "is" : "is not")
             << " divisible by 2" << endl;
    }
    delete[] results;
    return (0);
}
```

Expected output:
```
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `10-even_numbers.cpp`, `even_numbers.h`

### 11. Delete At Index
**Mandatory**

Write a template class that implements a list with deletion at specific position.

Requirements:
* Template class with deletion operation
* Handle negative indices
* Handle out of range indices
* Return modified list
* Include proper error handling

```cpp
int main(void)
{
    List<int> list;
    list.append(1);
    list.append(2);
    list.append(3);
    list.append(4);
    list.append(5);

    list.deleteAt(3);
    list.display();
    return (0);
}
```

Expected output:
```
1 2 3 5
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `11-delete_at.cpp`, `delete_at.h`

### 12. Value Swapper
**Mandatory**

Create a template function that swaps values using pointers.

Requirements:
* Function should be template-based
* Handle different data types
* Use pointer manipulation
* Include const-correctness
* Implement as header-only library

```cpp
int main(void)
{
    int a = 10, b = 89;
    cout << "Before: a=" << a << " - b=" << b << endl;

    swap(&a, &b);
    cout << "After: a=" << a << " - b=" << b << endl;
    return (0);
}
```

Expected output:
```
Before: a=10 - b=89
After: a=89 - b=10
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x02-cpp_headers_libs`
* Files: `12-swap.h`

The tasks progress in difficulty and build upon previous concepts while introducing new ones. Each task includes clear requirements, example usage, and expected output in a consistent format.
