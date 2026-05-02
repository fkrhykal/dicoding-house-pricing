from decimal import Decimal
from fastapi import FastAPI
from fastapi import Depends
from typing import Annotated
from pydantic import BaseModel, Field
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
import joblib
import uvicorn

class Parameter(BaseModel):
    Id: Decimal
    MSSubClass: Decimal
    MSZoning: Decimal
    LotFrontage: Decimal
    LotArea: Decimal
    Street: Decimal
    LotShape: Decimal
    LandContour: Decimal
    Utilities: Decimal
    LotConfig: Decimal
    LandSlope: Decimal
    Neighborhood: Decimal
    Condition1: Decimal
    Condition2: Decimal
    BldgType: Decimal
    HouseStyle: Decimal
    OverallQual: Decimal
    OverallCond: Decimal
    YearBuilt: Decimal
    YearRemodAdd: Decimal
    RoofStyle: Decimal
    RoofMatl: Decimal
    Exterior1st: Decimal
    Exterior2nd: Decimal
    MasVnrType: Decimal
    MasVnrArea: Decimal
    ExterQual: Decimal
    ExterCond: Decimal
    Foundation: Decimal
    BsmtQual: Decimal
    BsmtCond: Decimal
    BsmtExposure: Decimal
    BsmtFinType1: Decimal
    BsmtFinSF1: Decimal
    BsmtFinType2: Decimal
    BsmtFinSF2: Decimal
    BsmtUnfSF: Decimal
    TotalBsmtSF: Decimal
    Heating: Decimal
    HeatingQC: Decimal
    CentralAir: Decimal
    Electrical: Decimal
    FirstFlrSF: Decimal = Field(alias='1stFlrSF')
    SecondFlrSF: Decimal = Field(alias='2ndFlrSF')
    LowQualFinSF: Decimal
    GrLivArea: Decimal
    BsmtFullBath: Decimal
    BsmtHalfBath: Decimal
    FullBath: Decimal
    HalfBath: Decimal
    BedroomAbvGr: Decimal
    KitchenAbvGr: Decimal
    KitchenQual: Decimal
    TotRmsAbvGrd: Decimal
    Functional: Decimal
    Fireplaces: Decimal
    FireplaceQu: Decimal
    GarageType: Decimal
    GarageYrBlt: Decimal
    GarageFinish: Decimal
    GarageCars: Decimal
    GarageArea: Decimal
    GarageQual: Decimal
    GarageCond: Decimal
    PavedDrive: Decimal
    WoodDeckSF: Decimal
    OpenPorchSF: Decimal
    EnclosedPorch: Decimal
    ThreeSsnPorch: Decimal = Field(alias='3SsnPorch')
    ScreenPorch: Decimal
    PoolArea: Decimal
    MiscVal: Decimal
    MoSold: Decimal
    YrSold: Decimal
    SaleType: Decimal
    SaleCondition: Decimal

class Result(BaseModel):
    SalePrice: Decimal

class Model:
    def __init__(self):
        self.model: GradientBoostingRegressor = joblib.load('gbr_model.joblib')
    def predict(self, params: Parameter):
        return self.model.predict(params)
        

app = FastAPI()


@app.post("/predict")
def predict(params: Parameter, model: Annotated[Model, Depends(Model)]):
    df = pd.DataFrame([params.model_dump(by_alias=True)])
    result =  model.predict(df)
    return Result(SalePrice=result[0])

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)