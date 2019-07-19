#!/usr/bin/env python
# coding: utf-8

# In[197]:

from storeString1 import x
from storeString2 import y
#from storeStrings import s 
import pandas as pd
import re


# =============================================================================
# x = ''
# =============================================================================


# =============================================================================
# def storeString1(inString):
#     global x
#     x = inString
#     
#     # Do something with the string
#     print(inString)
#     return
# =============================================================================

# =============================================================================
# y = ''
# =============================================================================


# =============================================================================
# def storeString2(inString):
#     global y
#     y = inString
#     
#     # Do something with the string
#     print(inString)
#     return
# =============================================================================
# ## importing files as file and dict

# In[129]:


# =============================================================================
# file = pd.read_excel('datafile1.xlsx')
# dict1 = pd.read_excel('Dict.xlsx',names=['Name'])
# =============================================================================

# =============================================================================

# =============================================================================
data_file = x
dict_file = y
file = pd.read_excel(data_file)
dict1 = pd.read_excel(dict_file,names=['Name'])

# #code for appending dicts need to be added here

# ## Define Functions

# In[169]:


def dict_process(df):
    df = df['Name'].tolist()
    low_dict = [x.lower() for x in df]
    
    return low_dict


# In[182]:


def file_process(df):
    processed_body = []
    for i in range (len(df)):
        data = df['Body'][i]
        data = data.replace('\n','').replace('\r','').replace(' | ',' ').replace(',',' ')
        data = data.lower()
        #data = list(data.split())
        processed_body.append(data)
    df['Processed_body'] = processed_body
    return df       
    


# In[249]:


def masking(file, dictionary):
    masked_body = []
    qty = 0
    #dictionary = dictionary['Name']
    for i in range (len(file)):
        data = file['Processed_body'][i]
        data = list(data.split())
        
        sent = []
        for j in range (len(data)):
            word = data[j]
            if word in dictionary :
                qty += 1
                word = list(word)
                for y in range (len(word)):
                    word[y] = 'X'
                word = convert(word)
            else:
                word = word
            sent.append(word)
        
        
        data = convert_fin(sent)
        masked_body.append(data)
        
    file['Masked'] = masked_body
    file = file.drop(['Body','Processed_body'],axis=1)
    file = file[['Subject', 'Masked', 'From_name', 'From address', 'From(type)', 'to name',
       'category', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9' ]]
    
    return file, qty
        
        
def numMasking(file):
    masked_body = []
    qty  = 0
    for i in range (len(file)):
        data = file['Processed_body'][i]
        dictionary = re.findall('[0-9]+',data)
        data = list(data.split())
        
        sent = []
        for j in range (len(data)):
            word = data[j]
            if word in dictionary :
                qty +=1
                word = list(word)
                for y in range (len(word)):
                    word[y] = 'X'
                word = convert(word)
            else:
                word = word
            sent.append(word)
        
        
        data = convert_fin(sent)
        masked_body.append(data)
        
    file['Processed_body'] = masked_body
    
    return file,qty


def emailMasking(file):
    masked_body = []
    qty = 0
    for i in range (len(file)):
        data = file['Processed_body'][i]
        dictionary = re.findall('\S+@\S+',data)
        data = list(data.split())
        
        sent = []
        for j in range (len(data)):
            word = data[j]
            if word in dictionary :
                qty += 1
                word = list(word)
                for y in range (len(word)):
                    word[y] = 'X'
                word = convert(word)
            else:
                word = word
            sent.append(word)
        
        
        data = convert_fin(sent)
        masked_body.append(data)
        
    file['Processed_body'] = masked_body
    
    return file, qty
        


# In[234]:


def convert(s): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x
        #new += " "
  
    # return string  
    return new 





def convert_fin(s): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x
        new += " "
  
    # return string  
    return new 





dictionary = dict_process(dict1)


processed_data = file_process(file)

file,numqty = numMasking(processed_data)
file,emailqty = emailMasking(file)
file, nameqty = masking(processed_data,dictionary)

numqty = "Number of numbers masked  :  " + str(numqty)
emailqty = "Number of emails masked   :  "+ str(emailqty)
nameqty = "Number of Names masked    :  " + str(nameqty)

print(numqty)
print(emailqty)
print(nameqty)
## s is imported from storeStrings module

file.to_excel('Output.xlsx')

