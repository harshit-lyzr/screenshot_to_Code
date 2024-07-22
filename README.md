# Lyzr Screenshot to Code

Welcome to the Lyzr Screenshot to Code! This application, built with Lyzr Automata, helps you generate HTML, CSS, and JavaScript code by analyzing a screenshot of a landing page. Simply upload an image of the landing page, and the app will provide you with the code to recreate the page.

## Features

- Upload a landing page screenshot.
- Automatically analyze the image and generate HTML, CSS, and JavaScript code.
- Maintains the structure and layout of the original screenshot.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Streamlit
- PIL (Pillow)
- dotenv
- base64
- OpenAI API key
- Lyzr Automata

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/lyzr-screenshot-to-code.git
    cd lyzr-screenshot-to-code
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project root directory and add your OpenAI API key:

    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

### Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload an image of your landing page screenshot using the file uploader.

4. Click the "Generate" button to analyze the image and generate the code.

5. The generated code will be displayed on the screen.

### Code Explanation

- **Streamlit Configuration**: Sets up the Streamlit application with a custom page title, layout, and sidebar state.
- **Header Customization**: Uses custom CSS to hide the default app header and adjust padding.
- **Image and Title**: Displays the application logo and title.
- **OpenAI API Integration**: Loads the API key from the environment variables and initializes the GPTVISION model.
- **Image Encoding**: Encodes the uploaded image in base64 format for processing.
- **Prompt Definition**: Defines the prompt to guide the OpenAI model in generating the HTML, CSS, and JavaScript code.
- **File Upload**: Allows users to upload an image and display it on the screen.
- **Code Generation**: Processes the uploaded image and generates the code using the GPTVISION model.

### Project Structure
    lyzr-screenshot-to-code/
    │
    ├── .env
    ├── app.py
    ├── lyzr-logo.png
    ├── lyzr-logo-cut.png
    ├── requirements.txt
    └── utils.py


### Contributing

Contributions are welcome! Please fork the repository and submit a pull request.





