import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Takes the calculated compound interest and generates a chart
def generate_chart(compounded_interest):
    years = []
    amounts = []
    for i, amount in enumerate(compounded_interest):
        years.append(i)
        amounts.append(round(amount, 2))

    fig, ax = plt.subplots()

    bars = ax.bar(years, amounts, color="lightblue")

    ax.bar_label(bars, label_type='edge', rotation=90, padding=2)
    ax.set_title("Compounded interest")
    ax.set_xlabel("Years")
    ax.set_ylabel("Total Value")

    return fig

# Draws the graph for displaying on gui
def draw_chart(canvas, figure):

    for child in canvas.winfo_children():
        child.destroy()

    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg