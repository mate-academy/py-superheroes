import io
from contextlib import redirect_stdout
from unittest import mock
from unittest.mock import Mock

import pytest

import app.main as main
from app.main import Superhero, FlyingSuperhero, StrengthSuperhero


@pytest.mark.parametrize(
    "class_name", ["Superhero", "FlyingSuperhero", "StrengthSuperhero"]
)
def test_classes_should_be_defined(class_name: str) -> None:
    assert hasattr(main, class_name)


@pytest.mark.parametrize(
    "class_name,methods",
    [
        ("Superhero", ["__init__", "use_power", "calculate_power"]),
        ("FlyingSuperhero", ["__init__", "use_power", "fly", "calculate_power"]),
        (
            "StrengthSuperhero",
            ["__init__", "use_power", "lift_weight", "calculate_power"],
        ),
    ],
)
def test_classes_should_have_corresponding_methods(
    class_name: str, methods: str
) -> None:
    class_to_test = getattr(main, class_name)
    for method in methods:
        assert (
            hasattr(class_to_test, method) is True
        ), f"Class '{class_to_test}' should have method {method}"


def test_superhero_use_power_method() -> None:
    superhero = Superhero("Spider-Man", 12)
    f = io.StringIO()
    with redirect_stdout(f):
        superhero.use_power()
    assert f.getvalue() == "Spider-Man is using their power.\n"


def test_superhero_calculate_power_method() -> None:
    superhero = Superhero("Spider-Man", 12)
    assert superhero.calculate_power() == 24


@pytest.mark.parametrize(
    "name,power_level,flight_speed",
    [
        ("Superman", 20, 5),
        ("Iron Man", 15, 3),
    ],
)
def test_flying_superhero_use_power_method(
    name: str, power_level: int, flight_speed: int
) -> None:
    flying_hero = FlyingSuperhero(name, power_level, flight_speed)
    f = io.StringIO()
    with redirect_stdout(f):
        flying_hero.use_power()
    assert f.getvalue() == f"{name} is using their power.\n{name} is flying.\n"


@pytest.mark.parametrize(
    "name,power_level,flight_speed",
    [
        ("Superman", 20, 5),
        ("Iron Man", 15, 3),
    ],
)
def test_flying_superhero_fly_method(
    name: str, power_level: int, flight_speed: int
) -> None:
    flying_hero = FlyingSuperhero(name, power_level, flight_speed)
    f = io.StringIO()
    with redirect_stdout(f):
        flying_hero.fly()
    assert f.getvalue() == f"{name} is flying.\n"


@pytest.mark.parametrize(
    "name,power_level,flight_speed,expected_power",
    [
        ("Superman", 20, 5, 140),
        ("Iron Man", 15, 3, 75),
    ],
)
def test_flying_superhero_calculate_power_method(
    name: str, power_level: int, flight_speed: int, expected_power: int
) -> None:
    flying_hero = FlyingSuperhero(name, power_level, flight_speed)
    assert flying_hero.calculate_power() == expected_power


@pytest.mark.parametrize(
    "name,power_level,lifting_capacity",
    [
        ("Hulk", 25, 10),
        ("Thor", 18, 5),
    ],
)
def test_strength_superhero_use_power_method(
    name: str, power_level: int, lifting_capacity: int
) -> None:
    strength_hero = StrengthSuperhero(name, power_level, lifting_capacity)
    f = io.StringIO()
    with redirect_stdout(f):
        strength_hero.use_power()
    assert (
        f.getvalue() == f"{name} is using their power.\n{name} is lifting a weight.\n"
    )


@pytest.mark.parametrize(
    "name,power_level,lifting_capacity",
    [
        ("Hulk", 25, 10),
        ("Thor", 18, 5),
    ],
)
def test_strength_superhero_lift_weight_method(
    name: str, power_level: int, lifting_capacity: int
) -> None:
    strength_hero = StrengthSuperhero(name, power_level, lifting_capacity)
    f = io.StringIO()
    with redirect_stdout(f):
        strength_hero.lift_weight()
    assert f.getvalue() == f"{name} is lifting a weight.\n"


@pytest.mark.parametrize(
    "name,power_level,lifting_capacity,expected_power",
    [
        ("Hulk", 10, 10, 2000),
        ("Thor", 18, 5, 3240),
    ],
)
def test_strength_superhero_calculate_power_method(
    name: str, power_level: int, lifting_capacity: int, expected_power: int
) -> None:
    strength_hero = StrengthSuperhero(name, power_level, lifting_capacity)
    assert strength_hero.calculate_power() == expected_power


@mock.patch.object(Superhero, "use_power")
def test_flying_superhero_use_power_calls_super(mock_super_use_power: Mock) -> None:
    flying_hero = FlyingSuperhero("Superman", 20, 5)
    flying_hero.use_power()
    mock_super_use_power.assert_called_once(), "Superhero.use_power was not called"


@mock.patch.object(Superhero, "use_power")
def test_strength_superhero_use_power_calls_super(mock_super_use_power: Mock) -> None:
    strength_hero = StrengthSuperhero("Hulk", 25, 10)
    strength_hero.use_power()
    mock_super_use_power.assert_called_once(), "Superhero.use_power was not called"
