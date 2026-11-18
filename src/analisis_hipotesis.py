import pandas as pd


def analizar_hipotesis_1(df_limpio):
    df_h1 = df_limpio[["Stress Level", "Quality of Sleep"]].copy()
    resultado_h1 = df_h1.groupby("Stress Level")["Quality of Sleep"].agg(["count", "mean"])
    print(resultado_h1.round(2))
    print(df_h1.corr(numeric_only=True))
    return df_h1


def analizar_hipotesis_2(df_limpio):
    df_h2 = df_limpio[["Gender", "Sleep Duration"]].copy()
    resultado_h2 = df_h2.groupby("Gender")["Sleep Duration"].agg(["count", "mean", "median", "std"])
    print(resultado_h2.round(2))

    # Duración en minutos tomando de referencia la media de cada género y lo convertimos en minutos
    x = 7.23 - 7.04
    minutos = x * 60
    print(minutos)
    return df_h2


def analizar_hipotesis_3(df_limpio):
    df_h3 = df_limpio[["BMI Category", "Quality of Sleep"]].copy()
    resultado_h3 = df_h3.groupby("BMI Category")["Quality of Sleep"].agg(["count", "mean", "median", "std"]).reindex(["Normal Weight", "Overweight", "Obese"])
    print(resultado_h3.round(2))
    print(pd.crosstab(df_h3["BMI Category"], df_h3["Quality of Sleep"]))
    return df_h3, resultado_h3


def analizar_hipotesis_4(df_limpio):
    df_h4 = df_limpio[["BMI Category", "Sleep Disorder"]].copy()
    resultado_h4 = df_h4.pivot_table(index="BMI Category", columns="Sleep Disorder", aggfunc="size", fill_value=0)
    print(resultado_h4)

    # Sabemos el IMC, calculamos el % trastorno
    total_filas = resultado_h4.sum(axis=1)
    pct_filas = resultado_h4.div(total_filas, axis=0) * 100
    print(pct_filas.round(1))

    # Sabemos el trastorno, calculamos el % sobre su IMC
    total_col = resultado_h4.sum(axis=0)
    pct_col = resultado_h4.div(total_col, axis=1) * 100
    print(pct_col.round(1))

    print(df_h4.value_counts())
    return df_h4


def analizar_hipotesis_5(df_limpio):
    df_h5 = df_limpio[["Occupation", "Stress Level", "Quality of Sleep", "Sleep Duration"]].copy()
    resumen_h5 = df_h5.groupby("Occupation")[["Stress Level", "Quality of Sleep", "Sleep Duration"]].agg(["count", "mean"])
    resumen_h5 = resumen_h5.sort_values(by=("Stress Level", "mean"), ascending=False)
    print(resumen_h5.round(2))
    return df_h5, resumen_h5


def analizar_hipotesis_6(df_limpio):
    df_h6 = df_limpio[["Age", "Stress Level", "Quality of Sleep", "Sleep Duration"]].copy()
    df_h6["Grupo_Edad"] = pd.cut(
        df_h6['Age'], bins=[20, 35, 45, 65], labels=['27-35 años', '36-45 años', '46+ años'])
    resumen_h6 = df_h6.groupby("Grupo_Edad")[["Stress Level", "Quality of Sleep", "Sleep Duration"]].agg(["count", "mean"])
    resumen_h6 = resumen_h6.sort_values(by=("Stress Level", "mean"), ascending=False)
    print(resumen_h6.round(2))
    return df_h6, resumen_h6