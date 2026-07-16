import gradio as gr
import requests
import os

# FastAPI Backend URL
FASTAPI_URL = "https://resume-backend-vtcr.onrender.com/generate"


def generate(name, role, skills, experience):

    payload = {
        "name": name,
        "role": role,
        "skills": skills,
        "experience": experience
    }

    try:
        response = requests.post(FASTAPI_URL, json=payload)

        if response.status_code == 200:
            return response.json()["objective"]
        else:
            return f"Backend Error: {response.status_code}"

    except Exception as e:
        return f"Unable to connect to the backend.\n{str(e)}"


demo = gr.Interface(
    fn=generate,
    inputs=[
        gr.Textbox(label="Name"),
        gr.Textbox(label="Job Role"),
        gr.Textbox(label="Skills"),
        gr.Textbox(label="Years of Experience")
    ],
    outputs=gr.Textbox(
        label="Generated Resume Objective",
        lines=6
    ),
    title="Resume Objective Generator",
    description="Generate a professional resume objective using FastAPI and Gradio."
)

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        inbrowser=True
    )