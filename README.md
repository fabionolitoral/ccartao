# basic-python Documentation

Template basic for python projects

## 1. Folder Structure
```
ccartao/
│
├── ccartao/
│   ├── __init__.py           # Make directory a Python package
│   ├── main.py               # Program entry point
│   ├── config.py             # Project settings and constants
│   ├── utils.py              # Utility functions
│   ├── models/               # Class definitions and data models
│   │   ├── __init__.py
│   │   ├── model_a.py
│   │   └── model_b.py
│   ├── services/             # Business logic, communication with APIs, etc.
│   │   ├── __init__.py
│   │   ├── service_a.py
│   │   └── service_b.py
│   ├── controllers/          # Controllers (MVC), interaction between models and views
│   │   ├── __init__.py
│   │   ├── controller_a.py
│   │   └── controller_b.py
│   ├── utils/                # Utility functions
│   │   ├── __init__.py
│   │   ├── util_a.py
│   │   └── util_b.py
│   └── views/                # User interface or view templates
│       ├── __init__.py
│       ├── view_a.py
│       └── view_b.py
├── logs/                    # Log files
│   ├── app.log              # Main application log file
│   ├── errors.log           # Error log, if separate
|   ├── .gitkeep 
│   └── ...                  # Other logs (rotated, for example)
│
├── tests/                   # Unit and integration tests
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_utils.py
│   ├── test_models.py
│   ├── test_services.py
│   └── test_controllers.py
|
|── docs
│   ├── README.md
│   └── architecture.md
│
├── scripts/                  # Helper or utility scripts
│   ├── data_migration.py
│   └── setup_env.py
|
├── tmp/                      # Temporary files
│   ├── tmp_1.tmp
│   ├── tmp_2.tmp
|   ├── ...                   # Other temporary files
|   └── .gitkeep              # File to keep empty folder in Git
|
|── vendor/                   # Third-party scripts/libraries
|
├── .gitignore                # Files and folders to ignore by Git
├── requirements.txt          # Project dependencies
├── setup.py                  # Project installation and configuration script
└── README.md                 # Project Overview and Documentation
```

### Description of folders and files

- [ ] **ccartao/**: Main folder of your project, which contains the source code.

- [ ] **main.py**: Ponto de entrada da aplicação. Pode ser chamado app.py ou run.py dependendo da convenção que você preferir.

- [ ] **config.py**: Entry point of the application. Can be called app.py or run.py depending on the convention you prefer.

- [ ] **utils.py**: Utility functions that do not fit directly into any other category.

- [ ] **models/**: Folders containing classes and data structures, especially useful if you are dealing with complex databases or models.

- [ ] **services/**: Files that handle business logic, calls to external APIs, or other core functionality.

- [ ] **controllers/**: Layer that interacts between models and views, especially in MVC-based architectures.

- [ ] **views/**: View templates or user interfaces, depending on the type of application (web, CLI, GUI).

- [ ] **tests/**: Folder dedicated to unit and integration tests. Each test file corresponds to a module of the project.

- [ ] **scripts/**: Helper scripts such as database migrations, environment startup scripts, etc.

- [ ] **docs/**: Project documentation, including README.md, architecture diagrams, and any other necessary documentation.

- [ ] **.gitignore**: List of files and folders that should not be tracked by Git.

- [ ] **.gitkeep**: Empty file to hold an empty folder in Git, since Git doesn't track empty folders.

- [ ] **tmp/**: Folder for temporary files that should not be tracked by Git. Can be useful for storing cache files, temporary logs, etc.

- [ ] **vendor/**: Folder for third-party scripts or libraries that are not available via pip or another package manager.

- [ ] **requirements.txt**: List of project dependencies. Can be generated with pip freeze > requirements.txt.

- [ ] **setup.py**: Project configuration script for installation via pip or similar.

## 2. Install Application

### 2.1 Virtual environment

#### Creation
```
python -m venv venv
```

#### Activation
```
#linux
source venv/bin/activate

#windows
.\venv\Scripts\activate
```

### 2.2 Install dependencies

```
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

### 2.3 Update dependencies
```
pip freeze > requirements.txt
```

### 2.4 Tests

#### 2.4.1 Install pytest
```
pip install pytest
```

#### 2.4.2 Install coverage
```
pip install pytest-cov
```

Edit the .coveragerc file and add the folders you want to cover.

```
[run]
source = ./folder-to-cover

[report]
exclude_lines =
    def __str__
```

## 3. Run Application

```
python main.py
```

## 4. Testing

```
pytest
```

## 5. Coverage

```
pytest -v --cov=src tests/ --cov-report term-missing
```