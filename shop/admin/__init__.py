from shop.admin.banners import BannerAdmin, LowerBannerAdmin
from shop.admin.blogs import BlogAdmin
from shop.admin.categories import CategoryAdmin, PopularCategoryAdmin, \
    BrandDirectoryCategoryAdmin
from shop.admin.products import ProductAdmin, \
    ProductOfTheDayAdmin, BestProductAdmin
from shop.admin.services_for_site import TestimonialAdmin, OurServiceAdmin, \
    OurCompanyAdmin, LogoPhotoAdmin, SocialNetworkAdmin
from shop.admin.customer import CustomerAdmin
from shop.admin.orders import OrderAdmin, OrderItemAdmin


__all__ = (
    "ProductAdmin",
    "ProductOfTheDayAdmin",
    "BestProductAdmin",
    "BlogAdmin",
    "BannerAdmin",
    "LowerBannerAdmin",
    "TestimonialAdmin",
    "OurServiceAdmin",
    "OurCompanyAdmin",
    "LogoPhotoAdmin",
    "SocialNetworkAdmin",
    "CategoryAdmin",
    "PopularCategoryAdmin",
    "BrandDirectoryCategoryAdmin",
    "CustomerAdmin",
    "OrderAdmin",
    "OrderItemAdmin",
)
