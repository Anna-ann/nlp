import tkinter as tk
from tkinter import filedialog, Listbox, Scrollbar, Button, Label, messagebox, Toplevel
from text_processor import preprocess_text, identify_precedent_phenomena
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class PrecedentAnalyzerGUI:
    def __init__(self, master, identified_phenomena):
        self.master = master
        master.title("Identified Precedent Phenomena")
        self.identified_phenomena = identified_phenomena
        self.listbox = Listbox(master, width=60, height=20, font=("Courier", 12))
        self.listbox.pack(pady=10)
        scrollbar = Scrollbar(master, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.view_details_button = Button(master, text="View Details", command=self.view_details)
        self.view_details_button.pack()
        self.cultural_analysis_button = Button(master, text="Cultural Analysis", command=self.cultural_analysis)
        self.cultural_analysis_button.pack()
        self.social_impact_button = Button(master, text="Social Impact Analysis", command=self.social_impact_analysis)
        self.social_impact_button.pack()
        self.visualization_button = Button(master, text="Visualize Data", command=self.visualize_data)
        self.visualization_button.pack()

    def set_identified_phenomena(self, identified_phenomena):
        self.listbox.delete(0, tk.END)
        for phenomenon in identified_phenomena:
            self.listbox.insert(tk.END, phenomenon['name'])

    def view_details(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showinfo("Error", "Please select a phenomenon.")
            return
        selected_phenomenon = self.identified_phenomena[selected_index[0]]
        self.show_analysis_results(selected_phenomenon, "Details")

    def cultural_analysis(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showinfo("Error", "Please select a phenomenon.")
            return
        selected_phenomenon = self.identified_phenomena[selected_index[0]]
        self.show_analysis_results(selected_phenomenon, "Cultural Analysis")

    def social_impact_analysis(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showinfo("Error", "Please select a phenomenon.")
            return
        selected_phenomenon = self.identified_phenomena[selected_index[0]]
        self.show_analysis_results(selected_phenomenon, "Social Impact Analysis")

    def visualize_data(self):
        visualization_window = Toplevel(self.master)
        visualization_window.title("Data Visualization")
        names = [phenomenon['name'] for phenomenon in self.identified_phenomena]
        recognition_levels = [phenomenon['recognition_level'] for phenomenon in self.identified_phenomena]
        level_mapping = {'Very Low': 0, 'Low': 25, 'Moderate': 50, 'High': 75, 'Very High': 100}
        mapped_levels = [level_mapping[level] for level in recognition_levels]
        fig, ax = plt.subplots()
        ax.bar(names, mapped_levels, color='skyblue')
        ax.set_xlabel('Phenomenon Names')
        ax.set_ylabel('Recognition Levels')
        ax.set_title('Recognition Levels of Identified Phenomena')
        canvas = FigureCanvasTkAgg(fig, master=visualization_window)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, visualization_window)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas = canvas

    def show_analysis_results(self, phenomenon, analysis_type):
        if hasattr(self, "result_label"):
            self.result_label.destroy()
        result_label = Label(self.master, text="", justify=tk.LEFT)
        result_label.pack()
        if analysis_type == "Details":
            self.display_details(result_label, phenomenon)
        elif analysis_type == "Cultural Analysis":
            self.display_cultural_analysis(result_label, phenomenon)
        elif analysis_type == "Social Impact Analysis":
            self.display_social_impact_analysis(result_label, phenomenon)
        self.result_label = result_label

    def display_details(self, window, phenomenon):
        details_message = f"Name: {phenomenon['name']}\n"
        details_message += f"Cultural Significance: {phenomenon['cultural_meaning']}\n"
        details_message += f"Recognition Level: {phenomenon['recognition_level']}\n"
        label = Label(window, text=details_message, justify=tk.LEFT)
        label.pack()

    def display_cultural_analysis(self, window, phenomenon):
        cultural_message = f"Cultural Analysis for {phenomenon['name']}\n"
        cultural_message += f"Cultural Significance: {phenomenon['cultural_meaning']}\n"
        cultural_message += f"Recognition Level: {phenomenon['recognition_level']}\n"
        cultural_message += f"General Interpretation: {phenomenon['interpretation']}\n"
        cultural_message += f"Symbolic Meaning: {phenomenon['symbolic_meaning']}\n"
        cultural_message += f"Associated Event: {phenomenon['associated_event']}\n"
        cultural_message += f"Adaptable Usage: {phenomenon['adaptable_usage']}\n"
        cultural_message += f"Semantic Association: {phenomenon['semantic_association']}\n"
        cultural_message += f"Collocation Patterns: {phenomenon['collocation_patterns']}\n"
        cultural_message += f"Evolution Over Time: {phenomenon['evolution_over_time']}\n"
        cultural_message += f"Cultural Variations: {phenomenon['cultural_variations']}"
        label = Label(window, text=cultural_message, justify=tk.LEFT)
        label.pack()

    def display_social_impact_analysis(self, window, phenomenon):
        social_impact_message = f"Social Impact Analysis for {phenomenon['name']}\n"
        social_impact_message += f"Symbolic Meaning: {phenomenon['symbolic_meaning']}\n"
        social_impact_message += f"Related Story: {phenomenon['associated_event']}\n"
        label = Label(window, text=social_impact_message, justify=tk.LEFT)
        label.pack()

def main():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select File",
                                           filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if not file_path:
        return
    text = preprocess_text(file_path)
    identified_phenomena = identify_precedent_phenomena(text)
    root = tk.Tk()
    app = PrecedentAnalyzerGUI(root, identified_phenomena)
    app.set_identified_phenomena(identified_phenomena)
    root.mainloop()

if __name__ == "__main__":
    main()
