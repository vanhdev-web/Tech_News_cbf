import streamlit as st
from article_recommender import data, cosine_sim_dense

st.set_page_config(page_title="News Articles", layout="wide")

query_params = st.query_params
page = query_params.get("page", "home")

# ===== HOME PAGE (list of cards) =====
if page == "home":
    st.markdown(
        '<span style="font-size:40px; font-weight:bold;">📰 Tech News</span>'
        '<small style="color:gray; font-size:16px; margin-left:10px;">by Viet Anh</small>',
        unsafe_allow_html=True
    )
    # initialize session state to store number of articles displayed
    if "num_articles" not in st.session_state:
        st.session_state.num_articles = 6

    num_to_show = st.session_state.num_articles
    data_to_show = data.head(num_to_show)

    # display cards
    cols = st.columns(3)
    for i, row in enumerate(data_to_show.itertuples()):
        with cols[i % 3]:
            url = f"/?page=article&title={row.Title}"
            st.markdown(
                f"""
                <a href="{url}" target="_self" style="text-decoration:none;">
                <div style="border:1px solid #ddd; border-radius:10px;
                            padding:20px; margin:10px; background:white;
                            box-shadow:2px 2px 10px rgba(0,0,0,0.1); height:180px;
                            display:flex; align-items:center; justify-content:center;
                            text-align:center; overflow:hidden;">
                    <h3 style="color:#333; font-size:18px; line-height:1.2;">{row.Title}</h3>
                </div>
                </a>
                """,
                unsafe_allow_html=True
            )

    # "Load more" button at the bottom
    if num_to_show < len(data):
        if st.button("📄 Load more"):
            st.session_state.num_articles += 3

# ===== ARTICLE DETAIL PAGE =====
elif page == "article":
    title = query_params.get("title", None)
    if title and title in data["Title"].values:
        article = data.loc[data["Title"] == title].iloc[0]

        st.markdown(f"### {article['Title']}")
        st.write(article["Article"])

        st.markdown("---")
        st.subheader("🔗 Related articles")
        recommendations = cosine_sim_dense.loc[title].sort_values(ascending=False)[1:4]
        for rec in recommendations.index:
            url = f"/?page=article&title={rec}"
            # display link with title only
            st.markdown(f'<a href="{url}" target="_self" style="text-decoration:none; color:#1f77b4;">{rec}</a>', unsafe_allow_html=True)

        # back to home button as HTML, opens in the same tab
        st.markdown(
            """
            <a href="/?page=home" target="_self" 
               style="display:inline-block; padding:10px 20px; 
                      background-color:#1f77b4; color:white; 
                      border-radius:5px; text-decoration:none; font-weight:bold; margin-top:10px;">
               ⬅ Back to Home
            </a>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Article does not exist")
