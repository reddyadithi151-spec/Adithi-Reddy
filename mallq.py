import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MallMate - Smart Shopping Companion",
    page_icon="🛍️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #F8FAFC;
}
.header {
    font-size: 34px;
    font-weight: 700;
    color: #111827;
}
.subheader {
    font-size: 18px;
    color: #6B7280;
}
.offer-card {
    padding: 15px;
    border-radius: 15px;
    background: linear-gradient(135deg,#6366F1,#8B5CF6);
    color: white;
    margin-bottom: 10px;
}
.product-card {
    background: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    margin-bottom: 10px;
}
.review-box {
    background: #ffffff;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR PROFILE ----------------
with st.sidebar:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=100
    )
    st.title("👤 Profile")
    st.text_input("Username", "Adithi")
    st.text_input("Email", "adithi@example.com")
    st.button("Edit Profile")

# ---------------- BOTTOM NAVIGATION ----------------
page = st.radio(
    "",
    ["🏠 Home", "🔍 Search", "🗺️ Map", "❤️ Wishlist", "👤 Profile"],
    horizontal=True
)

# ---------------- SAMPLE DATA ----------------
products = pd.DataFrame({
    "Product": ["Nike Shoes", "Apple Watch", "Zara Jacket", "Samsung Buds"],
    "Store": ["Nike", "Imagine", "Zara", "Samsung"],
    "Price": [5999, 32999, 2499, 6999],
    "Available": ["Yes", "Yes", "Low Stock", "Yes"]
})

# ---------------- HOME ----------------
if page == "🏠 Home":

    st.markdown('<div class="header">🛍️ MallMate</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subheader">Your Smart Shopping Companion</div>',
        unsafe_allow_html=True
    )

    search = st.text_input("🔍 Search products, stores, brands...")

    st.subheader("🔥 Featured Offers")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="offer-card">
        <h3>Up to 50% OFF</h3>
        <p>Zara Summer Collection</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="offer-card">
        <h3>Buy 1 Get 1</h3>
        <p>Selected Nike Footwear</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("⭐ Personalized Recommendations")

    recommendations = [
        "Nike Air Max",
        "Apple AirPods",
        "Levi's Jeans",
        "Adidas Hoodie"
    ]

    for item in recommendations:
        st.markdown(
            f"<div class='product-card'>{item}</div>",
            unsafe_allow_html=True
        )

# ---------------- SEARCH ----------------
elif page == "🔍 Search":

    st.header("🔍 Product Search")

    query = st.text_input("Search Product")

    if query:
        results = products[
            products["Product"].str.contains(query, case=False)
        ]

        st.subheader("Search Results")
        st.dataframe(results, use_container_width=True)

    st.subheader("💰 Price Comparison")
    st.dataframe(products, use_container_width=True)

    st.subheader("📦 Product Availability Tracking")
    st.dataframe(
        products[["Product", "Store", "Available"]],
        use_container_width=True
    )

# ---------------- MAP ----------------
elif page == "🗺️ Map":

    st.header("🗺️ Interactive Mall Map")

    st.info(
        "Interactive navigation can be integrated using Mapbox or Indoor Mapping APIs."
    )

    st.image(
        "https://images.unsplash.com/photo-1519567241046-7f570eee3ce6",
        use_container_width=True
    )

    st.subheader("Store Directory")

    categories = {
        "Fashion": ["Zara", "H&M", "Levi's"],
        "Electronics": ["Apple", "Samsung", "Croma"],
        "Food": ["KFC", "Subway", "Starbucks"],
        "Sports": ["Nike", "Adidas", "Puma"]
    }

    selected = st.selectbox(
        "Choose Category",
        list(categories.keys())
    )

    st.write(categories[selected])

    st.subheader("📍 Indoor Navigation")

    start = st.selectbox(
        "Current Location",
        ["Entrance", "Food Court", "Level 1", "Level 2"]
    )

    destination = st.selectbox(
        "Destination Store",
        ["Nike", "Apple", "Zara", "Samsung"]
    )

    if st.button("Navigate"):
        st.success(
            f"Showing route from {start} to {destination}"
        )

# ---------------- WISHLIST ----------------
elif page == "❤️ Wishlist":

    st.header("❤️ Wishlist")

    wishlist = [
        "Apple Watch",
        "Nike Air Max",
        "Samsung Buds"
    ]

    for item in wishlist:
        st.markdown(
            f"<div class='product-card'>{item}</div>",
            unsafe_allow_html=True
        )

    st.subheader("📝 Shopping List Planner")

    shopping_item = st.text_input(
        "Add Item to Shopping List"
    )

    if shopping_item:
        st.success(f"{shopping_item} added to shopping list")

# ---------------- PROFILE ----------------
elif page == "👤 Profile":

    st.header("👤 User Profile")

    st.metric("Wishlist Items", 12)
    st.metric("Saved Stores", 5)
    st.metric("Offers Redeemed", 8)

    st.subheader("⭐ Store Ratings & Reviews")

    st.markdown("""
    <div class="review-box">
    <b>Nike Store</b><br>
    ⭐⭐⭐⭐⭐ Excellent service and collection.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="review-box">
    <b>Zara</b><br>
    ⭐⭐⭐⭐ Great discounts this season.
    </div>
    """, unsafe_allow_html=True)

# ---------------- AI SHOPPING ASSISTANT ----------------
st.divider()

st.subheader("🤖 AI Shopping Assistant")

user_msg = st.text_input(
    "Ask MallMate anything..."
)

if user_msg:
    st.chat_message("user").write(user_msg)

    response = (
        "I can help you find products, compare prices, "
        "locate stores, discover offers, and build your shopping list."
    )

    st.chat_message("assistant").write(response)

# ---------------- OFFERS NOTIFICATIONS ----------------
st.divider()

st.subheader("🔔 Real-Time Offers")

st.success("Nike: Extra 20% OFF for the next 2 hours")
st.info("Apple Store: Free accessories on selected products")
st.warning("Samsung: Limited stock on Galaxy Buds")