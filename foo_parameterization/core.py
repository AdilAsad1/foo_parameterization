import math

def foo_volume(radius):
    """
    Calculate the volume of a sphere using the Foo et al. parameterization.

    Parameters:
    radius (float): The radius of the sphere.

    Returns:
    float: The calculated volume of the sphere.
    """
    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")
    
    # Placeholder for a complex calculation, using the simple volume formula for now
    volume = (4/3) * math.pi * radius ** 3
    return volume