Set1 = {5,7,8,2,4}
Set2 = {3,7,1,3,9,5}
Set3 = {67,12,45,77}
# part a
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("a part :", Part_A_Set)
# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("b part :", Part_B_Set)
# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("c part :",Part_C_Set)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("d part :", Part_D_Set)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("e part is", Part_E_Set)
