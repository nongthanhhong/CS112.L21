#Cách giải dưới đây giả định rằng tất cả đã được sắp xếp theo thời gian kết thúc của hoạt động.
#n là tổng số hoạt động
#s[] là một mảng chưa thời gian bắt đầu của tất cả hoạt động
#f[] là một mảng chứa thời gian kết thúc của tất cả hoạt động 
def printMaxActivities(s , f ):
    n = len(f)
    print("The following activities are selected:")
    # Hoạt động đầu tiên luôn được chọn
    # i là hoạt động cuối cùng được chọn
    i = 0
    print(i+1,end=' ')
    # xem xét các hoạt động còn lại
    #j là hoạt động đang xem xét
    for j in range(n):
        # nếu hoạt động này có thời gian bắt đầu lớn hơn
        # hoặc bằng với thời gian kết thúc 
        # của hoạt động trước thì chọn nó
        if s[j] >= f[i]:
            print(j+1,end=' ')
            #giờ đặt hoạt động cuối cùng được chọn 
            #là hoạt động vừa được chọn
            i = j
# kiểm tra thử xem nó có hoạt động không
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
printMaxActivities(s , f)

---------------------------------
#Chương trình cho dãy hoạt động chưa sắp xếp
def MaxActivities(arr, n):
    selected = []
    
    # Sắp xếp hoạt động theo thời gian kết thúc
    Activity.sort(key = lambda x:x[1])
    
    # Hoạt động đầu tiên luôn được chọn
    i = 0
    selected.append(arr[i])
    for j in range(1, n):
      '''nếu hoạt động đang chọn có thời gian bắt đầu
      lớn hơn hoặc bằng với thời gian kết thúc
      của hoạt động trước thì chọn nó'''
      if arr[j][0] >= arr[i][1]:
        selected.append(arr[j])
        i = j
    return selected

# Kiểm tra
Activity = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [8, 9]]
n = len(Activity)
selected = MaxActivities(Activity, n)
print("Following activities are selected :")
print(selected)