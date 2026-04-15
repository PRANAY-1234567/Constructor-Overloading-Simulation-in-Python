# 🔢 Constructor Overloading Simulation in Python (Numbers Class)

## 📌 Description

This Python program demonstrates how to simulate **constructor overloading** using default arguments. The `Numbers` class can initialize values in three different ways:

* Default values
* Single value for all variables
* Three different values

---

## 🚀 Features

* Simulates multiple constructors in Python
* Supports:

  * Default constructor
  * Single-parameter constructor
  * Three-parameter constructor
* Displays values using a method

---

## 🛠️ How It Works

1. The constructor `__init__(self, a=None, b=None, c=None)` uses default arguments.
2. Based on the arguments passed:

   * **No arguments** → initializes `n1=1, n2=2, n3=3`
   * **One argument** → assigns same value to all (`n1=n2=n3=a`)
   * **Three arguments** → assigns values individually
3. The `display()` method prints the values.

---

## 💻 Code

```python id="n8r2pl"
class Numbers:
    def __init__(self, a=None, b=None, c=None):
        # Default constructor
        if a is None and b is None and c is None:
            self.n1 = 1
            self.n2 = 2
            self.n3 = 3

        # Constructor with 1 argument
        elif b is None and c is None:
            self.n1 = self.n2 = self.n3 = a

        # Constructor with 3 arguments
        else:
            self.n1 = a
            self.n2 = b
            self.n3 = c

    def display(self):
        print(f"n1 = {self.n1}\tn2 = {self.n2}\tn3 = {self.n3}")


# Main program
obj1 = Numbers()            # default constructor
obj2 = Numbers(100)         # one argument
obj3 = Numbers(10, 25, 38)  # three arguments

obj1.display()
obj2.display()
obj3.display()
```

---

## ▶️ Example Output

```id="k3z9xt"
n1 = 1	n2 = 2	n3 = 3
n1 = 100	n2 = 100	n3 = 100
n1 = 10	n2 = 25	n3 = 38
```

---

## 📚 Concepts Used

* Class and Object
* Constructor (`__init__`)
* Default arguments
* Conditional logic
* Method definition

---

## 🎯 Use Case

This program helps beginners understand:

* How Python handles constructors differently from languages like Java/C++
* How to simulate **constructor overloading** using default parameters

---

## 🔧 Future Improvements

* Add input validation
* Allow variable number of arguments using `*args`
* Add methods like sum, average, max, min

---

## 📄 License

This project is open-source and free to use.

<img width="809" height="875" alt="image" src="https://github.com/user-attachments/assets/e19b0812-9851-4068-96db-1ea8f0da490a" />
