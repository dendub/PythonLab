def first():
    print("Enter number of cookies:")
    num = input()
    if int(num) <= 9:
        print("Number of cookies:" + num)
    else:
        print("Too many cookies")

def second():
    print("Enter a string:")
    str1 = input()
    print (str1[1:-1]) #Принтит стринг без указанах char

def third():
    strduplicate = ""
    print("Enter a first string:")
    str1 = input()
    print("Enter a second string:")
    str2 = input()
    strduplicate = str1
    str1 = str2[:1] + str1[1:]
    str2 = strduplicate[:1] +str2[1:]
    print("First:")
    print(str1)
    print("Second:")
    print(str2)

def fourth():
    strings = ["malina", "banan", "moloko", "korovak", "kurica", "hlebh"]
    for x in range(len(strings)):
        if len(strings[x]) > 2 and strings[x][0] == strings[x][-1:]:
            print(strings[x])

def fifth():
    list1 = ["xmalina", "xklubnika", "xananas"]
    list2 = ["xkartocha", "xapelsin", "bumaga"]
    list1.sort()
    list2.sort()
    for x in range(len(list1)):
        if list1[x][0] == "x":
            print(x,"th element of list1:::::::::")
            print(list1[x])
    for x in range(len(list2)):
        if list2[x][0] == "x":
            print(x, "th element of list2:::::::::")
            print(list2[x])

def sixth():
    #a = len(thislist)-1
    #a = int(a)
    #for x in range(a-1):
     #   if thislist[x] == thislist[x+1]:
      #      thislist.remove(thislist[x+1])
       #     print("Hello")
        #    a = a-1

    list1 = [4, 5, 3, 3, 12,1,1, 2, 2, 2, 2, 3, 4, 5, 6, 7, 7, 7]
    print(list1)
#    a = len(list(dict.fromkeys(list1)))
 #   print(a)
    #print(len(list1))
    #a=0
    #a=int(a)
   # for x in range(len(list1)-1):
    #    if list1[x] == list1[x + 1]:
     #       a=a+1
   # print(a)
    for x in range(12):
        if list1[x] == list1[x + 1]:
            list1.remove(list1[x])
    for x in range(11):
        if list1[x] == list1[x + 1]:
            list1.remove(list1[x])

    print(list1)

def seventh():
    list=[]
    dict = {}
    dict['r'] = 'raz'
    dict['d'] = 'dwa'
    dict['t'] = 'trzy'
    del dict['r']
    for key in sorted(dict.keys()):
        print ((key), dict[key])
    f = open("index.txt", 'rU')
    lines = f.readlines()
    count = len(open("index.txt").readlines())
    for x in range(count):
        num = lines[x][:6]
        #dict[lines[x][:6]] = dict[lines[x][6:]]

    print()
    #for line in f:
     #   print(line)

    f.close()
#string[-n:] - выдеает последние n(любое число) элементов в стринге
#string[n:] - выдает без первых n элементов
#string[:n] - без первых n элементов
#string[:-n] - последние n
def eighth():
        wc=0
        list = {}
        f = open("index.txt", 'r')
        count = len(open("index.txt").readlines())
        #print(open("index.txt").readlines())
        list = open("index.txt").readlines()
        for x in range(len(list)):
            for j in range(len(list[x])):
                if(list[x][j] == '\n'):
                        wc = wc + 1
        print (wc)

#first()
#second()
#third()
#fourth()
#fifth()
#sixth()
#seventh()
eighth()