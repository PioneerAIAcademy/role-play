import os
import base64
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Configure page
st.set_page_config(
    page_title="PathwayConnect Missionary Training",
    page_icon="images/pathway.png",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Initialize OpenAI client
# Try to get API key from Streamlit secrets first, then fall back to environment variable
try:
    api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
except:
    api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# Define available personas
PERSONAS = {
    "jorge": {
        "name": "Jorge Vargas",
        "description": "Jorge - Honor Code Concerns",
        "prompt_file": "roleplay-content/prompts/jorge-system-prompt.md",
        "hint": "Non-member concerned about religious requirements. Tests your ability to explain policies with cultural sensitivity."
    },
    "katra": {
        "name": "Katra",
        "description": "Katra - Low Confidence",
        "prompt_file": "roleplay-content/prompts/katra-system-prompt.md",
        "hint": "Adult learner with low confidence. Tests your empathy and ability to provide encouragement and practical support."
    },
    "vitoria": {
        "name": "Vitoria da Silva",
        "description": "Vitoria - English Learner",
        "prompt_file": "roleplay-content/prompts/vitoria-system-prompt.md",
        "hint": "Limited English speaker. Tests your ability to communicate clearly and identify language barriers."
    }
}

def load_system_prompt(persona_key):
    """Load system prompt from markdown file for the given persona."""
    try:
        prompt_path = PERSONAS[persona_key]["prompt_file"]
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        st.error(f"Error loading persona prompt: {str(e)}")
        return ""

def load_grading_prompt():
    """Load the grading system prompt from markdown file."""
    try:
        with open("roleplay-content/prompts/grading-system-prompt.md", 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        st.error(f"Error loading grading prompt: {str(e)}")
        return ""

def format_conversation_transcript(messages, persona_key):
    """Format the conversation transcript for evaluation.

    Args:
        messages: List of message dictionaries with 'role' and 'content'
        persona_key: The key of the selected persona

    Returns:
        Formatted transcript string
    """
    persona_name = PERSONAS[persona_key]["name"]

    transcript = f"Student: {persona_name}\n\n## Full Conversation Transcript\n\n"

    for message in messages:
        if message["role"] == "user":
            transcript += f"Missionary: {message['content']}\n\n"
        elif message["role"] == "assistant":
            transcript += f"{persona_name}: {message['content']}\n\n"

    return transcript

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Make action buttons more subtle and elegant */
    div[data-testid="column"] button {
        transition: all 0.2s ease;
        opacity: 0.6;
    }
    div[data-testid="column"] button:hover {
        opacity: 1;
        transform: scale(1.1);
    }

    /* Sidebar branding */
    .sidebar-logo {
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 1rem;
    }

    .sidebar-logo img {
        width: 140px;
        height: auto;
        margin-bottom: 0.5rem;
        filter: brightness(0) saturate(100%) invert(73%) sepia(89%) saturate(1742%) hue-rotate(360deg) brightness(98%) contrast(101%);
    }

    .sidebar-title {
        font-size: 1.1em;
        font-weight: 600;
        color: #1a1a1a;
        margin: 0.5rem 0 0.3rem 0;
        line-height: 1.3;
    }

    .sidebar-subtitle {
        font-size: 0.85em;
        color: #666;
        margin: 0;
        font-weight: 400;
        line-height: 1.4;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with persona selector and clear history button
with st.sidebar:
    # Sidebar branding with BYU-Pathway logo (made yellow)
    # Read and encode the SVG logo
    with open("images/byu-pw-stackedgray.svg", "r") as f:
        svg_content = f.read()
        svg_b64 = base64.b64encode(svg_content.encode()).decode()

    st.markdown(
        f"""
        <div class="sidebar-logo">
            <img src="data:image/svg+xml;base64,{svg_b64}" alt="BYU-Pathway Worldwide">
            <div class="sidebar-title">Missionary Training</div>
            <div class="sidebar-subtitle">Student Orientation Practice</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()
    st.header("⚙️ Training Setup")
    st.divider()
    st.subheader("Select Student")

    # Initialize selected persona in session state
    if "selected_persona" not in st.session_state:
        st.session_state.selected_persona = "jorge"  # Default to Jorge

    # Create dropdown for persona selection
    persona_options = [PERSONAS[key]["description"] for key in PERSONAS.keys()]
    persona_keys = list(PERSONAS.keys())

    # Find current index
    current_index = persona_keys.index(st.session_state.selected_persona)

    selected_display = st.selectbox(
        "Choose which student you'll meet with:",
        persona_options,
        index=current_index,
        key="persona_selector"
    )

    # Get the key of the selected persona
    new_persona_key = persona_keys[persona_options.index(selected_display)]

    # Display persona hint
    selected_persona_info = PERSONAS[new_persona_key]
    st.caption(selected_persona_info['hint'])

    # If persona changed, reset conversation and update selection
    if new_persona_key != st.session_state.selected_persona:
        st.session_state.selected_persona = new_persona_key
        st.session_state.messages = []
        st.rerun()


    st.divider()
    st.subheader("Actions")
    if st.button("🔄 Start New Conversation", type="primary", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption("💡 **Tip:** Take your time to build rapport and listen carefully to the student's concerns before offering solutions.")
    st.divider()
    st.caption(f"**Current Student:** {PERSONAS[st.session_state.selected_persona]['name']}")

# Initialize chat history and evaluation state in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "evaluation_result" not in st.session_state:
    st.session_state.evaluation_result = None
if "show_evaluation" not in st.session_state:
    st.session_state.show_evaluation = False

# Welcome screen when no messages OR display chat history
if len(st.session_state.messages) == 0:
    # Get selected persona info
    current_persona = PERSONAS[st.session_state.selected_persona]

    # Instructions box
    st.info(f"""
**📋 Your Training Scenario:**

You are about to conduct a **New Student Orientation Visit** with **{current_persona['name']}**.

**What is this?**
This is a practice role-play where you'll talk with an AI-simulated student who has specific concerns about starting their PathwayConnect journey. Your goal is to help them feel prepared, supported, and confident.

**What should you do?**
1. **Introduce yourself** as a BYU-Pathway missionary
2. **Listen carefully** to the student's concerns
3. **Answer their questions** with accurate information
4. **Provide encouragement** and connect them with resources
5. **Help them feel ready** to begin their program

**About this student:**
{current_persona['hint']}

**Ready to begin?** Type your opening message below to start the orientation visit.
    """)

    st.markdown("<br>", unsafe_allow_html=True)
else:
    # Display all previous messages
    for idx, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            # Action buttons row with subtle styling
            cols = st.columns([0.9, 0.05, 0.05])

            with cols[1]:
                if st.button("⎘", key=f"copy_{idx}", help="Copy message", use_container_width=True):
                    st.toast("Copied!", icon="✅")

            # Only show regenerate for assistant messages
            if message["role"] == "assistant":
                with cols[2]:
                    if st.button("↻", key=f"regen_{idx}", help="Regenerate response", use_container_width=True):
                        # Remove messages from this point and regenerate
                        st.session_state.messages = st.session_state.messages[:idx]
                        st.rerun()

# Generate response if last message is from user (and not showing evaluation)
if not st.session_state.show_evaluation and len(st.session_state.messages) > 0 and st.session_state.messages[-1]["role"] == "user":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Load the system prompt for the selected persona
                system_prompt = load_system_prompt(st.session_state.selected_persona)

                # Prepare messages for API with system message
                api_messages = [{"role": "system", "content": system_prompt}]
                api_messages.extend([{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages])

                # Call OpenAI Responses API with full conversation history
                response = client.responses.create(
                    model="gpt-5.1",
                    input=api_messages,
                    reasoning={"effort": "none"}  # Fast response mode
                )

                # Extract assistant's reply
                assistant_message = response.output_text

                # Display and add assistant response to chat history
                st.markdown(assistant_message)
                st.session_state.messages.append({"role": "assistant", "content": assistant_message})
                st.rerun()

            except Exception as e:
                error_message = f"Error: {str(e)}"
                st.error(error_message)
                # Add error to chat history
                st.session_state.messages.append({"role": "assistant", "content": error_message})
                st.rerun()

# Display evaluation results if available
if st.session_state.show_evaluation and st.session_state.evaluation_result:
    st.divider()
    st.markdown("## 📊 Evaluation Results")
    st.markdown(st.session_state.evaluation_result)

    # Options after evaluation
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Start New Conversation", type="primary", use_container_width=True):
            st.session_state.messages = []
            st.session_state.evaluation_result = None
            st.session_state.show_evaluation = False
            st.rerun()
    with col2:
        if st.button("📋 Review Conversation", use_container_width=True):
            st.session_state.show_evaluation = False
            st.rerun()

# Evaluation button - MOVED HERE to render after all messages and response generation
# This ensures it stays in one place, right above the chat input
if len(st.session_state.messages) > 0 and not st.session_state.show_evaluation:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎓 End Conversation and Evaluate", type="primary", use_container_width=True):
            # Trigger evaluation
            with st.spinner("Evaluating conversation..."):
                try:
                    # Load grading prompt
                    grading_prompt = load_grading_prompt()

                    # Format conversation transcript
                    transcript = format_conversation_transcript(
                        st.session_state.messages,
                        st.session_state.selected_persona
                    )

                    # Call API for evaluation
                    eval_messages = [
                        {"role": "system", "content": grading_prompt},
                        {"role": "user", "content": transcript}
                    ]

                    response = client.responses.create(
                        model="gpt-5.1",
                        input=eval_messages,
                        reasoning={"effort": "medium"}  # Medium effort for thorough evaluation
                    )

                    # Store evaluation result
                    st.session_state.evaluation_result = response.output_text
                    st.session_state.show_evaluation = True
                    st.rerun()

                except Exception as e:
                    st.error(f"Error during evaluation: {str(e)}")

# Chat input (hidden when showing evaluation)
if not st.session_state.show_evaluation:
    if prompt := st.chat_input("What would you like to say?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Rerun immediately to hide welcome screen
        st.rerun()
