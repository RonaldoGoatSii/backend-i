from fastapi import FastAPI

api = FastAPI()

@api.get("/shop")
def list_product():
    ...


@api.get("/shop/{category}")
def list2_product(category:str):
    return f"category - {category}"

@api.get("/shop/{category}/{product}")
def list3_product(category:str, product:str):
    return f"category - -{category} || product - {product}"

@api.post("/shop")
def list4_product():
    ...