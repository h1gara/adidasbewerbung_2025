import streamlit as st
import pandas as pd
import plotly.express as px

# App title
st.set_page_config(page_title="Gara Hasan - Bewerbung für adidas", page_icon="👟", layout="wide")

# Adidas Logo
st.image("https://upload.wikimedia.org/wikipedia/commons/2/20/Adidas_Logo.svg", width=200)

# Title Section
st.title("👋 Hallo adidas!")
st.subheader("Interaktive Bewerbung für das Duale Studium in Data Science + KI")

# Intro Section
st.header("Warum bin ich der perfekte Kandidat?")
st.write(
    "Mit meiner Erfahrung in Kundenbetreuung, Vertrieb und Projektmanagement - u.a. bei der EM 2024 in der Allianz Arena - bringe ich ein einzigartiges Skillset mit, das perfekt zu Ihrer Vision bei adidas passt."
)

# Persönliches Bild hinzufügen
st.image("https://via.placeholder.com/500x300.png?text=Dein+Bild", caption="Gara Hasan auf Reisen", width=500)

# Berufserfahrung visualisieren
data = {
    "Jahr": [2023, 2024],
    "Projekt": ["Werkstudent bei Siemens", "Einsatzleitung EM 2024 Allianz Arena"],
    "Beschreibung": [
        "Beratung von Kunden zu technischen Produkten und Lösungen.",
        "Organisation und Betreuung der Team-Hotels und Stadien während der EM."
    ],
}
df = pd.DataFrame(data)

st.subheader("📊 Berufserfahrung")
fig = px.timeline(df, x_start="Jahr", x_end="Jahr", y="Projekt", title="Berufserfahrung von Gara Hasan", text="Beschreibung")
st.plotly_chart(fig)

# Datenanalyse-Sektion
st.header("Datenanalyse: Kundenzufriedenheit bei adidas")
st.write(
    "Um zu zeigen, wie ich datenbasiert arbeiten kann, habe ich eine kleine Analyse erstellt. Hier untersuchen wir, welche Produkte bei Kunden am besten ankommen."
)

# Dummy-Daten für die Analyse
data_analysis = {
    "Produkt": ["Sneaker", "Laufschuhe", "Sportbekleidung", "Zubehör"],
    "Kundenzufriedenheit": [90, 85, 88, 80],
}
df_analysis = pd.DataFrame(data_analysis)

# Plot erstellen
fig_analysis = px.bar(
    df_analysis, x="Produkt", y="Kundenzufriedenheit", color="Produkt", title="Kundenzufriedenheit nach Produktkategorie"
)
st.plotly_chart(fig_analysis)

# Weitere Bilder hinzufügen
st.image("https://via.placeholder.com/500x300.png?text=Eventbild+1", caption="Gara bei der EM 2024")
st.image("https://via.placeholder.com/500x300.png?text=Eventbild+2", caption="Teamwork bei Projekten")

# Abschluss mit Quiz
st.header("🤔 Quiz: Passt Gara Hasan zu adidas?")
quiz_answer = st.radio(
    "Was denken Sie?",
    ("Ja", "Ja, definitiv!"),
)
if quiz_answer:
    st.success("Vielen Dank! Ich freue mich auf ein persönliches Gespräch.")

# Footer with adidas style
st.write("---")
st.markdown(
    "<div style='text-align: center;'>📧 Kontakt: <a href='mailto:gara867@gmail.com'>gara867@gmail.com</a> | 📞 +49 160 7795690</div>",
    unsafe_allow_html=True
)
