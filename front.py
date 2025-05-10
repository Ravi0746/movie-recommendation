import streamlit as st 
import pickle 
import pandas as pd 
from streamlit_option_menu import option_menu
import re  
import os
import requests

st.set_page_config(
    page_title="Movie Recommendation",  
    page_icon="🍿",  
    layout="wide",  
)

def fetch(movie_id):
    res=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=325a7999fb4e89115d52e25d2d50f716".format(movie_id))
    d=res.json()
    return "https://image.tmdb.org/t/p/w500/"+d["poster_path"]
def recommend(movie):
        index=mov[mov["original_title"]==movie].index[0]
        distance = sim[index]
        list=sorted(enumerate(distance),reverse=True,key=lambda x:x[1])[1:11]
        
        recommend_movie=[]
        fetch_poster=[]
        for i in list :
            movie_id=mov.iloc[i[0]].id
            recommend_movie.append(mov.iloc[i[0]].original_title)
            fetch_poster.append(fetch(movie_id))
        return recommend_movie , fetch_poster
def validate_email(email):

    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

def validate_password(password):
    
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.match(password_regex, password)

def navigate_to(page):
    st.session_state.page = page

with st.sidebar:
    menu=option_menu("MENU",options=["Home 🎥", "About ℹ️","Login 🔓", "Create Account 📝", "Contact Us 🔑"],menu_icon=["shop-window"],icons=["house-fill","exclamation-lg","twitter","pen-fill","person-square"],styles={
            "container": {"padding": "5px", "background-color": "#0d0d0d"},
            "icon": {"color": "#f5c518", "font-size": "20px"},
            "nav-link": {"font-size": "18px", "margin": "5px 0px", "color": "red"},
            "nav-link-selected": {"background-color": "#EAC251", "color": "black", "border-radius": "10px"},
          })
text_colors = {
    "Home 🎥": "#f5c518",       
    "About ℹ️": "#2196F3",      
    "Login 🔓": "#FF5733",      
    "Create Account 📝": "#A569BD",  
    "Contact Us 🔑": "#4CAF50"  
}


text_color = text_colors.get(menu, "red")    
if menu=="Login 🔓":
    st.title("🎥 MOVIE RECOMMEND SYSTEM")
    st.title("Login 🔓") 
    text_color = "#f5c518"
    with st.form(key="Login 🔓"):
        email=st.text_input("Email")
        password=st.text_input("Password")
        btn=st.form_submit_button("Submit")
        if btn:
            if not validate_email(email):
                st.error("Invalid email format. Please enter a valid email.")
            elif not validate_password(password):
                st.error(
                    "Invalid password. Password must be at least 8 characters long, "
                    "contain one uppercase letter, one lowercase letter, and one digit."
                )
            else:
                st.success("Login successful!")
elif menu=="Home 🎥":
    #st.title("🎥 MOVIE RECOMMEND SYSTEM")
    mov=pickle.load(open("movie_dict2.pkl","rb"))
    sim=pickle.load(open("similarity.pkl","rb"))
    #mov=pd.DataFrame(mov)
    print(type(mov))
    col1, col2,col3 = st.columns([1,3,1])
    with col1:
       img=st.image("img.png",use_container_width=False,width=200,)
    with col2:
       #img=st.image("img.png",use_container_width=False,width=200,)
       st.write("\n" * 30)
       st.write("\n" * 13)
       #st.write("\n" * 9)
       st.markdown(""" <div style="position: absolute; top: 0.0; left: 25px; width: 100%;">
        <h1>🎥 MOVIE RECOMMEND SYSTEM</h1>
    </div>""", unsafe_allow_html=True)
    option=st.selectbox("chooose movie for recommendation",mov["original_title"].values)
    if st.button("Recommend"):
        names,poster=recommend(option)
        
        
        cols1 = st.columns(5)
        cols1[0].image(poster[0])
        cols1[0].header(names[0])
        cols1[1].image(poster[1])
        cols1[1].header(names[1])
        cols1[2].image(poster[2])
        cols1[2].header(names[2])
        cols1[3].image(poster[3])
        cols1[3].header(names[3])
        cols1[4].image(poster[4])
        cols1[4].header(names[4])


        cols2 = st.columns(5)
        cols2[0].image(poster[5])
        cols2[0].header(names[5])
        cols2[1].image(poster[6])
        cols2[1].header(names[6])
        cols2[2].image(poster[7])
        cols2[2].header(names[7])
        cols2[3].image(poster[8])
        cols2[3].header(names[8])
        cols2[4].image(poster[9])
        cols2[4].header(names[9])
        


       #st.markdown("<h1 style='font-size: 50px;'>🎥 MOVIE RECOMMEND SYSTEM</h1>", unsafe_allow_html=True)
       #st.markdown("# 🎥 MOVIE RECOMMEND SYSTEM")
    #col3, col4 = st.columns([2, 6])
    #with col4:
        
       #st.markdown("""" <div style="position: absolute; top: 0.0; right: 25px; width: 100%;">
        #<h1>🎥 MOVIE RECOMMEND SYSTEM</h1>
    #</div>""", unsafe_allow_html=True)
    #def recommend(movie):
        #index=data[data["original_title"]==movie].index[0]
        #distance = similarity[index]
        #list=sorted(enumerate(distance),reverse=True,key=lambda x:x[1])[1:11] 

    
    
    #import abiut
