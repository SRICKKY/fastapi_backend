from typing import List

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from pymongo import MongoClient
from pymongo.errors import PyMongoError


from dependencies.db import get_mongo_db
from models.product import Product, ProductInDB
from dependencies.auth import get_current_user

router = APIRouter()

@router.post("/products/", response_model=ProductInDB)
async def create_product(
    product: Product, 
    mongo_db=Depends(get_mongo_db), 
    current_user=Depends(get_current_user)
    ):
    product_doc = product.dict()
    result = await mongo_db.products.insert_one(product_doc)
    product_in_db = ProductInDB(id=str(result.inserted_id), **product.dict())
    return product_in_db


@router.get("/products/{product_id}", response_model=ProductInDB)
async def read_product(
    product_id: str, 
    mongo_db: MongoClient = Depends(get_mongo_db)):
    try:
        product_doc = await mongo_db.products.find_one({"_id": ObjectId(product_id)})
        if product_doc:
            return ProductInDB(id=str(product_doc["_id"]), **product_doc)
        raise HTTPException(status_code=404, detail="Product not found")
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"MongoDB error: {str(e)}")


@router.get("/products/", response_model=List[ProductInDB])
async def list_products(mongo_db=Depends(get_mongo_db)):
    products = await mongo_db.products.find().to_list(10)
    return [
        ProductInDB(id=str(product["_id"]), **product)
        for product in products
    ]