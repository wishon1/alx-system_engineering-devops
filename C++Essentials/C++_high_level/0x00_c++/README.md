---

# **0x00. C++ - Hello, World**  
## **C++ Foundations**  
**Weight:** 1  
**Project Duration:** 1 day  
**Auto QA review:** Enabled  
**Mandatory Tasks:** 100%  
**Optional Tasks:** 0%  

---

## **Concepts**  
For this project, we expect you to look at these concepts:  
- C++ programming basics  
- Compiling and running C++ programs  
- Coding style and best practices  

---

## **Author’s Disclaimer**  
Welcome to the C++ world!  

The first projects are more "C-oriented"—no tricks, no advanced syntax—just simple fundamentals.  
If you've already worked with C, transitioning to C++ should be smooth.  

Enjoy!  

— **Wisdom A. Honest**  

---

## **Resources**  
Read or watch:  
- [C++ Tutorial - Learn C++ Programming](https://www.learncpp.com/)  
- [C++ Getting Started](https://cplusplus.com/doc/tutorial/)  
- [C++ Input and Output (cin, cout)](https://www.cplusplus.com/doc/tutorial/basic_io/)  
- [C++ Data Types](https://www.geeksforgeeks.org/c-data-types/)  
- [C++ Coding Style Guide](https://google.github.io/styleguide/cppguide.html)  

---

## **Learning Objectives**  
By the end of this project, you should be able to:  
- Understand why C++ is an important language  
- Compile and run a simple C++ program  
- Use basic input/output (`cin`, `cout`)  
- Declare and initialize variables in C++  
- Follow proper C++ coding style  
- Write simple functions in C++  

---

## **Requirements**  
### **C++ Scripts**  
- Allowed editors: `vi`, `vim`, `emacs`  
- All files will be compiled on **Ubuntu 20.04 LTS** using `g++` with the options:  
  ```bash
  g++ -Wall -Werror -Wextra -pedantic -std=c++17
  ```
- Each file should end with a **new line**  
- Code must follow the **Google C++ Style Guide**  
- No more than **5 functions per file**  
- **Header file (`lists.h`)** must contain function prototypes  
- Header files should be include-guarded  

---

## **Tasks**  

### **0. Run a C++ File**  
**Mandatory**  
Write a shell script that compiles and runs a C++ file.  
The C++ file name will be saved in the environment variable `$CPPFILE`.  

**Example:**  
```bash
g++ -o output $CPPFILE && ./output
```  

---

### **1. Hello, World!**  
**Mandatory**  
Write a C++ program that prints `"Hello, World!"`, followed by a new line.  

**Example:**  
```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```
**Output:**  
```
Hello, World!
```

---

### **2. Printing with Variables**  
**Mandatory**  
Write a C++ program that declares a `std::string` variable with the value `"C++ is powerful!"` and prints it using `cout`.  

**Example:**  
```cpp
#include <iostream>
#include <string>

int main() {
    std::string message = "C++ is powerful!";
    std::cout << message << std::endl;
    return 0;
}
```

---

### **3. Simple Input and Output**  
**Mandatory**  
Write a C++ program that asks the user for their name and prints:  
```
Hello, <name>!
```  
**Example:**  
```cpp
#include <iostream>
#include <string>

int main() {
    std::string name;
    std::cout << "Enter your name: ";
    std::cin >> name;
    std::cout << "Hello, " << name << "!" << std::endl;
    return 0;
}
```

---

### **4. Data Types and Variables**  
**Mandatory**  
Write a C++ program that declares and prints variables of different types:  
- `int`  
- `double`  
- `char`  
- `bool`  

**Example:**  
```cpp
#include <iostream>

int main() {
    int age = 25;
    double pi = 3.14159;
    char grade = 'A';
    bool isCodingFun = true;

    std::cout << "Age: " << age << std::endl;
    std::cout << "Pi: " << pi << std::endl;
    std::cout << "Grade: " << grade << std::endl;
    std::cout << "Is coding fun? " << isCodingFun << std::endl;
    
    return 0;
}
```

---

### **5. Basic Arithmetic**  
**Mandatory**  
Write a C++ program that asks the user for two numbers and prints their sum, difference, product, and quotient.  

**Example:**  
```cpp
#include <iostream>

int main() {
    int a, b;
    std::cout << "Enter two numbers: ";
    std::cin >> a >> b;

    std::cout << "Sum: " << a + b << std::endl;
    std::cout << "Difference: " << a - b << std::endl;
    std::cout << "Product: " << a * b << std::endl;
    std::cout << "Quotient: " << a / b << std::endl;

    return 0;
}
```

---

### **6. Conditions and Comparisons**  
**Mandatory**  
Write a C++ program that asks the user for a number and checks if it's even or odd.  

---

### **7. Looping through Numbers**  
**Mandatory**  
Write a C++ program that prints numbers from **1 to 10** using a `for` loop.  

---

### **8. Function: Add Two Numbers**  
**Mandatory**  
Write a function that takes two integers as arguments and returns their sum.  

**Example:**  
```cpp
int add(int a, int b) {
    return a + b;
}
```

---

### **9. Function Overloading: Multiply**  
**Mandatory**  
Write two overloaded functions `multiply()` that:  
- Takes **two integers** and returns their product  
- Takes **two doubles** and returns their product  

---

### **10. Using Arrays**  
**Mandatory**  
Write a C++ program that declares an array of **5 integers** and prints its elements using a loop.  

---

### **11. Using Vectors**  
**Mandatory**  
Write a C++ program that stores **5 words** in a `std::vector<std::string>` and prints them.  

---

## **Optional Tasks**  
*(Not required for 100% completion but recommended for deeper understanding.)*  

### **12. Swapping Variables**  
**Optional**  
Write a function `swapValues(int &a, int &b)` that swaps two integers using **pass-by-reference**.  

---

## **Project Submission**  
- **GitHub Repository:** `alx-low_level_programming`  
- **Directory:** `0x00-cpp-hello_world`  
- **Files:**  
  - `0-run_cpp_file.sh`  
  - `1-hello_world.cpp`  
  - `2-print_variable.cpp`  
  - `3-input_output.cpp`  
  - `4-data_types.cpp`  
  - `5-basic_arithmetic.cpp`  
  - `6-conditions.cpp`  
  - `7-loops.cpp`  
  - `8-function_add.cpp`  
  - `9-overloading_multiply.cpp`  
  - `10-array.cpp`  
  - `11-vector.cpp`  
  - `12-swap_function.cpp` (optional)  

---

### **Zen of C++**  
- Simplicity is better than complexity.  
- Efficiency matters, but readability is key.  
- Mastery comes from practice—keep coding!  
