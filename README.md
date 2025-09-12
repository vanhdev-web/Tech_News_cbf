# Tech_News_Content-based_Filtering

A recommendation system to suggest relevant articles using content-based filtering. This application uses Streamlit to create an interactive user interface, pandas for data manipulation, and scikit-learn for calculating cosine similarity to recommend similar articles.
You can visit the website here: https://tech-news.streamlit.app/  


![Demo GIF](demo/technew.gif)

## Table of Contents

. [Dataset Overview](#dataset-overview)  
. [Features and Functionality](#features-and-functionality)  
. [Technology Stack](#technology-stack)  
. [Prerequisites](#prerequisites)  
. [Installation Instructions](#installation-instructions)  
. [Usage Guide](#usage-guide)  
. [Contributing Guidelines](#contributing-guidelines)  
. [License Information](#license-information)

## Dataset Overview
* Dataset overview  
![ảnh demo](https://drive.google.com/uc?export=view&id=1lZYIvsyDenC2Lugs2jzYjyzy_r2mz3Nh)


* Samples   
![ảnh demo](https://drive.google.com/uc?export=view&id=1BNeSTo03p3J5upoYYlTTyHUpbF3ml4By)


* Variables  
![ảnh demo](https://drive.google.com/uc?export=view&id=1-TMavcG6kOtGIfCc0hVqlWB0ZNEeCXe8)
![ảnh demo](https://drive.google.com/uc?export=view&id=1UEOHRa9rSFogOQV8SIaldk0dCn1hZqS_)

  
  


## Features and Functionality

*   **Home Page:** Displays a list of news article cards, with the ability to load more articles.
*   **Article Detail Page:** Shows the full article content and provides links to related articles based on cosine similarity.
*   **Content-Based Filtering:** Recommends articles based on the content of the article currently being viewed.
*   **Interactive UI:** Uses Streamlit for a user-friendly experience.

## Technology Stack

*   Python 3.x
*   Streamlit
*   Pandas
*   Scikit-learn

## Prerequisites

Before you begin, ensure you have the following installed:

*   Python 3.x
*   Pip package manager

You'll also need to install the required Python packages. You can do this using pip:

```bash
pip install streamlit pandas scikit-learn
```

## Installation Instructions

1.  Clone the repository:

    ```bash
    git clone https://github.com/vanhdev-web/Tech_News_cbf.git
    cd Tech_News_cbf
    ```

2.  Install the dependencies (as mentioned in the Prerequisites section).

## Usage Guide

To run the application:

1.  Navigate to the repository directory in your terminal.
2.  Execute the following command:

    ```bash
    streamlit run app.py
    ```

3.  Streamlit will provide a local URL (usually `http://localhost:8501`) to access the application in your web browser.

### Interacting with the Application

*   **Home Page:**
    *   Browse the list of article cards.
    *   Click on a card to view the full article on the Article Detail Page.
    *   Click the "📄 Load more" button to display additional articles.

*   **Article Detail Page:**
    *   Read the full content of the selected article.
    *   Click on the related article links to navigate to other relevant articles.
    *   Use the "⬅ Back to Home" button to return to the main listing.


## Contributing Guidelines

Contributions are welcome! Here are the steps to contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix:

    ```bash
    git checkout -b feature/your-feature-name
    ```

3.  Implement your changes and ensure the code follows the project's coding standards.
4.  Commit your changes with descriptive commit messages.
5.  Push your branch to your forked repository.
6.  Create a pull request to the `main` branch of the original repository.

## License Information

License is not specified for this project. All rights are reserved by the owner.
