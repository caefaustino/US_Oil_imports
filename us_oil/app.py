# 0 - Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import pickle

# 1- Page title
st.title("U.S. Crude Oil Imports (2009-2024)")
st.write("""
        This page presents data on crude oil imports by the United States from 2009 to 2024. 
        The information includes the volume of imported oil, the origins and destinations, and the types of crude oil imported.
        Explore the data to gain insights into the trends and patterns of oil imports over the years.
        """)
st.image("../Petroleo5.jpg")

# 2- File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# 3- Data Overview
st.header("Data Overview")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
else:
    st.write("Please upload a CSV file to see the data overview.")
st.divider()

# 4- Data Analysis
st.header("Data Analysis")

# 4.1- Temporal Analysis
st.subheader("Temporal Analysis")

# 4.1.1 - Total Volume Imported per Year
# Aggregating the data to obtain the total volume per year
df_yearly = df.groupby('year')['quantity'].sum().reset_index()
# Creating graph
fig_yearly = px.bar(df_yearly, x='year', y='quantity',
                    title='Total Volume Imported per Year',
                    labels={'quantity':'Volume (in thousands of barrels)', 'year':'Year'})
fig_yearly.show()
# Showing graph
st.plotly_chart(fig_yearly)

# 4.1.2 - Total Volume Imported Month by Month
# Creating a 'date' column by combining 'year' and 'month'
df['date'] = pd.to_datetime(df[['year', 'month']].assign(DAY=1))
# Aggregating the data to obtain the total volume per month
df_monthly = df.groupby('date')['quantity'].sum().reset_index()
# Creating graph
fig_monthly = px.bar(df_monthly, x='date', y='quantity',
                      title='Total Volume Imported Month by Month',
                      labels={'quantity':'Volume (in thousands of barrels)', 'date':'Year-Month'})
fig_monthly.show()
#Showing graph
st.plotly_chart(fig_monthly)
#Comments
st.write("""
         The decrease in U.S. oil imports from 2009 to 2020 can be attributed to several
         interconnected reasons, reflecting changes in domestic production, energy policies, 
         technological advancements, and global market dynamics. Here are some of the possible reasons:
         """)
st.markdown("*Increased Domestic Oil Production*")
st.write("""
         Shale Revolution (Shale Boom): Starting in the mid-2000s, the U.S. experienced a significant
          increase in oil production, largely due to the development of hydraulic fracturing (fracking)
          and horizontal drilling technologies. This allowed access to large shale oil reserves,
          increasing domestic production and reducing dependence on imports. Improvements in Efficiency
          and Exploration/Production Technology: Technological advances enabled the exploration of oil
          reserves that were previously inaccessible or uneconomical, contributing to increased domestic supply.
         """)
st.markdown("*Changes in Energy Policies*")
st.write("""
         Energy Security Policies: The U.S. implemented policies aimed at increasing the country's energy
          security by reducing dependence on external sources of oil, especially from politically
          unstable regions. Incentives for Domestic Production: Government incentives and favorable
          regulations stimulated oil exploration and production in the U.S., supporting the growth of
          domestic production.
         """)
st.markdown("*Advances in Energy Efficiency and Transition to Alternative Energy Sources*")
st.write("""
         More Efficient Vehicles: The introduction of stricter fuel efficiency standards for vehicles contributed
          to reduced oil consumption. Growth of Renewable Energies: Increased investment in alternative energy
          sources, such as wind and solar, reduced dependence on oil as an energy source. Changes in Consumer
          Behavior: Greater environmental awareness and changes in consumption patterns also contributed to
          reduced demand for oil.
         """)
st.markdown("*Economic and Market Changes*")
st.write("""
         *Fluctuations in Oil Prices:* Volatility in oil prices, including periods of low prices, can make imports
          less attractive compared to domestic production.
        """)
st.write("""
         *Economic Growth and Energy Demand:* The global economic recession of 2008-2009 led to a decrease in
          energy demand, including oil, which may have impacted imports in subsequent years.
        """)
