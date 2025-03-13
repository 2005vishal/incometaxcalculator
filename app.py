import streamlit as st
import calculator as cl
import pandas as pd
import plotly.express as px

# Create an instance of the class
tax_calculator = cl.IncomeTaxCalculator()

st.title("🖩Income Tax Calculator")
st.header("⚡ Quick Calculation!")
st.subheader("💻 Develop And Deploy by Vishal Patwa....")

col1, col2, col3= st.columns(3)

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.selectbox('Select Tax Payer', options=['Individual'])

with col2:
    st.selectbox('Select Age', options=['0-60'])

with col3:
    st.selectbox('Select Residential Status', options=['Resident'])

col4,col5 = st.columns(2)
with col4:
    income = st.number_input("Enter your income:", min_value=0,value=60000000)
with col5:
    deduction = st.number_input("Enter deduction under 80C, 80D, etc.", min_value=0, max_value=150000)

taxable_new, tax_new, surcharge_new, cess_new, total_tax_new = tax_calculator.new_tax_regime_calculator(income, deduction)
taxable_old, tax_old, surcharge_old, cess_old, total_tax_old = tax_calculator.old_tax_regime_calculator(income, deduction)

def format_indian_currency(value):
    return "{:,.0f}".format(value).replace(',', '_').replace('_', ',')

data = {
    " ": ['Gross Salary', "std: Dedction", "Gross Income", "Deduction under 80,80C", 'Total Income', "Tax", "Surcharge", "Cess", "Total Tax"],
    "New Tax Regime 2025-26": [
        format_indian_currency(income),
        format_indian_currency(75000 if income > 0 else 0),
        format_indian_currency((income - 75000) if income > 0 else 0),
        format_indian_currency(deduction),
        format_indian_currency(taxable_new if income > 0 else 0),
        format_indian_currency(tax_new),
        format_indian_currency(surcharge_new),
        format_indian_currency(cess_new),
        format_indian_currency(total_tax_new)
    ],
    "Old Tax Regime 2024-25": [
        format_indian_currency(income),
        format_indian_currency(50000 if income > 0 else 0),
        format_indian_currency((income - 50000) if income > 0 else 0),
        format_indian_currency(deduction),
        format_indian_currency(taxable_old if income > 0 else 0),
        format_indian_currency(tax_old),
        format_indian_currency(surcharge_old),
        format_indian_currency(cess_old),
        format_indian_currency(total_tax_old)
    ]
}

df = pd.DataFrame(data)
st.write(df)



# graph and and chart ploting df
df_new_tax = pd.DataFrame(data = { " ": ["Tax","Surcharge","Cess","Total Tax"],
                                   "New Tax Regime 2025-26": [tax_new,surcharge_new,cess_new,total_tax_new],
                                   "Old Tax Regime 2024-25": [tax_old,surcharge_old,cess_old,total_tax_old]
})

st.subheader("𝞹📈🧠📚New Tax Regime v/s Old Tax Regime")
col6,col7 = st.columns(2)
with col6:
    st.bar_chart(df_new_tax, x=' ', y='New Tax Regime 2025-26')

with col7:
    st.bar_chart(df_new_tax, x=' ', y='Old Tax Regime 2024-25')

st.subheader("⭕New Tax Regime v/s Old Tax Regime")
col8, col9 = st.columns(2)
with col8:
    fig1 = px.pie(data_frame=df_new_tax, names=df_new_tax[" "], values='New Tax Regime 2025-26',color=' ',
             color_discrete_map={'Total Tax':'lightcyan',
                                 'Tax':'cyan',
                                 'Cess':'royalblue',
                                 'Surcharge':'darkblue'},title = "New Tax Regime")
    st.plotly_chart(fig1)

with col9:
    fig2 = px.pie(data_frame=df_new_tax, names=df_new_tax[" "], values='Old Tax Regime 2024-25',color=' ',
             color_discrete_map={'Total Tax':'lightcyan',
                                 'Tax':'cyan',
                                 'Cess':'royalblue',
                                 'Surcharge':'darkblue'} ,title = "Old Tax Regime")
    st.plotly_chart(fig2)










