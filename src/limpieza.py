import pandas as pd

from src.configuracion import CSV_LIMPIO


def revisar_duplicados(df):
    #Identifica registros duplicados excluyendo Person ID (sin eliminarlos)
    mascara = df.drop(columns=["Person ID"]).duplicated()
    duplicados = df[mascara]
    print(f"\n--- Duplicados detectados (sin Person ID): {len(duplicados)} filas ---")
    return duplicados


def normalizar_bmi(df):
    #Unifica "Normal" como "Normal Weight" en la columna BMI Category
    df_limpio = df.copy()
    df_limpio["BMI Category"] = df_limpio["BMI Category"].replace({"Normal": "Normal Weight"})
    print("\n--- Distribución de BMI Category tras normalizar ---")
    print(df_limpio["BMI Category"].value_counts())
    return df_limpio


def imputar_nulos_sueno(df):
    #Reemplaza los valores nulos de Sleep Disorder por "No_Disorder".
    df_limpio = df.copy()
    df_limpio["Sleep Disorder"] = df_limpio["Sleep Disorder"].fillna("No_Disorder")
    print("\n--- Valores nulos tras imputar Sleep Disorder ---")
    print(df_limpio.isnull().sum())
    return df_limpio


def separar_presion_arterial(df):
    #Divide Blood Pressure en SYS y DIA (int)
    df_limpio = df.copy()
    df_limpio[["SYS", "DIA"]] = (
        df_limpio["Blood Pressure"].str.split("/", n=1, expand=True).astype(int)
    )

    inconsistencias = df_limpio[df_limpio["SYS"] <= df_limpio["DIA"]]
    print(f"\n--- Registros con SYS <= DIA: {len(inconsistencias)} ---")

    df_limpio = df_limpio.drop("Blood Pressure", axis=1)
    return df_limpio


def guardar_datos_limpios(df_limpio):
    #Guarda el DataFrame limpio en la ruta configurada (CSV_LIMPIO).
    df_limpio.to_csv(CSV_LIMPIO, index=False)
    print(f"\nDataset limpio guardado en: {CSV_LIMPIO}")