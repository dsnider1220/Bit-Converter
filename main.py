from tkinter import *
from tkinter import ttk
class main:
    def __init__(self, root):
    
        root.title("Bit Converter")

        mainScreen = ttk.Frame(root, padding=(10, 10, 10, 10))
        mainScreen.grid(column=0, row=0, sticky=NSEW)

        mainLabel = "Bit Converter"

        mainLabelPlace = ttk.Label(
            mainScreen,
            text=mainLabel,
            anchor=CENTER
            
        )

        mainLabelPlace.grid(column=0, row=0, columnspan=2, sticky=EW)

        # Radio buttons
        conversionRadio = StringVar(value="Binary")

        binaryRadio = ttk.Radiobutton(
            mainScreen,
            text="Binary",
            value="Binary",
            variable=conversionRadio
        )

        hexRadio = ttk.Radiobutton(
            mainScreen,
            text="Hexadecimal",
            value="Hexadecimal",
            variable=conversionRadio
        )

        decimalRadio = ttk.Radiobutton(
            mainScreen,
            text="Decimal",
            value="Decimal",
            variable=conversionRadio
        )

        binaryRadio.grid(column=0, row=2, sticky=W, padx=5 )
        hexRadio.grid(column=0, row=3, sticky=W, padx=5)
        decimalRadio.grid(column=0, row=4, sticky=W, padx=5)


        # User input
        userInput = ttk.Entry(mainScreen, width=20)

        submitButton = ttk.Button(
            mainScreen,
            text="Calculate",
            command=lambda: convert_bits()
        )

        conversion = StringVar()

        conversionLabel = ttk.Label(
            mainScreen,
            textvariable=conversion,
            background="yellow",
            borderwidth=8,
            relief="ridge"
        )


        userInput.grid(column=1, row=2, rowspan=2, sticky=EW, padx=5)
        submitButton.grid(column=1, row=4, sticky=EW, padx=5)
        conversionLabel.grid(column=1, row=5, columnspan=2, sticky=EW, padx=5)


        def convert_bits():
            user_value = userInput.get().strip()
            selected_conversion = conversionRadio.get()
    
            try:
                if selected_conversion == "Binary":
                    # Convert binary input to decimal
                    decimal_value = int(user_value, 2)
                    binary_value = bin(decimal_value)[2:]
                    hex_value = hex(decimal_value)[2:].upper()
                    conversion.set(
                        f"Decimal: {decimal_value}\nHexadecimal: {hex_value}\nBinary: {binary_value}"
                    )
    
                elif selected_conversion == "Hexadecimal":
                    # Convert hexadecimal input to decimal
                    decimal_value = int(user_value, 16)
                    binary_value = bin(decimal_value)[2:]
                    hex_value = hex(decimal_value)[2:].upper()
                    conversion.set(
                        f"Decimal: {decimal_value}\nHexadecimal: {hex_value}\nBinary: {binary_value}"
                    )
    
                elif selected_conversion == "Decimal":
                    # Convert decimal input to binary and hexadecimal
                    decimal_value = int(user_value)
                    binary_value = bin(decimal_value)[2:]
                    hex_value = hex(decimal_value)[2:].upper()
    
                    conversion.set(
                        f"Decimal: {decimal_value}\nHexadecimal: {hex_value}\nBinary: {binary_value}"
                    )
    
            except ValueError:
                conversion.set("Invalid input.")

root = Tk()
main(root)
root.mainloop()