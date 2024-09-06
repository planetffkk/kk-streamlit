import streamlit as st
import numpy as numpy
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title("Streamlit 入門w")

st.write("DataFrame")

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')


if st.checkbox('Show Image'):
    img = Image.open('buranko_girl_smile.png')
    st.image(img, caption='KK', use_column_width=True)

option = st.selectbox(
    'あなたの好きな数字を教えてください',
    list(range(1, 11))
)

'あなたの好きな数字は', option, 'です'

text = st.sidebar.text_input('あなたの趣味を教えてください')


condition = st.sidebar.slider('あなたの今の体調は', 0 ,100, 50)#最小値は０、最大値は１００、デフォルト数値は50という記述

'あなたの趣味:', text
'今日の体調は:', condition


st.write('プログレスバーの表示')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)


