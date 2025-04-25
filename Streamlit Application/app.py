import streamlit as st
import easyocr
from PIL import Image, ImageDraw
import pandas as pd
import numpy as np
import logging
import io

reader = easyocr.Reader(['en'])

logging.getLogger('PIL').setLevel(logging.CRITICAL)

def extract_text_with_bbox(image):
    """
    Extracts text and bounding boxes from the image using OCR.

    Args:
        image (PIL.Image.Image): The image to process.

    Returns:
        list: A list of dictionaries, where each dictionary contains the text and
              bounding box coordinates.
    """
    try:
        results = reader.readtext(np.array(image), detail=1)
        extracted_data = []
        for i, (bbox, text, _) in enumerate(results):
            bbox_int = [[int(coord) for coord in point] for point in bbox]
            extracted_data.append({
                "text": text,
                "bbox": bbox_int,
            })
        return extracted_data
    except Exception as e:
        st.error(f"Error during OCR: {e}")
        return []

def check_rbl_and_extract_data(image):
    """
    Checks for "RBL" and extracts specific data from the image.

    Args:
        image (PIL.Image.Image): The image to process.

    Returns:
        pandas.DataFrame: A DataFrame containing the extracted data,
                        or None if "RBL" is not found or an error occurs.
    """
    extracted_data = extract_text_with_bbox(image)
    rbl_found = False
    for data in extracted_data:
        bbox = data['bbox']
        text = data['text']
        # Check for "RBL" within the specified bounding box
        if (
            bbox[0][0] >= 222 and bbox[0][1] >= 111 and
            bbox[1][0] <= 588 and bbox[1][1] >= 111 and
            bbox[2][0] <= 588 and bbox[2][1] <= 190 and
            bbox[3][0] >= 222 and bbox[3][1] <= 190 and
            "RBL" in text
        ):
            rbl_found = True
            break

    if not rbl_found:
        return None  # Return None if not RBL form

    # Extract the specified data
    extracted_values = {
        "Application Date": get_text_in_bbox(extracted_data, [1835, 95, 2204, 139]),
        "Application Date Value": get_text_in_bbox(extracted_data, [2232, 60, 2541, 152]),
        "First Name Value": get_text_in_bbox(extracted_data, [436, 732, 816, 794]),
        "Last Name Value": get_text_in_bbox(extracted_data, [867, 742, 1004, 793]),
        "DOB Date": get_text_in_bbox(extracted_data, [485, 944, 529, 991]),
        "DOB Month": get_text_in_bbox(extracted_data, [570, 938, 661, 992]),
        "DOB Year": get_text_in_bbox(extracted_data, [848, 939, 892, 988]),
        "Address Label": get_text_in_bbox(extracted_data, [119, 1992, 348, 2030]),
        "Address Value 1": get_text_in_bbox(extracted_data, [435, 1970, 722, 2047]),
        "Address Value 2": get_text_in_bbox(extracted_data, [764, 1975, 1324, 2038]),
        "Address Lane Label": get_text_in_bbox(extracted_data, [116, 2065, 351, 2103]),
        "Address Lane Value": get_text_in_bbox(extracted_data, [433, 2051, 809, 2120]),
        "Pin Code Label": get_text_in_bbox(extracted_data, [1085, 2208, 1225, 2247]),
        "Pin Code Value": get_text_in_bbox(extracted_data, [1268, 2202, 1542, 2259]),
    }

    df = pd.DataFrame([extracted_values])
    return df.T  # Transpose the DataFrame before returning

def get_text_in_bbox(extracted_data, bbox):
    """
    Gets the text within a specified bounding box.

    Args:
        extracted_data (list): List of dictionaries containing extracted data.
        bbox (list): A list of four integers representing the bounding box
                       coordinates [x_min, y_min, x_max, y_max].

    Returns:
        str: The extracted text within the bounding box, or "Not Found" if no
             text is found within the box.
    """
    x_min, y_min, x_max, y_max = bbox
    for data in extracted_data:
        data_bbox = data['bbox']
        text = data['text']
        # Check if the bounding box of the text falls within the specified bounding box
        if (
            data_bbox[0][0] >= x_min and data_bbox[0][1] >= y_min and
            data_bbox[1][0] <= x_max and data_bbox[1][1] >= y_min and
            data_bbox[2][0] <= x_max and data_bbox[2][1] <= y_max and
            data_bbox[3][0] >= x_min and data_bbox[3][1] <= y_max
        ):
            return text
    return "Not Found"

def draw_bboxes(image, extracted_data):
    """
    Draws bounding boxes around the detected text on the image.

    Args:
        image (PIL.Image.Image): The image to draw on.
        extracted_data (list): A list of dictionaries, where each dictionary
                              contains the text and bounding box coordinates.

    Returns:
        PIL.Image.Image: The image with the bounding boxes drawn.
    """
    draw = ImageDraw.Draw(image)
    if extracted_data: # Check if extracted_data is not empty
        for data in extracted_data:
            bbox = data['bbox']
            text = data['text']  # Get the text for display
            try:
                draw.rectangle(bbox, outline="red", width=2)  # Draw the rectangle
                # Display the text near the bounding box.  Adjust position as needed.
                draw.text((bbox[0][0], bbox[0][1] - 10), text, fill="red")
            except Exception as e:
                print(f"Error drawing rectangle: {e}, bbox: {bbox}, text: {text}")
    return image

def main():
    """
    Main function to run the Streamlit application.
    """
    st.title("Automated Personal Loan Document Processing")
    st.write("Upload an image of your Loan Application Form.")

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Open the image using PIL.
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Check for RBL and extract data
        rbl_data = check_rbl_and_extract_data(image)
        if rbl_data is not None:
            df = rbl_data
            df.columns = ['Value']
            st.subheader("Extracted Data")
            st.markdown("You can edit for any correction below:",)
            edited_df = st.data_editor(df, num_rows="dynamic")  # Display the editable DataFrame
            st.markdown("---")  # Add a horizontal line
            st.subheader("Final Form data")
            st.text("Preview the data (this cannot be edited) ")
            st.dataframe(edited_df)

            # Create a download button for the edited data
            csv_data = edited_df.to_csv(index=True)  # Convert DataFrame to CSV
            st.download_button(
                label="Download Final Form Data as CSV",
                data=csv_data,
                file_name="final_form_data.csv",
                mime="text/csv",
            )
        else:
            # If not RBL, perform full OCR and display results
            st.subheader("All Extracted Data:")
            all_extracted_data = extract_text_with_bbox(image)  # Extract all data

            if all_extracted_data:
                # Create a DataFrame from the extracted data
                df_all_data = pd.DataFrame(all_extracted_data)
                df_all_data.insert(1, 'Enter Value', '')  # Add a new column for user input at index 1
                st.write("Final Form data")
                edited_df_all_data = st.data_editor(df_all_data, num_rows="dynamic")
                st.dataframe(edited_df_all_data)  # Display the DataFrame
            else:
                st.write("No text found in the image.")

if __name__ == "__main__":
    main()

