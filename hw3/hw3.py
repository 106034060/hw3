
# coding: utf-8

# In[20]:


print("Please type anything")
stri=input()
num=dict()
x=0
for i in range(len(stri)):
    for j in range(len(stri)):
        if stri[i]==stri[j]:
            x=x+1
    num[stri[i]]=x
    x=0
for item in num.items():
    letter,number=item
    print("\""+letter+"\"",":",number)

