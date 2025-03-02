#嵌套列表：m1[[1,2],[3,4]]
def matrix_add(m1,m2):
    # 嵌套列表推导式:
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
result = matrix_add([[1,2],[3,4]],[[5,6],[7,8]])
print(result)
#推导过程：
# m1=[[1,2],    m1[0][0]+m2[0][0]
#     [3,4]]    m1[0][1]+m2[0][1]
# m2=[[5,6],    m1[1][0]+m2[1][0]
#     [7,8]]    m1[1][1]+m2[1][1]