
# Python

A brief description of what this project does and who it's for

#### Take input from user
    var1=input("Enter your input")
    print(var1)
#### To check datatype
    print(type(50.2))
#### Will tell memory space location
    print(id(10))

#### Data structures in python
    str(), int(), float(), list(), tuple(), dict(), set()
#### If coniditon
    age=35
    if age>18:
        print('Eligible');
    elif age<18 :
        print('Not eligible');
    else :
        print('Out of the league');

#### For loop 
    for x in range(0,10):
        print(x)

    output->0,9
#### For each loop
    for x in range(1,10):
        print(x)
    output->1,9
##### For each but iterating by 3
    for x in range(1,10,3):
        print(x)
    output->1,4,7
##### While loop
    x=20
    while x<=20:
        print(x)
        x+=10
#### Working with OS
    import os 

    os.system('clear') 
        to clear previous content
    
    os.system('whoami')
        user ka name dedega

    for x in range(2):
        os.makedirs(str(x))
    os.system('ls -a')

    print(os.getcwd()) -> current working directory

    import os
    os.system('echo print \( \\"Hello World \\" \) >test.py')
    os.system("python3 test.py")


#### Array in python
    x=[]
    for a in range (1,21):
        x.append(a) 
    print(a)  ->output 20 dega jo length h list ki kyuki last value to 20 gyi hai isme
    print(type(a)) -> int aaya kyuki integer value jaa rhi h

    print(x) -> list dega puri
    print(type(x)) -> list type aayega

    x=[]
    for a in range (1,21):
        x.append(a) 
    print(x[:6]) -> 1,2,3,4,5,6 -->0 to 5 dega aur 6 excluded rhega 

#### Playing with array (imp)
    
    x=[]
    for a in range (1,21):
        x.append(a) 
    print(x[2:6:2]) -> 3,5
    [starting_index: last_index: increment]
    last_index consider nhi hoga
#### Strings with for each
    x='Shubham'
    for a in x :
        print (a)
    -> iterate krega sbko

#### print(set(x)) -> m,h,a,b,s,u -> remove duplicate (random honge) 

#### print(tuple(x))-> S,h,u,b,h,a,m

    []->list
    {}->dict -> key value pair
    ()->tuple
    {}->set

    mutability and immutability
    string , tuple -> mutability

#### Extra Info but important
    __init__.py -> 2 underscore -> saare package bnaliye but dunder zaruri h -> isme bina package nhi dikhega
    .pyc file is executable file (hexadecimal format)

    magic headers library or database -> hr file ke starting or end me kuch bytes hote h jo decide krta h ki file ka nature kya h

    using for loop and range function print 1 to 10 in reverse order

    __iter__ and __next__ -> ye kisi me bhi ho toh vo iterator h
    __next__ agli value ko point krta h

    del varName -> do deallocate memory

