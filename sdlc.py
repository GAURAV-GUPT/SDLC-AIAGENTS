import streamlit as st
import pandas as pd
import base64
from io import BytesIO

# --- Page Configuration ---
st.set_page_config(
    page_title="SDLC Agent Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Session State Initialization ---
if 'tab' not in st.session_state:
    st.session_state.tab = "Project Details"
if 'project_details' not in st.session_state:
    st.session_state.project_details = {}
if 'brd_content' not in st.session_state:
    st.session_state.brd_content = None
if 'user_stories' not in st.session_state:
    st.session_state.user_stories = None
if 'acceptance_criteria' not in st.session_state:
    st.session_state.acceptance_criteria = None
if 'test_cases' not in st.session_state:
    st.session_state.test_cases = None
if 'generated_code' not in st.session_state:
    st.session_state.generated_code = None


# --- Helper Functions ---
def get_download_link(content, filename, text):
    """Generates a link to download the given content as a file."""
    if content:
        b64 = base64.b64encode(content.encode()).decode()
        return f'<a href="data:file/txt;base64,{b64}" download="{filename}">{text}</a>'
    return ""

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
tabs = ["Project Details", "Upload BRD", "User Stories", "Acceptance Criteria", "Test Cases", "Code"]
st.session_state.tab = st.sidebar.radio("Go to", tabs, index=tabs.index(st.session_state.tab))


# --- Main Content ---
st.title("Software Development Lifecycle Agent Assistant")

# --- Project Details Tab ---
if st.session_state.tab == "Project Details":
    st.header("1. Project Details")
    with st.form("project_details_form"):
        st.session_state.project_details['name'] = st.text_input("Project Name", st.session_state.project_details.get('name', ''))
        st.session_state.project_details['client'] = st.text_input("Client", st.session_state.project_details.get('client', ''))
        st.session_state.project_details['product_owner'] = st.text_input("Product Owner", st.session_state.project_details.get('product_owner', ''))
        st.session_state.project_details['business_domain'] = st.text_input("Business Domain", st.session_state.project_details.get('business_domain', ''))
        st.session_state.project_details['pm'] = st.text_input("Project Manager (PM)", st.session_state.project_details.get('pm', ''))
        st.session_state.project_details['ba'] = st.text_input("Business Analyst (BA)", st.session_state.project_details.get('ba', ''))
        st.session_state.project_details['sa'] = st.text_input("Solution Architect (SA)", st.session_state.project_details.get('sa', ''))
        st.session_state.project_details['start_date'] = st.date_input("Start Date", pd.to_datetime(st.session_state.project_details.get('start_date', pd.Timestamp.now())))
        st.session_state.project_details['end_date'] = st.date_input("Planned End Date", pd.to_datetime(st.session_state.project_details.get('end_date', pd.Timestamp.now() + pd.DateOffset(months=6))))
        st.session_state.project_details['budget'] = st.number_input("Budgeted Amount ($)", value=st.session_state.project_details.get('budget', 100000.0), step=1000.0)
        st.session_state.project_details['language'] = st.selectbox("Programming Language", ["Python", "JavaScript", "Java", "C#", "Go", "Rust"], index=["Python", "JavaScript", "Java", "C#", "Go", "Rust"].index(st.session_state.project_details.get('language', 'Python')))

        submitted = st.form_submit_button("Save Project Details")
        if submitted:
            st.success("Project details saved!")
            st.session_state.tab = "Upload BRD"
            st.experimental_rerun()

# --- Upload BRD Tab ---
elif st.session_state.tab == "Upload BRD":
    st.header("2. Upload Business Requirement Document (BRD)")
    uploaded_file = st.file_uploader("Choose a BRD file", type=['txt', 'md', 'docx', 'pdf'])
    if uploaded_file is not None:
        try:
            st.session_state.brd_content = uploaded_file.getvalue().decode("utf-8")
            st.success("BRD uploaded successfully!")
            if st.button("Proceed to User Stories"):
                st.session_state.tab = "User Stories"
                st.experimental_rerun()
        except Exception as e:
            st.error(f"Error reading file: {e}")

# --- User Stories Tab ---
elif st.session_state.tab == "User Stories":
    st.header("3. User Stories")
    if st.session_state.brd_content:
        if st.session_state.user_stories is None:
            with st.spinner("Generating user stories... This may take a moment."):
                # This is a placeholder for the actual agent logic
                st.session_state.user_stories = f"Based on the BRD for project '{st.session_state.project_details.get('name', 'N/A')}', here are the generated user stories:\n\n1. As a user, I want to be able to log in to the system so that I can access my personalized dashboard.\n2. As an administrator, I want to be able to manage user accounts so that I can add, edit, and delete users."
        st.text_area("Generated User Stories", st.session_state.user_stories, height=300)
        st.markdown(get_download_link(st.session_state.user_stories, "user_stories.txt", "Download User Stories"), unsafe_allow_html=True)
        if st.button("Proceed to Acceptance Criteria"):
            st.session_state.tab = "Acceptance Criteria"
            st.experimental_rerun()
    else:
        st.warning("Please upload a BRD in the previous step.")

# --- Acceptance Criteria Tab ---
elif st.session_state.tab == "Acceptance Criteria":
    st.header("4. Acceptance Criteria")
    if st.session_state.user_stories:
        if st.session_state.acceptance_criteria is None:
            with st.spinner("Generating acceptance criteria..."):
                # Placeholder for agent logic
                st.session_state.acceptance_criteria = "For User Story 1:\n- Given a user is on the login page, when they enter valid credentials and click 'Login', then they should be redirected to their dashboard.\n- Given a user is on the login page, when they enter invalid credentials, then an error message should be displayed."
        st.text_area("Generated Acceptance Criteria", st.session_state.acceptance_criteria, height=300)
        st.markdown(get_download_link(st.session_state.acceptance_criteria, "acceptance_criteria.txt", "Download Acceptance Criteria"), unsafe_allow_html=True)
        if st.button("Proceed to Test Cases"):
            st.session_state.tab = "Test Cases"
            st.experimental_rerun()
    else:
        st.warning("Please generate user stories first.")

# --- Test Cases Tab ---
elif st.session_state.tab == "Test Cases":
    st.header("5. Test Cases")
    if st.session_state.acceptance_criteria:
        if st.session_state.test_cases is None:
            with st.spinner("Generating test cases..."):
                # Placeholder for agent logic
                st.session_state.test_cases = "Test Case ID: TC001\nTest Case Title: Successful Login\nSteps:\n1. Navigate to login page.\n2. Enter valid username.\n3. Enter valid password.\n4. Click 'Login' button.\nExpected Result: User is redirected to the dashboard."
        st.text_area("Generated Test Cases", st.session_state.test_cases, height=300)
        st.markdown(get_download_link(st.session_state.test_cases, "test_cases.txt", "Download Test Cases"), unsafe_allow_html=True)
        if st.button("Proceed to Code Generation"):
            st.session_state.tab = "Code"
            st.experimental_rerun()
    else:
        st.warning("Please generate acceptance criteria first.")

# --- Code Tab ---
elif st.session_state.tab == "Code":
    st.header("6. Generated Code")
    if st.session_state.test_cases:
        if st.session_state.generated_code is None:
            with st.spinner(f"Generating code in {st.session_state.project_details.get('language', 'the selected language')}..."):
                # Placeholder for agent logic
                lang = st.session_state.project_details.get('language', 'Python')
                code_snippet = ""
                if lang == "Python":
                    code_snippet = """
def login(username, password):
    # In a real application, you would check credentials against a database
    if username == "admin" and password == "password":
        return True
    return False

# Example usage:
if login("admin", "password"):
    print("Login successful!")
else:
    print("Invalid credentials.")
"""
                elif lang == "JavaScript":
                    code_snippet = """
function login(username, password) {
    // In a real application, you would check credentials against a database
    if (username === "admin" && password === "password") {
        return true;
    }
    return false;
}

// Example usage:
if (login("admin", "password")) {
    console.log("Login successful!");
} else {
    console.log("Invalid credentials.");
}
"""
                st.session_state.generated_code = f"Here is some example code for the login functionality in {lang}:\n\n```\n{code_snippet}\n```"

        st.markdown(st.session_state.generated_code, unsafe_allow_html=True)
        st.markdown(get_download_link(st.session_state.generated_code, f"generated_code.{'py' if st.session_state.project_details.get('language', 'Python') == 'Python' else 'js'}", "Download Code"), unsafe_allow_html=True)
    else:
        st.warning("Please generate test cases first.")

