import streamlit as st
from openai import OpenAI
<<<<<<< Updated upstream
import pandas as pd
=======
<<<<<<< Updated upstream
=======
import pandas as pd
import plotly.express as px
>>>>>>> Stashed changes
>>>>>>> Stashed changes

st.title("Data Analytics ChatBot")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

<<<<<<< Updated upstream
file_read = st.file_uploader("")
if file_read is not None:
    file = pd.read_csv(file_read)
    st.write(file)

if prompt := st.chat_input("Nhập yêu cầu?"):
    if prompt == "Analyse":
        prompt = file.to_string()

=======
<<<<<<< Updated upstream
if prompt := st.chat_input("Nhập yêu cầu?"):
=======
file_read = st.file_uploader("")
if file_read is not None:
    file = pd.read_csv(file_read)
    st.write(file)

if prompt := st.chat_input("Input"):
    if prompt.lower() == "analyse":
        prompt = file.to_string()
        num_rows, num_column = file.shape
        if num_column == 1:
            display_data = px.histogram(file, x=file.columns[0], title='T')
        elif num_column >= 2:
            display_data = px.line(file, x=file.columns[1], y=file.columns[2], title="This is line chart for "+file.columns[0]+" after years")
        st.plotly_chart(display_data)

>>>>>>> Stashed changes
>>>>>>> Stashed changes
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message('user'):
        st.markdown(prompt)

    with st.chat_message('assistant'):
        full_response = ""
        holder = st.empty()

        #
        # for word in prompt.split():
        #     full_response += word + " "
        #     time.sleep(0.1)
        #     holder.markdown(full_response + "_")
        # holder.markdown(full_response)

        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {
                    "role": m["role"],
                    "content": m["content"]
                }
                    for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            holder.markdown(full_response + "_")
            holder.markdown(full_response)
        holder.markdown(full_response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )




