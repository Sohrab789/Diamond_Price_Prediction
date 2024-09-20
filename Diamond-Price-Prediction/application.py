import streamlit as st
from src1.pipelines.prediction_pipeline import CustomData, PredictPipeline

# Streamlit does not need an explicit application instance

# Home page (equivalent to Flask's index.html)
st.title("Diamond Price Prediction")

# Sidebar or main page form
st.header("Enter the Diamond Details for Prediction")

# Create input fields similar to form.html in Flask
carat = st.number_input('Carat', min_value=0.0, max_value=10.0, value=1.0, step=0.01)
depth = st.number_input('Depth', min_value=0.0, max_value=100.0, value=61.0, step=0.1)
table = st.number_input('Table', min_value=0.0, max_value=100.0, value=55.0, step=0.1)
x = st.number_input('X Dimension (mm)', min_value=0.0, max_value=20.0, value=5.0, step=0.01)
y = st.number_input('Y Dimension (mm)', min_value=0.0, max_value=20.0, value=5.0, step=0.01)
z = st.number_input('Z Dimension (mm)', min_value=0.0, max_value=20.0, value=3.0, step=0.01)

cut = st.selectbox('Cut Quality', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox('Color Grade', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
clarity = st.selectbox('Clarity Grade', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

# Button to trigger prediction
if st.button('Predict Price'):
    # Collect the data into CustomData class
    data = CustomData(
        carat=carat,
        depth=depth,
        table=table,
        x=x,
        y=y,
        z=z,
        cut=cut,
        color=color,
        clarity=clarity
    )
    
    # Convert data to DataFrame
    final_new_data = data.get_data_as_dataframe()
    st.write("Final Data for Prediction:", final_new_data)
    # Initialize the prediction pipeline and get prediction
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(final_new_data)
    
    # Display the result
    st.success(f'Predicted Diamond Price: ${round(pred[0], 2)}')
