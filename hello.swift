print("Hello")
print("this is my first swift file")
print("First i saved the file as hello.swift")
print("then i ran this code in terminal:")
print(" swiftc hello.swift")
print("This created a swift file called 'hello'")
print("Now, anytime i type './hello' into terminal")
print("this code will run")
print("however, each time you edit the file")
print("you must run 'swiftc hello.swift' again")
print("or else updates will not be active")

// This is how to comment a single line
/* this is how to comment
multiple lines */

var name = "Austin"
var status = "fat"
print("Checking up on \(name)... \nHe is currently \(status)")

// understanding booleans
var x:Bool
x = true
var y = false

if x && y {   // false : && (and operator) returns true if both x and y are true
  // if x is false, then the code will not run for y
  print("both x and y are true")
} else {
    print("x and y are not both true")
}


if x || y { // true: || (or operator) returns true if either x or y is true
  print("one of x or y is true")
} else {
    print("neither x nor y are true")
}

if x == !y {  // true: ! (not operator) inverts boolen , so true becomes false, etc.
  print("x is the opposite boolean of y")
} else {
    print("x and y are same boolean")
}
