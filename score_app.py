import io
import numpy as np 
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image 


def calculate_average(scores):
    return sum(scores) / len(scores)

def percentage_distribution(scores):
    bins = {"80-100": 0, "60-79": 0, "<60": 0}
    for score in scores:
        if score >= 80:
            bins["80-100"] += 1
        elif score >= 60:
            bins["60-79"] += 1
        else:
            bins["<60"] += 1
    return bins



def main():
    st.title("Phân tích điểm số học sinh")
    uploaded_file = st.file_uploader("Chọn file Excel", type=["xlsx"])
    if uploaded_file:
        # Đọc dữ liệu file
        df = pd.read_excel(uploaded_file)

        # get Điểm số
        scores = df["Điểm số"].astype(float).tolist()

        # calculate average
        average = calculate_average(scores)
        st.write(f"Điểm trung bình: {average}")

        # percentage distribution
        dist = percentage_distribution(scores)
        labels = list(dist.keys())
        values = list(dist.values())
        st.write(dist)

        # show distribution
        fig, ax = plt.subplots(figsize=(1, 1))
        ax.pie(
            values, 
            labels=labels, 
            autopct='%1.1f%%', 
            textprops= {'fontsize': 3.5}
        )

        ax.axis('equal')
        plt.tight_layout(pad=0.1)
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi = 300)
        img = Image.open(buf)
        st.write("Biểu đồ phân bố điểm")
        st.image(img    )

        
if __name__ == "__main__":
    main()
