#!/usr/bin/env python
# coding: utf-8

# In[ ]:


original = input('Masukan kata :')
alay =""
for i in original : 
    if i == 'a':
        alay = original.replace('a','@')
    elif i == 'b':
        alay = original.replace('b','13')
    elif i == 'e':
        alay = original.replace('e','3')
    elif i =='g':
        alay = original.replace('g','9')
    elif i == 'i':
        alay = original.replace('i','!')
    elif i == 'k':
        alay = original.replace('k','l<')
    else :
        original += "";

print(alay)

