import json

from sqlalchemy import update, text
from sqlalchemy.sql import select, desc
from sqlalchemy.orm import Query

from app.config import db, commit_rollback

from app.model import Trees, Features, HasFeatures, Pollutions, Purifies, ListPrices


class TreeRepository:

    @staticmethod
    async def get_by_id(trees_id: str):
        """ get data with index_tree  """
        query_tree = select(Trees).where(Trees.indexTree == trees_id)
        query_prices = select(ListPrices).select_from(ListPrices).where(ListPrices.indexTree == trees_id).order_by(ListPrices.price)
        query_purify = select(Pollutions.desc).select_from(Purifies).outerjoin(Pollutions, full=False).where(Purifies.indexTree == trees_id)

        tree_data = (await db.execute(query_tree)).all()
        tree_prices = (await db.execute(query_prices)).all()
        tree_purify = (await db.execute(query_purify)).all()

        results = {'tree': tree_data, 'price': tree_prices, 'purify': tree_purify}

        return results

    @staticmethod
    async def search_by_name(trees_name: str):
        """ get data with name for search  """
        search = f'%{trees_name}%'
        '''query = select(Trees).filter(Trees.name.like(search))'''
        query_tree = select(Trees).filter(Trees.name.like(search))
        tree_data = (await db.execute(query_tree)).all()
        print(tree_data)
        if(len(tree_data) != 0):
            print(tree_data[0]['Trees'].indexTree)
            tree_index = tree_data[0]['Trees'].indexTree
            query_prices = select(ListPrices).select_from(ListPrices).where(ListPrices.indexTree == tree_index).order_by(ListPrices.price)
            query_purify = select(Pollutions.desc).select_from(Purifies).outerjoin(Pollutions, full=False).where(Purifies.indexTree == tree_index)

            tree_prices = (await db.execute(query_prices)).all()
            tree_purify = (await db.execute(query_purify)).all()

            results = {'tree': tree_data, 'price': tree_prices, 'purify': tree_purify}
        elif(len(tree_data) == 0):
            results = 'data not found'

        return results

    @staticmethod
    async def get_all_flower():
        query = select(Trees).where(Trees.type == "FLOWER")
        return (await db.execute(query)).all()

    @staticmethod
    async def get_all_leaf():
        query = select(Trees).where(Trees.type == "LEAF")
        return (await db.execute(query)).all()

    @staticmethod
    async def get_all_cactus():
        query = select(Trees).where(Trees.type == "CACTUS")
        return (await db.execute(query)).all()

    @staticmethod
    async def get_all_data(trees_id: str):

        query = select(Trees, Features.name, Pollutions.desc).select_from(Trees).join(HasFeatures).join(Features).join(Purifies).join(Pollutions).where(Trees.indexTree == trees_id)
        return (await db.execute(query)).all()

    @staticmethod
    async def get_purify_p01():

        query = select(Trees).select_from(Purifies).join(Trees).join(Pollutions).where(Purifies.indexPollution == 'P01')
        return (await db.execute(query)).all()

    @staticmethod
    async def get_purify_p02():

        query = select(Trees).select_from(Purifies).join(Trees).join(Pollutions).where(Purifies.indexPollution == 'P02')
        return (await db.execute(query)).all()

    @staticmethod
    async def get_purify_p03():

        query = select(Trees).select_from(Purifies).join(Trees).join(Pollutions).where(Purifies.indexPollution == 'P03')
        return (await db.execute(query)).all()

    @staticmethod
    async def get_purify_p04():

        query = select(Trees).select_from(Purifies).join(Trees).join(Pollutions).where(Purifies.indexPollution == 'P04')
        return (await db.execute(query)).all()

    @staticmethod
    async def get_purify_p05():

        query = select(Trees).select_from(Purifies).join(Trees).join(Pollutions).where(Purifies.indexPollution == 'P05')
        return (await db.execute(query)).all()

    @staticmethod
    async def get_purify_p10():

        query = select(Trees).select_from(Purifies).join(Trees).join(Pollutions).where(Purifies.indexPollution == 'P10')
        return (await db.execute(query)).all()

    @staticmethod
    async def get_purify_p11():

        query = select(Trees).select_from(Purifies).join(Trees).join(Pollutions).where(Purifies.indexPollution == 'P11')
        return (await db.execute(query)).all()










