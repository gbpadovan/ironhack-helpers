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

from IPython.display import Markdown, display
import re

def pprint_sql(query = ''):
    """
    Print the visualization of a formatted SQL query in a Jupyter Notebook.
    
    Params:
    ------
    query: str, default = ''
        The SQL query to be formatted and printed in Jupyter Notebook.
    
    Usage:
        pprint_sql('SELECT * FROM TABLE WHERE product_id = 1') 

    Future improvements: 
        - Accept any query-like language.
        - Automatically indent code
    """
     
    display(Markdown(f'''```mysql\n {query}```'''))
    
    return

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
        
    Usage:
        text = 'for i in range(10):
                    for j in range(20):
                        mylist.append( i * j )'
        loop2compr(text)

    Params:
    ------
        forloop: string
        Text containing the for-loop
    
    Returns:
    -------
        String containing the list-comprehension of a given for-loop
    """
    # Tokens
    content_pattern = r'append(.*)'
    list_pattern = r'(\w+.?\d?\(?\)?).append'
    item_pattern = r'for (\w\d*\.?\w*\(?\'?\w*\d*\'?\)?)'
    iterator_pattern = r'in (\w+\.?\d?):'
    condition_pattern = r'if (.*?):'
   
    # Parser
    content = re.findall(content_pattern, text)
    list_result = re.findall(list_pattern, text)
    item = re.findall(item_pattern, text)
    iterator = re.findall(iterator_pattern, text)
    condition = re.findall(condition_pattern, text)

    parsed_list = [
            ['['], 
            [i for i in content], 
            [f'for {i} in {j} ' for (i,j) in zip(item,iterator) ],
            [f'if {i}' for i in condition],
            [']'] 
        ]

    # Code Generator
    print(" ".join([j for i in foo for j in i]))


def normalize_cols(df, inplace=False):
    """
    Normalize column names in a dataframe.

    This function changes the name of each Data Frame column replacing 
    whitespace with underline (except at word ends, where it is stripped) 
    and all letters in lower case.
    
    Params 
    ------
        df: pandas DataFrame 
            Dataframe for the column name normalization            
        inplace: bool, optional
            Whether to return a new dataframe containing the changes or 
            to make the changes in the dataframe itself.
    """
    col_names = [ col.strip().replace(' ','_').lower() for col in df.columns ]
    mapper = dict(zip(df.columns, col_names))
    
    return df.rename(columns=mapper, inplace=inplace)

