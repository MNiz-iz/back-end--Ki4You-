import numpy as np
import pandas as pd


async def distance_asymmetric_binary(i, j):
    #measure for asymmetric binary is d(i,j) = b+c / a+b+c
    a = 0
    b = 0
    c = 0
    print(str(i))
    print(str(j))
    for num in range(len(i)):
        index = num
        if (i[index] == 1 and j[index] == 0):
            b = b+1
        elif (i[index] == 1 and j[index] == 1):
            a = a+1
        elif (i[index] == 0 and j[index] == 1):
            c = c+1
    up = b+c
    down = a+b+c
    distance = up/down
    return ( i, j, a, b, c, distance )


async def sort_ranking(matrix_distance):
    matrix_rank = []

    for rank in range(3):
        q = 'index == '+str(rank)
        rank_dis = matrix_distance.query(q).values.tolist()
        tree_index = rank_dis[0][0]
        if (rank == 0):
            matrix_rank.append(tree_index)
        elif (rank == 1):
            matrix_rank.append(tree_index)
        elif (rank == 2):
            matrix_rank.append(tree_index)

    return matrix_rank


def cal_ranking(distance_matrix, data_matrix, input_fromUser):
    dist = []
    run_cactus = 0
    check = 0

    print('data testing : ' + str(input_fromUser))

    for dat in data_matrix.index:
        que = 'index == ' + str(dat)
        data = data_matrix.query(que).values.tolist()
        data_array = sum(data, [])
        print(str(data_array))
        predict = distance_asymmetric_binary(input_fromUser, data_array)
        d = [predict[5]]
        dist.append(d)

    dist = pd.DataFrame(data=dist, columns=['distance'])

    matrix_distance = pd.concat([distance_matrix, dist], axis=1)
    matrix_distance = matrix_distance.sort_values(ascending=True, by=['distance'], ignore_index=True)
    ranking = sort_ranking(matrix_distance)
    print(matrix_distance)
    print (ranking)
    return (ranking)

