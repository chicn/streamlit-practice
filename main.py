import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')
st.write('DataFrame')


##################################################################
## 表の表示 (https://docs.streamlit.io/library/api-reference/data)
##################################################################
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.write(df)