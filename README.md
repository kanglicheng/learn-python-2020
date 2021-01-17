# learn-python-2020

Note: to view this file in VS code, install "markdown preview enhanced" by Yiyi Wang. cmd-shift v (ctrl-shift v)to open preview to side.

###Week 1:
Implement the following: guess_number, mysum, and run_timing from "Python Workout"

Exercise: Write a function that accepts a list of integers and returns the product
i.e multiply_all([2, 3, 3]) -> 18

Homework: Write a function average() that prompts for integer inputs and returns their average. If "K" or "k" is entered, the function exits and returns average of all numbers entered.

average()
please enter a number:
5
5
10
10
K
"average is 7.5"

### week 2

1. **Pig Latin**

- If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the
  word. So “air” becomes “airway” and “eat” becomes “eatway.”
- If the word begins with any other letter, then we take the first letter, put it on
  the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”
  and “computer” becomes “omputercay.”

2. In **Ubbi Dubbi**, every vowel (a, e, i, o, or u) is prefaced with ub.
   Ask the user for a word, and return its Ubbi Dubbi form.
   examples: - elephant -> ubelubephubant. - octopus -> uboctubopubus

3. **running average** Write a function get_average() that prompts the user to enter a sequence of space separated numbers. Return the average of that sequence.
   examples: get_average()
   1 2 3 4 5 6
   "average is 3.5"

### week 3

**Dictionary, set**
Dictionaries are python's hashtables, they store key-value pairs. Sets are also hash-based data structures, they are typically used to maintain a unique collection. A dictionary is created by using a pair of brackets, {}. They are especially useful for tracking information either by accumulation or updates. For example, given a list of words, find the letter(s) that appeared most frequently. Key access is O(1) since the location is determined by hashing and not by scanning. Similarly sets are useful for checking containment in O(1) time, for example, keeping track of visited nodes in graph traversal (bfs, dfs, etc).

1. Total rainfall by city (data organization exercise). Write a function that takes a list of tuples that represent rainfall data collected in the format (city, rainfall) and returns a dictionary displaying each city, and the total rainfall observed.
   example: `get_rainfall([("boston", 10), ("sf", 5), ("seattle", 20), ("sf", 3), ("boston", 5)]) -> {"boston":15, "seattle": 20, "sf":8}`
2. Inventory/menu exercise- Declare a constant menu dictionary with initial values `MENU = {'sandwich': 10, 'tea': 7, 'salad': 9} `. Then write a function take_order() that prompts the user for an item. If the item is available, print "OK" and update the inventory , otherwise if the item is not in the menu or has no inventory left, print "item not available". example: `take_order(), "salad", "salad", "tea",` now `MENU = {'sandwich': 10, 'tea': 6, 'salad': 7} `

3. Write a function most_repeating(words) that takes in a list of words and returns the word with the most repeating letters. Assuming input strings are only lowercase and that there is a single word with highest occurence.
   words = ['this', 'is', 'an', 'elementary', 'test', 'example']
   most_repeating(words) -> "elementary", e is repeated 3 times
4. Write a function, called how_many_different, that
   takes a single list of integers and returns the number of different integers it contains. example: how_many_different([1, 2, 1, 1, 3]) -> 3

### week 4, Classes, Object-oriented programming

- [Introduction to classes](https://docs.python.org/3.7/tutorial/classes.html)
  In this exercise, you’ll define a class, Scoop, that represents a single scoop of ice cream. Each scoop should have a single attribute, flavor, a string that you can initialize
  when you create the instance of Scoop.
  Once your class is created, write a function, not in Scoop class (create_scoops) that creates three instances of the Scoop class, each of which has a different flavor, and puts three instances into a list called scoops (figure 9.2). Finally, iterate over your
  scoops list, printing the flavor of each scoop of ice cream you’ve created.
  i.e my_scoop = Scope("vanilla")
  print(my_scoop.flavor) -> "vanilla"

  **Animals**
  In this exercise, we want to create a set of classes to represent animals in a zoo. We’re going to assume that our zoo contains four different types of animals: sheep,
  wolves, snakes, and parrots. (The zoo is going through some budgetary difficulties, so
  our animal collection is both small and unusual.) Create classes for each of these types, such that we can print each of them and get a report on their color, species, and
  number of legs.

  i.e.
  s = Sheep('white')
  print(s.species)
  print(s.color)
  print(s.number_of_legs)

### Python

- [Beaz practical python course](https://github.com/dabeaz-course/practical-python/blob/master/Notes/Contents.md)
- [Effective Python](https://books.google.com/books?id=bTUFCAAAQBAJ&newbks=1&newbks_redir=0&lpg=PP1&dq=effective%20python&pg=PP1#v=onepage&q=effective%20python&f=false)

### General programming

- [Google technical development guide](https://techdevguide.withgoogle.com/)
- [Structure and Interpretation of Computer Programs](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book.html)
