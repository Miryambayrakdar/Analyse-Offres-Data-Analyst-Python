import pandas as pd

df = pd.read_csv("/Users/miryam/Desktop/Projet-Data-Jobs/data/DataAnalyst.csv")

print(df.shape)
print(df.columns)
df = df.drop(columns=["Unnamed: 0"])
print(df.columns)

print(df.isnull().sum())
df = df.dropna(subset=["Company Name"])#suppression de la ligne où le nom de la compagnie est nul(une seule)
print(df.duplicated().sum())

df["Company Name"]=df["Company Name"].str.replace(r"\s\d\.\d$", "", regex=True)

df = df[df["Sector"] != "-1"]
df=df[df["Rating"]!=-1]

import matplotlib.pyplot as plt

top_10_job=df["Job Title"].value_counts().head(10)
graph1=top_10_job.plot(kind="bar")
for barre in graph1.patches:
    hauteur= barre.get_height()
    plt.text(barre.get_x() + barre.get_width()/2,
             hauteur,
             int(hauteur),
             ha="center")
    
plt.title("Les 10 métiers les plus proposés")
plt.xlabel("Métier")
plt.ylabel("Nombre d'offres")
plt.tight_layout()
plt.show()

top_10_location=df["Location"].value_counts().head(10)
graph2=top_10_location.plot(kind="bar")

for barre in graph2.patches:
    hauteur= barre.get_height()
    plt.text(barre.get_x() + barre.get_width()/2,
             hauteur,
             int(hauteur),
             ha="center")

plt.title("Les 10 villes qui recrutent le plus")
plt.xlabel("Ville")
plt.ylabel("Nombre d'offres")
plt.tight_layout()
plt.show()


top_10_secteur=df["Sector"].value_counts().head(10)
graph3=top_10_secteur.plot(kind="bar")

for barre in graph3.patches:
    hauteur= barre.get_height()
    plt.text(barre.get_x() + barre.get_width()/2,
             hauteur,
             int(hauteur),
             ha="center")

plt.title("Les 10 secteurs d'activités les plus présent")
plt.xlabel("Secteur")
plt.ylabel("Nombre d'activités")
plt.tight_layout()
plt.show()

top_10_entreprise=df["Company Name"].value_counts().head(10)

graph4=top_10_entreprise.plot(kind="bar")

for barre in graph4.patches:
    hauteur= barre.get_height()
    plt.text(barre.get_x() + barre.get_width()/2,
             hauteur,
             int(hauteur),
             ha="center")

plt.title("Les 10 entreprises qui recrutent le plus")
plt.xlabel("Entreprise")
plt.ylabel("Nombre d'offres")
plt.tight_layout()
plt.show()

rep_notes_entreprise=df["Rating"]
graph5=rep_notes_entreprise.hist()

for barre in graph5.patches:
    hauteur= barre.get_height()
    plt.text(barre.get_x() + barre.get_width()/2,
             hauteur,
             int(hauteur),
             ha="center")

plt.title("Répartition des notes")

plt.xlabel("Note")

plt.ylabel("Nombre d'entreprises")
plt.tight_layout()

plt.show()


competences={"SQL":df["Job Description"].str.contains("SQL",case=False).sum(),
             "Excel":df["Job Description"].str.contains("Excel",case=False).sum(),
             "Tableau":df["Job Description"].str.contains("Tableau",case=False).sum(),
             "Python":df["Job Description"].str.contains("Python",case=False).sum(),
             "SAS":df["Job Description"].str.contains("SAS",case=False).sum(),
             "R":df["Job Description"].str.contains(r"\bR\b",case=False).sum(),
             "Git":df["Job Description"].str.contains("Git",case=False).sum(),
             "Oracle":df["Job Description"].str.contains("Oracle",case=False).sum(),
             "AWS":df["Job Description"].str.contains("AWS",case=False).sum(),
             "SQL Server":df["Job Description"].str.contains("SQL Server",case=False).sum()
             }
             

print(competences)

competences_df = pd.DataFrame(
    list(competences.items()),
    columns=["Compétence", "Nombre d'offres"]
)

print(competences_df)
competences_tab = competences_df.sort_values(
    by="Nombre d'offres",
    ascending=False
)

print(competences_tab)

competences_tab = competences_tab.set_index("Compétence")

graph_competences=competences_tab.plot(kind="bar")

for barre in graph_competences.patches:
    hauteur= barre.get_height()
    plt.text(barre.get_x() + barre.get_width()/2,
             hauteur,
             int(hauteur),
             ha="center")

plt.title("Les compétences les plus demandées dans les offres de Data Analyst")
plt.xlabel("Compétence")
plt.ylabel("Nombre d'offres")
plt.tight_layout()
plt.show()

df = df[df["Salary Estimate"] != "-1"]

df["Salary Estimate"] = df["Salary Estimate"].str.split("(").str[0]
df["Salary Estimate"] = df["Salary Estimate"].str.replace("$", "", regex=False)
df["Salary Estimate"] = df["Salary Estimate"].str.replace("K", "", regex=False)

df[["Salaire Min", "Salaire Max"]] = df["Salary Estimate"].str.split("-", expand=True)

df["Salaire Min"] = df["Salaire Min"].astype(int)
df["Salaire Max"] = df["Salaire Max"].astype(int)

df["Salaire Moyen"] = (df["Salaire Min"] + df["Salaire Max"]) / 2

print(df["Salary Estimate"].head(10))

graph_salaire=df["Salaire Moyen"].hist()

for barre in graph_salaire.patches:
    hauteur= barre.get_height()
    plt.text(barre.get_x() + barre.get_width()/2,
             hauteur,
             int(hauteur),
             ha="center")

plt.title("Répartition des salaires moyens")

plt.xlabel("Salaire moyen (en milliers de dollars)")

plt.ylabel("Nombre d'offres")

plt.show()