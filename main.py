import FreeSimpleGUI as sg
from calculations import *
from chart import generate_chart, draw_chart

sg.theme("darkgreen4")

initial_value_label = sg.Text("Initial Value: ")
initial_value_input = sg.Input(key="initial_value")

interest_rate_label = sg.Text("Interest Rate (%): ")
interest_rate_input = sg.Input(key="interest_rate")

compounding_period_label = sg.Text("Compounding Period:")
compounding_period_dropdown = sg.DropDown(values=["Annually", 
                                                  "Semi-Annually",
                                                  "Quarterly", 
                                                  "Monthly", 
                                                  "Daily"],
                                          key="compounding_period")
years_label = sg.Text("Years:")
years_input = sg.Input(key="years")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="Output")

compounded_chart = sg.Canvas(key="compounded_chart")

label_column = sg.Column([[initial_value_label], [interest_rate_label],
                          [years_label], [compounding_period_label],[convert_button]])
input_column = sg.Column([[initial_value_input], [interest_rate_input],
                          [years_input], [compounding_period_dropdown], [output_label]])

layout = [[label_column, input_column], [compounded_chart]]

window = sg.Window("Compound Interest Calculator", layout=layout)

while True:
    event, values = window.read()

    match event:

        case "Convert":
            initial_value = values["initial_value"]
            interest_rate = values["interest_rate"]
            period = values["compounding_period"]
            years = values["years"]
            try:
                converted = compoundInterest(initial_value, interest_rate, period, years)
                chart = generate_chart(converted)
                draw_chart(window["compounded_chart"].TKCanvas, chart) # Displays chart

            except ValueError:
                window["Output"].update(value=f"Invalid Input", text_color="red")

            except TypeError:
                window["Output"].update(value=f"Invalid Input", text_color="red")

        case sg.WIN_CLOSED:
            break
window.close()