st.markdown("*Development of Export Infrastructure*")
st.write("""
         *Export Capacity:* With the increase in domestic production, the U.S. began developing its oil export
          infrastructure, shifting from a large importer to an active participant in the global oil export market.
        """)
st.write("""
         These factors, among others, contributed to the decrease in U.S. oil imports during the period from 2009 to 
         2020. The interaction of these variables reflects the complexity of global energy market dynamics and 
         national strategies regarding oil production, consumption, and trade.Starting from 2020, we can notice a
          slight upward trend in imports, which can be explained by the post-pandemic economic recovery and the
          consequent increase in energy demand.
         """)

# 4.2 - Analysis by Origin
# Calculating total volume imported
total_volume = df['quantity'].sum()
# Creating a dataset that groups total volume by origin
df_origin = df.groupby('originName')['quantity'].sum().reset_index()
df_origin = df_origin.sort_values('quantity', ascending=False)
df_origin['percentage'] = (df_origin['quantity']/total_volume)*100
df_origin['cumulative_percentage'] = df_origin['percentage'].cumsum()
# Creating graph
fig_origin = px.bar(df_origin.head(20), x='originName', y='quantity',
             title='Total Volume per Origin',
             labels={'quantity':'Volume (in thousands of barrels)', 'originName':'Origin'},
             color='quantity')
fig_origin.show()
# Showing graph
st.plotly_chart(fig_origin)
# Comments
st.write("""
         When analyzing the major exporters of crude oil to the United States, it is notable that approximately 25%
          of the imports are classified under "World" and 17% under "NON-OPEC." These classifications provide insights
          into the diversity and sources of U.S. oil imports.
         """)
st.markdown("*World Classification*")
st.write("""
         The "World" category likely aggregates data from multiple countries or regions that do not fall into specific
          predefined categories. This could include smaller exporters or a mix of countries that individually contribute
          less significantly to the total import volume but collectively form a substantial portion. The 25% figure
          indicates that the U.S. sources a significant portion of its oil from a diverse array of global suppliers,
          reflecting a strategy of diversification to enhance energy security and reduce dependency on any single source or region.
         """)
st.markdown("*NON-OPEC Classification*")
st.write("""
         The "NON-OPEC" classification, accounting for 17% of the imports, refers to countries that are not members of
          the Organization of the Petroleum Exporting Countries (OPEC). NON-OPEC countries include major oil producers
          like Canada, Russia, and Brazil. The substantial share from NON-OPEC countries highlights the importance of these
          nations in the global oil market and their role in supplying the U.S. with crude oil. This diversification helps
          mitigate the risks associated with geopolitical tensions and production quotas often seen within OPEC.
         """)
st.markdown("*Interpretation and Implications*")
st.write("""
         The combined 42% of imports from "World" and "NON-OPEC" sources underscores the U.S. strategy to maintain a balanced
          and diversified import portfolio. This approach helps to ensure a stable supply of crude oil, mitigating risks
          associated with over-reliance on specific countries or geopolitical blocs. It also reflects the dynamic nature of
          the global oil market, where the U.S. leverages a wide range of suppliers to meet its energy needs.

         In summary, the significant shares of oil imports classified under "World" and "NON-OPEC" illustrate the U.S.'s
          strategic efforts to diversify its sources of crude oil, enhancing energy security and stability in the face of
          global market fluctuations and geopolitical uncertainties.
         """)

# 4.3 - Analysis by Destination
# Creating a dataset that groups total volume by destination
df_destination = df.groupby('destinationName')['quantity'].sum().reset_index()
df_destination = df_destination.sort_values('quantity', ascending=False)
df_destination['percentage'] = (df_destination['quantity']/total_volume)*100
df_destination['cumulative_percentage'] = df_destination['percentage'].cumsum()
st.write(df_destination.head(15))
st.write("""
         The interpretation of the classification "USA" as the primary destination for imported oil, followed by specific regions
          like PADD3, PADD2, Texas, and PADD5, requires a detailed understanding of the logistics and distribution of oil in
          the United States. Here is a detailed analysis:
         """)
