class Item :
    def __init__(self,prof,weight,index):
        self.prof = prof
        self.weight = weight
        self.index = index

def fk(arr,W):
    arr.sort(key = lambda x : (x.prof/x.weight),reverse = True)
    final_value =0.0
    fraction = []
    for Item in arr :
        if Item.weight <= W :
            W -= Item.weight
            final_value += Item.prof
            fraction.append(Item.index)
        else :
            final_value += Item.prof * W / Item.weight
            fraction.append(Item.index)
            break
    return final_value,fraction

if __name__ == "__main__" :
    arr = [Item(10,1,1),Item(12,2,2),Item(28,4,3)]
    print(fk(arr,6))
