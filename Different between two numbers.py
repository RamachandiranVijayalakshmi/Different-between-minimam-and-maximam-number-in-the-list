b=[2,4,5,6,7,8,10,11,12,23]
def num(a):
    print('Original List is:',a)
    return (max(a)-min(a))
print('Diffrent between minimam and maximam value in the list is:',num(b))