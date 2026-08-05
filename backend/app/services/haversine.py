"""
services/haversine.py — M-14: GPS / Haversine distance
Pure math — no external geocoding service, no ML.
Stub — implement in Day 5.
"""
import math


def haversine_distance_m(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
) -> float:
    """
    Calculate great-circle distance between two GPS coordinates.
    Returns distance in metres.

    Formula: Haversine (WGS-84 earth radius = 6_371_000 m)

    Args:
        lat1, lon1: Reference point (project anchor from project_locations).
        lat2, lon2: Worker's reported GPS position.
    """
    R = 6_371_000  # Earth radius in metres
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def is_within_radius(
    worker_lat: float,
    worker_lng: float,
    project_lat: float,
    project_lng: float,
    radius_m: int,
) -> tuple[bool, float]:
    """
    Returns (within_radius, distance_m).
    Use this in attendance/mark endpoint before accepting the mark.
    """
    distance = haversine_distance_m(project_lat, project_lng, worker_lat, worker_lng)
    return distance <= radius_m, round(distance, 2)
