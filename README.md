This project involves performing hierarchical clustering on socioeconomic data from various countries. The clustering process helps visualize which countries have similar socioeconomic situations based on specific features.

## Project Description

The primary objective of this project is to process real-world socioeconomic data, implement hierarchical clustering, and visualize the clustering process. This project focuses on hierarchical agglomerative clustering (HAC), a method of cluster analysis that seeks to build a hierarchy of clusters.

## Data Description
Each country in the dataset is described by a row in a CSV file, containing the following six socioeconomic statistics:

  1. Population: Total population of the country.
  2. Net migration: The net number of people entering or leaving the country.
  3. GDP ($ per capita): Gross Domestic Product per capita.
  4. Literacy (%): Literacy rate of the population.
  5. Phones (per 1000): Number of phone lines per 1000 people.
  6. Infant mortality (per 1000 births): Number of infant deaths per 1000 live births.


## Clustering Process
The clustering process involves several key steps:

  1. Data Loading: Reading the data from a CSV file.
  2. Feature Calculation: Converting each country's data into a six-dimensional feature vector.
  3. Normalization: Normalizing the feature vectors to ensure that each feature contributes equally to the distance calculations.
  4. Hierarchical Clustering: Performing hierarchical agglomerative clustering using complete linkage to group countries based on socioeconomic similarity.
  5. Visualization: Creating a dendrogram to visualize the hierarchical clustering.

## Hierarchical Agglomerative Clustering (HAC)
HAC is a bottom-up clustering method where each observation starts in its cluster, and pairs of clusters are merged as one moves up the hierarchy. Complete linkage (or maximum linkage) is used, where the distance between two clusters is defined as the maximum distance between any single point in the first cluster and any single point in the second cluster.

The goal is to create a dendrogram, which is a tree diagram used to visualize the arrangement of the clusters produced by the clustering algorithm.

<img width="632" alt="Hierarchical-Clustering-of-Socioeconomic-Data-image" src="https://github.com/sumin910han/Hierarchical-Clustering-of-Socioeconomic-Data/assets/153245618/6c81281b-e0b6-493b-8ffa-b4cfc6387303">

