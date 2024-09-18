### Diamond_Price_Prediction 💍

#### Overview

Diamond_Price_Prediction is an open-source project that enables you to predict diamond prices based on various attributes. With advanced machine learning models and a user-friendly web application, this project provides a reliable solution for estimating diamond prices.

![Diamond Image](https://wtamu.edu/~cbaird/sq/images/diamond_art.png)

#### Table of Contents 

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Technologies Used](#technologies-used)
- [Contributions](#contributions)


### Introduction 🌟

Welcome to Diamond_Price_Prediction! This project is designed to assist you in estimating the prices of diamonds based on their attributes. Whether you're a gem enthusiast or a jeweler, our project offers a reliable way to predict diamond prices.

### Features 🚀

##### Data Ingestion and Transformation 📊

We've introduced robust data ingestion and transformation components to preprocess raw data efficiently. This ensures data quality and reliability in our predictive models.

![Data Transformation](https://www.getdbt.com/ui/img/blog/data_transformation.png)

### Advanced Machine Learning Models 🤖

Our project now incorporates advanced machine learning models for diamond price prediction. These models offer improved accuracy and generalization.

#### Web Application 🌐

We are thrilled to present our web-based user interface for easy input and prediction of diamond prices. You can now interact with our model through a user-friendly web application.

- **Input Form:** Users can input various attributes of a diamond, including carat, depth, table, dimensions (x, y, z), cut, color, and clarity.
- **Machine Learning Prediction:** The application uses a trained machine learning model to predict the price of the diamond based on the provided attributes.
- **User-Friendly Interface:** The web app features an attractive and intuitive interface, making it easy for users to enter data and receive predictions.
- **Background Image:** The app uses a captivating background image to enhance the visual appeal and engagement of users.

### Getting Started 🛠️

The dataset used in the Diamond Price Prediction Web App project is a collection of diamond attributes and their corresponding prices. The dataset is utilized to train a machine learning model that can predict the price of a diamond based on its various characteristics. The dataset provides a valuable resource for understanding the relationships between diamond attributes and their market values.

#### Attributes in the Dataset:

- `carat`: Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
- `cut`: Quality of Diamond Cut.
- `color`: Color of Diamond.
- `clarity`: Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
- `depth`: The depth of the diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface).
- `table`: A diamond's table is the facet that can be seen when the stone is viewed face up.
- `x`: Diamond X dimension.
- `y`: Diamond Y dimension.
- `z`: Diamond Z dimension.

![Diamond Anatomy](https://github.com/BahramJannesar/DiamondsMachineLearning/raw/master/Image/Anglo-DiamondAnatomy_03.jpg)


### Prerequisites 📋

Before using this project, ensure you have the following prerequisites in place:

- Python (3.7 or higher)
- Required dependencies (install with `pip install -r requirements.txt`)
- Access to a web browser 🌐

### Technologies Used:

- Front-End: HTML, CSS
- Back-End: Python (Flask framework)
- Machine Learning: Linear Regression, Lasso Regression, Ridge Regression, Decision Tree

### Installation 💻

##### Step 1 - Clone the repository to your local machine using Git:

```bash
git clone https://github.com/Adi3042/Diamond-Price-Prediction.git
cd Diamond-Price-Prediction
```

##### Step 2 - Create a conda environment after opening the repository

```bash
conda create -p venv python==3.8
conda activate venv/
```

##### Step 3 - Install the requirements

Open your terminal and execute the following command:

```bash
pip install -r requirements.txt
```

##### Step 4 - Run the application server

Open your terminal and execute the following command:

```bash
python application.py
```

##### Step 5 -

1. Visit the web app. :- http://127.0.0.1:5000/
2. Enter the attributes of the diamond in the input form.
3. Click the "Predict" button.
4. Receive the predicted price of the diamond.

### Contributions:

Contributions to this project are welcome! If you have ideas for improvement, bug fixes, or additional features, feel free to create a pull request or open an issue.
