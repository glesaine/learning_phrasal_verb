import pyjarowinkler  # Module implementing the pyjarowinkler metric
from pyjarowinkler import distance

def relevant(string1, string2):
    list1 = string1.split(' ')  # Creating a list of tokens separated by ' '
    list1_copy = deepcopy(list1)  # Avoiding binding
    list2 = string2.split(' ')  # Creating a list of tokens separated by ' '
    list2_copy = deepcopy(list2)  # Avoiding binding
    for token in list1:  # For each token in the first list
        if token in list2_copy:  # If the token is in the copy of list 2 remove in both copies, list2_copy is used to ensure the presence of the token
            list1_copy.remove(token)
            list2_copy.remove(token)
    string1_copy, string2_copy = ' '.join(list1_copy), ' '.join(list2_copy)
    # If one string is included in the other, return original strings
    if (string1_copy == '') or (string2_copy == ''):
        return(string1, string2)
    return(str(string1_copy), str(string2_copy))

    def jw_distance(string1, string2, is_winkler=True):
        if string1 == string2:  # The strings are the same, do not calculate the distances
            return(1)
        # Use the relevant function in order to calculate the distance only between non-identical tokens of the strings
        string1, string2 = relevant(string1, string2)
        return(distance.get_jaro_distance(string1, string2, is_winkler))
