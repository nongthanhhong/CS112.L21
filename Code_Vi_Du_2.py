def Add(dict,key):
	k=dict.get(key,0)
	if k ==0:
		dict[key]=1
	else:
		dict[key]+=1

def MaxBag(slt,arr,m):
	n=len(Items)
	remain=m
	#sắp xếp theo đơn giá giảm dần
	Items.sort(key = lambda x:x[1]/x[0],reverse=True)
	i=0
	while True:
		#Nếu đồ vât có cân nặng nhẹ hơn
		#hoặc bằng khối lượng còn lại mà túi
		#mang được thì thêm vào túi
		if arr[i][0]<= remain:
			remain-= arr[i][0]
			Add(slt,arr[i][0])
		elif arr[n-1][0] <=remain:
			i+=1
		else:
			break

#Kiểm tra
Items=[[15,30],[10,25],[2,2],[4,6]]
m=37
selected={}

MaxBag(selected,Items,m)
print("The following items are selected and their quantity")
print(selected)