elif menu=="About ℹ️":
    st.title("About ℹ️")
    st.header("Welcome to the Movie Recommendation System! 🎬")
    st.markdown("This system is designed to help users discover movies based on their preferences. The recommendation algorithm uses multiple techniques to suggest movies that are likely to match the user’s tastes"
"Whether you're in the mood for a thrilling action film, a heartwarming drama, or a thought-provoking documentary, our system is here to guide you to the perfect movie.")
    
    st.header("How It Works")
    st.markdown("A recommendation system utilizes various filtering techniques to suggest movies:\n"
             "\n****Content-Based Filtering**** – This method analyzes movie features such as genre, director, actors, and descriptions. It then recommends movies similar to the ones a user has previously watched or rated highly.\n"
             "\n****Collaborative Filtering**** – This technique identifies users with similar tastes and recommends movies based on what others with similar preferences have liked.\n"
             "\n****Hybrid Approach**** – A combination of both methods ensures more accurate and diverse recommendations.")
    st.header("Benefits of a Movie Recommendation System")
    st.markdown("****Personalized Experience**** – Users receive recommendations based on their interests, making it easier to find movies they enjoy.\n"
                "\n****Time-Saving**** – Instead of browsing through thousands of movies, users get a curated list that matches their taste.\n"
                "\n****Business Growth**** – Streaming services like Netflix, Amazon Prime, and Disney+ use recommendation systems to increase watch time, customer retention, and overall revenue.\n"
                "\n****Enhanced Learning Experience**** – For developers, building a recommendation system helps in understanding data collection, preprocessing, feature engineering, machine learning models, and evaluation techniques.")
elif menu=="Create Account 📝":
    st.title("🎥 MOVIE RECOMMEND SYSTEM")
    with st.form(key="Create Account 📝"):
        st.title("Create Account 📝")
        user=st.text_input("Username",placeholder="Enter your Username.......")
        email=st.text_input("Email",placeholder="Enter Email.......")
        password=st.text_input(placeholder="Enter Password.......",label="password",type="password")
        st.checkbox("I agree to the Terms and Conditions")
        btn=st.form_submit_button("Create Account")
        
if menu == "Home 🎥":
    text_color = "#f5c518"  
    button_color = "#f5c518"  
    input_border_color = "#f5c518"  
    #content = "Welcome to the Home Page!"
elif menu == "About ℹ️":
    text_color = "#2196F3"  
    button_color = "#2196F3"  
    input_border_color = "#2196F3"  
    #content = "Learn more About Us here."
elif menu == "Login 🔓":
    text_color = "#FF5733"  
    button_color = "#FF5733"  
    input_border_color = "#FF5733"  
    #content = "Please Login to continue."
elif menu == "Create Account 📝":
    text_color = "#A569BD"  
    button_color = "#A569BD"  
    input_border_color = "#A569BD"  
    #content = "Create a new account to join us."
elif menu == "Contact Us 🔑":
    text_color = "#4CAF50"  
    button_color = "#4CAF50"  
    input_border_color = "#4CAF50"  
    content = None  


st.markdown(f"""
    <style>
    .main-text {{
        color: {text_color};
        font-size: 28px;
        font-weight: bold;
    }}
    .stButton > button {{
        background-color: {button_color};
        color: white;
        font-size: 18px;
        border-radius: 5px;
    }}
    .stTextInput input {{
        border: 2px solid {input_border_color};
        color: {text_color};
    }}
    .stTextArea textarea {{
        border: 2px solid {input_border_color};
        color: {text_color};
    }}
    .stTextInput label, .stTextArea label {{
        color: {text_color};
    }}
    </style>
    """, unsafe_allow_html=True)

#st.markdown(f'<p class="main-text">{menu} Page</p>', unsafe_allow_html=True)

# Handle Contact Us form
if menu == "Contact Us 🔑":
    st.title("📩 Contact Us")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Submit"):
        if name and email and message:
            st.success("✅ Your message has been sent!")
        else:
            st.error("❌ Please fill all fields before submitting.")


