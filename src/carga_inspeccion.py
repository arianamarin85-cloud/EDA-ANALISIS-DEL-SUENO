import pandas as pd
from src.configuracion import CSV_ORIGINAL

def cargar_datos():
    #Cargamos el Dataset.
    return pd.read_csv(CSV_ORIGINAL)



def ver_primeras_filas(df, n=5):
    #Muestra las primeras filas del DataFrame.
    print(f"\n--- Primeras {n} filas ---")
    print(df.head(n))


def ver_dimensiones_y_tipos(df):
    #Muestra tamaño, nombres de columnas, tipos de datos e información general.
    print("\n--- Tamaño (filas, columnas) ---")
    print(df.shape)

    print("\n--- Columnas ---")
    print(df.columns)

    print("\n--- Tipos de datos---")
    print(df.dtypes)

    print("\n--- Información general(df.info) ---")
    df.info()


def ver_valores_nulos(df):
    #Comprueba las columnas que tienen valores nulos y la cantidad que hay en cada una.
    print("\n--- Revisamos si hay valores nulos ---")
    print(df.isnull().any())

    print("\n--- Cantidad de valores nulos por columna ---")
    print(df.isnull().sum())



def ver_estadisticas_descriptivas(df):
    #Muestra el resumen estadístico de columnas numéricas y categóricas.
    print("\n--- Estadísticas descriptivas del dataframe ---")
    print(df.describe(include="all"))


def inspeccionar_datos(df):
    #Ejecuta las funciones del primer paso de inspección.
    ver_primeras_filas(df, n=2)
    ver_dimensiones_y_tipos(df)
    ver_valores_nulos(df)
    ver_estadisticas_descriptivas(df)
