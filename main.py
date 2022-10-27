import streamlit as st
import webbrowser
import time
import pyautogui
from os import getcwd, path, mkdir

if not path.exists(getcwd() + '/images'):
    mkdir(getcwd() + '/images', 666)


st.title('Web Screen-Shoter!')
st.write('Faster web screenshot, do MORE in ONE click.')

col1, col2 = st.columns([4, 2], gap = 'medium')

with col1:
    delay = st.text_input('Delay per process (second):', value = 7, placeholder = 'Insert delay in second')
    text = st.text_area('Website URL (sparated by new line):', placeholder='Insert web URL')
    button_status = st.button('Start')

    if button_status:
        urls = text.split('\n')
        
        with col2:
            for i, url in enumerate(urls):
                webbrowser.open(url, 0, True)
                time.sleep(int(delay))
                image = pyautogui.screenshot()
                save_in = getcwd() + f'/images/{i + 1}.jpg'
                image.save(save_in)
                st.image(image)
                
                