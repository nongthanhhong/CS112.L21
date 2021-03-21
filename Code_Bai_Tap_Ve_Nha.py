


import sys 
 
 # Khởi tạo một đồ thị
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printSolution(self, dist): 
        print("Vertex \tDistance from Source")
        for node in range(self.V): 
            print(node, "\t", dist[node])
    '''Hàm tìm kiếm đỉnh gần nhất chưa được đưa
    vào cây đường đi ngắn nhất'''
    def minDistance(self, dist, sptSet): 
  
        # Khởi tạo khoảng cách tối thiểu cho node tiếp theo
        min = sys.maxsize
  
        '''Tìm kiếm đỉnh không gần nhất 
        chưa nằm trong cây đường đi ngắn nhất'''
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False:
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    '''Hàm thực hiện thuật toán đường đi ngắn nhất nguồn đơn của Dijkstra       cho một đồ thị được biểu diễn bằng cách sử dụng biểu diễn ma trận kề'''
    def dijkstra(self, src): 
  
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
           '''Chọn đỉnh có khoảng cách tối thiểu từ tập hợp các đỉnh chưa              được xử lý. u luôn bằng src trong lần lặp đầu tiên'''
           u = self.minDistance(dist, sptSet) 
  
           '''Đặt đỉnh khoảng cách nhỏ nhất vào trong cây đường 
           đi ngắn nhất'''
           sptSet[u] = True
           
           '''Chỉ cập nhật giá trị khoảng cách của các đỉnh liền kề của
           đỉnh đã chọn nếu khoảng cách hiện tại lớn hơn khoảng cách mới 
           và đỉnh không có trong cây đường dẫn ngắn nhất'''
           for v in range(self.V): 
               if self.graph[u][v] > 0 and sptSet[v] == False:
                   if dist[v] > dist[u] + self.graph[u][v]: 
                       dist[v] = dist[u] + self.graph[u][v] 
  
        self.printSolution(dist) 
  
# Test
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
  
g.dijkstra(0)
  


import sys 
 
 # Khởi tạo một đồ thị
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printSolution(self, dist): 
        print("Vertex \tDistance from Source")
        for node in range(self.V): 
            print(node, "\t", dist[node])
    '''Hàm tìm kiếm đỉnh gần nhất chưa được đưa
    vào cây đường đi ngắn nhất'''
    def minDistance(self, dist, sptSet): 
  
        # Khởi tạo khoảng cách tối thiểu cho node tiếp theo
        min = sys.maxsize
  
        '''Tìm kiếm đỉnh không gần nhất 
        chưa nằm trong cây đường đi ngắn nhất'''
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False:
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    '''Hàm thực hiện thuật toán đường đi ngắn nhất nguồn đơn của Dijkstra       cho một đồ thị được biểu diễn bằng cách sử dụng biểu diễn ma trận kề'''
    def dijkstra(self, src): 
  
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
           '''Chọn đỉnh có khoảng cách tối thiểu từ tập hợp các đỉnh chưa              được xử lý. u luôn bằng src trong lần lặp đầu tiên'''
           u = self.minDistance(dist, sptSet) 
  
           '''Đặt đỉnh khoảng cách nhỏ nhất vào trong cây đường 
           đi ngắn nhất'''
           sptSet[u] = True
           
           '''Chỉ cập nhật giá trị khoảng cách của các đỉnh liền kề của
           đỉnh đã chọn nếu khoảng cách hiện tại lớn hơn khoảng cách mới 
           và đỉnh không có trong cây đường dẫn ngắn nhất'''
           for v in range(self.V): 
               if self.graph[u][v] > 0 and sptSet[v] == False:
                   if dist[v] > dist[u] + self.graph[u][v]: 
                       dist[v] = dist[u] + self.graph[u][v] 
  
        self.printSolution(dist) 
  
# Test
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
  
g.dijkstra(0)
  