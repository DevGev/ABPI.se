from __future__ import annotations
from typing import Optional, List, Dict, Any, Callable
from itertools import combinations, product
from pydantic import BaseModel, HttpUrl, Field, ValidationError, validator
from datetime import datetime, date
import json
import re


class Trademark(BaseModel):
    title: str
    type: Optional[str]
    image_url: Optional[str]
    registration: Optional[TrademarkRegistration]
    application: Optional[TrademarkApplication]


class Trademarks(BaseModel):
    trademarks: List[Trademark]


class TrademarkRegistration(BaseModel):
    date: Optional[str] = None
    expiry: Optional[str] = None


class TrademarkApplication(BaseModel):
    date: Optional[str] = None


class TrademarkData(BaseModel):
    title: Optional[str] = None
    type: Optional[str] = None
    image_url: Optional[str] = None
    registration: Optional[TrademarkRegistration] = None
    application: Optional[TrademarkApplication] = None
