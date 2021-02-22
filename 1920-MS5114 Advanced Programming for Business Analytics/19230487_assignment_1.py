# MS5114 Advanced Programming for Business Analytics - Assignment 1

# Studnet Name : Jayakarthi Boovendran
# StudentID : 19230487
# Course: MBY



# 1. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
    output="Number of donuts: "+str(count)
    if count>=10:
        output="Number of donuts: many"
    return output


# 2. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
    if len(s)>=2:
      return s[0:2]+s[-2:]
    else:
      return ''


# 3. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
    firstChar=s[0]
    s=s.replace(firstChar,'*')
    return firstChar+s[1:]


# 4. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
    return b[0:2]+a[2:]+' '+a[0:2]+b[2:]


# 5. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
  count=0
  for word in words:
    if (len(word)>=2 and word[0]==word[-1]):
      count=count+1
  return count


# 6. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
  list1=[]
  list2=[]
  for word in words:
    if word[0]=='x':
      list1.append(word)
    else:
      list2.append(word)
  list1.sort()
  list2.sort()
  return list1+list2


# 7. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
    tuples.sort(key=lambda tup:tup[-1])
    return tuples


# 8. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    if len(a)%2==0:
        a_front=a[0:len(a)//2]
        a_back=a[len(a)//2:]
    else:
        a_front=a[0:(len(a)//2)+1]
        a_back=a[(len(a)//2)+1:]

    if len(b)%2==0:
        b_front=b[0:len(b)//2]
        b_back=b[len(b)//2:]
    else:
        b_front=b[0:(len(b)//2)+1]
        b_back=b[(len(b)//2)+1:]
    
    return a_front+b_front+a_back+b_back


# 9. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    for item in list2:
        list1.append(item)
    list1.sort()
    return list1


# 10.
#  Write a function called accept_login(users, username, password) with three parameters:
# users a dictionary of username keys and password values (already created below),
# username a string for a login name and password a string for a password.
# The function should return
# True if the user exists and the password is correct and False otherwise.

users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}


def accept_login(users, user, password):
    if(user in users.keys()and users[user]==password):
        return True
    else:
        return False


# 11.
# Write a function called
# find_value(mydict, val)
# that accepts a dictionary called mydict (already created below) and a variable of any type called
# val. The function should return a list of keys that map to the value val in mydict.
mydict = {
    "day1": "sunny",
    "day2": "rainy",
    "day3": "sunny"
}


def find_value(mydict, val):
    result=[]
    for key in mydict.keys():
        if(mydict[key]==val):
            result.append(key)
    return result


# 12. Write a function to invert a dictionary. It should accept a dictionary as a parameter and return a
# dictionary where the keys are
# values from the input dictionary and the values are lists of keys from the input dictionary.
# For example, this input:
# { "key1" : "value1", "key2" : "value2", "key3" : "value1" }
# should return this dictionary:
# { "value1" : ["key1", "key3"], "value2" : ["key2"] }

my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value1"
}


def invert_dict(my_dict):
    keys=my_dict.keys()
    values=my_dict.values()
    new_dict=dict({})
    keylist=[]
    for key1 in keys:
      for key2 in keys:
        if(my_dict[key1]==my_dict[key2] and key1!=key2):
          keylist.append(key2)
      if len(keylist)>1:
        keylist.sort()
        new_dict[my_dict[key1]]=keylist
        keylist=[]
      else:
        list2=[]
        list2.append(key1)
        new_dict[my_dict[key1]]=list2
    return new_dict



# 13.
# Write a function called word_frequencies(mylist) that accepts a list of strings
# called mylist and returns a dictionary where
# the keys are the words from mylist and the values are the number
# of times that word appears in mylist:
# INPUT
mylist = ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'e']


# OUTPUT
# {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}


def word_frequencies(mylist):
    Dict=dict({})
    for key in mylist:
        count=0
        for string in mylist:
            if(key==string):
                count=count+1
        Dict[key]=count
    return Dict




def test_donuts():
    print('Calling donuts function with different values:')
    print(donuts(4))
    # it must return 'Number of donuts: 4'
    print(donuts(9))
    # it must return 'Number of donuts: 9'
    print(donuts(10))
    # it must return 'Number of donuts: many'
    print(donuts(99))
    # it must return 'Number of donuts: many'


def test_both_ends():
    print('Calling both_ends function with different values:')
    print(both_ends('spring'))
    # it must return 'spng'
    print(both_ends('Hello'))
    # it must return 'Helo'
    print(both_ends('a'))
    # it must return ''
    print(both_ends('xyz'))
    # it must return 'xyyz'


def test_fix_start():
    print('Calling fix_start function with different values:')
    print(fix_start('babble'))
    # it must return 'ba**le'
    print(fix_start('aardvark'))
    # it must return 'a*rdv*rk'
    print(fix_start('google'))
    # it must return 'goo*le'
    print(fix_start('donut'))
    # it must return 'donut'


def test_mix_up():
    print('Calling mix_up function with different values:')
    print(mix_up('mix', 'pod'))
    # it must return 'pox mid'
    print(mix_up('dog', 'dinner'))
    # it must return 'dig donner'
    print(mix_up('gnash', 'sport'))
    # it must return ''spash gnort''
    print(mix_up('pezzy', 'firm'))
    # it must return 'fizzy perm'


def test_match_ends():
    print('Calling match_ends function with different values:')
    print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
    # it must return 3
    print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
    # it must return 2
    print(match_ends(['aaa', 'be', 'abc', 'hello']))
    # it must return 1


def test_front_x():
    print('Calling front_x function with different values:')
    print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
    # it must return ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
    # it must return ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))
    # it must return ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']


def test_sort_last():
    print('Calling sort_last function with different values:')
    print(sort_last([(1, 3), (3, 2), (2, 1)]))
    # it must return [(2, 1), (3, 2), (1, 3)]
    print(sort_last([(2, 3), (1, 2), (3, 1)]))
    # it must return [(3, 1), (1, 2), (2, 3)]
    print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))
    # it must return [(2, 2), (1, 3), (3, 4, 5), (1, 7)]


def test_front_back():
    print('Calling front_back function with different values:')
    print(front_back('abcd', 'xy'))
    # it must return 'abxcdy'
    print(front_back('abcde', 'xyz'))
    # it must return 'abcxydez'
    print(front_back('Kitten', 'Donut'))
    # it must return 'KitDontenut'


def test_linear_merge():
    print('Calling linear_merge function with different values:')
    print(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']))
    # it must return ['aa', 'bb', 'cc', 'xx', 'zz'])
    print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))
    # it must return ['aa', 'bb', 'cc', 'xx', 'zz'])
    print(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']))
    # it must return ['aa', 'aa', 'aa', 'bb', 'bb'])


def test_accept_login():
    print('Calling accept_login function with different values:')
    print(accept_login(users, 'user1', 'password1'))
    # it must return True
    print(accept_login(users, 'mary', 'password1'))
    # it must return False
    print(accept_login(users, 'user2', 'password1'))
    # it must return False


def test_find_value():
    print('Calling find_value function with different values:')
    print(find_value(mydict, 'sunny'))
    # it must return ['day1', 'day3']
    print(find_value(mydict, 'rainy'))
    # it must return ['day2']
    print(find_value(mydict, 'cloudy'))
    # it must return []


def test_invert_dict():
    print('Calling invert_dict function with different values:')
    print(invert_dict(my_dict))
    # it must return { "value1" : ["key1", "key3"], "value2" : ["key2"] }
    my_dict_2 = {
        'week1': 'workout1',
        'week2': 'workout2',
        'week3': 'workout1',
        'week4': 'workout3'
    }
    print(invert_dict(my_dict_2))
    # it must return {'workout1': ['week1', 'week3'], 'workout2': ['week2'], 'workout3': ['week4']


def test_word_frequencies():
    print('Calling word_frequencies function with different values:')
    print(word_frequencies(mylist))
    # it must return {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
    my_word_list = 'The greatest glory in living lies not in never falling but in rising every time we fall'.split()  # by Nelson Mandela
    print(word_frequencies(my_word_list))
    # it must return {'The': 1, 'greatest': 1, 'glory':1, 'in': 3, 'living':1, 'lies':1, 'not': 1, 'never': 1,
    # 'falling': 1, 'but': 1, 'rising':1, 'every': 1, 'time':1, 'we': 1, 'fall': 1}


if __name__ == '__main__':
    print('1\n')
    test_donuts()
    print('\n2\n')
    test_both_ends()
    print('\n3\n')
    test_fix_start()
    print('\n4\n')
    test_mix_up()
    print('\n5\n')
    test_match_ends()
    print('\n6\n')
    test_front_x()
    print('\n7\n')
    test_sort_last()
    print('\n8\n')
    test_front_back()
    print('\n9\n')
    test_linear_merge()
    print('\n10\n')
    test_accept_login()
    print('\n11\n')
    test_find_value()
    print('\n12\n')
    test_invert_dict()
    print('\n13\n')
    test_word_frequencies()
	
