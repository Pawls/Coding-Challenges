from LinkedList import LinkedList

def removeDups(ll):
    result = [x.data for x in ll]
    return sorted(set(result), key=result.index)

    
ll = LinkedList()
ll.add(9,3,2,4,3,3,5,6,6)
print(ll)
print(removeDups(ll))
