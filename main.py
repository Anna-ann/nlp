import tkinter as tk
from analyzer_gui import PrecedentAnalyzerGUI
from text_processor import preprocess_text
from analyzer import identify_precedent_phenomena

def main():
    file_path = tk.filedialog.askopenfilename(initialdir="/", title="Select File",
                                               filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if not file_path:
        return

    text = preprocess_text(file_path)

    doc = nlp(text)

    identified_phenomena = identify_precedent_phenomena(doc)

    root = tk.Tk()
    app = PrecedentAnalyzerGUI(root, identified_phenomena)
    root.mainloop()

if __name__ == "__main__":
    main()
