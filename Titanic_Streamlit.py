import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go


st.set_page_config(layout="wide")


df = pd.read_csv('/Users/mohannedalsahaf/Desktop/Tuwaiq Data Science Bootcamp/titanic_cleaned_last.csv')
df = df.dropna(subset=['Embarked'])


df['Sex'] = df['Sex'].str.capitalize()
df['Survived'] = df['Survived'].map({0: 'Died', 1: 'Survived'})
df['Survived_num'] = df['Survived'].map({'Died': 0, 'Survived': 1})
df['Pclass'] = df['Pclass'].map({1: '1st Class', 2: '2nd Class', 3: '3rd Class'})
embark_map = {'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'}
df['Embarkation Port'] = df['Embarked'].map(embark_map)


st.sidebar.header("🔍 Filter Passengers")
gender_filter = st.sidebar.multiselect("Select Gender", df['Sex'].unique(), default=df['Sex'].unique())
survival_filter = st.sidebar.multiselect("Select Survival Status", df['Survived'].unique(), default=df['Survived'].unique())
class_filter = st.sidebar.multiselect("Select Ticket Class", df['Pclass'].unique(), default=df['Pclass'].unique())
age_min, age_max = int(df['Age'].min()), int(df['Age'].max())
age_filter = st.sidebar.slider("Select Age Range", age_min, age_max, (age_min, age_max))


filtered_df = df[
    (df['Sex'].isin(gender_filter)) &
    (df['Survived'].isin(survival_filter)) &
    (df['Pclass'].isin(class_filter)) &
    (df['Age'].between(age_filter[0], age_filter[1]))
]


route_data = pd.DataFrame({
    'Location': [
        'Belfast (Construction)', 'Southampton (Start)', 'Cherbourg', 'Queenstown',
        'Iceberg Warnings', 'Wreck Site', 'New-York City'
    ],
    'Latitude': [54.5973, 50.9097, 49.6333, 51.8494, 42.0, 41.7325, 40.7128],
    'Longitude': [-5.9301, -1.4044, -1.6167, -8.2944, -48.0, -49.9469, -74.0060]
})



st.title("🚢 Titanic EDA Dashboard")
st.markdown("Explore Titanic Data")


st.subheader("📌 Summary Metrics")
total_passengers = filtered_df.shape[0]
average_age = filtered_df['Age'].mean()
average_fare = filtered_df['Fare'].mean()
col1, col2, col3 = st.columns(3)
col1.metric("Total Passengers", f"{total_passengers}")
col2.metric("Average Age", f"{average_age:.1f} years")
col3.metric("Average Fare", f"${average_fare:.2f}")

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    lon=route_data['Longitude'],
    lat=route_data['Latitude'],
    mode='lines+markers+text',
    text=route_data['Location'],
    marker=dict(size=6, color='orange'),
    line=dict(width=2, color='yellow'),
    textposition='top center'
))


wreck = route_data[route_data['Location'] == 'Wreck Site']
fig.add_trace(go.Scattergeo(
    lon=wreck['Longitude'],
    lat=wreck['Latitude'],
    mode='markers+text',
    marker=dict(size=10, color='red', symbol='x'),
    text=["Wreck Site"],
    textposition='top center'
))


fig.update_layout(
    title='Titanic Journey Map',
    geo=dict(
        scope='world',
        projection_type='natural earth',
        showland=True,
        landcolor="rgb(230, 230, 230)",
        showocean=True,
        oceancolor="LightBlue",
        showcountries=True,
        lataxis_range=[30, 60],
        lonaxis_range=[-80, 10],
    ),
    height=600
)


st.subheader("🌍 Titanic Journey Route")
st.plotly_chart(fig, use_container_width=True)  


st.subheader("📈 Key Visuals")
vcol1, vcol2, vcol3 = st.columns(3)


with vcol1:
    gender_counts = filtered_df['Sex'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']
    gender_fig = px.bar(gender_counts, x='Gender', y='Count', color='Gender',
                        title="Gender Distribution",
                        color_discrete_map={'Female': 'hotpink', 'Male': 'deepskyblue'})
    st.plotly_chart(gender_fig, use_container_width=True)


with vcol2:
    survival_counts = filtered_df['Survived'].value_counts().reset_index()
    survival_counts.columns = ['Survival Status', 'Count']
    pie_fig = px.pie(survival_counts, names='Survival Status', values='Count',
                     title="Survival Rate",
                     color='Survival Status',
                     color_discrete_map={'Survived': 'green', 'Died': 'red'})
    st.plotly_chart(pie_fig, use_container_width=True)


with vcol3:
    class_counts = filtered_df['Pclass'].value_counts().reset_index()
    class_counts.columns = ['Ticket Class', 'Count']
    class_fig = px.bar(class_counts, x='Ticket Class', y='Count', color='Ticket Class',
                       title="Passengers per Class")
    st.plotly_chart(class_fig, use_container_width=True)


st.subheader("📊 Additional Insights")


fare_data = filtered_df.groupby(['Pclass', 'Sex'])['Fare'].mean().reset_index()
fare_fig = px.bar(fare_data, x='Pclass', y='Fare', color='Sex', barmode='group',
                  title="Fare by Class and Gender",
                  color_discrete_map={'Female': 'hotpink', 'Male': 'deepskyblue'})
st.plotly_chart(fare_fig, use_container_width=True)


age_fig = px.histogram(filtered_df, x='Age', color='Sex', nbins=30, marginal="box",
                       title="Age Distribution by Gender",
                       color_discrete_map={'Female': 'hotpink', 'Male': 'deepskyblue'})
st.plotly_chart(age_fig, use_container_width=True)


st.subheader("🔍 Deeper Passenger Insights")


st.markdown("### 🚻 Survival Rate by Class and Gender")
survival_by_class_gender = filtered_df.groupby(['Pclass', 'Sex', 'Survived']).size().reset_index(name='Count')
fig1 = px.bar(survival_by_class_gender, x='Pclass', y='Count', color='Survived',
              barmode='group', facet_col='Sex',
              title='Survival by Class and Gender',
              color_discrete_map={'Survived': 'green', 'Died': 'red'})
st.plotly_chart(fig1, use_container_width=True)


st.markdown("### 👨‍👩‍👧‍👦 Survival Based on Family Size")
filtered_df['FamilySize'] = filtered_df['SibSp'] + filtered_df['Parch'] + 1
fig2 = px.histogram(filtered_df, x='FamilySize', color='Survived', barmode='overlay',
                    nbins=10, title='Survival Count by Family Size',
                    color_discrete_map={'Survived': 'green', 'Died': 'red'})
st.plotly_chart(fig2, use_container_width=True)


st.markdown("### 🚢 Number of Passengers by Embarkation Port")
embark_counts = filtered_df['Embarkation Port'].value_counts().reset_index()
embark_counts.columns = ['Embarkation Port', 'Passenger Count']
fig3 = px.bar(embark_counts, x='Embarkation Port', y='Passenger Count', color='Embarkation Port',
              title='Passengers per Embarkation Port')
st.plotly_chart(fig3, use_container_width=True)


st.subheader("🧮 Correlation Heatmap")
numeric_df = df[['Age', 'Fare', 'SibSp', 'Parch','NumbericSex','Survived_num']].dropna()
corr = numeric_df.corr()
heatmap = ff.create_annotated_heatmap(
    z=corr.values,
    x=list(corr.columns),
    y=list(corr.index),
    annotation_text=corr.round(2).values,
    colorscale='Viridis'
)
st.plotly_chart(heatmap, use_container_width=True)


