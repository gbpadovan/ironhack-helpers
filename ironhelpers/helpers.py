"""
Mini-library to collect some helper functions for daily use.

The idea is to start by slowly developing functions that will
help in daily use. We can start by just defining functions and 
importing the package and later we can restructure the full 
library in a better design. It can be an opportunity to 
learn the development of a code as a team as well as some 
design patterns.

Also, everyone is welcome to join the fun.
"""


def loop2compr(forloop = ''):
    """
    Return a string containing the list-comprehension for a given for loop (given as a string as well)
    
    This function accepts a string containing the information of a foor-loop and tries to transform it 
    into the representation of a list-comprehension.
    It accepts a for-loop syntax containing:
        - any number of FORs (ex.:' for i in myList: 
                                       for j in myOtherList: ...' )
        - items in a for containing numbers (ex.: 'for i2 in myList:')
        - results stored as an append in a list (ex.: 'myList.append(i)') 
        - 


    Params:
    ------
        forloop: string
        Text containing the for-loop
    
    Returns:
    -------
        String containing the list-comprehension of a given for-loop
    """

    content_pattern = r'append(.*)'
    list_pattern = r'(\w+.?\d?\(?\)?).append'
    item_pattern = r'for (\w\d*\.?\w*\(?\'?\w*\d*\'?\)?)'
    iterator_pattern = r'in (\w+\.?\d?):'
    condition_pattern = r'(if .*):'

    content = re.findall(pattern, text)
    list_result = re.findall(list_pattern, text)
    item = re.findall(item_pattern, text)
    iterator = re.findall(iterator_pattern, text)
    condition = re.findall(condition_pattern, text)

    
