##1.roots of quadratic
##2.Area of a regular polygon
##3.Arc length
##4.Capitalize first and last word
##5.swapcase words in list
##6.split
##7.Occurence

def main():
      print("THIS COMPREHENSIVE PROGRAM CONTAINS ESSENTIAL PYTHON PROGRAMS NEEDED FOR CLASS 12th STUDENT(CBSE BOARD)")





main()



################       MAKING BASIC SEQEUNTIAL DATATYPES USING FUNCTIONS       ###################

import sequencemakerpro

############   SORTING LISTS IN PYTHON    ####################

import sorterpro

##############################################################






def filemaker(filename,typ=''):
      filename=str(filename)
      if typ=='text':
            filename=filename+'.txt'
      elif  typ=='binary':
          filename=filename+'.dat'
      elif  typ=='csv':
          filename=filename+'.dat'
      elif  typ=='csv':
          filename=filename+'.dat'
      else:
          pass
      with open(filename,'w') as fh:
          pass


def string(choice):
    print(choice)
    if choice =='1':
        print("You Have Chosen String Slicing Operation")
        str1=input("Enter the string:")
        strt=int(input("Enter the starting index:"))
        stop=int(input("Enter the stopping index:"))
        step=int(input("Enter step value (Optional): "))
        fstr=str1[strt:stop:step]
        print("The Sliced String is: ",fstr)
    elif choice =='2':
        print("You Have Chosen Unpacking A String Operation")
        ch=input("Would You Like To Unpack Your String As A List or Tuple (L/T): ")
        if ch.upper() == "L":
            str1=input("Enter the string: ")
            print(list(str1))
        elif ch.upper() == "T":
            str1=input("Enter the string: ")
            print(tuple(str1))
    elif choice =='3':
        print("You Have Chosen To Use Built-in String Operators")
        print("""Here Are The Available String Operators
                1.isalpha()
                2.isdigit()
                3.lower()
                4.islower()
                5.upper()
                6.isupper()
                7.lstrip() or lstrip(chars)
                8.rstrip() or rstrip(chars)
                9.isspace()
                10.istitle()
                11.join(sequence)
                12.swapcase()
                13.partition(separator)
                14.ord()
                15.chr()""")
        ch= input("Enter Your desired choice(1-15): ")
        ch=ch.lower()
        str1=input("Enter Your Desired String ")
        if ch=='1':
            print("You Have Selected The isalpha() Function")
            print(str1.isalpha())
        elif ch=='2':
            print("You Have Selected The isdigit() Function")
            print(str1.isdigit())
        elif ch=='3':
            print("You Have Selected The lower() Function")
            print(str1.lower())
        elif ch=='4':
            print("You Have Selected The islower() Function")
            print(str1.islower())    
        elif ch=='5':
            print("You Have Selected The upper() Function")
            print(str1.upper())
        elif ch=='6':
            print("You Have Selected The isupper() Function")
            print(str1.isupper())
        elif ch=='7':
            print("You Have Selected The lstrip() or with chars Function")
            char=input("Enter string charectors to exclude from left side (Optional: )")
            print(str1.lstrip(char))
        elif ch=='8':
            print("You Have Selected The rstrip() or with chars Function")
            char=input("Enter string charectors to exclude from right side (Optional: )")
            print(str1.rstrip(char))
        elif ch=='9':
            print("You Have Selected The isspace() Function")
            print(str1.isspace())
        elif ch=='10':
            print("You Have Selected The istitle() Function")
            print(str1.istitle())
        elif ch=='11':
            print("You Have Selected The join(sequence) Function")
            sequence=input("Enter Your string separator: ")
            print(sequence.join(str1))
        elif ch=='12':
            print("You Have Selected The swapcase() Function")
            print(str1.swapcase())
        elif ch=='13':
            print("You Have Selected The partition() Function, This returns a tuple")
            separator=input("Enter Separator string: ")
            print(str1.partition(separator))
        elif ch=='14':
            print("You Have Selected The ord() Function")
            print(ord(str1))
        elif ch=='15':
            print("You Have Selected The chr() Function")
            print(chr(str1))
        else:
             print("Invalid choice, Enter a value between 1-15")


