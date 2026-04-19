# Civil Engineering Unit Converter - User Manual

Welcome to the Civil Engineering Unit Converter! This application is designed specifically for Civil Engineering students and professionals to quickly convert values between standard dimensions, including specialized Thai land measurement units.

## Installation and Setup

### Prerequisites
- You must have **Python 3.x** installed on your system.
- You will need an active internet connection to download dependencies.

### Installation
1. Open your terminal or command prompt.
2. Navigate to the folder containing the application:
   ```bash
   cd path/to/Application CVE 200
   ```
3. Install the required graphics library using pip:
   ```bash
   pip install -r requirements.txt
   ```
   *(This will install the `customtkinter` library, which provides the modern GUI components).*

### Launching the Application
Run the application by executing the main script:
```bash
python main.py
```
The graphical interface will appear on your screen, automatically matching your operating system's light or dark mode.

---

## How to Use the Converter

### Step 1: Select the Category
At the top of the window, locate the **Category** dropdown menu. Click on it to select the dimension you are calculating. The options are:
- **Force** (e.g., Newtons, Kilonewtons, Kips)
- **Stress** (e.g., Pascals, Megapascals, psi, kgf/cm²)
- **Area** (e.g., Square meters, Hectares, Rai, Ngan, Square Wa)

*Note: Changing the category will automatically update the available units in the following steps.*

### Step 2: Enter the Value
Locate the **Value to Convert** input box. Type the number you wish to convert.
- You can use decimals (e.g., `14.5`).
- Do not type text or unit symbols into this box; only the numeric value is allowed.

### Step 3: Choose Your Units
- Under **From Unit**, select the original unit of your value.
- Under **To Unit**, select the desired unit you want the value converted into.

### Step 4: Convert
Click the large blue **Convert** button. The converted result will appear prominently at the bottom of the window.

## Troubleshooting
- **Red "Invalid number input." text appears**: Ensure you only typed numbers (and a decimal point, if necessary) in the value box. Remove any letters, spaces, or commas.
- **Red "Please enter a value." text appears**: You clicked the convert button before typing a number.
- **Application looks broken or fails to launch**: Make sure you installed `customtkinter` correctly using the setup instructions above.

## Supported Units

### Force
- Newton (N)
- Kilonewton (kN)
- Meganewton (MN)
- Kilogram-force (kgf)
- Ton-force (metric) (tf)
- Pound-force (lbf)
- Kip (kilopound)

### Stress
- Pascal (Pa)
- Kilopascal (kPa)
- Megapascal (MPa)
- Gigapascal (GPa)
- kgf/cm² (ksc)
- Pounds per square inch (psi)
- Kips per square inch (ksi)
- Pounds per square foot (psf)

### Area
- Square meter (m²)
- Square centimeter (cm²)
- Square millimeter (mm²)
- Hectare (ha)
- Square inch (sq in)
- Square foot (sq ft)
- Square yard (sq yd)
- Acre (ac)
- Rai (Thai Land Unit)
- Ngan (Thai Land Unit)
- Square Wa (Thai Land Unit)
