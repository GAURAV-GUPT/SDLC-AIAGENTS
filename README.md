# Multi-Agent SDLC Manager 🤖

This is a Streamlit application that streamlines the **Software Development Lifecycle (SDLC)** by using multiple AI agents. It acts as a digital product team, guiding you from high-level project planning to code generation and documentation.

## How it Works

The application uses a **chain of specialized AI agents**, with each agent focusing on a specific stage of the SDLC. The output from one stage becomes the input for the next, ensuring a cohesive and well-documented workflow.

## Key Features

  * **Project Details:** Start by entering your project's core information, including the name, client, and a preferred programming language.
  * **BRD Upload:** Upload a Business Requirements Document (BRD) to provide the foundational requirements for the project.
  * **User Story Generation:** An AI Business Analyst agent reads the BRD and automatically generates a list of detailed user stories in the "As a... I want... So that..." format.
  * **Acceptance Criteria:** A QA expert agent takes the user stories and creates precise acceptance criteria using the **Given/When/Then** format.
  * **Test Case Creation:** A QA engineer agent leverages the acceptance criteria to produce comprehensive test cases with clear steps, expected results, and test data.
  * **BDD Script Generation:** An expert in **Behavior-Driven Development (BDD)** converts the test cases into Gherkin-formatted feature files.
  * **Selenium Script Automation:** An automation specialist agent writes automated test scripts using **Selenium WebDriver** based on the BDD scenarios.
  * **Code Generation:** A master programmer agent writes a fully functional and commented program based on all the previously generated requirements and test cases.
  * **Architecture Diagram:** A solutions architect agent generates a **Mermaid script** to visualize the system's architecture, providing a high-level overview of the components.

-----

## Installation and Setup

### Prerequisites

  * Python 3.7+
  * An OpenAI API Key

### Step-by-Step Guide

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *Note: The `requirements.txt` file should contain:*

    ```
    streamlit
    langchain-openai
    streamlit-mermaid
    ```

3.  **Set Your OpenAI API Key:**
    Create a `.env` file in the project root and add your API key:

    ```
    OPENAI_API_KEY="your-api-key-here"
    ```

    Alternatively, you can uncomment the sidebar code in `app.py` to enter your key directly in the application.

4.  **Run the Application:**

    ```bash
    streamlit run app.py
    ```

The application will open in your default web browser.

-----

## Usage

1.  Navigate through the tabs on the left sidebar.
2.  Start with **"Project Details"** to configure your project.
3.  Proceed to **"Upload BRD"** to provide the initial requirements.
4.  Use the **"Generate"** buttons in each subsequent tab to create the next deliverable in the SDLC.
5.  Download the generated files at any stage using the provided download buttons.

## Contributions

Contributions are welcome\! If you have suggestions for new features, bug fixes, or improvements, please feel free to open an issue or submit a pull request.