def lists(choice):
    if choice =="1":
        print("Out of context and too complex hence left out, sincere apologies")
    elif choice =="2":
        print("You Have Chosen List Slicing")
        l1=listmaker()
        print("This is the created list: ",l1)
        strt=int(input("Enter the starting index:"))
        stop=int(input("Enter the stopping index:"))
        stch=input("Do you need slice the list in steps-? (y/n): ")
        if stch.lower()=='y':
            step=int(input("Enter step value: "))
            flist1=l1[strt:stop:step]
            print("The Sliced String is: ",flist1)
        else:
            flist=l1[strt:stop]
            print(flist)
    elif choice=='3':
        print("You Have Chosen To Use Built-in List Operators")
        print("""Here Are The Available List Operators
                1.cmp()
                2.len()
                3.max()
                4.min()
                5.list()
                6.sum()
                7.append()
                8.index()
                9.sort()
                10.remove()
                11.reverse()""")
        ch= input("Enter Your desired choice(1-15): ")
        ch=ch.lower()
        if ch=='1':
            print("You Have Selected The cmp() compares two listFunction")
            print(cmp(l1,l1))
        elif ch=='2':
            print("You Have Selected The len() Function")
            print(len(l1))
        elif ch=='3':
            print("You Have Selected The max() Function")
            print(max(l1))
        elif ch=='4':
            print("You Have Selected The min() Function")
            print(min(l1))    
        elif ch=='5':
            print("You Have Selected The list() (converts tuple/strings to list) Function")
            string=input("Here only strings are used,input a string to convert it into a list: ")
            print(list(string))
        elif ch=='6':
            print("You Have Selected The sum() Function, only for lists with all numeric values")
            print(sum(l1))
        elif ch=='7':
            print("You Have Selected The append() Function, this adds a values/element to the end of the list")
            y=input("Is the element to be a number or not(y/n): ")
            if y.lower=='y':
                ele=int(input("Enter a numeric value to append to list: "))
                l1.append(ele)
            else:
                ele=input("Enter a element to append to the list: ")
                l1.append(ele)
        elif ch=='8':
            print("You Have Selected The sort() Function")
            print(l1.sort())
        elif ch=='9':
            print("You Have Selected The remove() Function, This removes the firt occurence of an element from a list")
            ele=input("Enter the element to remove")
            l1=l1.remove(ele)
            print(l1)
        elif ch=='10':
            print("You Have Selected The reverse() Function")
            print(l1.reverse())

    elif choice == '4':
        l1=listmaker()
        print("The created list is",l1)
        j=int(input("How many copies do you need to create?: "))
        k=0            
        while k<=j:
            k+=1
            newl1=l1.copy()
            print(newl1)


def tuples():
    print("1.Iterating through a tuple \n2.Tuple Slicing \n3.Member ship checking")
    choice=input("Enter you choice: ")
    if choice =="1":
        print("You have chosen to display all the of the tuple using a loop")
        t=tuplemaker()
        for i in t:
            print(i)
    elif choice=='2':
        print("You have chosen tuple slicing operation")
        t=tuplemaker()
        print("This is the created tuple: ",t)
        strt=int(input("Enter the starting index:"))
        stop=int(input("Enter the stopping index:"))
        stch=input("Do you need slice the tuple in steps-? (y/n): ")
        if stch.lower()=='y':
            step=int(input("Enter step value: "))
            ftuple1=t[strt:stop:step]
            print("The Sliced String is: ",ftuple1)
        else:
            ftuple=l1[strt:stop]
            print(ftuple)
    elif choice=='3':
        print("You have selected the membership checking operation")
        t=tuplemaker()
        e=input("Enter the element to search")
        if e in t == True:
            print(e,"is present in the tuple at the index",t.index(e))


