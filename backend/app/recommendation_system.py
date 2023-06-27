import numpy as np
import pandas as pd
from app.distance_similarity_asym import distance_asymmetric_binary, sort_ranking


async def recommend_flower(input_fromUser):
    #recommend flower
    flower_matrix = pd.read_csv('C:/Users/mina/Desktop/Ki4You/backend/app/data_files/data_matrix/flower_matrix.csv')
    distance_flower = pd.read_csv('C:/Users/mina/Desktop/Ki4You/backend/app/data_files/data_matrix/distance_flower.csv')

    dist = []

    print('data testing : ' + str(input_fromUser))

    for dat in flower_matrix.index:
        que = 'index == ' + str(dat)
        data = flower_matrix.query(que).values.tolist()
        data_array = sum(data, [])
        print(str(data_array))
        predict = await distance_asymmetric_binary(input_fromUser, data_array)
        d = [predict[5]]
        dist.append(d)

    dist = pd.DataFrame(data=dist, columns=['distance'])

    matrix_distance = pd.concat([distance_flower, dist], axis=1)
    matrix_distance = matrix_distance.sort_values(ascending=True, by=['distance'], ignore_index=True)
    ranking = await sort_ranking(matrix_distance)
    print(matrix_distance)
    print(ranking)
    return ranking


async def recommend_leaf(input_fromUser):
    #recommend leaf
    # recommend flower
    leaf_matrix = pd.read_csv('C:/Users/mina/Desktop/Ki4You/backend/app/data_files/data_matrix/leaf_matrix.csv')
    distance_leaf = pd.read_csv('C:/Users/mina/Desktop/Ki4You/backend/app/data_files/data_matrix/distance_leaf.csv')

    dist = []

    print('data testing : ' + str(input_fromUser))

    for dat in leaf_matrix.index:
        que = 'index == ' + str(dat)
        data = leaf_matrix.query(que).values.tolist()
        data_array = sum(data, [])
        print(str(data_array))

        predict = await distance_asymmetric_binary(input_fromUser, data_array)
        d = [predict[5]]
        dist.append(d)

    dist = pd.DataFrame(data=dist, columns=['distance'])

    matrix_distance = pd.concat([distance_leaf, dist], axis=1)
    matrix_distance = matrix_distance.sort_values(ascending=True, by=['distance'], ignore_index=True)
    ranking = await sort_ranking(matrix_distance)
    print(matrix_distance)
    print(ranking)
    return ranking


async def recommend_cactus(input_fromUser):
    #recommend cactus
    cactus_matrix = pd.read_csv('C:/Users/mina/Desktop/Ki4You/backend/app/data_files/data_matrix/cactus_matrix.csv')
    distance_cactus = pd.read_csv('C:/Users/mina/Desktop/Ki4You/backend/app/data_files/data_matrix/distance_cactus.csv')

    dist = []

    print('data testing : ' + str(input_fromUser))

    for dat in cactus_matrix.index:
        que = 'index == ' + str(dat)
        data = cactus_matrix.query(que).values.tolist()
        data_array = sum(data, [])
        print(str(data_array))

        predict = await distance_asymmetric_binary(input_fromUser, data_array)
        d = [predict[5]]
        dist.append(d)

    dist = pd.DataFrame(data=dist, columns=['distance'])

    matrix_distance = pd.concat([distance_cactus, dist], axis=1)
    matrix_distance = matrix_distance.sort_values(ascending=True, by=['distance'], ignore_index=True)
    ranking = await sort_ranking(matrix_distance)
    print(matrix_distance)
    print(ranking)
    return ranking
