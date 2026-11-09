import streamlit as st
import numpy as np
import pandas as pd
import time

option=st.radio("jjjjj?",["1111","55555"])



with st.expander("lllllllllllllllllllllllll"):
  st.write("llllllllllllll")
  st.write("llllllllllll")



bar=st.progress(0)

for i in range (100):
  bar.progress(i+1)

msg=st.empty()
msg.text("kkkkkkkkkkk")



t=st.progress(0)
for i in range(10):
  t.progress(i+1)
  time.sleep(.3)

  