def dictionary(ch):
    if ch =='1':
        print("You have chosen to update a dictionary: ")
        x=input("Do wish to create a dictionary or use a premade one to test the software-? (y/n): ")
        if x.lower()=='y':
            dict1=dictionarymaker('dict')
            print("This will be your dictionary: ", dict1)
        elif x.lower()=='n':
            print("This will be your dictionary")
            print("Your Dictionary will have famous gun names as keys and their rate of fire as the values respectively")
            print("Note: Here rpm stands for rounds per minute")
            Dictionary={"M4-Carbine":"700-900rpm","Browning M2":"500-600rpm","Kalashnikov Ak-47":"600rpm","Ak-74":"600rpm","Gau-8/A Avenger":"3900rpm"}
            print("Your Dictionary will be,",Dictionary)       
        k=input("Enter the key whose value you wish to change: ")
        v=input("Enter new value to be assigned to the key: ")
        Dictionary[k]=v
        print("The updated dictionary is, ", Dictionary)

    elif ch=='2':
        print("You have chosen to display all the of the dictionary using a loop")
        x=input("Do wish to create a dictionary or use a premade one to test the software-? (y/n): ")
        if x.lower()=='y':
            dict1=dictionarymaker('dict')
            print("This will be your dictionary: ", dict1)
        elif x.lower()=='n':
            print("This will be your dictionary")
            print("Your Dictionary will have famous gun names as keys and their rate of fire as the values respectively")
            print("Note: Here rpm stands for rounds per minute")
            Dictionary={"M4-Carbine":"700-900rpm","Browning M2":"500-600rpm","Kalashnikov AK-47":"600rpm","AK-74":"600rpm","GAU-8/A Avenger":"3900rpm"}
            print("Your Dictionary will be,",Dictionary)
            print('\n\n')
        for i in Dictionary:
            print(i)
        e=input("Do you wish to iterate through the values and display them? (y/n): ")
        if e.lower()=='y':
            ks=Dictionary.values()
            for i in ks:
                print(i)
        else:
            pass
    elif ch=='3':
        print("You have chosen to use built-in dictionary functions")
        print("""Here Are The Available Dictionary Operators
                1.cmp()
                2.len()
                3.str()
                4.type()
                5.clear()
                6.copy()
                7.items()
                8.update()
                9.values()
                """)
        ch= input("Enter Your desired choice(1-9): ")
        ch=ch.lower()
        if ch=='1':
            d1=dictionarymaker('dict')
            d2=dictionarymaker('dict')
            print("You Have Selected The cmp() compares two Dictionaries")
            print(cmp(d1,d2))
        elif ch=='2':
            print("You Have Selected The len() Function")
            print(len(dictionarymaker('dict')))
        elif ch=='3':
            print("You Have Selected The str() Function")
            print(str(dictionarymaker()))
        elif ch=='4':
            print("You Have Selected The type() Function")
            print(type(Dictionary))
        elif ch=='5':
            print("You Have Selected The clear() Function")
            d=dictionarymaker('dict')
            print("dictionary before clearing,",d)
            d.clear()           
            print("dictionary after clearing,",d)
        elif ch =='6':
               d1=dictionarymaker()
               print("The created dictionary is",d1)
               j=int(input("How many copies do you need to create?: "))
               k=0
               while k<=j:
                   k+=1
                   newd1=d1.copy()
                   print(newl1)
        elif ch=='7':
            print("You Have Selected The item() Function")
            d=dictionarymaker('dict')
            print(d.items())
        elif ch=='8':
           print("You Have Selected The update() Function, (adds two dictionaries together)")
           d1=dictionarymaker('dict')
           d2=dictionarymaker('dict')
           print(d1.update(d2))
        elif ch=='9':
            print("You Have Selected The values() Function, returns a list of all values inside the dictionary")
            d=dictionarymaker('dict')
            print(d.values())




