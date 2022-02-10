import pytest
from django.db import IntegrityError

from portfolioSite.applications.programmingProjects import models

## params to be used in tests
params_categories = [
    ("LargeProject"),
    ("scripting"),
    ("website"),
]

## Fixtures
#########################################################################


@pytest.fixture
def create_project_categories(django_db_blocker):
    with django_db_blocker.unblock():

        large = models.ProjectCategory(category_name="LargeProject")
        scripting = models.ProjectCategory(category_name="scripting")
        website = models.ProjectCategory(category_name="website")
        large.save()
        scripting.save()
        website.save()


@pytest.fixture
def create_projects():
    # large = models.Project()
    # scripting = models.ProjectCategory()
    # website = models.ProjectCategory()
    # large.save()
    # scripting.save()
    # website.save()
    pass


#######################################################
## tests


@pytest.mark.django_db
@pytest.mark.parametrize(
    "cat_name",
    params_categories,
)
def test_programmingProjects_catagories_in_db(
    cat_name,
    create_project_categories,
):

    result = models.ProjectCategory.objects.get(category_name=cat_name)
    assert result.category_name == cat_name


## create new posts with all fields


def test_programmingProjects_project_in_db(create_project_categories, create_projects):
    # assert projects have been created
    # assert that they have correct category

    assert 4 == 4


@pytest.mark.parametrize(
    "cat_name",
    params_categories,
)
@pytest.mark.django_db
def test_programmingProjects_delete_category(cat_name, create_project_categories):
    cat_count = models.ProjectCategory.objects.all().count()
    assert cat_count == 3
    item = models.ProjectCategory.objects.get(category_name=cat_name)
    item.delete()
    cat_count = models.ProjectCategory.objects.all().count()
    assert cat_count == 2

    # TODO - make sure projects still exist if project is deleted and project no longer has category assigned


#     # edit two projects

#     # test that they have been changed in db

#     pass


# search by tags


# search for post in category
