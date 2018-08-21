#Q=1
list=['arpit','rahul','rohit','aviral']
print(list)
#Q=2
list2=['google','apple','facebook','microsoft','tesla']
print(list+list2)
#Q=3
number=[1,1,2,2,3,2,4]
print(number.count(2))
#Q=4
numbers=[1,8,2,9,3,6,10,5,4,7]
numbers.sort()
print(numbers)
#Q=5
final_list=[]
listA=[1,2,5,6,7]
listB=[8,7,9,4]
final_list=listA+listB
final_list.sort()
print(final_list)
#Q=6
list3=[1,2,3,4,5,6,7,8,9]
even=0;
odd=0;
for i in list3:
    if i%2==0:
        even=even+1;
    else:
            odd=odd+1;
print("no. of even numbers",even)
print("no.of odd numbers",odd)
