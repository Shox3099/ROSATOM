from sys import maxsize
from itertools import permutations

#function for calculating the shortest path
#input data graph, point to start, number of elements,list place
def travellingSalesmanProblem(graph, s,V,place):
   #array elements without first
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
   #create random various
    next_permutation = permutations(vertex)
    cont = next_permutation
    #cycle for calculating distance over all various combinations
    for i in next_permutation:

        current_pathweight = 0

        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        if min_path >= current_pathweight:
            cont = i
            min_path = current_pathweight
    #output shortest path
    print(place[0],"->", end="")
    for j in cont:
        if j == 1:
            print(place[1],"->",end="")
        elif j == 2:
            print(place[2],"->",end="")
        elif j == 3:
            print(place[3],"->",end="")
        elif j == 4:
            print(place[4],"->",end="")
    print(place[0])
    print("Время затраченное на путь:",min_path,"мин")

    return min_path


if __name__ == "__main__":
    V=5
    place = ["Краcнопресненская"
     ,"Библиотека имени Ленина"
     ,"Охотный ряд"
     , "Кропоткинская"
     ,"Третьяковская"]
    graph = [[0, 17, 19, 15, 16],
             [17, 0, 3, 3, 15],
             [19, 3, 0, 4, 12],
             [15, 3, 4, 0, 17],
             [16, 15, 12, 17, 0]]

    s = 0
    travellingSalesmanProblem(graph, s,V,place)