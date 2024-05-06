# Importamos las librerias
import streamlit as st
import pytz
from datetime import datetime, timedelta

def main():
    # Encabezado de la aplicación
    st.image("assets/timezones.png")
    st.header("Aplicación para convertir fechas mundiales")
    st.write("La aplicación permite consultar la hora en diferentes localizaciones y operar con fechas")

    # Obtener nombres y códigos de países
    country_names = pytz.country_names
    country_codes = {v: k for k, v in country_names.items()} 

    # Crear columnas para la interfaz de usuario
    col1, col2, col3 = st.columns(3)
    with col1:
        # Selector de país
        country_selector = st.selectbox("Seleccione el pais:", list(country_names.values()))
        country_code = country_codes[country_selector]
        utc_offset = pytz.country_timezones.get(country_code)

        # Calcular el desfase horario
        if utc_offset:
            tz = pytz.timezone(utc_offset[0])
            utc_offset = tz.utcoffset(datetime.now()).total_seconds() / 3600
        else:
            utc_offset = "No se encontró información de UTC para este país"

    with col2:
        # Selector de fecha
        date_selector = st.date_input("Seleccione la fecha:")
    with col3:
        # Selector de hora
        time_selector =  st.time_input("Seleccione la hora:")

    # Botón para guardar la fecha y hora seleccionadas
    save_datetime = st.button("Guardar")

    # Si no hay ningún dato guardado en la sesión, inicializar una lista vacía
    if 'saved' not in st.session_state:
        st.session_state.saved = []

    # Guardar la fecha y hora seleccionadas en la sesión
    if save_datetime:
        st.session_state.saved = [country_selector, date_selector, time_selector]

    # Si se han guardado la fecha, hora y país, mostrar el resultado
    if len(st.session_state.saved) == 3:
        st.success(f"{country_selector}, {date_selector}, {time_selector}, {country_code}, {utc_offset}")

        # Selector de países adicionales
        add_country = st.multiselect("Seleccione el pais:", list(country_names.values()), format_func=lambda x: x)
        add = st.button("Agregar")

        # Si se hace clic en el botón "Agregar", calcular y mostrar la hora para los países seleccionados
        if add:
            selected_country = st.session_state.saved[0]
            selected_date = st.session_state.saved[1]
            selected_time = st.session_state.saved[2]

            # Iterar sobre los países seleccionados para calcular y mostrar la hora
            for country, country_name in country_names.items():
                if country_name in add_country:
                    timezone = pytz.country_timezones.get(country)
                    if timezone:
                        # Obtener la hora local en el país seleccionado
                        local_datetime = datetime.combine(selected_date, selected_time)
                        local_timezone = pytz.timezone(timezone[0])
                        local_datetime_with_tz = local_timezone.localize(local_datetime)
                        offset = local_datetime_with_tz.utcoffset().total_seconds() / 3600
            
                        hora_1 = local_datetime_with_tz.strftime('%Y-%m-%d %H:%M:%S')

                        # Calcular la diferencia horaria entre el país seleccionado y el nuevo país
                        dif = utc_offset - offset
                        nueva_hora = datetime.strptime(hora_1, '%Y-%m-%d %H:%M:%S') - timedelta(hours=dif)

                        nueva_hora_str = nueva_hora.strftime('%Y-%m-%d %H:%M:%S')
                        
                        # Mostrar la nueva hora
                        st.success(f"En {country_name} serán las {nueva_hora_str}")
                        st.write(f"Cuando sean las: {hora_1}, en {selected_country} serán las: {nueva_hora_str} en {country_name}")

    # Pie de página
    st.write("Desarrollada con <3 por dataSfar")

main()
