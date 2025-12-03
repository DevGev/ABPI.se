from __future__ import annotations
from typing import Optional, List, Dict, Any, Callable
from itertools import combinations, product
from pydantic import BaseModel, HttpUrl, Field, ValidationError, validator
from datetime import datetime, date
import json
import re


class Address(BaseModel):
    address_line: Optional[str] = None
    box_address_line: Optional[str] = None
    zip_code: Optional[str] = None
    post_place: Optional[str] = None


class Location(BaseModel):
    country_part: Optional[str] = None
    county: Optional[str] = None
    municipality: Optional[str] = None
    coordinates: Optional[Any] = None


class Industry(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    style: Optional[str] = None
    sales_rank: Optional[int] = None


class Certificate(BaseModel):
    type: Optional[str] = None
    sub_type: Optional[str] = None
    start_date: Optional[date] = None

    @validator("start_date", pre=True)
    @staticmethod
    def parse_start_date(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%Y-%m-%d")
        return value


class Role(BaseModel):
    name: str
    type: Optional[str] = None
    role: Optional[str] = None
    birth_date: Optional[date] = None
    business_person: Optional[bool] = None

    @validator("birth_date", pre=True)
    @staticmethod
    def parse_start_date(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%Y-%m-%d")
        return value


class RoleGroup(BaseModel):
    name: Optional[str] = None
    roles: List[Role]


class Roles(BaseModel):
    number_of_roles: int
    role_groups: List[RoleGroup]


class CorporateStructure(BaseModel):
    number_of_companies: Optional[int] = None
    number_of_subsidiaries: Optional[int] = None
    parent_company_name: Optional[str] = None
    parent_company_organisation_number: Optional[str] = None
    parent_company_country_code: Optional[str] = None


class CompanyAccountItem(BaseModel):
    code: str
    amount: Optional[float] = None


class CompanyAccount(BaseModel):
    year: Optional[str] = None
    period: Optional[str] = None
    currency: Optional[str] = None
    accounts: List[CompanyAccountItem]


class OpeningHoursDay(BaseModel):
    all_day: bool
    closed: bool
    open_hours: bool
    opening_hour: str
    opening_minutes: str
    closing_hour: str
    closing_minutes: str


class OpeningHours(BaseModel):
    monday: Optional[OpeningHoursDay] = None
    tuesday: Optional[OpeningHoursDay] = None
    wednesday: Optional[OpeningHoursDay] = None
    thursday: Optional[OpeningHoursDay] = None
    friday: Optional[OpeningHoursDay] = None
    saturday: Optional[OpeningHoursDay] = None
    sunday: Optional[OpeningHoursDay] = None
    description: Optional[str] = None


class ExternalLink(BaseModel):
    url: HttpUrl
    description: Optional[str] = None


class SocialMediaLinks(BaseModel):
    linked_in_url: Optional[HttpUrl] = None
    facebook_url: Optional[HttpUrl] = None
    youtube_url: Optional[HttpUrl] = None
    instagram_url: Optional[HttpUrl] = None
    twitter_url: Optional[HttpUrl] = None


class CompanyType(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    parent_code: Optional[str] = None


class ContactPerson(BaseModel):
    type: Optional[str] = None
    name: Optional[str] = None
    role: Optional[str] = None
    birth_date: Optional[date] = None
    business_person: Optional[bool] = None

    @validator("birth_date", pre=True)
    @staticmethod
    def parse_birth_date(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%Y-%m-%d")
        return value


class RegistryStatusEntry(BaseModel):
    label: str
    value: bool


class SignatoryCombination(BaseModel):
    name: str
    signees: List[str]


class Announcement(BaseModel):
    date: date
    text: Optional[str] = None
    type: str

    @validator("date", pre=True)
    @staticmethod
    def parse_birth_date(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%Y-%m-%d")
        return value


class Shareholder(BaseModel):
    name: str
    share: Optional[str] = None
    number_of_shares: int


class Vehicles(BaseModel):
    number_of_vehicles: Optional[int] = None


class AlternativeName(BaseModel):
    name: str
    description: Optional[str] = None


class CompanyAddresses(BaseModel):
    visitor_address: Optional["Address"]
    postal_address: Optional["Address"]
    legal_visitor_address: Optional["Address"]
    legal_postal_address: Optional["Address"]


class FinancialSummary(BaseModel):
    revenue: Optional[float]
    profit: Optional[float]
    currency: Optional[str]
    share_capital: Optional[float]
    estimated_turnover: Optional[str]
    turnover_year: Optional[int]
    company_accounts_last_updated_year: Optional[int]


class ShareholderSummary(BaseModel):
    total_shareholders: Optional[int]
    shareholders_last_updated_date: Optional[str]


class RegistryFlags(BaseModel):
    registered_for_vat: Optional[bool]
    registered_for_nav: Optional[bool]
    registered_for_voluntary: Optional[bool]
    registered_for_payroll_tax: Optional[bool]
    registered_for_vat_description: Optional[str]


class CompanyBasicInfo(BaseModel):
    name: str
    organization_number: str
    legal_name: Optional[str]
    main_office: Optional[str]
    description: Optional[str]
    home_page: Optional[HttpUrl]
    phone_numbers: List[str]
    email: Optional[str]
    purpose: Optional[str]
    registration_date: Optional[str]
    foundation_date: Optional[str]


class Company(BaseModel):
    basic_info: Optional[CompanyBasicInfo]
    registry_status: Optional[RegistryStatusEntry]
    company_type: Optional[CompanyType]
    addresses: Optional[CompanyAddresses]
    location: Optional[Location]
    contact_person: Optional[ContactPerson]
    home_page: Optional[HttpUrl]
    marketing_protection: Optional[bool]
    industries: List[Industry] = []
    current_industry: Optional[Industry]
    certificates: List[Certificate] = []
    company_accounts: List[CompanyAccount] = []
    financial_summary: Optional[FinancialSummary]
    registry_flags: Optional[RegistryFlags]
    number_of_employees: Optional[int]
    mortgages: Optional[bool]
    roles: Optional[Roles]
    signatory_combinations: List[SignatoryCombination] = []
    external_links: List[ExternalLink] = []
    social_media_links: Optional[SocialMediaLinks]
    corporate_structure: Optional[CorporateStructure]
    announcements: List[Announcement] = []
    shareholders: List[Shareholder] = []
    shareholder_summary: Optional[ShareholderSummary]
    number_of_vehicles: Optional[int]
    names: List[AlternativeName] = []
    opening_hours: Optional[OpeningHours]
