from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def customer_clustering(df):
    cluster_df = df.groupby('Customer ID').agg({
        'Sales':['sum','mean','count']
    })

    cluster_df.columns = ['total','avg','orders']

    scaler = StandardScaler()
    scaled = scaler.fit_transform(cluster_df)

    kmeans = KMeans(n_clusters=3, random_state=42)
    cluster_df['cluster'] = kmeans.fit_predict(scaled)

    return cluster_df