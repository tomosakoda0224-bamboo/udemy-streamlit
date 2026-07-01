#streamlit run c:/Users/user/python202604/main.py
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 40, 25]
})

st.table(df.style.highlight_max(axis=0)) #ただの表を表示するときはtable 動的な表はst.dataframeで表示



#shift+@=`(バッククオーテーション)
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""



df1 = pd.DataFrame(
     np.random.rand(20,3),
     columns=['a', 'b', 'c']
)
st.line_chart(df1)



df2 = pd.DataFrame(
     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
     columns=['lat', 'lon'] #lat=緯度、#lon=経度
)
st.map(df2)



option = st.selectbox(
    'あなたが好きな数字を教えてください、',
    list(range(1, 11))
)
odo = (option*32-7+12.5)/12.11
'あなたの好きな数字は、', odo, 'です。'



st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('衛生管理者免許証.jpg')
    st.image(img, caption='Tomohiro Sakoda', use_column_width=True)



st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')


text = st.text_input('あなたの趣味を教えてください。') #st.sidebar.***でサイドバーに表示可能
'あなたの趣味：', text, 'です。'



condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition



st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!!!!'



expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の内容を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の内容を書く')