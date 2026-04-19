# Verification Plan: Civil Engineering Unit Converter

This document outlines the test cases to verify the accuracy of the unit conversions implemented in the application. These test cases compare the application's output with expected manual calculations based on standard engineering conversion factors.

## Testing Methodology

For each category (Force, Stress, Area), several conversions should be performed in the application. The results must match the expected values within an acceptable tolerance for floating-point arithmetic (e.g., up to 4-5 decimal places).

## 1. Force Conversions

| From Unit | Value | To Unit | Expected Result | Calculation Basis |
| :--- | :--- | :--- | :--- | :--- |
| Kilonewton (kN) | 5 | Newton (N) | 5000 N | 1 kN = 1000 N |
| Meganewton (MN) | 2.5 | Kilonewton (kN) | 2500 kN | 1 MN = 1000 kN |
| Kip (kip) | 10 | Kilonewton (kN) | ~44.4822 kN | 1 kip ≈ 4.44822 kN |
| Kilogram-force (kgf) | 100 | Newton (N) | 980.665 N | 1 kgf = 9.80665 N |
| Ton-force (tf) | 2 | Kilonewton (kN) | ~19.6133 kN | 1 tf = 9.80665 kN |

## 2. Stress/Pressure Conversions

| From Unit | Value | To Unit | Expected Result | Calculation Basis |
| :--- | :--- | :--- | :--- | :--- |
| Megapascal (MPa) | 30 | Kilopascal (kPa) | 30000 kPa | 1 MPa = 1000 kPa |
| Megapascal (MPa) | 25 | kgf/cm² (ksc) | ~254.929 ksc | 1 MPa ≈ 10.197162 ksc |
| Pounds per sq in (psi) | 4000 | Megapascal (MPa) | ~27.579 MPa | 1 psi ≈ 0.00689476 MPa |
| Kips per sq in (ksi) | 60 | Megapascal (MPa) | ~413.685 MPa | 1 ksi ≈ 6.89476 MPa |

## 3. Area Conversions (Including Thai Units)

| From Unit | Value | To Unit | Expected Result | Calculation Basis |
| :--- | :--- | :--- | :--- | :--- |
| Square meter (m²) | 10000 | Hectare (ha) | 1 ha | 1 ha = 10000 m² |
| Rai (Thai) | 1 | Square meter (m²) | 1600 m² | 1 Rai = 1600 m² |
| Rai (Thai) | 1 | Ngan (Thai) | 4 Ngan | 1 Rai = 4 Ngan |
| Ngan (Thai) | 1 | Square Wa (Thai) | 100 Sq Wa | 1 Ngan = 100 Sq Wa |
| Square Wa (Thai) | 100 | Square meter (m²) | 400 m² | 1 Sq Wa = 4 m² |
| Acre (ac) | 1 | Square meter (m²) | ~4046.86 m² | 1 Acre ≈ 4046.856 m² |

## Edge Cases to Test

1. **Zero Value**: Entering `0` in any category should result in `0`.
2. **Negative Values**: While physical magnitudes are generally positive in basic structural dimensions, the math should compute correctly for components like compressive vs tensile forces.
3. **Invalid Input**: Typing text like `abc` should trigger a red "Invalid number input." error message rather than crashing the application.
4. **Extremely Large/Small Numbers**: Entering values like `0.00000001` or `1000000000` should elegantly format to scientific notation (e.g., `1e-08`).
