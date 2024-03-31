import streamlit as st
from st_social_media_links import SocialMediaIcons

# Example usage
social_media_links = [
    "https://www.facebook.com/ThisIsAnExampleLink",
    "https://www.youtube.com/ThisIsAnExampleLink",
    "https://www.instagram.com/ThisIsAnExampleLink",
    "https://github.com/jlnetosci/st-social-media-links",
]

#colors = ["#000000", None, "SteelBlue", None]

social_media_icons = SocialMediaIcons(
    social_media_links, 
    #colors
    )

social_media_links2 = [
    "https://www.tiktok.com/ThisIsAnExampleLink",
    "https://www.linkedin.com/ThisIsAnExampleLink",
    "https://www.twitch.com/ThisIsAnExampleLink",
    "https://www.pinterest.com/ThisIsAnExampleLink",
]

social_media_icons2 = SocialMediaIcons(social_media_links2)

st.title("Streamlit Social Media Links!")

st.markdown("""<div style="text-align: justify;">This is an example page for the <a href="https://" target="_blank"><code>st-social-media-links</code> package </a>. If you are interested you can also read our <a href="https://www.github.com/jlnetosci/ssml" target="_blank">documentation</a>.</div><p>""", unsafe_allow_html=True)

st.markdown("""<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ut vehicula lacus. Nunc varius nisi sit amet interdum mollis. Ut eleifend aliquam elit. Proin lobortis sit amet nisl sed euismod. Integer pharetra porttitor rutrum. Cras sed imperdiet dui. Nam in dui orci. Etiam rutrum dolor eget aliquam bibendum. Pellentesque massa est, scelerisque facilisis mollis sed, pellentesque vitae tortor. Sed volutpat dignissim turpis et ullamcorper. Aliquam sed nibh volutpat magna scelerisque malesuada. Nam dapibus est ac nisl imperdiet, ac egestas lorem bibendum. Vivamus placerat purus at quam imperdiet, sed ullamcorper neque dapibus. <p><p>
Ut sem odio, mattis eget magna nec, facilisis auctor nunc. Praesent tempor erat turpis, ut vulputate orci eleifend id. Praesent placerat sem ut mattis ornare. Nullam cursus justo eget nisl maximus blandit. Nullam non enim nec justo fermentum venenatis non in justo. Donec hendrerit ipsum id mauris blandit scelerisque. Donec scelerisque consequat venenatis. Duis sodales lectus eu risus condimentum, at volutpat neque porta. Mauris pellentesque orci pulvinar convallis pellentesque. Quisque rutrum mauris et magna lacinia tincidunt. Quisque a consectetur sem. Vestibulum purus magna, congue nec nisi sed, lobortis hendrerit enim. Curabitur imperdiet sodales dui et volutpat. Fusce fermentum eu dolor ut sodales. Phasellus eros velit, porta sed hendrerit lobortis, lacinia sed nunc. Sed libero leo, sollicitudin id mi vitae, ullamcorper tempor turpis.</div>""", unsafe_allow_html=True)

st.divider()
social_media_icons.render(sidebar=False, justify_content="center")
st.write("")

with st.expander("See code"):
    st.code("""social_media_links = [
        "https://www.facebook.com/ThisIsAnExampleLink",
        "https://www.youtube.com/ThisIsAnExampleLink",
        "https://www.instagram.com/ThisIsAnExampleLink",
        "https://github.com/jlnetosci/st-social-media-links",
        ]

        social_media_icons = SocialMediaIcons(social_media_links) 

        social_media_icons.render(sidebar=False, justify_content="center")
        """, language='python')

st.sidebar.title("Streamlit Social Media Links Sidebar!")

st.sidebar.markdown("""<div style="text-align: justify;">Nulla facilisi. Donec eu eleifend nibh. Ut aliquam rhoncus semper. Nullam fringilla aliquam justo, a vestibulum massa congue eget. Vivamus urna urna, accumsan vel magna non, hendrerit volutpat leo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Interdum et malesuada fames ac ante ipsum primis in faucibus. </div>""", unsafe_allow_html=True)
st.sidebar.divider()
social_media_icons.render(sidebar=True, justify_content="center")
st.sidebar.write("")
with st.sidebar.expander("See code"):
    st.code("""social_media_links = [
        "https://www.facebook.com/ThisIsAnExampleLink",
        "https://www.youtube.com/ThisIsAnExampleLink",
        "https://www.instagram.com/ThisIsAnExampleLink",
        "https://github.com/jlnetosci/st-social-media-links",
        ]

        social_media_icons = SocialMediaIcons(social_media_links) 

        social_media_icons.render(sidebar=True, justify_content="center")
        """, language='python')

st.sidebar.divider()
st.sidebar.markdown("""<div style="text-align: justify;">Praesent interdum, lacus ac malesuada suscipit, turpis ligula tincidunt mi, eu suscipit tortor nibh nec ligula. In diam erat, tristique tempus leo a, egestas tristique nisl. Vivamus euismod sodales lorem, vel ultrices urna laoreet in. Maecenas dapibus nibh nulla, id consectetur risus vehicula vel. Aenean ex turpis, imperdiet ac commodo non, rhoncus quis dolor. In ut tempus lacus.</div>""", unsafe_allow_html=True)

st.sidebar.divider()
social_media_icons2.render(sidebar=True, justify_content="space-evenly")
st.sidebar.write("")
with st.sidebar.expander("See code"):
    st.code("""social_media_links2 = [
        "https://www.tiktok.com/ThisIsAnExampleLink",
        "https://www.linkedin.com/ThisIsAnExampleLink",
        "https://www.twitch.com/ThisIsAnExampleLink",
        "https://www.pinterest.com/ThisIsAnExampleLink",
        ]

        social_media_icons2 = SocialMediaIcons(social_media_links2) 

        social_media_icons2.render(sidebar=True, justify_content="space-evenly")
        """, language='python')
