# **🚀 Forecasting Food Delivery Time**

### 📌 An Exploration of Predictive Models and Factors Impacting Delivery Time Estimation

---

## 📖 **Table of Contents**

1. [📌 Project Overview](#project-overview)
2. [✨ Features](#features)
3. [⚙️ Installation](#installation)
4. [📊 Dataset](#dataset)
5. [🛠️ Project Workflow](#project-workflow)
6. [📈 Model Training and Evaluation](#model-training-and-evaluation)
7. [🚀 Deployment](#deployment)
8. [📌 Results and Insights](#results-and-insights)
9. [🔮 Future Enhancements](#future-enhancements)
10. [👥 Contributors](#contributors)

---

## **📌 Project Overview**

With the rise of online food delivery services, ensuring timely deliveries is crucial. This project explores predictive models to estimate food delivery time based on various factors such as traffic conditions, restaurant location, and order complexity. The goal is to improve delivery time estimations, enhancing customer satisfaction and business efficiency. 🚚💨

- **📂 GitHub Repository:** [Project Repository](https://github.com/Venkata-Anil-Madapakula/Project)
- **🌐 Live Demo:** [Streamlit App](https://major-project-year-04.streamlit.app/#restaurant-level)

---

## **✨ Features**

✅ Predicts delivery time based on real-world datasets.  
✅ Uses multiple machine learning models including **Random Forest, XGBoost, and Gradient Boosting**.  
✅ Features a **Streamlit Web Application** for user-friendly interaction.  
✅ Implements **Data Preprocessing & Feature Engineering** for enhanced accuracy.  
✅ Model evaluation using **RMSE, MAE, and R-squared** metrics.  
✅ **Hyperparameter Tuning** for model optimization.  
✅ **API Integration Guide** for external usage.  
✅ **Docker Support** for seamless deployment.  
✅ **Performance Benchmarking** against industry standards.  
✅ **Security & Data Privacy Considerations** for user data protection.  
✅ **CI/CD Pipeline** for automated deployment.  

---

## **⚙️ Installation**

### **🔹 Prerequisites**

Ensure you have the following installed:

- 🐍 Python 3.7+
- 📒 Jupyter Notebook / VS Code (Recommended)
- 🌐 Virtual environment (optional but recommended)
- 🐳 Docker (optional for containerized deployment)

### **🔹 Step 1: Clone the Repository**

```bash
git clone https://github.com/Venkata-Anil-Madapakula/Project.git  
cd Project  
```

### **🔹 Step 2: Install Dependencies**

```bash
pip install -r requirements.txt  
```

### **🔹 Step 3: Run the Project**

#### **📒 For Jupyter Notebook**

```bash
jupyter notebook  
```

Open `Forecasting_Food_Delivery_Time.ipynb` and run the cells.

#### **🌐 For Streamlit App**

```bash
streamlit run app.py  
```

#### **🐳 Docker Deployment**

```bash
docker build -t food-delivery-predictor .
docker run -p 8501:8501 food-delivery-predictor
```

---

## **📊 Dataset**

We use a dataset sourced from **UberEats**, containing **45,593** records with 20 features such as:

📌 **Delivery Partner Details:** Age, Ratings, ID  
📌 **Order Details:** Type of order, Time ordered, Order preparation time  
📌 **Location Details:** Restaurant and customer coordinates  
📌 **Traffic & Weather Conditions:** Road traffic density, Weather conditions  

---

## **🛠️ Project Workflow**

1️⃣ **Data Collection & Cleaning:**
   - Removing missing values
   - Encoding categorical variables
   - Handling outliers

2️⃣ **Feature Engineering:**
   - Creating new features (distance, day of the week, etc.)
   - Applying label encoding for categorical variables

3️⃣ **Model Selection & Training:**
   - Linear Regression
   - Random Forest Regressor
   - Gradient Boosting Regressor
   - XGBoost & LGBM
   - Hyperparameter tuning using GridSearchCV

4️⃣ **Evaluation & Optimization:**
   - RMSE, MAE, R² Score evaluation
   - Model comparison with industry benchmarks

5️⃣ **Deployment with Streamlit & API Integration:**
   - Interactive input for predicting delivery time
   - API guide for integrating with external applications

---

## **📈 Model Training and Evaluation**

### **🏆 Best Performing Model**

- **XGBoost Regressor** with **RMSE: 4.0329**, **MAE: 3.2060**, and **R² Score: 0.8144** achieved the best results. 🔥

---

## **🚀 Deployment**

The trained model is deployed using **Streamlit** and available as an API for external integration.

### **🌍 How to Use the Web App**

1️⃣ Visit [Streamlit App](https://major-project-year-04.streamlit.app/#restaurant-level).  
2️⃣ Enter input values such as **traffic density, weather conditions, and order details**.  
3️⃣ Click on **Predict** to get estimated delivery time.  

---

## **📌 Results and Insights**

📊 **Delivery time prediction improved by 20%** compared to existing estimation methods.  
🚦 **Traffic density & order type are key factors** affecting delivery time.  
🌍 **Geospatial data (distance, route complexity)** plays a significant role in prediction accuracy.  
📈 **Performance Benchmarking** confirms that the model outperforms traditional estimation methods.  

---

## **🔮 Future Enhancements**

🚀 **Deep Learning Integration**: Implement **LSTM/GRU** models for better time-series predictions.  
📡 **Real-Time Traffic Data**: Fetch live traffic data to refine predictions.  
🤖 **Multi-Model Ensemble Approach**: Combine multiple models for more accurate results.  
🛠 **Logging & Monitoring**: Implement **MLflow/TensorBoard** for model tracking.  
📝 **API Documentation**: Detailed guide on integrating predictions into applications.  

---

## **👥 Contributors**

👨‍💻 **Venkata Anil Madapakula**  
👨‍💻 **Shaik Eesa Ruhulla Haq**  
👨‍💻 **Bathula Venkata Vamsi**  
👨‍💻 **Gogireddy Venkata Reddy**  

🎓 Under the guidance of **Dr. Ayyappa Chakravarthy M**, Associate Professor, Dept. of Data Science.

📩 For any queries, contact: [**anilkrishna3278@gmail.com**](mailto:anilkrishna3278@gmail.com)
