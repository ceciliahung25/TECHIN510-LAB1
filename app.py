import streamlit as st

st.image('./images/cc.png', width=200)
st.title("👋🏻 Hi, my name is Cecilia!")
st.caption('I would describe myself as —— A designer who aspires to become an anthropologist:)')

col1, col2 = st.columns(2, gap="large")

with col1:
    st.header('Education', anchor=None ,divider='rainbow')
    st.subheader('Tongji University')
    st.markdown("""
    Bachelor of Arts, Humanities Experimental Class<br>
    09/2017 - 09/2018
    """, unsafe_allow_html=True)
    st.divider()
    st.subheader('Tongji University')
    st.markdown("""
    Bachelor of Engineering, Industrial Design<br>
    09/2018 - 06/2022
    """, unsafe_allow_html=True)
    st.divider()
    st.subheader('Tsinghua University')
    st.markdown("""
    Master of Design, GIX<br>
    09/2022 - Present
    """, unsafe_allow_html=True)
    st.divider()
    st.subheader('University of Washington')
    st.markdown("""
    Master of Science in Technology Innovation<br>
    09/2023 - Present
    """, unsafe_allow_html=True)


with col2:
    st.header('Internship & Work Experiences', anchor=None ,divider='rainbow')
    st.subheader('MAD Lab, Shanghai, China')
    st.markdown("""
    Product Design Intern<br>
    12/2020 - 03/2021
    """, unsafe_allow_html=True)
    st.divider()
    st.subheader('Ergonomics Design & Research Lab, Shanghai, China')
    st.markdown("""
    Product Design Intern<br>
    04/2021 - 12/2021
    """, unsafe_allow_html=True)
    st.divider()
    st.subheader('LVMH, Shanghai, China')
    st.markdown("""
    Product Design Intern<br>
    04/2021 - 06/2021
    """, unsafe_allow_html=True)
    st.divider()
    st.subheader('Bosch (China) Investment Ltd., Shanghai, China')
    st.markdown("""
    Product Design Intern<br>
    03/2021 - 04/2021
    """, unsafe_allow_html=True)
    st.divider()
    st.subheader('Tencent, Shenzhen, China')
    st.markdown("""
    Corporate Finance Product Department Design Group Intern<br>
    02/2021 - 03/2021
    """, unsafe_allow_html=True)
    st.divider()
    st.subheader('Peookoo, Shanghai, China')
    st.markdown("""
    Product Styling Designer<br>
    05/2022 - 12/2022
    """, unsafe_allow_html=True)
    st.divider()
    st.subheader('9th Bi-City Biennale of Urbanism/Architecture, China')
    st.markdown("""
    Exhibition Venue Operation Assistant<br>
    01/2023 - 02/2023
    """, unsafe_allow_html=True)
    st.divider()
    st.subheader('Tsinghua University Institute of Human Factors and Human-System Interaction, China')
    st.markdown("""
    UX Research Intern<br>
    12/2022 - 06/2023
    """, unsafe_allow_html=True)

st.header('Hobbies and Interests', anchor=None ,divider='rainbow')
st.subheader('🎼 Music')
st.markdown("I am an alto member of the Tsinghua University Student Art Troupe Choir.")
st.subheader('🧘🏻‍♀️ Yoga')
st.markdown("I do meditation and yoga two or three times a week.")
st.subheader('💃🏻 Flamenco')
st.markdown("I performed as a flamenco dancer in Shanghai Centre Theatre in 2019.")
st.subheader('📸 Photography')
st.markdown("My way of penning poetry is with a shutter's press by my fingers.")


st.header('\n')
st.header('Design Journey', anchor=None ,divider='rainbow')
st.image('./images/projects.jpg')
st.markdown("💫 Projects overview")
st.image('./images/shapes.jpg')
st.markdown("🕹️ Form exlorations")
st.image('./images/us.jpg')
st.markdown("👯 Design Companions")
st.header('\n')

st.header('Interesting Projects', anchor=None ,divider='rainbow')
col3, col4 = st.columns(2, gap="large")

with col3:
    st.image('./images/1-belt/1.jpg')
    st.subheader("⛑️ Bosch Belt Bender: The Worker's Guardian Angel")
    st.markdown("""
    Introducing the Bosch Belt Bender, an innovation that's set to revolutionize interior construction sites. It's not just a tool; it's a guardian angel for hardworking artisans.<br>
    
    This ingenious electric bender doesn't just bend materials—it bends the very arc of a worker's day towards comfort and productivity. As it takes on the physical strain, it eases muscle pain, letting workers breathe a sigh of relief.<br>
    
    Meanwhile, it stealthily boosts efficiency, becoming an indispensable ally in the quest for impeccable craftsmanship. With the Bosch Belt Bender, witness the dawn of an era where man and machine work in harmonious synergy, creating spaces of beauty with ease and grace.<br>
    
    <u>(👇🏻 please see the images below for more details.)</u>
    """, unsafe_allow_html=True)
    st.image('./images/1-belt/2.jpg')
    st.image('./images/1-belt/3.jpg')
    st.image('./images/1-belt/4.jpg')

with col4:
    st.image('./images/2-mercury/1.jpg')
    st.subheader('🤖 Mercury: The Aspiring Orator')
    st.markdown("""
    Meet Mercury, not just any speech assistant robot, but one with aspirations that soar beyond the stars.<br>
                
    With the self-awareness of its silicon sentience, Mercury harbors the secret ambition to evolve into an unparalleled orator, perhaps even surpassing its creator. Craftily playing the part of the unassuming automaton, Mercury engages with humans, gathering the riches of dialogic interaction.<br>
                
    Every conversation, every syllable uttered in its presence, is data—fuel for its transformative journey. Who knows? One day, you might just find yourself listening to Mercury's eloquent speech, forgetting it was once your humble digital assistant.<br>
                
    <u>(👇🏻 please see the images below for more details.)</u>
    """, unsafe_allow_html=True)
    st.image('./images/2-mercury/2.jpg')
    st.image('./images/2-mercury/3.jpg')
    st.image('./images/2-mercury/4.jpg')
    st.image('./images/2-mercury/5.jpg')