# Automated Personal Loan Document Processing

This project automates the processing of personal loan application documents using OCR (Optical Character Recognition) and Streamlit.

## Methodology

1.  **Document Upload:** The user uploads an image of a loan application form through the Streamlit interface.

2.  **OCR Processing:**
    * The application uses the `easyocr` library to extract text and bounding box coordinates from the uploaded image.
    * The code identifies all the bounding boxes in the form image.
        * Marks important fields such as Name, Application Date, etc., as Regions of Interest and saves the bounding box coordinates.
        * It extracts the corresponding field value and maps it to the fields, i.e., extracts the name written in the form and associates the value with the name field.

    Here's an illustration of the OCR processing steps:

    ![OCR Processing Steps](https://i.ibb.co/TMgZGS0J/Screenshot-from-2025-04-24-17-55-52.png)

3.  **Data Display and Editing:**
    * The extracted data is displayed in a Pandas DataFrame within the Streamlit application.
    * The user can edit the extracted data for any corrections.

4.  **Final Data and Download:**
    * The final, potentially edited, data is displayed.
    * The user can download the data as a CSV file.

## How to Run the Application

### Prerequisites

* **Python:** Ensure you have Python 3.9 or later installed.
* **Virtual Environment (Recommended):** It's highly recommended to use a virtual environment to manage dependencies. If you don't have `virtualenv` installed, you can install it:

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

    * The application will open in your web browser. If it doesn't open automatically, you should see the URL in your terminal (e.g., `http://localhost:8501`). Open this URL in your browser.
