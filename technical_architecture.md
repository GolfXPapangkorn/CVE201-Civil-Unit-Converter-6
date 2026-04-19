# Technical Architecture

This document explains the software architecture and technical decisions behind the Civil Engineering Unit Converter application.

## Overview

The application is built using Python, utilizing the `customtkinter` library for a modern graphical user interface (GUI). It employs a modular architecture, strictly separating the user interface elements (`main.py`) from the core mathematical and logic operations (`conversions.py`). This separation of concerns allows for easier testing, scaling, and maintainability.

## 1. Directory Structure

- `main.py`: The entry point for the application. It handles the window, widgets, event listeners, and data validation.
- `conversions.py`: A pure-logic module containing dictionaries mapping units to their base scale, and a conversion function.
- `requirements.txt`: The dependency list (e.g., `customtkinter`).

## 2. Data Strategy: Dictionary Mapping via Base Units

Rather than writing combinatorial `if/else` logic to convert every unit to every other unit (which requires $N \times (N-1)$ formulas), the application uses a "Base Unit Strategy" ($2N$ operations).

For each physical category, a single **Base Unit** is selected where its scaling factor is exactly `1.0`. All other units in that category are mapped to how many base units they equate to.

- **Force Base Unit**: Newton (N)
- **Stress Base Unit**: Pascal (Pa)
- **Area Base Unit**: Square meter (m²)

### Example: Area Dictionary
```python
AREA_UNITS = {
    "Square meter (m²)": 1.0,           # Base Unit
    "Rai (Thai)": 1600.0,               # 1 Rai = 1600 m²
    "Ngan (Thai)": 400.0,               # 1 Ngan = 400 m²
    "Square Wa (Thai)": 4.0             # 1 Sq Wa = 4 m²
}
```

### The Conversion Algorithm
The conversion happens in two computational steps:
1. **Convert to Base Unit**: `base_value = input_value * units_dict[from_unit]`
2. **Convert to Target Unit**: `final_result = base_value / units_dict[to_unit]`

This ensures extending the application to support new units (e.g., `Hectare`) requires only adding a single line to the dictionary, not dozens of new functions.

## 3. User Interface (`main.py`)

The application is encapsulated within a custom class `UnitConverterApp` inheriting from `customtkinter.CTk`.

### Key Components:
- **`change_category` Callback**: This triggers whenever the user selects a new dimension (Force, Stress, Area) from the top dropdown. It dynamically updates the internal lists of the "From Unit" and "To Unit" OptionMenus and resets the input and output fields to prevent state contamination between categories.
- **`perform_conversion` Callback**: Triggered by the "Convert" button. It fetches the string from the entry widget, attempts to cast it to a `float`, and handles `ValueError` exceptions smoothly by displaying an error message instead of crashing.
- **Output Formatting**: The result handles floating-point anomalies. If numbers are extremely large or small, it dynamically shifts to scientific notation. Otherwise, it strips trailing zeros and limits the string to six decimal places for visual clarity.
