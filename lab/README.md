<img src="https://i.imgur.com/DPzk4Ok.png">

# Python Containers - Lab

**This lab is NOT deliverable**

## Setup

create an excerise.py file in your lab folder, check your answers by running it with `python3 exercise.py`

## Exercises

#### Exercise 1

- Create a list named `students` containing some student names (strings).
- Print out the second student's name.
- Print out the last student's name.

#### Exercise 2

- Create a tuple named `foods` containing the same number of foods (strings) as there are names in the `students` list.
- Use a `for` loop to print out the string "_food goes here_ is a good food".

#### Exercise 3

- Using a `for` loop, print just the last two food strings from `foods`.

#### Exercise 4

- Create a dictionary named `home_town` containing the keys of `city`, `state` and `population`.
- Print a string with this format:<br>"I was born in _city_, _state_ - population of _population_"

#### Exercise 5

- Iterate over the _key: value_ pairs in `home_town` and print a string for each item, for example:<br>"city = Arcadia"<br>"state = California"<br>"population = 58000"

#### Exercise 6

- Create an empty list named `cohort`.
- Using a `for` loop, add one dictionary to the `cohort` list for each student name. Each dictionary should have this shape:

 ```python
 {
   'student': 'Tina',
   'fav_food' 'Cheeseburger'
 }
 ```

- Iterate over `cohort` printing out each element.

#### Exercise 7

- Using the list of `students` and list comprehension, assign to a variable named `awesome_students` a new list containing strings similar to this:<br>`["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]`
- Iterate over `awesome_students` printing out each string.

#### Exercise 8

- Using the tuple `foods` and list comprehension within a `for` loop, print each food string that contains the letter `a`.

## Solution

A solution can be found [here](https://replit.com/@jim_clark/Python-Containers-Lab-Example-Solutions#exercises.py).


# Hungry for more?

## try these exercises

# Exercises

## Exercise 1: List Manipulation and Slicing
1. Create a list named `numbers` containing the integers from 1 to 20.
2. Print the first five elements of the `numbers` list.
3. Print the last five elements of the `numbers` list.
4. Create a new list named `even_numbers` that contains only the even numbers from the `numbers` list using slicing.
5. Replace the middle element of the `numbers` list with the string "middle" and print the modified list.

## Exercise 2: Tuple Operations
1. Create a tuple named `fruits` containing five different fruit names.
2. Print the second and third elements of the `fruits` tuple.
3. Create a new tuple named `more_fruits` by concatenating the `fruits` tuple with another tuple containing three more fruit names.
4. Check if the fruit "apple" is in the `more_fruits` tuple and print an appropriate message.
5. Convert the `more_fruits` tuple to a list, sort it alphabetically, and print the sorted list.

## Exercise 3: Ranges and List Comprehension
1. Create a list named `squares` containing the squares of numbers from 1 to 10 using a list comprehension.
2. Create a list named `cubes` containing the cubes of numbers from 1 to 10 using a list comprehension.
3. Create a list named `odd_numbers` containing the odd numbers from 1 to 20 using the `range` function.
4. Create a list named `divisible_by_five` containing the numbers from 1 to 50 that are divisible by 5 using the `range` function.
5. Print the first five elements of the `squares` list and the last five elements of the `cubes` list.

## Exercise 4: Slicing and Ranges
1. Create a list named `letters` containing the first 10 letters of the alphabet.
2. Print every second letter from the `letters` list.
3. Print the `letters` list in reverse order using slicing.
4. Create a list named `first_half` containing the first half of the `letters` list.
5. Create a list named `second_half` containing the second half of the `letters` list.

## Exercise 5: Combining Lists and Tuples
1. Create a list named `names` containing five different names.
2. Create a tuple named `ages` containing five different ages corresponding to the `names` list.
3. Use a for loop to print out each name along with their corresponding age.
4. Create a new list named `name_age_pairs` containing tuples, where each tuple is a pair of a name and an age from the `names` list and `ages` tuple.
5. Sort the `name_age_pairs` list by age and print the sorted list.

