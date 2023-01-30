spisok=[] #пустой список
numbers=[1,2,3,4,5]
abc=["Abc","B","C"]
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1-добавить букву в список ")
    print("2-склеить список\n3-добавить букву на i - позицию ")
    print("4-удалить элемент")
    print("5-удаляет i-ый элемент и возвратить его")
    print("6-")
    valik=int(input())
    if valik==1:
        a=input("Введи букву ")
        slovo_list.append(a)
        print(f"Добавили {a} новый список",slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=input("Введи букву, которую хочешь добавить ")
        i=int(input("Введи номер позиции, куда хочешь добавить букву "))
        slovo_list.insert(i-1,a) # позиция i начинает 0,1,2...
        print(slovo_list)
    elif valik==4:
        a=input("Введи букву, которую хочешь удалить ")
        a=a.lower()
        listcopy_list=[]
        for t in (slovo_list):
            listcopy_list.append(t.lower())
        n=listcopy_list.count(a)
        if n>0:
            for i in range(n):
                listcopy_list.remove(a)
        else:
            print("Искомой буквы нет")
        print(listcopy_list)

    elif valik==5:
        a=int(input("Введи позицию которую хочешь удалить "))
        if a>=0 and a<len(slovo_list):
            slovo_list.pop(a-1)
            print(slovo_list)
        else:
            print("Ei ole see postion")
    elif valik==6:
        a=int(input("Введи "))
        print(slovo_list.index(a,[slovo]))


    


       
        
        