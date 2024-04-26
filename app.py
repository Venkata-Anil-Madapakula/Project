import numpy as np
import pickle
import streamlit as st

# Define global dictionaries for mappings
Weather_conditions_dic = {'Cloudy': 0, 'Fog': 1, 'Sandstorms': 2, 'Stormy': 3, 'Sunny': 4, 'Windy': 5}
Road_traffic_density_dic = {'High ': 0, 'Jam ': 1, 'Low ': 2, 'Medium ': 3}
Type_of_order_dic = {'Buffet ': 0, 'Drinks ': 1, 'Meal ': 2, 'Snack ': 3}
Type_of_vehicle_dic = {'bicycle ': 0, 'electric_scooter ': 1, 'motorcycle ': 2, 'scooter ': 3}
Festival_dic = {'No ': 0, 'Yes ': 1}
City_dic = {'Metropolitian ': 0, 'Semi-Urban ': 1, 'Urban ': 2}

# Defing global dictionaries for mappings for non catagorical inputs user friendly
Vehicle_Condition_Classes = {0: 'Good', 1: 'Above avarage', 2: 'Avarage', 3: 'Poor'}
Month_Classes = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
week_end_classes = {'It is not weekend':0, 'It is weekend':1}
# Reverse the dictionary to map names to numerical values
Reverse_Vehicle_Condition_Classes = {v: k for k, v in Vehicle_Condition_Classes.items()}

with open('Model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('Scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

def predict(age, ratings, Weather, Road_traffic, vehicle_condition, Type_order, Type_vehicle, mul_deliveries, Festival, day_week, city,  
            day, Month, order_prepare_time, distance):
    
    # Convert categorical features to numerical values using the dictionaries
    weather_numeric = Weather_conditions_dic[Weather]
    road_traffic_numeric = Road_traffic_density_dic[Road_traffic]
    order_type_numeric = Type_of_order_dic[Type_order]
    vehicle_type_numeric = Type_of_vehicle_dic[Type_vehicle]
    festival_numeric = Festival_dic[Festival]
    city_numeric = City_dic[city]
    month = Month_Classes[Month]
    week_end = week_end_classes[day_week]

    # For the prediction, use the numerical value
    vehicle_condition_numeric = Reverse_Vehicle_Condition_Classes[vehicle_condition]

    # Create input array with the numerical values for the prediction input
    input_data = np.array([[age, ratings, weather_numeric, road_traffic_numeric, vehicle_condition_numeric, order_type_numeric, vehicle_type_numeric,
                            mul_deliveries, festival_numeric, week_end, city_numeric, day, month, order_prepare_time, distance]])

    # Scale the input data using the scaler
    input_df = scaler.transform(input_data)
    

    # Make prediction using the model
    return model.predict(input_df)[0]

if __name__ == '__main__':
    st.markdown(
    "<h1 style='text-align: center; background-color: #3498db; color: white; padding: 10px; margin-bottom: 20px;'>Food Delivery Time Prediction</h1>",
    unsafe_allow_html=True
)
    

    # Create a column layout to add the image alongside the prediction
    col1, col2 = st.columns([1, 1], gap='large')
    col1.markdown(
    "<h4 style='text-align: center; background-color: #3498db; color: white; padding: 10px; margin-bottom: 20px;'>Customer Level</h4>",
    unsafe_allow_html=True
)
    col2.markdown(
    "<h4 style='text-align: center; background-color: #3498db; color: white; padding: 10px; margin-bottom: 20px;'>Delivery Person Level</h4>",
    unsafe_allow_html=True
)
    order_type = col1.selectbox("Select the type of order", tuple(Type_of_order_dic.keys()))
    distance = col1.slider('Select the distance in meters', min_value=1, max_value=19709)
    month = col1.selectbox('Select the month', tuple(Month_Classes.keys()))
    day = col1.slider('Select the date', min_value=1, max_value=31)
    
    col1.markdown(
    "<h4 style='text-align: center; background-color: #3498db; color: white; padding: 10px; margin-bottom: 20px;'>Restaurant Level</h4>",
    unsafe_allow_html=True
)
    order_prepare_time = col1.slider("Select the time (min) for food preparation", min_value=5, max_value=15)
    festival = col1.selectbox("Select Festival (No/Yes)", tuple(Festival_dic.keys()))
    week_end= col1.selectbox("Select it is weekend or not", tuple(week_end_classes.keys()))
    age = col2.slider('Delivery Person age', min_value=18, max_value=50)
    ratings = col2.slider("Delivery Person rating", min_value=1.0, max_value=6.0)
    mul_deliveries = col2.selectbox("Select the multiple deliveries", (0, 1, 2, 3))
    city = col2.selectbox("Select the type of city", tuple(City_dic.keys()))
    weather = col2.selectbox("Select the type of weather condition", tuple(Weather_conditions_dic.keys()))
    road_traffic = col2.selectbox("Select the type of traffic condition", tuple(Road_traffic_density_dic.keys()))
    vehicle_type = col2.selectbox("Select the type of vehicle for food delivery", tuple(Type_of_vehicle_dic.keys()))
    vehicle_condition = col2.selectbox("Select the type of vehicle condition", tuple(Vehicle_Condition_Classes.values()))
    
    # Check if the entered day is valid for the entered month
    if (month == 'February' and day > 28) or ((month in ['April', 'June','September', 'November']) and day > 30):
        
        st.image('2.Not possible.png', use_column_width=True)

        # Display the predicted value in the streamlit(bottom of the page)
         
        st.warning(f'There  is  no  date {day}  in  month  {month}.  Please  enter  a  valid  date  and  month.')      
    else:
        # st.success(f'You selected day {day} in month {month}.')
        # Display the user inputs
       
        result = predict(age, ratings, weather, road_traffic, vehicle_condition, order_type, vehicle_type, mul_deliveries, festival,week_end, city,  
                day, month, order_prepare_time, distance)

        # Add an image to the second column (you need to specify the image URL)
        st.image('1.Result image.png', width=550)

        # Display the predicted value in the first column
        st.markdown(f"<p style='font-size:35px;'>Predicted time for food delivery: {round(result)} minutes</p>", unsafe_allow_html=True)
