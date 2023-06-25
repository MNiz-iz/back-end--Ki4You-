from fastapi import Path, APIRouter, Query, Body, Request, Form

from app.repository.tree_data import TreeRepository
from app.schema import ResponseSchema

router = APIRouter(
    prefix="/tree_data",
    tags=['tree']
)


@router.get("/{id}")
async def get_data_by_id(
        trees_id: str = Path(..., alias="id")
):
    result = await TreeRepository.get_by_id(trees_id)
    return result


@router.get("/search/{name}")
async def search_tree(
        trees_name: str = Path(..., alias="name")
):
    data = await TreeRepository.search_by_name(trees_name)
    return data


@router.get("/all_data/flower")
async def fetch_all_flower():
    data = await TreeRepository.get_all_flower()
    return data


@router.get("/all_data/leaf")
async def fetch_all_leaf():
    data = await TreeRepository.get_all_leaf()
    return data


@router.get("/all_data/cactus")
async def fetch_all_cactus():
    data = await TreeRepository.get_all_cactus()
    return data


@router.get("/purify/p01")
async def search_purify_p01():
    data = await TreeRepository.get_purify_p01()
    print(data)
    return data


@router.get("/purify/p02")
async def search_purify_p02():
    data = await TreeRepository.get_purify_p02()
    print(data)
    return data


@router.get("/purify/p03")
async def search_purify_p03():
    data = await TreeRepository.get_purify_p03()
    print(data)
    return data


@router.get("/purify/p04")
async def search_purify_p04():
    data = await TreeRepository.get_purify_p04()
    print(data)
    return data


@router.get("/purify/p05")
async def search_purify_p05():
    data = await TreeRepository.get_purify_p05()
    print(data)
    return data


@router.get("/purify/p10")
async def search_purify_p10():
    data = await TreeRepository.get_purify_p10()
    print(data)
    return data


@router.get("/purify/p11")
async def search_purify_p11():
    data = await TreeRepository.get_purify_p11()
    print(data)
    return data


@router.get("/all/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all(
        trees_id: str = Path(..., alias="id")
):
    data = await TreeRepository.get_all_data(trees_id)
    return ResponseSchema(detail="success get all data", result=data)

