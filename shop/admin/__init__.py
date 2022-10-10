from shop.admin.banners import BannerAdmin, LowerBannerAdmin
from shop.admin.blogs import BlogAdmin
from shop.admin.categories import CategoryAdmin, PopularCategoryAdmin, \
    BrandDirectoryCategoryAdmin, DjangoMpttAdmin
from shop.admin.comments import CommentAdmin
from shop.admin.products import ProductAdmin, \
    ProductOfTheDayAdmin, BestProductAdmin
from shop.admin.services_for_site import TestimonialAdmin, OurServiceAdmin, \
    OurCompanyAdmin, LogoPhotoAdmin, SocialNetworkAdmin

__all__ = (
    "ProductAdmin",
    "ProductOfTheDayAdmin",
    "BestProductAdmin",
    "CommentAdmin",
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
    "DjangoMpttAdmin",
)
