# some python libraries we'll be using
import re, string, calendar
from wikipedia import page
from bs4 import BeautifulSoup

from typing import List, Match
from utilities import *

# Assignment 8 Part II

# NOTE: To stop from being rate limited, I modified the code to save each fetch as a variable.

def get_planet_radius(planet_name: str) -> str:
    """Gets the radius of the given planet

    Args:
        planet_name - name of the planet to get radius of

    Returns:
        radius of the given planet
    """
    infobox_text = clean_text(get_first_infobox_text(get_page_html(planet_name)))
    # TODO: fill this in
    pattern = "Polar radius\s*(?P<radius>[\d,\.]+)"
    error_text = "Page infobox has no polar radius information"
    match = get_match(infobox_text, pattern, error_text)
    return match.group("radius")


def get_birth_date(name: str) -> str:
    """Gets birth date of the given person

    Args:
        name - name of the person

    Returns:
        birth date of the given person
    """
    infobox_text = clean_text(get_first_infobox_text(get_page_html(name)))
    # TODO: fill this in
    pattern = "(?P<birth>\d{4}-\d{2}-\d{2})"
    error_text = (
        "Page infobox has no birth information (at least none in xxxx-xx-xx format)"
    )
    match = get_match(infobox_text, pattern, error_text)
    return match.group("birth")


if __name__ == "__main__":
    print("\n<<<<<<<<<<<<<< Testing Planet Radius >>>>>>>>>>>>>>")
    # should be 3376.2
    mars_radius = get_planet_radius("Mars")
    print(f'Mars has a polar radius of roughly {mars_radius} km')
    # should be 6356.752
    earth_radius = get_planet_radius("Earth")
    print(f'Earth has a polar radius of roughly {earth_radius} km')
    # should be 66854
    jupiter_radius = get_planet_radius("Jupiter")
    print(f'Jupiter has a polar radius of roughly {jupiter_radius} km')
    # should be 54364
    saturn_radius = get_planet_radius("Saturn")
    print(f'Saturn has a polar radius of roughly {saturn_radius} km')

    # uncomment below lines for tests once you think you're getting the right output
    print('\n<<<< Running asserts, this might take a sec >>>>')
    assert mars_radius == "3376.2", "Incorrect radius for Mars"
    assert earth_radius == "6356.752", "Incorrect radius for Earth"
    assert jupiter_radius == "66842", "Incorrect radius for Jupiter"
    assert saturn_radius == "54364", "Incorrect radius for Saturn"
    print('\n<<<< Planet radius tests passed >>>>')

    print("\n<<<<<<<<<<<<<< Testing Birth Dates >>>>>>>>>>>>>>")
    # should be 1906-12-09
    grace_hopper_birth = get_birth_date("Grace Hopper")
    print(format_birth(grace_hopper_birth, "Grace Hopper"))
    # should be 1912-06-23
    alan_turing_birth = get_birth_date("Alan Turing")
    print(format_birth(alan_turing_birth, "Alan Turing"))
    # should be 1955-06-08
    tim_berners_lee_birth = get_birth_date("Tim Berners-Lee")
    print(format_birth(tim_berners_lee_birth, "Tim Berners-Lee"))
    # should be 1949-01-17
    anita_borg_birth = get_birth_date("Anita Borg")
    print(format_birth(anita_borg_birth, "Anita Borg"))

    # uncomment below lines for tests once you think you're getting the right output
    print('\n<<<< Running asserts, this might take a sec >>>>')
    assert grace_hopper_birth == "1906-12-09", "Incorrect birth date for Grace Hopper"
    assert alan_turing_birth == "1912-06-23", "Incorrect birth date for Alan Turing"
    assert tim_berners_lee_birth == "1955-06-08", "Incorrect birth date for Tim Berners-Lee"
    assert anita_borg_birth == "1949-01-17", "Incorrect birth date for Anita Borg"
    print('\n<<<< Birth date tests passed >>>>')

    print('\n<<<< All tests passed! >>>>')
