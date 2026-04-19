# conversions.py

# Dictionaries mapping units to their base unit equivalents.
# Base Units:
# - Force: Newton (N)
# - Stress: Pascal (Pa)
# - Area: Square Meter (m²)

FORCE_UNITS = {
    "Newton (N)": 1.0,
    "Kilonewton (kN)": 1000.0,
    "Meganewton (MN)": 1000000.0,
    "Kilogram-force (kgf)": 9.80665,
    "Ton-force (metric) (tf)": 9806.65,
    "Pound-force (lbf)": 4.4482216152605,
    "Kip (kip)": 4448.2216152605
}

STRESS_UNITS = {
    "Pascal (Pa)": 1.0,
    "Kilopascal (kPa)": 1000.0,
    "Megapascal (MPa)": 1000000.0,
    "Gigapascal (GPa)": 1000000000.0,
    "kgf/cm² (ksc)": 98066.5,
    "Pounds per square inch (psi)": 6894.75729,
    "Kips per square inch (ksi)": 6894757.29,
    "Pounds per square foot (psf)": 47.88025898
}

AREA_UNITS = {
    "Square meter (m²)": 1.0,
    "Square centimeter (cm²)": 0.0001,
    "Square millimeter (mm²)": 0.000001,
    "Hectare (ha)": 10000.0,
    "Square inch (sq in)": 0.00064516,
    "Square foot (sq ft)": 0.09290304,
    "Square yard (sq yd)": 0.83612736,
    "Acre (ac)": 4046.8564224,
    "Rai (Thai)": 1600.0,
    "Ngan (Thai)": 400.0,
    "Square Wa (Thai)": 4.0
}

def get_conversion_categories():
    """Returns a dictionary containing the available units for each category."""
    return {
        "Force": list(FORCE_UNITS.keys()),
        "Stress": list(STRESS_UNITS.keys()),
        "Area": list(AREA_UNITS.keys())
    }

def convert(value, from_unit, to_unit, category):
    """
    Converts a value from one unit to another within a specific category.
    
    Args:
        value (float): The numeric value to convert.
        from_unit (str): The unit to convert from.
        to_unit (str): The unit to convert to.
        category (str): The category of the units (Force, Stress, Area).
        
    Returns:
        float: The converted value.
    """
    if category == "Force":
        units = FORCE_UNITS
    elif category == "Stress":
        units = STRESS_UNITS
    elif category == "Area":
        units = AREA_UNITS
    else:
        raise ValueError(f"Invalid category: {category}")
    
    if from_unit not in units or to_unit not in units:
        raise ValueError(f"Invalid unit for category {category}")
        
    # Convert the input value to the base unit
    base_value = value * units[from_unit]
    
    # Convert from the base unit to the target unit
    result = base_value / units[to_unit]
    
    return result
