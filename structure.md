pipe-break-prediction/
│
├── data/                              # Project data
│   ├── raw/                           # Raw FOIL datasets
│   │   ├── wm_breaks_2004-2019.csv
│   │   ├── wm_breaks_2021.csv
│   │   ├── wm_breaks_2022.csv
│   │   └── FOIL_Request.pdf
│   └── processed/                    # Cleaned, transformed, or encoded versions
│       ├── breaks_cleaned.csv
│       └── breaks_model_ready.csv
│
├── notebooks/                         # Jupyter notebooks (pipeline steps)
│   ├── 00_data_ingestion.ipynb
│   ├── 01_preprocessing.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_evaluation.ipynb
│   ├── 05_results_visualization.ipynb
│   ├── 06_dashboard_prep.ipynb
│   └── README_notebooks.md
│
├── app/                               # Streamlit app
│   ├── main.py                        # Main entry point
│   ├── config.py                      # Theme, constants, app-level settings
│   ├── pages/                         # Modular pages using Streamlit's multipage support
│   │   ├── 01_Home.py
│   │   ├── 02_RiskMap.py
│   │   ├── 03_FeatureInsights.py
│   │   └── 04_ModelResults.py
│   ├── components/                    # Reusable UI parts
│   │   ├── filters.py
│   │   ├── sidebar.py
│   │   └── metrics_cards.py
│   ├── data/                          # Cache for display-ready CSVs
│   │   └── top_risk_segments.csv
│   └── utils/                         # Backend helpers
│       ├── load_data.py
│       ├── model_inference.py
│       └── format_helpers.py
│
├── report/                            # Quarto-generated technical report
│   ├── _quarto.yml
│   ├── index.qmd
│   ├── styles.css
│   ├── pipe-break-report.html         # Final rendered version
│   └── sections/                      # All report content here
│       ├── executive-summary.qmd
│       ├── problem-statement.qmd
│       ├── methodology.qmd
│       ├── model-development.qmd
│       ├── results.qmd
│       ├── discussion.qmd
│       ├── conclusion.qmd
│       ├── future-work.qmd
│       └── references.qmd
│
├── docs/                              # Project documentation & planning
│   ├── overview.md                    # High-level project summary
│   ├── dashboard_roadmap.md           # Streamlit app vision
│   ├── blog/                          # Blog drafts, outline, Medium-ready
│   └── whitepaper/                    # Whitepaper notebooks, strategy docs
│       ├── pipe_break_predictive_model_plan.ipynb
│       ├── pipeline_break_project_blueprint.ipynb
│       ├── polished_pdf_report_options.ipynb
│       └── whitepaper_project_notes.ipynb
│
├── src/                               # Core Python logic for processing/training
│   ├── __init__.py
│   ├── preprocess.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── utilities/
│       ├── cleanup_mapping.py
│       └── foil_utils.py
│
├── tests/                             # Unit tests for source code
│   └── test_preprocess.py
│
├── environment.yml                    # Conda environment definition
├── .gitignore
└── README.md                          # Usage + install instructions for the repo
