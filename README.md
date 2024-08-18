Precedent Phenomena Analyzer
Overview

The Precedent Phenomena Analyzer is a Python application that uses natural language processing (NLP) to identify and analyze precedent phenomena from text files. It provides a graphical user interface (GUI) for users to interact with the results, view detailed information, and visualize data.
Features

    Text Processing: Uses NLP to preprocess and analyze text.
    Multi-language Support: Identifies language and applies appropriate NLP models.
    GUI Interface: Interactive GUI for viewing and analyzing identified phenomena.
    Data Visualization: Visualize the recognition levels of identified phenomena.

Requirements

    Python 3.x
    tkinter (for GUI)
    spacy (for NLP)
    stanza (for additional language support)
    langdetect (for language detection)
    matplotlib (for data visualization)
    sqlite3 (for database access)

Installation

    Clone the Repository:

    bash

git clone https://github.com/your-username/precedent-phenomena-analyzer.git
cd precedent-phenomena-analyzer

Install Required Libraries:

bash

pip install spacy stanza langdetect matplotlib

Download the necessary language models:

bash

    python -m spacy download en_core_web_sm
    python -m spacy download ru_core_news_md
    python -c "import stanza; stanza.download('kk')"

    Database Setup:

    Ensure you have the selected_precedents.db SQLite database in the same directory as your scripts. This database should contain the table precedent_phenomena with the following columns:
        name
        cultural_meaning
        recognition_level
        interpretation
        symbolic_meaning
        associated_event
        adaptable_usage
        semantic_association
        collocation_patterns
        evolution_over_time
        cultural_variations

Usage

    Run the Application:

    Execute the main.py script to start the application:

    bash

    python main.py

    Select a File:

    A file dialog will open. Select a text file to analyze.

    Interact with the GUI:
        View Details: Click to see detailed information about the selected phenomenon.
        Cultural Analysis: View cultural analysis of the selected phenomenon.
        Social Impact Analysis: See the social impact analysis of the selected phenomenon.
        Visualize Data: Open a window to visualize the recognition levels of identified phenomena.

File Descriptions

    main.py: The main script that initializes the GUI and handles file selection.
    analyzer_gui.py: Contains the PrecedentAnalyzerGUI class for the graphical user interface.
    text_processor.py: Includes functions for preprocessing text and identifying precedent phenomena.
    analyzer.py: Contains the identify_precedent_phenomena function for extracting phenomena from the text.
    lang_processor.py: Handles language detection and NLP model selection.

Contribution

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
