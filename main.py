import customtkinter as ctk
import conversions
import os
import sys

# For pyinstaller to find resources if needed
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Configure appearance
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

class UnitConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Civil Engineering Unit Converter")
        self.geometry("550x650")
        self.resizable(False, False)

        # Get categories and units
        self.categories = conversions.get_conversion_categories()
        self.current_category = "Force"

        # --- Main Frame for padding ---
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # --- Title ---
        self.title_label = ctk.CTkLabel(self.main_frame, text="Unit Converter", font=ctk.CTkFont(size=32, weight="bold"))
        self.title_label.pack(pady=(10, 20))

        # --- Category Selection ---
        self.category_frame = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.category_frame.pack(fill="x", pady=10)

        self.category_label = ctk.CTkLabel(self.category_frame, text="Select Category:", font=ctk.CTkFont(size=16, weight="bold"))
        self.category_label.pack(side="left", padx=20, pady=15)

        self.category_optionmenu = ctk.CTkSegmentedButton(
            self.category_frame, 
            values=list(self.categories.keys()),
            command=self.change_category,
            font=ctk.CTkFont(size=14)
        )
        self.category_optionmenu.pack(side="right", padx=20, pady=15, fill="x", expand=True)
        self.category_optionmenu.set("Force")

        # --- Input Section ---
        self.input_frame = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.input_frame.pack(fill="x", pady=10)

        self.value_label = ctk.CTkLabel(self.input_frame, text="Value to Convert:", font=ctk.CTkFont(size=15, weight="bold"))
        self.value_label.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")

        self.value_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Enter numeric value...", font=ctk.CTkFont(size=15), height=40)
        self.value_entry.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew", columnspan=3)

        self.from_label = ctk.CTkLabel(self.input_frame, text="From Unit:", font=ctk.CTkFont(size=14))
        self.from_label.grid(row=2, column=0, padx=20, pady=(5, 5), sticky="w")

        self.from_optionmenu = ctk.CTkOptionMenu(self.input_frame, values=self.categories[self.current_category], font=ctk.CTkFont(size=14), height=35)
        self.from_optionmenu.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="ew")

        # Swap Button
        self.swap_button = ctk.CTkButton(self.input_frame, text="⇄", width=40, height=35, command=self.swap_units, font=ctk.CTkFont(size=20))
        self.swap_button.grid(row=3, column=1, padx=5, pady=(0, 20))

        self.to_label = ctk.CTkLabel(self.input_frame, text="To Unit:", font=ctk.CTkFont(size=14))
        self.to_label.grid(row=2, column=2, padx=20, pady=(5, 5), sticky="w")

        self.to_optionmenu = ctk.CTkOptionMenu(self.input_frame, values=self.categories[self.current_category], font=ctk.CTkFont(size=14), height=35)
        self.to_optionmenu.grid(row=3, column=2, padx=20, pady=(0, 20), sticky="ew")

        if len(self.categories[self.current_category]) > 1:
            self.to_optionmenu.set(self.categories[self.current_category][1])

        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.columnconfigure(2, weight=1)

        # --- Buttons Section ---
        self.buttons_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.buttons_frame.pack(fill="x", pady=10)

        self.clear_button = ctk.CTkButton(self.buttons_frame, text="Clear", font=ctk.CTkFont(size=16), command=self.clear_input, fg_color="#E74C3C", hover_color="#C0392B", height=45)
        self.clear_button.pack(side="left", padx=(0, 10), expand=True, fill="x")

        self.convert_button = ctk.CTkButton(self.buttons_frame, text="Convert", font=ctk.CTkFont(size=16, weight="bold"), command=self.perform_conversion, height=45)
        self.convert_button.pack(side="right", padx=(10, 0), expand=True, fill="x")

        # --- Output Section ---
        self.output_frame = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.output_frame.pack(fill="x", pady=10)

        self.result_label = ctk.CTkLabel(self.output_frame, text="Result:", font=ctk.CTkFont(size=15, weight="bold"))
        self.result_label.pack(anchor="w", padx=20, pady=(15, 0))

        self.result_value = ctk.CTkLabel(self.output_frame, text="---", font=ctk.CTkFont(size=32, weight="bold"), text_color="#1f6aa5")
        self.result_value.pack(padx=20, pady=(5, 20))

    def change_category(self, new_category):
        self.current_category = new_category
        new_units = self.categories[new_category]
        
        self.from_optionmenu.configure(values=new_units)
        self.from_optionmenu.set(new_units[0])
        
        self.to_optionmenu.configure(values=new_units)
        to_idx = 1 if len(new_units) > 1 else 0
        self.to_optionmenu.set(new_units[to_idx])
        
        self.clear_input()

    def swap_units(self):
        from_val = self.from_optionmenu.get()
        to_val = self.to_optionmenu.get()
        self.from_optionmenu.set(to_val)
        self.to_optionmenu.set(from_val)
        if self.value_entry.get().strip():
            self.perform_conversion()

    def clear_input(self):
        self.value_entry.delete(0, 'end')
        self.result_value.configure(text="---", text_color="#1f6aa5")

    def perform_conversion(self):
        try:
            val_str = self.value_entry.get().strip()
            if not val_str:
                self.show_error("Please enter a value.")
                return
                
            value = float(val_str)
            from_unit = self.from_optionmenu.get()
            to_unit = self.to_optionmenu.get()
            
            result = conversions.convert(value, from_unit, to_unit, self.current_category)
            
            if "(" in to_unit and ")" in to_unit:
                unit_symbol = to_unit.split('(')[-1].replace(')', '')
            else:
                unit_symbol = to_unit
            
            if result == 0:
                formatted_result = "0"
            elif abs(result) < 0.0001 or abs(result) > 1000000:
                formatted_result = f"{result:.6e}"
            else:
                formatted_result = f"{result:.6f}".rstrip('0').rstrip('.')
                
            if formatted_result == "":
                formatted_result = "0"

            self.result_value.configure(text=f"{formatted_result} {unit_symbol}", text_color=("#1f6aa5", "#569BFF"))
            
        except ValueError:
            self.show_error("Invalid number input.")

    def show_error(self, message):
        self.result_value.configure(text=message, text_color="#E74C3C")

if __name__ == "__main__":
    app = UnitConverterApp()
    app.mainloop()
