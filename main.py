from turtle import done, down
import streamlit as st
import webbrowser
import time
import pyautogui
from os import getcwd, path, mkdir
from zipfile import ZipFile
import shutil

if not path.exists(getcwd() + '/images'):
    mkdir(getcwd() + '/images', 666)


st.set_page_config(
    page_title = 'Web Screen-Shoter! | Tude Maha',
    menu_items = {
        'About': '''
            ## Web Screen-Shoter!
            Visit the GitHub repository: https://github.com/tudemaha/web-screenshoter
            
            Created with :heart: by [Tude Maha](https://instagram.com/tudemaha)
        '''
    })


st.title('Web Screen-Shoter!')
st.write('Faster web screenshot, do MORE in ONE click.')

col1, col2 = st.columns([4, 2], gap = 'medium')

with col1:
    delay = st.text_input('Delay per process (second):', value = 7, placeholder = 'Insert delay in second')
    text = st.text_area('Website URLs (sparated by new line):', placeholder='Insert web URL')
    button_status = st.button('Start')

    if button_status:
        if len(text) != 0:
            urls = text.split('\n')
            for i, url in enumerate(urls):
                webbrowser.open(url, 0, True)
                time.sleep(int(delay))
                image = pyautogui.screenshot()
                save_in = getcwd() + f'/images/{i + 1}.jpg'
                image.save(save_in)
                with col2:
                    st.image(image)

            with ZipFile('screenshots.zip', 'w') as zipObj:
                for i, _ in enumerate(urls):
                    filePath = getcwd() + f'/images/{i + 1}.jpg'
                    zipObj.write(filePath, path.basename(filePath))
                
            shutil.rmtree(getcwd() + '/images')
            
            with open(getcwd() + '/screenshots.zip', 'rb') as zip_download:
                st.write('Screenshots ready to download!')
                st.download_button('Download Screenshots', zip_download, 'screenshots.zip')
        
        else:
            st.error('Must enter at least one URL', icon = '🚨')