# Automated Personal Loan Document Processing

This project automates the processing of personal loan application documents using OCR (Optical Character Recognition) and Streamlit.

## Methodology

1.  **Document Upload:** The user uploads an image of a loan application form through the Streamlit interface.

2.  **OCR Processing:**
    * The application uses the `easyocr` library to extract text and bounding box coordinates from the uploaded image.
    * The code checks if the image is an RBL form.
        * If it is an RBL form, specific data fields are extracted.
        * If it is not an RBL form, all text in the image is extracted.

3.  **Data Display and Editing:**
    * The extracted data is displayed in a Pandas DataFrame within the Streamlit application.
    * The user can edit the extracted data for any corrections.

4.  **Final Data and Download:**
    * The final, potentially edited, data is displayed.
    * The user can download the data as a CSV file.

## How to Run the Application

### Prerequisites

* **Python:** Ensure you have Python 3.9 or later installed.
* **Virtual Environment (Recommended):** It's highly recommended to use a virtual environment to manage dependencies.  If you don't have `virtualenv` installed, you can install it:

    ```bash
    pip install virtualenv
    ```

### Steps

1.  **Clone the Repository (If applicable):** If you have the code in a remote repository (e.g., GitHub), clone it to your local machine:

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create a Virtual Environment (Recommended):**

    * Navigate to the project directory:

        ```bash
        cd your_project_directory
        ```

    * Create a virtual environment:

        ```bash
        python -m venv venv
        ```

    * Activate the virtual environment:

        * **On Windows:**

            ```bash
            venv\Scripts\activate
            ```

        * **On macOS/Linux:**

            ```bash
            source venv/bin/activate
            ```

3.  **Install Dependencies:**

    * Install the required Python packages using `pip`:

        ```bash
        pip install -r requirements.txt
        ```

        * If you don't have a `requirements.txt` file, create one with the following:

            ```
            streamlit
            easyocr
            Pillow
            pandas
            numpy
            ```

4.  **Run the Application:**

    * Run the Streamlit application:

        ```bash
        streamlit run app.py
        ```

5.  **Access the Application:**

    * The application will open in your web browser.  If it doesn't open automatically, you should see the URL in your terminal (e.g., `http://localhost:8501`).  Open this URL in your browser.

## How to Push Code to a Repository (e.g., GitHub)

These instructions assume you want to use GitHub.  The general process is similar for other Git hosting services (e.g., GitLab, Bitbucket).

1.  **Create a Repository on GitHub:**

    * Go to <https://github.com/> and log in to your account.
    * Click the "+" button in the top right corner and select "New repository."
    * Give your repository a name (e.g., "personal-loan-ocr").
    * You can add a description (optional).
    * Choose whether you want the repository to be public or private.
    * You can choose to add a README file, but it's not required at this stage.
    * Click "Create repository."

2.  **Initialize a Git Repository on Your Local Machine (If you haven't already):**

    * Navigate to your project directory in your terminal:

        ```bash
        cd your_project_directory
        ```

    * Initialize a Git repository:

        ```bash
        git init
        ```

3.  **Add Your Files:**

    * Add the files you want to commit to the repository:

        ```bash
        git add .  # Adds all files in the current directory
        # Or, to add specific files:
        # git add app.py requirements.txt ...
        ```

4.  **Commit Your Changes:**

    * Commit the changes with a descriptive message:

        ```bash
        git commit -m "Initial commit of loan document processing application"
        ```

5.  **Link Your Local Repository to the Remote Repository:**

    * On your GitHub repository page, you'll see instructions on how to connect your local repository to the remote one.  It will look something like this:

        ```bash
        git remote add origin [https://github.com/your_username/your_repository_name.git](https://github.com/your_username/your_repository_name.git)
        ```

        * Replace `your_username` and `your_repository_name` with your actual GitHub username and repository name.  You can copy this command directly from your GitHub repository page.

6.  **Push Your Changes to GitHub:**

    * Push your committed changes to the remote repository:

        ```bash
        git push -u origin master  # or main, depending on your branch name
        ```
        * The `-u` flag sets the upstream branch, so you only need to use `git push` in the future.
        * If you created the repository after 2020, your default branch might be called `main` instead of `master`.  Check your GitHub repository page to see the correct branch name.

7.  **Subsequent Changes:**

    * After making further changes to your code:

        ```bash
        git add .
        git commit -m "Describe your changes here"
        git push
        ```

##  File Structure

Here's the expected file structure:

your_project_directory/app.py          # Streamlit application coderequirements.txt  # List of Python dependenciesProcfile        # Heroku Procfile (for Heroku deployment)setup.sh        #Heroku setupyour_image.jpg    # Example image file (optional)data.csv        # Example data file (optional)...
##  Important Notes

* **Virtual Environment:** Always work within a virtual environment to avoid conflicts between project dependencies.
* **requirements.txt:** Keep your `requirements.txt` file up-to-date.  Whenever you install a new package with `pip`, update this file:  `pip freeze > requirements.txt`
* **Git:** Use Git to version control your code and back it up to a remote repository like GitHub.  Commit your changes frequently with descriptive messages.
* **File Paths:** Use relative file paths in your code (e.g., `"data.csv"` instead of `"/Users/yourname/data.csv"`) so that your application works correctly in different environments.
* **Secrets:** Do not store API keys, passwords, or other sensitive information directly in your code.  Use environment variables or a secrets management solution.
