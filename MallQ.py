import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------
# PAGE CONFIG
# ----------------------

st.set_page_config(
    page_title="MallMate",
    page_icon="🛍️",
    layout="wide"
)

# ----------------------
# SAMPLE DATA
# ----------------------

products = pd.DataFrame({
    "Product": [
        "Nike Air Max",
        "Adidas Ultraboost",
        "iPhone 16",
        "Samsung S25",
        "Levi's Jeans",
        "Zara Jacket"
    ],
    "Store": [
        "Nike Store",
        "Adidas Store",
        "Apple Store",
        "Samsung Store",
        "Levi's",
        "Zara"
    ],
    "Price": [
        8999,
        9999,
        79999,
        74999,
        2999,
        4999
    ],
    "Offer": [
        "10% OFF",
        "15% OFF",
        "Free AirPods",
        "₹3000 Cashback",
        "20% OFF",
        "Buy 2 Get 1"
    ],
    "Floor": [
        "Ground",
        "Ground",
        "First",
        "First",
        "Second",
        "Second"
    ]
})

# ----------------------
# HEADER
# ----------------------

st.markdown("""
<h1 style='text-align:center; color:#ff4b4b;'>
🛍️ MallMate
</h1>
<h4 style='text-align:center;'>
Find Products • Compare Prices • Discover Deals
</h4>
""", unsafe_allow_html=True)

st.divider()

# ----------------------
# SIDEBAR
# ----------------------

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3081/3081559.png",
    width=120
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose Feature",
    [
        "🏠 Home",
        "🔍 Product Search",
        "📍 Store Locator",
        "💸 Price Comparison",
        "🎁 Offers",
        "🤖 AI Recommendations"
    ]
)

# ----------------------
# HOME
# ----------------------

if page == "🏠 Home":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Stores Connected", "120+")

    with col2:
        st.metric("Products Available", "15,000+")

    with col3:
        st.metric("Today's Deals", "250+")

    st.image(
        "https://images.unsplash.com/photo-1483985988355-763728e1935b",
        use_container_width=True
    )

    st.success(
        "Welcome to MallMate! Search products across all stores in one place."
    )

# ----------------------
# PRODUCT SEARCH
# ----------------------

elif page == "🔍 Product Search":

    st.subheader("Search Products")

    search = st.text_input(
        "What are you looking for?"
    )

    if search:

        result = products[
            products["Product"].str.contains(
                search,
                case=False
            )
        ]

        if len(result) > 0:
            st.dataframe(result, use_container_width=True)
        else:
            st.warning("No products found.")

# ----------------------
# STORE LOCATOR
# ----------------------

elif page == "📍 Store Locator":

    st.subheader("Store Locator")

    store = st.selectbox(
        "Choose Store",
        products["Store"].unique()
    )

    selected = products[
        products["Store"] == store
    ]

    floor = selected.iloc[0]["Floor"]

    st.success(
        f"{store} is located on the {floor} Floor"
    )

    st.map(
        pd.DataFrame({
            "lat":[17.4435],
            "lon":[78.3772]
        })
    )

# ----------------------
# PRICE COMPARISON
# ----------------------

elif page == "💸 Price Comparison":

    st.subheader("Compare Product Prices")

    chart = px.bar(
        products,
        x="Product",
        y="Price",
        color="Store",
        title="Product Price Comparison"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )

# ----------------------
# OFFERS
# ----------------------

elif page == "🎁 Offers":

    st.subheader("Today's Best Offers")

    for _, row in products.iterrows():

        st.info(
            f"🏪 {row['Store']} | "
            f"🛍️ {row['Product']} | "
            f"🎉 {row['Offer']}"
        )

# ----------------------
# AI RECOMMENDATIONS
# ----------------------

elif page == "🤖 AI Recommendations":

    st.subheader("Smart Shopping Assistant")

    budget = st.slider(
        "Select Budget",
        1000,
        100000,
        10000
    )

    recommendations = products[
        products["Price"] <= budget
    ]

    st.write(
        "Recommended Products:"
    )

    st.dataframe(
        recommendations,
        use_container_width=True
    )

    if st.button("✨ Get Smart Suggestion"):

        if budget > 50000:
            st.success(
                "Recommended: iPhone 16 📱"
            )
        elif budget > 10000:
            st.success(
                "Recommended: Adidas Ultraboost 👟"
            )
        else:
            st.success(
                "Recommended: Levi's Jeans 👖"
            )

        st.balloons()

# ----------------------
# FOOTER
# ----------------------

st.divider()

st.markdown(
    "<center>Made with ❤️ for Smart Mall Shopping</center>",
    unsafe_allow_html=True
)
