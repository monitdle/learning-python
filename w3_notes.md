# Notes of w3-exercises

  
## Some functions
```
	a = """Lorem ipsum dolor sit amet,
	consectetur adipiscing elit,
	sed do eiusmod tempor incididunt
	ut labore et dolore magna aliqua.”""
```
- multiple lines of strings with """ or '''

  
_len()_  
- prints length of a string
  

_in and not in_  
```
	txt = "The best things in life are free”
	print("free" in txt)
	or
	print("free" not in txt)

	# Output: True or False
```

  
_.strip()_  
- removes leading and trailing whitespace
  
  
_.format()_  
```
	age = 36
	txt = "My name is John, and I am {}”
	print(txt.format(age))
```
- {}           holds space for variable
- .format()    returns formatted version, using substitutions marked with ‘{}’

  

  
  
## if-Loops
- if: beginning of loop
- elif: other condition(s)
- else: everything else
- if not
- or
- and
  
  
### Nested If – loops in loops
```
	x = 41
	if x > 10:
	  print("Above ten,")
	  if x > 20:
	    print("and also above 20!")
	  else:
	    print("but not above 20.”)
```
  
  
_pass_  
```
	a = 33
	b = 200
	if b > a:
	  pass
```
if statements cannot be empty but if you for some reason have an if statement with no content  
-> pass to avoid getting error
  
  
  
## for-Loops
  
_continue_  
```
	fruits = ["apple", "banana", "cherry"]
	for x in fruits:
	  if x == "banana":
    	  print(x)
```
In the loop, when the item value is "banana", jump directly to the next item
  
  
_break_  
stops the loop before it has looped through all the items
```
	fruits = ["apple", "banana", "cherry"]
	for x in fruits:
	  print(x)
	  if x == "banana":
	    break
	# Output: 	apple
```

```
	fruits = ["apple", "banana", "cherry"]
	for x in fruits:
	  print(x)
	  if x == "banana":
	    break

	# Output:	apple
			banana
```
  
  
_continue_  
stops current iteration of the loop and continues with the next
```
	fruits = ["apple", "banana", "cherry"]
	for x in fruits:
	  if x == "banana":
	    continue
	  print(x)

	# does not print “banana”
```

  
_range(x)_  
- returns sequence of numbers until x (stop excluded as always)
- start: 0
- steps: 1
- stop = x → excluded
  
_range(y, x)_
- y = start
- x = stop → excluded
  
_range(y, x, z)_  
- z as step (like slicing)
  
  
_else_
- defines what happens when loop ends
- will NOT be executed if the loop is stopped by a break statement → break stronger than else
  
  
### Nested For – loops in loops:
The "inner loop" will be executed one time for each iteration of the "outer loop”

```
	adj = ["red", "big", "tasty"]
	fruits = ["apple", "banana", "cherry"]

	for x in adj:
	  for y in fruits:
	    print(x, y)

	# Output:	red apple
        		red banana
	      		red cherry
      			big apple
      			big banana
      			big cherry
      			tasty apple
      			tasty banana
      			tasty cherry
```
  
_pass_  
same as in for, just to avoid error



## Boolean value Exercises
_bool()_  
Output: True, unless the object is **empty**, **None**, or numerically equal to **zero**


