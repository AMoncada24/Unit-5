'''
############
Do Now 5.01
############

In your Console
---------------
Type the following code:

my_dictionary = {
'cat': 'a domestic feline',
'dog': 'a domestic canine',
'chair': 'furniture piece for sitting',
'car': 'automobile'
}
print(my_dictionary)
print(my_dictionary['dog'])
print(my_dictionary.get('dog'))
print('cat' in my_dictionary)
print('monkey' in my_dictionary)

In your Notebook
----------------
Respond to the following:

Write down what was printed out. What type is my_dictionary? 'dict' type, or dictionary.

Add a line of code that will print the definition of 'chair', then run the code again.

Write down what happens if you use my_dictionary['kittens']? What do you think that error means? It causes a KeyError, which means that it has no defined meaning, or an error in the 'key'.
'''
my_dictionary = {
'cat': 'a domestic feline',
'dog': 'a domestic canine',
'chair': 'furniture piece for sitting',
'car': 'automobile'
}
print(my_dictionary)
print(my_dictionary['dog'])
print(my_dictionary.get('dog'))
print('cat' in my_dictionary)
print('monkey' in my_dictionary)
print(my_dictionary['chair'])