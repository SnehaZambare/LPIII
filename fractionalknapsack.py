class Item:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight

def fractionalKnapsack(W, arr):
	arr.sort(key=lambda x: (x.value/x.weight), reverse=True)
	finalvalue = 0.0
	fractions = []
	for i in range(0,len(arr)):
		if arr[i].weight <= W:
			fractions.insert(i,1)
			W -= arr[i].weight
			finalvalue += arr[i].value
		else:
			fractions.insert(i, W/arr[i].weight)
			finalvalue += arr[i].value * W / arr[i].weight
			break
	return finalvalue, fractions

if __name__ == "__main__":

	W = 50
	arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
	max_val, fractions = fractionalKnapsack(W, arr)
	print("\nMaximum Profit is : ", max_val)
	print("\nThe fractions in which items are taken: ", fractions)