from src import carga_inspeccion
from src import limpieza
from src import analisis_hipotesis
from src import graficos


def main():
    # Carga e inspección de los datos
    df = carga_inspeccion.cargar_datos()
    carga_inspeccion.ver_primeras_filas(df)
    carga_inspeccion.ver_dimensiones_y_tipos(df)
    carga_inspeccion.ver_valores_nulos(df)
    carga_inspeccion.ver_estadisticas_descriptivas(df)

    # Limpieza y guardado de los datos
    limpieza.revisar_duplicados(df)
    df_limpio = limpieza.normalizar_bmi(df)
    df_limpio = limpieza.imputar_nulos_sueno(df_limpio)
    df_limpio = limpieza.separar_presion_arterial(df_limpio)
    limpieza.guardar_datos_limpios(df_limpio)

    # Pruebas de hipótesis
    df_h1 = analisis_hipotesis.analizar_hipotesis_1(df_limpio)
    df_h2 = analisis_hipotesis.analizar_hipotesis_2(df_limpio)
    df_h3, resultado_h3 = analisis_hipotesis.analizar_hipotesis_3(df_limpio)
    df_h4 = analisis_hipotesis.analizar_hipotesis_4(df_limpio)
    df_h5, resumen_h5 = analisis_hipotesis.analizar_hipotesis_5(df_limpio)
    df_h6, resumen_h6 = analisis_hipotesis.analizar_hipotesis_6(df_limpio)

    # Gráficos
    graficos.graficar_hipotesis_1(df_h1)
    graficos.graficar_hipotesis_2(df_h2)
    graficos.graficar_hipotesis_3(df_h3, resultado_h3)
    graficos.graficar_hipotesis_4(df_h4)
    graficos.graficar_hipotesis_5(df_h5, resumen_h5)
    graficos.graficar_hipotesis_6(df_h6, resumen_h6)


if __name__ == "__main__":
    main()