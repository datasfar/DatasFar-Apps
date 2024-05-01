import streamlit as st
import pandas as pd

# Subir dataset y generar dataframe
st.header("Visualizador de datos")
st.write("Visualiza datos a partir de un documento .csv")
data_set = st.file_uploader("Sube un documento csv", type="csv")

if data_set is not None:
    dataframe = pd.read_csv(data_set)

    # Dropear columnas
    st.write("Solo se mostraran las columnas seleccionadas:")
    columns_to_drop = [st.checkbox(column, value=True, key=column) for column in dataframe.columns]
    columns_to_drop = dataframe.columns[columns_to_drop]
    dataframe.drop(columns=columns_to_drop, inplace=False)
    st.write(dataframe)
 
    # Filtro a columna "str"
    selected_column = st.selectbox("Columnas", options=dataframe.columns)
    st.write("Filtrar filas por valor en una columna:")
    selected_value = st.text_input("Valor a filtrar en la columna seleccionada")
    filtered_data = dataframe[dataframe[selected_column] == selected_value]
    st.write(filtered_data)
