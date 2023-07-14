import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = [
        "Western",
        "Action",
        "Dramma"
    ]
    actors = [
        ["George", "Klooney"],
        ["Kianu", "Reaves"],
        ["Scarlett", "Keegan"],
        ["Will", "Smith"],
        ["Jaden", "Smith"],
        ["Scarlett", "Johansson"]
    ]
    for genre in genres:
        Genre.objects.create(genre)
    for actor in actors:
        Actor.objects.create(actor[0], actor[1])
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by()


if __name__ == "__main__":
    main()
