from pathlib import Path
import streamlit as st
import os
from streamlit_cropper import st_cropper
import subprocess
import glob
from PIL import Image, ImageEnhance, ImageOps

jeScanne = st.button("Je scanne mon image !", type="primary")
file=None
if jeScanne:
    subprocess.run(["bash", "./SCRIPTS/scanimage.sh"])
    most_recent_file = None
    most_recent_time = 0
    list_of_files = glob.glob('./SCANNER/*.png') # FIXME test only .PNG ?
    latest_file = max(list_of_files, key=os.path.getctime)
    file = os.path.abspath(latest_file)
    # st.session_state['scanned_file'] = file
    # Button to choose between webcam and local image
option = st.radio(
    "Choisir une image",
    ("⬆️ Téléverser un fichier", "📸 Utiliser la webcam"),
    horizontal=True
    )
if option == "⬆️ Téléverser un fichier":
    if file==None:
        file = st.file_uploader(
        "Choisis un fichier à imprimer",
        type=["png", "jpg", "gif", "webp", "bmp", "tiff"]
        )
elif option == "📸 Utiliser la webcam":
    if file==None:
        file = st.camera_input("Prendre une photo")

if file is not None:
    st.success("Fichier sélectionné! Tu peux passer à l'onglet \"crop\" !")
    image = Image.open(file)
    st.image(image, use_container_width=True)

    st.write(file)

    image,box = st_cropper(
                image,
                realtime_update=True,
                box_color="#ff0000",
                #aspect_ratio=aspect_ratio,
                return_type='both',
                stroke_width=3,
    )

            # Remove borders
    image = image.crop(
        (3, 3, image.size[0] -3, image.size[1] -3, ))
