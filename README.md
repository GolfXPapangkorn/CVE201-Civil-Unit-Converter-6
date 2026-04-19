# Civil Engineering Unit Converter 🏗️

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-success.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)

A modern, fast, and lightweight desktop application built in Python for Civil Engineering students and professionals. It provides quick and precise unit conversions for **Force**, **Stress**, and **Area**, with special support for Thai land measurement units.

## ✨ Features

- **Modern UI/UX**: Built with `customtkinter` for a sleek, responsive, and native-feeling interface that supports both Light and Dark modes.
- **Accurate Conversions**: Dictionary-based "Base Unit" logic ensures high accuracy for floating-point calculations while maintaining O(1) codebase extensibility.
- **Specialized Units**: Includes standard SI and Imperial units as well as local Thai area units (**Rai, Ngan, Square Wa**).
- **Quality of Life**: Features an instant unit swapping button (⇄), a clear button, and intelligent output formatting (standard decimals vs. scientific notation based on scale).

## 🧮 Supported Units

| Category | Available Units |
| :--- | :--- |
| **Force** | Newton (N), Kilonewton (kN), Meganewton (MN), Kilogram-force (kgf), Ton-force (tf), Pound-force (lbf), Kip |
| **Stress (Pressure)** | Pascal (Pa), Kilopascal (kPa), Megapascal (MPa), Gigapascal (GPa), kgf/cm² (ksc), psi, ksi, psf |
| **Area** | Square meter (m²), cm², mm², Hectare (ha), sq in, sq ft, sq yd, Acre, **Rai, Ngan, Square Wa** |

---

## 🚀 Installation & Setup

### Prerequisites
You must have Python 3.x installed on your system.
> *Note for Windows users:* Ensure you select **"Add Python to PATH"** during installation.

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/civil-engineering-unit-converter.git
cd civil-engineering-unit-converter
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
You can run the script manually:
```bash
python main.py
```
*(Windows users can also double-click `run_app.bat` for convenience).*

---

## 📦 Building an Executable (.exe)

If you wish to distribute this application as a standalone executable (so users do not need Python installed), you can compile it using `PyInstaller`.

1. Install PyInstaller (if not already installed via requirements):
   ```bash
   pip install pyinstaller
   ```
2. Build the `.exe`:
   ```bash
   pyinstaller --noconsole --onefile --windowed main.py
   ```
*(Windows users can simply double-click the included `build.bat` script to automate this).* 
The final executable will be generated inside the `dist/` folder.

## 📁 Repository Structure

```text
├── main.py                    # Main GUI application logic
├── conversions.py             # Pure-logic unit mapping dictionaries
├── requirements.txt           # Python dependencies (customtkinter)
├── .gitignore                 # Git ignore file
├── technical_architecture.md  # Explanation of codebase structure
├── verification_plan.md       # Unit conversion testing plan
├── user_manual.md             # Detailed usage instructions
├── run_app.bat                # Windows helper script to launch app
└── build.bat                  # Windows helper script to build .exe
```

## 🤝 Contributing
Contributions are welcome! If you would like to add new engineering units (e.g., Volume, Density, Moment of Inertia), simply update the dictionaries in `conversions.py` and submit a Pull Request.

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).
