import json
from fastapi import FastAPI, Path, APIRouter, Query, Body, Request, Form
from typing import Annotated

from fastapi.middleware.cors import CORSMiddleware
from app.schema import ResponseSchema, Types, Outdoor, Indoor, Semi, Pots, Garden, Hanging, Little, Mid, Freq, Half, \
    Full, S, M, L, Faintly, Purify, Aus, Inshade, Beginner, Flower, Exposestosun

from app.recommendation_system import recommend_flower, recommend_leaf, recommend_cactus
from app.repository.tree_data import TreeRepository


router = APIRouter() # Init FastAPI Ap

global recommend_data
recommend_data = {}


# FastAPI section
#insert data from frontend page
# http://127.0.0.1:8000/form/submitform
@router.post('/submitform')
#outdoor, indoor, semi, pots, gardent, hanging, water_little, mid, freq, sun_full, half, faintly, puri, aus, s, m, l
async def handle_form(types: Types, outdoor: Outdoor, indoor: Indoor, semi: Semi,
    pots: Pots, garden: Garden, hanging: Hanging, little: Little, mid: Mid,
    freq: Freq, full: Full, half: Half, faintly: Faintly, purify: Purify, aus: Aus,
    s_s: S, s_m: M, s_l: L):
    global recommend_data

    print("get reqest")

    input = {'types': types, 'outdoor': outdoor, 'indoor': indoor, 'semi': semi, 'pots': pots,'garden': garden,
             'hanging': hanging, 'little': little, 'mid': mid, 'freq': freq, 'full': full,
             'half': half, 'faintly': faintly, 'purify': purify, 'aus': aus, 's': s_s, 'm': s_m, 'l': s_l}

    type_fromUser = input['types'].types

    input_fromUser = [input['outdoor'].outdoor, input['indoor'].indoor, input['semi'].semi, input['pots'].pots,
                      input['garden'].garden, input['hanging'].hanging, input['little'].little, input['mid'].mid,
                      input['freq'].freq, input['full'].full, input['half'].half, input['faintly'].faintly,
                      input['purify'].purify, input['aus'].aus, input['s'].s_s, input['m'].s_m, input['l'].s_l]

    print(str(input_fromUser))

    if(type_fromUser == 'flower'):
        #recomend with flower
        recommend_tree = await recommend_flower(input_fromUser)
        recommend_tree_index = {'rank1': recommend_tree[0], 'rank2': recommend_tree[1], 'rank3': recommend_tree[2]}

        #fetch data from database with tree controller
        recommend_data1 = await TreeRepository.get_by_id(recommend_tree_index['rank1'])
        recommend_data2 = await TreeRepository.get_by_id(recommend_tree_index['rank2'])
        recommend_data3 = await TreeRepository.get_by_id(recommend_tree_index['rank3'])

        #recomend data return to get api
        recommend_data = {'t1': recommend_data1, 't2': recommend_data2, 't3': recommend_data3}

    if(type_fromUser == 'leaf'):
        #recomend with leaf
        recommend_tree = await recommend_leaf(input_fromUser)
        recommend_tree_index = {'rank1': recommend_tree[0], 'rank2': recommend_tree[1], 'rank3': recommend_tree[2]}

        # fetch data from database with tree controller
        recommend_data1 = await TreeRepository.get_by_id(recommend_tree_index['rank1'])
        recommend_data2 = await TreeRepository.get_by_id(recommend_tree_index['rank2'])
        recommend_data3 = await TreeRepository.get_by_id(recommend_tree_index['rank3'])

        #recomend data return to get api
        recommend_data = {'t1': recommend_data1, 't2': recommend_data2, 't3': recommend_data3}

    return recommend_data


#insert input from user (backend api) to frontend
#http://localhost:8888/form/submitfrom_cactus
@router.post('/submitfrom_cactus')
async def handle_form_cactus(pots: Pots, garden: Garden, hanging: Hanging, inshade: Inshade, beginner: Beginner,
                             expose: Exposestosun, flower: Flower, purify: Purify, aus: Aus, s_s: S, s_m: M, s_l: L):

    global recommend_data

    input = {'pots': pots, 'garden': garden, 'hanging': hanging, 'inshade': inshade, 'beginner': beginner, 'expose': expose,
             'flower': flower, 'purify': purify, 'aus': aus, 's': s_s, 'm': s_m, 'l': s_l}

    input_fromUser = [input['pots'].pots, input['garden'].garden, input['hanging'].hanging, input['inshade'].inshade,
                      input['beginner'].beginner, input['expose'].exposestosun, input['flower'].flower, input['purify'].purify,
                      input['aus'].aus, input['s'].s_s, input['m'].s_m, input['l'].s_l]

    #recommendation with input from user
    recommend_tree = await recommend_cactus(input_fromUser)
    recommend_tree_index = {'rank1': recommend_tree[0], 'rank2': recommend_tree[1], 'rank3': recommend_tree[2]}

    # fetch data from database with tree controller
    recommend_data1 = await TreeRepository.get_by_id(recommend_tree_index['rank1'])
    recommend_data2 = await TreeRepository.get_by_id(recommend_tree_index['rank2'])
    recommend_data3 = await TreeRepository.get_by_id(recommend_tree_index['rank3'])

    # recomend data return to get api
    recommend_data = {'t1': recommend_data1, 't2': recommend_data2, 't3': recommend_data3}

    return recommend_data


#return recomendation result to frontend
# http://127.0.0.1:8000/from/recommend_index
@router.get('/recommend_index')
async def get_recomend_tree():
    global recommend_data   #use global variable
    return recommend_data