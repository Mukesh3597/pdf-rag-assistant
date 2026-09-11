import streamlit as st
from datetime import datetime

from src.rag_pipeline import search, create_context, generate_answer


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="PDF RAG Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: #0f1117;
    }

    /* Main content width */
    .block-container {
        max-width: 1000px;
        padding-top: 35px;
        padding-bottom: 120px;
    }

    /* Header */
    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .main-subtitle {
        color: #9ca3af;
        font-size: 16px;
        margin-bottom: 30px;
    }

    /* Welcome box */
    .welcome-box {
        background: #181b22;
        border: 1px solid #292d36;
        border-radius: 14px;
        padding: 25px;
        margin-bottom: 25px;
    }

    /* Source box */
    .source-box {
        background: #181b22;
        border: 1px solid #292d36;
        border-radius: 10px;
        padding: 12px;
        margin-top: 10px;
        font-size: 14px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #111318;
    }

    /* Buttons */
    .stButton button {
        border-radius: 10px;
    }

    /* Chat input */
    div[data-testid="stChatInput"] {
        background: #181b22;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_started" not in st.session_state:
    st.session_state.chat_started = False


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🤖 PDF Assistant")

    st.caption("Your local PDF RAG chatbot")

    st.markdown("---")

    # -------------------------
    # New Chat
    # -------------------------

    if st.button(
        "➕ New Chat",
        use_container_width=True
    ):

        # Save current chat to history
        if st.session_state.messages:

            first_question = ""

            for msg in st.session_state.messages:

                if msg["role"] == "user":
                    first_question = msg["content"]
                    break

            if first_question:

                st.session_state.chat_history.append(
                    {
                        "title": first_question[:40],
                        "messages": st.session_state.messages.copy(),
                        "time": datetime.now().strftime("%H:%M")
                    }
                )

        st.session_state.messages = []
        st.session_state.chat_started = False

        st.rerun()


    # -------------------------
    # Clear Chat
    # -------------------------

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []
        st.session_state.chat_started = False

        st.rerun()


    st.markdown("---")


    # =====================================================
    # CHAT HISTORY
    # =====================================================

    st.subheader("💬 Chat History")

    if not st.session_state.chat_history:

        st.caption("No previous chats")

    else:

        for index, chat in enumerate(
            reversed(st.session_state.chat_history)
        ):

            if st.button(
                f"💬 {chat['title']}",
                key=f"history_{index}",
                use_container_width=True
            ):

                st.session_state.messages = chat["messages"].copy()
                st.session_state.chat_started = True

                st.rerun()


    st.markdown("---")


    # =====================================================
    # PDF INFORMATION
    # =====================================================

    st.subheader("📄 PDF")

    st.write("**100 Machine Learning**")
    st.write("Interview Questions & Answers")

    st.caption("24 pages")
    st.caption("100 questions")


    st.markdown("---")


    # =====================================================
    # TECHNOLOGY
    # =====================================================

    st.subheader("⚙️ Technology")

    st.write("🧠 Sentence Transformers")
    st.write("🔎 FAISS")
    st.write("🤖 Ollama")
    st.write("🦙 Llama 3.2 3B")


    st.markdown("---")


    # =====================================================
    # DOWNLOAD CHAT
    # =====================================================

    if st.session_state.messages:

        chat_text = ""

        for message in st.session_state.messages:

            if message["role"] == "user":

                chat_text += (
                    f"YOU:\n{message['content']}\n\n"
                )

            else:

                chat_text += (
                    f"AI:\n{message['content']}\n\n"
                )

            chat_text += "--------------------------------\n\n"


        st.download_button(
            "⬇️ Download Chat",
            data=chat_text,
            file_name="pdf_rag_chat.txt",
            mime="text/plain",
            use_container_width=True
        )


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🤖 PDF RAG Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Ask questions from your Machine Learning PDF'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# WELCOME SCREEN
# =========================================================

if not st.session_state.messages:

    st.markdown(
        """
        <div class="welcome-box">

        <h3>👋 Hello!</h3>

        <p>
        I can answer questions using the information
        available in your PDF.
        </p>

        <p>
        Ask me something about Machine Learning,
        Artificial Intelligence, Overfitting, Regression,
        Classification, and more.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown("### 💡 Try asking")


    # Suggested questions

    suggestions = [
        "What is Machine Learning?",
        "What is Artificial Intelligence?",
        "What is overfitting?",
        "What is supervised learning?",
        "What is regression?"
    ]


    cols = st.columns(2)


    for index, question in enumerate(suggestions):

        with cols[index % 2]:

            if st.button(
                question,
                key=f"suggestion_{index}",
                use_container_width=True
            ):

                st.session_state.pending_question = question

                st.rerun()


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"],
        avatar="👤" if message["role"] == "user" else "🤖"
    ):

        st.markdown(message["content"])


        # Show sources for AI messages

        if (
            message["role"] == "assistant"
            and "sources" in message
            and message["sources"]
        ):

            with st.expander(
                "📚 View PDF Sources"
            ):

                for source_index, source in enumerate(
                    message["sources"],
                    start=1
                ):

                    score = source["score"]

                    st.markdown(
                        f"**Source {source_index}** "
                        f"• Similarity: `{score:.3f}`"
                    )

                    st.write(
                        source["chunk"]
                    )

                    st.markdown("---")


# =========================================================
# GET QUESTION
# =========================================================

query = st.chat_input(
    "Ask anything about the PDF..."
)


# Suggested question handling

if (
    "pending_question" in st.session_state
    and st.session_state.pending_question
):

    query = st.session_state.pending_question

    st.session_state.pending_question = None


# =========================================================
# PROCESS QUESTION
# =========================================================

if query:

    st.session_state.chat_started = True


    # -----------------------------------------------------
    # Save user message
    # -----------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )


    # -----------------------------------------------------
    # Display user message immediately
    # -----------------------------------------------------

    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.markdown(query)


    # -----------------------------------------------------
    # Search PDF
    # -----------------------------------------------------

    results = search(query)


    # -----------------------------------------------------
    # Generate answer
    # -----------------------------------------------------

    if not results:

        answer = (
            "I could not find the answer in the PDF."
        )

    else:

        context = create_context(results)


        with st.chat_message(
            "assistant",
            avatar="🤖"
        ):

            with st.spinner("Thinking..."):

                answer = generate_answer(
                    query,
                    context
                )

            st.markdown(answer)


            # ---------------------------------------------
            # Sources
            # ---------------------------------------------

            with st.expander(
                "📚 View PDF Sources"
            ):

                for source_index, source in enumerate(
                    results,
                    start=1
                ):

                    score = source["score"]

                    st.markdown(
                        f"**Source {source_index}** "
                        f"• Similarity: `{score:.3f}`"
                    )

                    st.write(
                        source["chunk"]
                    )

                    st.markdown("---")


    # -----------------------------------------------------
    # Save AI message
    # -----------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": results if results else []
        }
    )


    # -----------------------------------------------------
    # Rerun
    # -----------------------------------------------------

    st.rerun()