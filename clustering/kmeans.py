from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


def elbow_method(df):

    X = df[["Annual_Income", "Spending_Score"]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    wcss = []

    for i in range(1, 11):

        model = KMeans(
            n_clusters=i,
            random_state=42,
            n_init=10
        )

        model.fit(X_scaled)

        wcss.append(model.inertia_)

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=list(range(1, 11)),

            y=wcss,

            mode="lines+markers",

            name="WCSS"

        )

    )

    fig.update_layout(

        title="Elbow Method",

        xaxis_title="Number of Clusters (K)",

        yaxis_title="WCSS",

        template="plotly_white",

        height=500

    )

    return pio.to_html(
        fig,
        full_html=False
    )


def perform_clustering(df, n_clusters=5):

    X = df[["Annual_Income", "Spending_Score"]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    df["Cluster"] = model.fit_predict(X_scaled)

    cluster_names = {
        0: "VIP Customers",
        1: "Careful Customers",
        2: "Potential Customers",
        3: "Budget Customers",
        4: "Average Customers"
    }

    df["Segment"] = df["Cluster"].map(cluster_names)

    fig = px.scatter(

        df,

        x="Annual_Income",

        y="Spending_Score",

        color=df["Cluster"].astype(str),

        title="Customer Segments",

        labels={"color": "Cluster"}

    )

    fig.update_layout(

        template="plotly_white",

        height=600

    )

    return df, pio.to_html(fig, full_html=False)

def cluster_summary(df):

    summary = (
        df.groupby("Segment")
          .size()
          .reset_index(name="Customers")
    )

    return summary