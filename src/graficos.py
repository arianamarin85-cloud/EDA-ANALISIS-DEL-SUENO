from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

CARPETA_IMAGENES = Path(__file__).resolve().parent.parent / "imagen"
CARPETA_IMAGENES.mkdir(parents=True, exist_ok=True)



def graficar_hipotesis_1(df_h1):
    f, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(
        df_h1.corr(),
        annot=True,
        linewidths=.5,
        ax=ax,
        vmin=-1,
        vmax=1,
        cmap="coolwarm"
    )
    ax.set_title("Correlación: Estrés vs Calidad del Sueño")
    plt.savefig(CARPETA_IMAGENES / "correlacion_estres_calidad_sueno.jpg")
    plt.show()


def graficar_hipotesis_2(df_h2):
    plt.figure()
    sns.boxplot(data=df_h2, x="Gender", y="Sleep Duration", hue="Gender")
    plt.title("Duración del sueño por género")
    plt.savefig(CARPETA_IMAGENES / "duracion_sueno_genero.jpg")
    plt.show()

    plt.figure(figsize=(7, 5))
    sns.histplot(data=df_h2, x="Sleep Duration", hue="Gender", kde=True, alpha=0.4)
    plt.title("Distribución de horas de sueño por género")
    plt.savefig(CARPETA_IMAGENES / "distribucion_horas_sueno_genero.jpg")
    plt.show()


def graficar_hipotesis_3(df_h3, resultado_h3):
    plt.figure()
    sns.boxplot(data=df_h3, x="BMI Category", y="Quality of Sleep", order=["Normal Weight", "Overweight", "Obese"], hue="BMI Category")
    plt.title("Relación IMC vs Calidad de Sueño")
    plt.savefig(CARPETA_IMAGENES / "relacion_imc_calidad_sueno.jpg")
    plt.show()

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(resultado_h3.index, resultado_h3["mean"], color='green', linestyle='--', marker='o')
    ax.set_title("Media de Calidad de Sueño por IMC")
    plt.savefig(CARPETA_IMAGENES / "media_calidad_sueno_imc.jpg")
    plt.show()


def graficar_hipotesis_4(df_h4):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df_h4, x="Sleep Disorder", hue="BMI Category")
    plt.title("Trastornos del sueño según categoría de IMC")
    plt.savefig(CARPETA_IMAGENES / "trastornos_sueno_imc.jpg")
    plt.show()


def graficar_hipotesis_5(df_h5, resumen_h5):
    fig, ax = plt.subplots(1, 3, figsize=(20, 6), sharey=True)
    sns.barplot(data=df_h5, y="Occupation", x="Stress Level", order=resumen_h5.index, ax=ax[0])
    ax[0].set_title("Nivel medio de estrés según ocupación")
    sns.barplot(data=df_h5, y="Occupation", x="Quality of Sleep", order=resumen_h5.index, ax=ax[1])
    ax[1].set_title("Calidad media del sueño")
    sns.barplot(data=df_h5, y="Occupation", x="Sleep Duration", order=resumen_h5.index, ax=ax[2])
    ax[2].set_title("Duración media de horas de sueño ")
    plt.tight_layout()
    plt.savefig(CARPETA_IMAGENES / "estres_sueno_ocupacion.jpg")
    plt.show()


def graficar_hipotesis_6(df_h6, resumen_h6):
    fig, ax = plt.subplots(1, 3, figsize=(15, 6), sharey=True)
    sns.barplot(data=df_h6, y="Grupo_Edad", x="Stress Level", order=resumen_h6.index, ax=ax[0], width=0.5)
    ax[0].set_title("Nivel medio de estrés según Edad")
    sns.barplot(data=df_h6, y="Grupo_Edad", x="Quality of Sleep", order=resumen_h6.index, ax=ax[1], width=0.5)
    ax[1].set_title("Calidad media del sueño")
    sns.barplot(data=df_h6, y="Grupo_Edad", x="Sleep Duration", order=resumen_h6.index, ax=ax[2], width=0.5)
    ax[2].set_title("Duración media de horas de sueño")
    plt.tight_layout()
    plt.savefig(CARPETA_IMAGENES / "estres_sueno_grupo_edad.jpg")
    plt.show()