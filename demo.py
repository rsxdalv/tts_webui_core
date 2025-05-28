import gradio as gr
from tts_webui_core.ui.randomize_seed import randomize_seed

with gr.Blocks() as demo:
    randomize_seed()

if __name__ == "__main__":
    demo.launch()
