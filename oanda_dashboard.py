# oanda_dashboard.py
import streamlit as st
import pandas as pd
google_sheet_url = "https://docs.google.com/spreadsheets/d/TON_ID_ICI/export?format=csv&id=TON_ID_ICI&gid=0"

st.set_page_config(page_title="Snipegold - Dashboard", layout="wide")
st.title("📊 Dashboard du Bot Snipegold")

try:
    df = pd.read_csv(google_sheet_url)
    df.columns = ["Date", "Heure", "Signal", "Prix", "TP", "SL", "PnL"]
    df["PnL"] = pd.to_numeric(df["PnL"], errors="coerce")

    dernier_trade = df.iloc[-1]
    total_trades = len(df)
    total_profit = df["PnL"].sum()
    gagnants = df[df["PnL"] > 0].shape[0]
    perdants = df[df["PnL"] < 0].shape[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("📍 Dernier signal", f"{dernier_trade['Signal']} à {dernier_trade['Prix']}")
    col2.metric("✅ Trades gagnants", gagnants)
    col3.metric("❌ Trades perdants", perdants)

    st.markdown("---")
    st.subheader("📆 Historique complet")
    st.dataframe(df[::-1], use_container_width=True)

    st.markdown("---")
    st.subheader("📈 Courbe des gains")
    st.line_chart(df["PnL"].cumsum())

except Exception as e:
    st.error(f"Erreur de chargement des données : {e}")
