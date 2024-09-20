from setuptools import find_packages, setup

setup(
    name="diamond_price_prediction",
    version="0.0.1",
    author="Sohrab Ali",
    author_email="modsohrabali@gmail.com",
    packages=find_packages(),
    install_requires=["streamlit",
        "pandas",
        "scikit-learn",
        "matplotlib"],
    python_requires=">=3.8",
)

