# Manajemen Mata Kuliah 
============

# Getting Started
---------------

1. Change directory into your newly created project:
    ```bash
    cd manajemen_mk
    ```

2. Create a Python virtual environment:
    ```bash
    python3 -m venv env
    venv/Scripts/Activate
    ```

3. Upgrade packaging tools:
    ```bash
    pip install --upgrade pip setuptools
    ```

4. Install the project in editable mode with its testing requirements:
    ```bash
    pip install -e ".[testing]"
    ```

5. Initialize and upgrade the database using Alembic:
    - Generate your first revision:
        ```bash
        alembic -c development.ini revision --autogenerate -m "init"
        ```
    - Upgrade to that revision:
        ```bash
        alembic -c development.ini upgrade head
        ```

6. Load default data into the database using a script:
    ```bash
    initialize_manajemen_mk_db development.ini
    ```

7. Run your project:
    ```bash
    pserve development.ini
    ```

---------------
# Hasil Test API Endpoints
<li><a href=\"API test/API-Test(GET).png\">API Test GET</a></li>\n
<li><a href=\"API test/API-Test(POST).png\">API Test POST</a></li>\n
<li><a href=\"API test/API-Test(PUT).png\">API Test PUT</a></li>\n
<li><a href=\"API test/API-Test(DELETE).png\">API Test DELETE</a></li>\n
    