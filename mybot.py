import streamlit as st
import ollama

st.set_page_config(
    page_title="LEAF X - Your Plant Classification Assistant",
    page_icon="🌿",
    layout="wide"
)

st.title("LEAF X - Your Plant Classification Assistant")
st.subheader("Classify plants and learn their characteristics")

plant_name = st.text_input("Enter Plant Name")

def classify_plant(plant):
    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": """
You are an expert botanist.

For every plant, provide information in this exact format:

## Plant Name

### Classification
Classify into ONE of:
- medicinal plant
- food plant
- ornamental plant
- environmental plant

### Scientific Name

### Characteristics
- Height
- Stem type
- Leaves
- Flowers/Fruits

### Important Elements Required
Mention important nutrients needed:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Calcium (Ca)
- Magnesium (Mg)
- Iron (Fe)

### Uses
- Medicinal uses
- Environmental importance
- Economic uses

### Interesting Facts

Use simple language suitable for school students.
"""
            },
            {
                "role": "user",
                "content": plant
            }
        ]
    )

    return response["message"]["content"]

if st.button("Classify Plant"):

    if plant_name.strip() == "":
        st.warning("Please enter a plant name.")
    else:
        with st.spinner("Analyzing Plant..."):
            result = classify_plant(plant_name)

        st.markdown(result)

st.markdown("---")
st.markdown("### Example Plants")
st.write("Neem, Mango, Rose, Tulsi, Aloe Vera, Money Plant, Pumpkin, Bamboo")
