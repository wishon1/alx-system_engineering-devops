# 0x01. C++ - If/Else, Loops, and Functions

## Project Information
* **Weight:** 1
* **Duration:** 2 days
* **Auto QA review available**

## Resources
Read or watch:
* [C++ Control Structures](http://www.cplusplus.com/doc/tutorial/control/)
* [Functions in C++](http://www.cplusplus.com/doc/tutorial/functions/)
* [Function Overloading](https://www.geeksforgeeks.org/function-overloading-cpp/)
* [C++ Loops](https://www.w3schools.com/cpp/cpp_loops.asp)
* [Understanding Scope in C++](https://www.geeksforgeeks.org/scope-of-variables-in-c/)

## Learning Objectives
By the end of this project, you should be able to explain:
- How to use conditional statements in C++
- Different types of loops and their use cases
- Function declaration and definition
- Function overloading principles
- Parameter passing and return types

## Tasks

### 0. Positive or Negative
**Mandatory**

Write a program that determines if a number is positive or negative.

Requirements:
* You can only use if...else statement once
* You can only use two cout statements
* You are not allowed to use ternary operators
* You are not allowed to use goto statements

```cpp
Expected output:
98 is positive
-98 is negative
0 is zero
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `0-positive_or_negative.cpp`

### 1. The Last Digit
**Mandatory**

Write a program that prints the last digit of a number.

Requirements:
* You can only use one if...else statement
* You can only use one loop
* You are not allowed to use arrays
* You are not allowed to use strings

```cpp
Expected output:
Last digit of 98 is 8
Last digit of 0 is 0
Last digit of -98 is -8
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `1-last_digit.cpp`

### 2. Alphabet Game
**Mandatory**

Write a program that prints the alphabet in lowercase.

Requirements:
* You can only use one cout statement
* You can only use one loop
* You are not allowed to store characters in a variable
* You are not allowed to use string library

```cpp
Expected output:
abcdefghijklmnopqrstuvwxyz
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `2-print_alphabet.cpp`

### 3. alphABET
**Mandatory**

Write a program that prints the alphabet in lowercase, and then in uppercase.

Requirements:
* You can only use one cout statement
* You can only use one loop
* You are not allowed to store characters in a variable
* You are not allowed to use string library

```cpp
Expected output:
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `3-print_alphabets.cpp`

### 4. Hexadecimal
**Mandatory**

Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal.

Requirements:
* You can only use one cout statement
* You can only use one loop
* You are not allowed to store numbers or strings in a variable

```cpp
Expected output:
0 = 0x0
1 = 0x1
2 = 0x2
...
97 = 0x61
98 = 0x62
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `4-print_hexa.cpp`

### 5. Print Combination
**Mandatory**

Write a program that prints numbers from 0 to 99.

Requirements:
* Numbers must be separated by , followed by a space
* Numbers should be printed in ascending order
* You can only use cout statement twice maximum
* You can only use one loop
* You are not allowed to store numbers or strings in a variable

```cpp
Expected output:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ..., 98, 99
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `5-print_numbers.cpp`

### 6. Islands Perimeter
**Mandatory**

Create a function that checks if character is lowercase.

Requirements:
* Function prototype: `bool islower(char c)`
* Returns true if c is lowercase
* Returns false otherwise
* You are not allowed to use any external libraries

```cpp
Expected output:
a is lowercase
H is not lowercase
A is not lowercase
z is lowercase
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `6-islower.cpp`

### 7. Temperature Calculator
**Mandatory**

Write function overloading to convert temperatures.

Requirements:
* Create functions for:
  * Celsius to Fahrenheit
  * Fahrenheit to Celsius
  * Celsius to Kelvin
  * Kelvin to Celsius
* You must use function overloading
* You cannot use arrays or strings

```cpp
Expected output:
32°F = 0°C
0°C = 273.15K
100°C = 212°F
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `7-temperature.cpp`

### 8. Fibonacci
**Mandatory**

Write a function that prints the first n numbers of Fibonacci sequence.

Requirements:
* Function prototype: `void print_fibonacci(int n)`
* You can only use while loop
* You cannot use arrays
* You cannot use recursion

```cpp
Expected output:
1 1 2 3 5 8 13 21 34 55 89 144
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `8-fibonacci.cpp`

### 9. Prime Factors
**Mandatory**

Write a function that finds and prints the largest prime factor of a number.

Requirements:
* Function prototype: `void largest_prime_factor(long int n)`
* You can only use while loop
* You cannot use arrays or strings
* You cannot use math library

```cpp
Expected output:
Largest prime factor of 1231952 is 2081
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `9-prime_factors.cpp`

### 10. Calculator
**Mandatory**

Create a simple calculator using function overloading.

Requirements:
* Implement addition, subtraction, multiplication, and division
* Handle both integer and floating-point numbers
* Use function overloading
* Handle division by zero
* You cannot use arrays or strings

```cpp
Expected output:
5 + 3 = 8
5.5 + 3.5 = 9.0
10 / 2 = 5
10 / 0 = Error: Division by zero
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `10-calculator.cpp`# 0x01. C++ - If/Else, Loops, and Functions

## Project Information
* **Weight:** 1
* **Duration:** 2 days
* **Auto QA review available**

## Resources
Read or watch:
* [C++ Control Structures](http://www.cplusplus.com/doc/tutorial/control/)
* [Functions in C++](http://www.cplusplus.com/doc/tutorial/functions/)
* [Function Overloading](https://www.geeksforgeeks.org/function-overloading-cpp/)
* [C++ Loops](https://www.w3schools.com/cpp/cpp_loops.asp)
* [Understanding Scope in C++](https://www.geeksforgeeks.org/scope-of-variables-in-c/)

## Learning Objectives
By the end of this project, you should be able to explain:
- How to use conditional statements in C++
- Different types of loops and their use cases
- Function declaration and definition
- Function overloading principles
- Parameter passing and return types

## Tasks

### 0. Positive or Negative
**Mandatory**

Write a program that determines if a number is positive or negative.

Requirements:
* You can only use if...else statement once
* You can only use two cout statements
* You are not allowed to use ternary operators
* You are not allowed to use goto statements

```cpp
Expected output:
98 is positive
-98 is negative
0 is zero
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `0-positive_or_negative.cpp`

### 1. The Last Digit
**Mandatory**

Write a program that prints the last digit of a number.

Requirements:
* You can only use one if...else statement
* You can only use one loop
* You are not allowed to use arrays
* You are not allowed to use strings

```cpp
Expected output:
Last digit of 98 is 8
Last digit of 0 is 0
Last digit of -98 is -8
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `1-last_digit.cpp`

### 2. Alphabet Game
**Mandatory**

Write a program that prints the alphabet in lowercase.

Requirements:
* You can only use one cout statement
* You can only use one loop
* You are not allowed to store characters in a variable
* You are not allowed to use string library

```cpp
Expected output:
abcdefghijklmnopqrstuvwxyz
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `2-print_alphabet.cpp`

### 3. alphABET
**Mandatory**

Write a program that prints the alphabet in lowercase, and then in uppercase.

Requirements:
* You can only use one cout statement
* You can only use one loop
* You are not allowed to store characters in a variable
* You are not allowed to use string library

```cpp
Expected output:
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `3-print_alphabets.cpp`

### 4. Hexadecimal
**Mandatory**

Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal.

Requirements:
* You can only use one cout statement
* You can only use one loop
* You are not allowed to store numbers or strings in a variable

```cpp
Expected output:
0 = 0x0
1 = 0x1
2 = 0x2
...
97 = 0x61
98 = 0x62
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `4-print_hexa.cpp`

### 5. Print Combination
**Mandatory**

Write a program that prints numbers from 0 to 99.

Requirements:
* Numbers must be separated by , followed by a space
* Numbers should be printed in ascending order
* You can only use cout statement twice maximum
* You can only use one loop
* You are not allowed to store numbers or strings in a variable

```cpp
Expected output:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ..., 98, 99
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `5-print_numbers.cpp`

### 6. Islands Perimeter
**Mandatory**

Create a function that checks if character is lowercase.

Requirements:
* Function prototype: `bool islower(char c)`
* Returns true if c is lowercase
* Returns false otherwise
* You are not allowed to use any external libraries

```cpp
Expected output:
a is lowercase
H is not lowercase
A is not lowercase
z is lowercase
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `6-islower.cpp`

### 7. Temperature Calculator
**Mandatory**

Write function overloading to convert temperatures.

Requirements:
* Create functions for:
  * Celsius to Fahrenheit
    * Fahrenheit to Celsius
	  * Celsius to Kelvin
	    * Kelvin to Celsius
		* You must use function overloading
		* You cannot use arrays or strings

		```cpp
		Expected output:
		32°F = 0°C
		0°C = 273.15K
		100°C = 212°F
		```

		**Repo:**
		* GitHub repository: `alx-low_level_programming`
		* Directory: `0x01-cpp_if_else_loops_functions`
		* File: `7-temperature.cpp`

		### 8. Fibonacci
		**Mandatory**

		Write a function that prints the first n numbers of Fibonacci sequence.

		Requirements:
		* Function prototype: `void print_fibonacci(int n)`
		* You can only use while loop
		* You cannot use arrays
		* You cannot use recursion

		```cpp
		Expected output:
		1 1 2 3 5 8 13 21 34 55 89 144
		```

		**Repo:**
		* GitHub repository: `alx-low_level_programming`
		* Directory: `0x01-cpp_if_else_loops_functions`
		* File: `8-fibonacci.cpp`

		### 9. Prime Factors
		**Mandatory**

		Write a function that finds and prints the largest prime factor of a number.

		Requirements:
		* Function prototype: `void largest_prime_factor(long int n)`
		* You can only use while loop
		* You cannot use arrays or strings
		* You cannot use math library

		```cpp
		Expected output:
		Largest prime factor of 1231952 is 2081
		```

		**Repo:**
		* GitHub repository: `alx-low_level_programming`
		* Directory: `0x01-cpp_if_else_loops_functions`
		* File: `9-prime_factors.cpp`

		### 10. Calculator
		**Mandatory**

		Create a simple calculator using function overloading.

		Requirements:
		* Implement addition, subtraction, multiplication, and division
		* Handle both integer and floating-point numbers
		* Use function overloading
		* Handle division by zero
		* You cannot use arrays or strings

		```cpp
		Expected output:
		5 + 3 = 8
		5.5 + 3.5 = 9.0
		10 / 2 = 5
		10 / 0 = Error: Division by zero
		```

		**Repo:**
		* GitHub repository: `alx-low_level_programming`
		* Directory: `0x01-cpp_if_else_loops_functions`
		* File: `10-calculator.cpp`.


		I'll add these additional tasks to the C++ project in the same format:

### 7. Character Case Checker
**Mandatory**

Write a function that checks for lowercase character.

Requirements:
* Function prototype: `bool islower(char c)`
* Returns true if c is lowercase
* Returns false otherwise
* You are not allowed to use any string functions
* You are not allowed to use existing character checking functions
* Tip: Use ASCII values

```cpp
int main(void)
{
    cout << "a is " << (islower('a') ? "lower" : "upper") << endl;
    cout << "H is " << (islower('H') ? "lower" : "upper") << endl;
    cout << "A is " << (islower('A') ? "lower" : "upper") << endl;
    cout << "3 is " << (islower('3') ? "lower" : "upper") << endl;
    cout << "g is " << (islower('g') ? "lower" : "upper") << endl;
    return (0);
}
```

Expected output:
```
a is lower
H is upper
A is upper
3 is upper
g is lower
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `7-islower.cpp`

### 8. String Uppercase
**Mandatory**

Write a function that prints a string in uppercase followed by a new line.

Requirements:
* Function prototype: `void uppercase(string str)`
* You can only use cout twice maximum
* You can only use one loop in your code
* You are not allowed to use string library functions
* You are not allowed to use existing character checking functions
* Tip: Use ASCII values

```cpp
int main(void)
{
    uppercase("best");
    uppercase("Best School 98 Battery street");
    return (0);
}
```

Expected output:
```
BEST
BEST SCHOOL 98 BATTERY STREET
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `8-uppercase.cpp`

### 9. Last Digit
**Mandatory**

Write a function that prints and returns the last digit of a number.

Requirements:
* Function prototype: `int print_last_digit(int number)`
* Returns the value of the last digit
* Print the last digit of number
* You are not allowed to use string manipulation

```cpp
int main(void)
{
    print_last_digit(98);
    print_last_digit(0);
    int r = print_last_digit(-1024);
    cout << r << endl;
    return (0);
}
```

Expected output:
```
8044
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `9-print_last_digit.cpp`

### 10. Addition Function
**Mandatory**

Write a function that adds two integers and returns the result.

Requirements:
* Function prototype: `int add(int a, int b)`
* Returns the value of a + b
* You are not allowed to use any external libraries

```cpp
int main(void)
{
    cout << add(1, 2) << endl;
    cout << add(98, 0) << endl;
    cout << add(100, -2) << endl;
    return (0);
}
```

Expected output:
```
3
98
98
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `10-add.cpp`

### 11. Power Function
**Mandatory**

Write a function that computes a to the power of b and returns the value.

Requirements:
* Function prototype: `double pow(int a, int b)`
* Returns the value of a ^ b
* You are not allowed to use math library
* Handle negative exponents

```cpp
int main(void)
{
    cout << pow(2, 2) << endl;
    cout << pow(98, 2) << endl;
    cout << pow(98, 0) << endl;
    cout << pow(100, -2) << endl;
    cout << pow(-4, 5) << endl;
    return (0);
}
```

Expected output:
```
4
9604
1
0.0001
-1024
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `11-pow.cpp`

### 12. FizzBuzz
**Mandatory**

Write a function that prints the numbers from 1 to 100 separated by a space.

Requirements:
* Function prototype: `void fizzbuzz()`
* For multiples of three print "Fizz" instead of the number
* For multiples of five print "Buzz"
* For numbers which are multiples of both three and five print "FizzBuzz"
* Each element should be followed by a space
* You are not allowed to use string library

```cpp
int main(void)
{
    fizzbuzz();
    cout << endl;
    return (0);
}
```

Expected output:
```
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz
```

**Repo:**
* GitHub repository: `alx-low_level_programming`
* Directory: `0x01-cpp_if_else_loops_functions`
* File: `12-fizzbuzz.cpp`
