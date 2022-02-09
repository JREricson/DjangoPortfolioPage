import pytest
from django.db import IntegrityError

from portfolioSite.applications.programmingProjects import models


def test_dumb():
    assert 5 == 5


def test_dumb2():
    assert 5 == 6


def create_project_categories():
    large = models.ProjectCategory(category_name="LargeProject")
    scripting = models.ProjectCategory(category_name="scripting")
    website = models.ProjectCategory(category_name="website")

# @pytest.mark.dbfixture
# @pytest.mark.parametrize(
#     "id, name, slug, is_active",
#     [
#         (1, "fashion", "fashion", 1),
#         (18, "trainers", "trainers", 1),
#         (35, "baseball", "baseball", 1),
#     ],
# )
# def test_inventory_category_dbfixture(db, db_fixture_setup, id, name, slug, is_active):
#     result = models.Category.objects.get(id=id)
#     assert result.name == name
#     assert result.slug == slug
#     assert result.is_active == is_active


## create categories


## create new posts with all fields

# search for post in category


##edit post categoy and tags
##check that changes were mae

##check that post has been changed

# delete posts

# check that posts have been deleted

# search by tags
