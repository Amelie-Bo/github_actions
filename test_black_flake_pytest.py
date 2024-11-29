import pandas as pd


df = pd.read_csv(
    "wine_corrupted.csv", sep=";", index_col=0, na_values={"!", "?", "rrr"}
)

# Renommer les colonnes
df.columns = df.columns.str.replace(" ", "_")

# Enlever le mg/L de fixed acidity, puis mettre au format float
df["fixed_acidity"] = df["fixed_acidity"].str[:-4].astype("float")

# Mettre le mode aux Nan de la variable catégorielle quality
df["quality"] = df["quality"].fillna(df["quality"].mode()[0])

# Mettre la mediane aux Nan des variables catégorielles
# df = df.fillna(df.median())

df.head(10)
