import streamlit as st
import numpy as numpy
import pandas as pd
import numpy as np
from PIL import Image

st.title("Streamlit 入門w")

st.write("DataFrame")

df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 40, 30, 20]
})

st.dataframe(df, width = 300, height = 200)

st.dataframe(df.style.highlight_max(axis=0), width = 300, height = 200)


df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)


df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)

st.write('Display Image')

img = Image.open('buranko_girl_smile.png')
st.image(img, caption='KK', use_column_width=True)

"""
# 章
## 節
### 項

```
import streamlit as st
import numpy as numpy
import pandas as pd

```

"""
#pythonのマークダウンの記述方法
