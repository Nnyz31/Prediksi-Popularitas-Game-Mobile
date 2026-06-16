import gradio as gr
import pickle
import numpy as np

# Load model
with open("model_popularitas_game.pkl", "rb") as file:
    model = pickle.load(file)

def prediksi_popularitas(rating, reviews):

    data = np.array([[rating, reviews]])

    hasil = model.predict(data)

    if hasil[0] == 1:
        return "🎮 Game Diprediksi Populer"
    else:
        return "📉 Game Diprediksi Tidak Populer"

demo = gr.Interface(
    fn=prediksi_popularitas,
    inputs=[
        gr.Number(label="Rating Game"),
        gr.Number(label="Jumlah Reviews")
    ],
    outputs=gr.Textbox(label="Hasil Prediksi"),
    title="Prediksi Popularitas Game Mobile",
    description="Prediksi popularitas game mobile menggunakan algoritma Random Forest."
)

demo.launch()