st.markdown("*USA Classification as General Destination*")
st.write("""
         The classification "USA" as a destination can be interpreted as an aggregation of all oil imports entering the country
          before being distributed to specific destinations. This means that initially, the oil is accounted for as imported to
          the U.S. as a whole, before being redistributed to various regions and states within the country. This approach simplifies
          the initial accounting and reflects the total entry of oil into the country.
         """)
st.markdown("*Regional Distribution and Logistics*")
st.write("""
         After the initial import, the oil is distributed to different regions and states, which are classified more specifically.
          The PADD (Petroleum Administration for Defense Districts) regions are geographic divisions used by the U.S. government to
          facilitate the administration and analysis of the oil market. The main PADD regions are:
         
         PADD1 (East Coast)

         PADD2 (Midwest)

         PADD3 (Gulf Coast)

         PADD4 (Rocky Mountain)

         PADD5 (West Coast)
         """)
st.markdown("*Interpretation of Regional Data*")
st.write("""
         ***PADD3 (Gulf Coast)*** includes states like Texas and Louisiana, which are major refining centers and have significant
          infrastructure for the import and processing of oil. The high percentage of imports to PADD3 reflects the refining capacity
          and strategic importance of this region in the U.S. oil industry.

         ***PADD2 (Midwest)*** covers the Midwest, a region that, although it does not have the same refining capacity as PADD3, is still a
          significant consumer of oil, especially for transportation and industry.

         ***TEXAS***, part of PADD3, is highlighted separately due to its importance as one of the largest oil-producing and refining states
          in the U.S. The specification of Texas reflects its refining capacity and robust infrastructure for the import and processing of oil.

         ***PADD5 (West Coast)*** includes states like California, Oregon, and Washington. This region is a major consumer of oil, especially
          due to the high fuel demand in California. The percentage of imports to PADD5 reflects the need to supply this highly populous
          and industrialized region.
         """)
st.markdown("*Conclusion*")
st.write("""
         The classification of "USA" as the primary destination for oil imports, followed by specific regions like PADD3, PADD2,
          Texas, and PADD5, can be interpreted as a methodological approach to account for the total entry of oil into the country
          before its internal redistribution. This reflects the complex logistics and distribution infrastructure of oil in the
          U.S., where imported oil is initially recorded as imported to the country as a whole and then distributed to specific 
          regions based on refining capacity, demand, and infrastructure.

         This approach allows for a clear and organized view of the distribution of imported oil, facilitating the analysis and
          management of the oil supply chain in the United States.
         """)

# 4.4 - Analysis of Type of Crude Oil
# Creating a dataset that groups total volume by oil type
df_oiltype = df.groupby('gradeName')['quantity'].sum().reset_index()
df_oiltype = df_oiltype.sort_values('quantity', ascending=False)
# Creating graph
fig_type = px.bar(df_oiltype, x='gradeName', y='quantity',
             title='Total Volume by Type of Oil',
             labels={'quantity':'Volume (in thousands of barrels)', 'gradeName':'Type'},
             color='quantity')
fig_type.show()
# Showing graph
st.plotly_chart(fig_type)
# Comments
st.write("""
         The predominance of Heavy Sour crude oil in U.S. imports results from a combination of economic, technological, and strategic factors.
          The advanced refining capacity of the U.S., the availability and cost of heavy crude, the diversification of import sources, the
          demand for specific refined products, environmental policies, and the global oil market all contribute to this trend. This approach
          allows the U.S. to maximize economic efficiency and energy security by leveraging its robust and diverse refining infrastructure.
         """)

# 5 - Predictions for the next 12 months
st.header('Predictions for the next 12 months')
# Loading the dataset with historical data and predictions saved with pickle
with open('predictions.pkl', 'rb') as file:
    predictions = pickle.load(file)
# Showing the last 20 rows
st.write('The following dataset presents the latest historical data and predictions for the next 12 months.',predictions.tail(20))