#### Playing with string
    str.replace('a','s')
    str.count('b')
    str.find('abc')
    str.upper('abc')
    str.lower('abc')
    str.startwith('abc')
    str.endwith('abc)

    y='https://www.geeksforgeeks.org/program-print-ascii-value-character/'
    if y.startswith('https') : print('true') 
    else : print('false')

    str.split('a')
    str.isaplha()
    str.istitle()
    str.isspace()
    str.isalnum()

    str.strip()
    str.lstrip()
    str.rstrip()
    spaces htane ke liye (beech ki nhi)
    str.split(',') string ko todne ke liye

    y='https://www.google.co.gov.cn.in.en.uk/home.php'
    a=y.replace("https://www.","")
    OR
    a=y.replace("https","").replace("://","").replace("www.","")
    output=a[a.find("."):].split("/")[0]
    print(output)   

#### Time function
    print (time,time()) 
        -> epoch date se time dega in mili seconds

    timestamp=1628379223
    print(time.gmtime(timestamp))
    print(time.localtime(timestamp))

    time.sleep(10)

    current_time=time.localtime()
    formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",current_time)
    print(formatted_time)

    strftime 
        -> for time formatting

#### pypi -> python package index
#### Function
    def printing(name):
        print("The name is",name,"\t Codex",name)
    printing ("ITER")


#### Main function
    print(__name__) -> __main__
    print(type(__name__)) -> str

    if __name__=="__main__":
        funcName()

#### _ -> underscore can be a variable also and behaves like a variable

    def many_args(*args):
        ->jb hmein pta na ho ki user kitne arguments daalne wala hoga
#### Playing with functions
    def printing(name,*data):
        print("The name is",name,"and the data is",data)
    printing ("Shubham",200588,"D&I","Gurgaon")

    def example(name="Codex")
    print(name)
    example("Iter")
        ->ye over write krdega codex ko
    example()
        -> ye codex hi dedega

    def funcName (name,clas,age=12)
    print(name,clas,age)
    funcName("Shubham","MCA")
        ->This will work. not below one
    def funcName (name,age=12,clas)
    print(name,clas,age)

        ->will not work
    def test(**var1):
        print(type(var1))
    test("a","b","c")
        ->will work and will give dictonary
    def test(**var1):
        print(type(var1))
        print(var1['a'])
    test(a="a",b="b",c="c")

#### Anonymous Function
    add = lambda x,y:x+y
    result=add(3,5)
    print(result)
        ->used for one time operations
    
        Extra knowledge

    def x(name):
        print(name)
    a=xb
    a("shubham")

    def x(name):
        print(name)
    a=x("shubham")

#### Create a variable of type function
    def x(name):
        print(name)
    a=x
    a("shubham")
    print(type(a))
    print(type(x))

#### def x(): pass ->empty function

####Import in python
    import moduleName as m
    import moduleName
    from moduleName import var,func,abc
    from moduleName import *
    from moduleName import * as x
    from packageName.className import funcName
#### List in python
    Reverse a list
    fruits = ['apple', 'banana', 'cherry']
    fruits.reverse()
    print(fruits)

    reverse a string
    str1='abcdefgh'
    str1=reversed(str1)
    a=''
    for x in str1:
        a+=x
    print(a)
#### Set in python
    set.add('value')-> to insert value
    set.pop() -> to delete first value
#### Dictionary in python
    dictionary={'key':value}
    dictionary = {'g': 1, 'e': 2, 'k': 3, 's': 4}
    dictionary.update({'si':5,'wgqh':6})
    print(sorted(dictionary))
    for x in dictionary.values():
        print(x)
    ->to print values only
    for key in dictionary:
        print(key,":",dictionary[key])
    -> to print pair
    for values in dictionary:
        print(values,":",dictionary[values])
    dictionary.pop('g') -> to delete


#### FILE HANDLING
    f=open("filename","mode")
    with open("test.abc","w+") as F:
        F.write("Hello everyone")

    Modes :
    r ->read only
    w -> write only
    a -> append only (update a file)
    a+ -> append plus read
    r+ -> read plus write
    w+ -> write plus read
    wb -> write binary
    rb -> read binary
    rw -> read write

    f.closed -> file open h ya closed
    f.mode -> kis mode me file opened h
    f.name-> give the name of file
    f.seek(24)-> utne byte pr jump krna
    f.tell -> position on file


#### Map in python
    map(arg1,arg2)
    map(x,[1,2,3])

#### RHA se LHA map krne ke liye map() use hota h
#### RHA->Right hand argument

#### 10 values input and map with function double krde
    1st option ->
                def x(val) : print(val*2)
                [print(a) for a in map(x,[1,2,3,4,5,6,7,8,9,10])]   
    2nd option ->
                [print(a) for a in map(lambda b: print(b*2),[1,2,3,4,5,6,7,8,9,10])]   


    [print (x) if x>10 ]-> if(x>10) : print(x)
    [ print(x) for x in range(20) ] -> for x in range(20) print(x)


#### global variable
    global pi
    pi=3.14 -> function me global rhega
#### decorator
    @decorator
    def login_check():
        #check
        #if logged in
        #or not

    def a():
        login_check()
        pass

    @login_check
    def b():
        #this is b
        login check fail hogya toh b nhi chlega agr pass hogya toh phle login_check chlega then b chlega 

