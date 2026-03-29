# import fastapi
from fastapi import FastAPI, Depends

from database import session, engine
from models.product import Product
import database_schemas.product
from sqlalchemy.orm import Session


# app = fastapi.FastAPI()
app = FastAPI()

database_schemas.product.Base.metadata.create_all(bind=engine)

products = [
    Product(id=1, name="iPhone 17", description="Latest iPhone", price=99.9, quantity=1),
    Product(id=2, name="MacBook Pro M3", description="High-performance laptop", price=1999.9, quantity=1),
    Product(id=3, name="iPad Pro", description="Powerful tablet", price=899.9, quantity=1),
    Product(id=4, name="Apple Watch Series 10", description="Smartwatch with health tracking", price=499.9, quantity=1),
    Product(id=5, name="AirPods Pro", description="Wireless noise-cancelling earbuds", price=249.9, quantity=1),
    Product(id=6, name="iMac M3", description="All-in-one desktop computer", price=1499.9, quantity=1),
]

def getDB():
    db = session()
    try:
        yield db
    finally:
        db.close()

def dbInit():
    db = session()

    count = db.query(database_schemas.product.Product).count()

    if count == 0:
        for product in products:
            db.add(database_schemas.product.Product(**product.model_dump()))

    db.commit()


dbInit()

@app.get("/")
def root():
    return {"message":"Hello motherfucking world"}

@app.get("/products")
def allProducts(db: Session = Depends(getDB)):
    db_products = db.query(database_schemas.product.Product).all()
    return {"products": db_products}

@app.get("/product/{id}")
def getProductById(id: int, db: Session = Depends(getDB)):
    # result = [product for product in products if product.id==id]
    db_product = db.query(database_schemas.product.Product).filter(database_schemas.product.Product.id == id).first()
    if db_product:
        return {"product": db_product}

    return {"message": "Product Not Found"}

@app.post("/addProduct")
def addProduct(product:Product, db: Session = Depends(getDB)):
    db.add(database_schemas.product.Product(**product.model_dump()))
    db.commit()
    return {"message": "Successfully Added."}

@app.put("/product/{id}")
def updateProduct(id: int, updatedProduct: Product, db: Session = Depends(getDB)):
    # for pos, product in enumerate(products):
    #     if product.id == id:
    #         products[pos] = updatedProduct

    db_product = db.query(database_schemas.product.Product).filter(database_schemas.product.Product.id == id).first()
    if db_product:
        db_product.id = id
        db_product.name = updatedProduct.name
        db_product.description = updatedProduct.description
        db_product.price = updatedProduct.price
        db_product.quantity = updatedProduct.quantity
        db.commit()
        return {"message": "Product updated successfully"}
    else:
        return {"products": products}

@app.delete("/deleteProduct/{id}")
def deleteProduct(id: int, db: Session = Depends(getDB)):
    db_product = db.query(database_schemas.product.Product).filter(database_schemas.product.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted successfully."}
    else:
        return {"message": "Product not found."}