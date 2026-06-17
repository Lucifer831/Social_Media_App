import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Social Media App", page_icon=":camera:", layout="centered")

st.title("Social Media App")
st.caption("Upload posts, browse the feed, and delete posts from your FastAPI backend.")


def api_url(path: str) -> str:
    return f"{API_URL}{path}"


def load_feed():
    response = requests.get(api_url("/feed"), timeout=10)
    response.raise_for_status()
    return response.json().get("posts", [])


with st.sidebar:
    st.header("Backend")
    backend_url = st.text_input("API URL", value=API_URL)
    if backend_url:
        API_URL = backend_url.rstrip("/")
    if st.button("Refresh feed", use_container_width=True):
        st.rerun()

tab_upload, tab_feed = st.tabs(["Upload", "Feed"])

with tab_upload:
    st.subheader("Create post")
    caption = st.text_input("Caption", placeholder="Write something...")
    file = st.file_uploader("Choose an image or video", type=["jpg", "jpeg", "png", "webp", "gif", "mp4", "mov"])

    if st.button("Upload post", type="primary", use_container_width=True):
        if not file:
            st.warning("Please choose a file first.")
        elif not caption.strip():
            st.warning("Please add a caption.")
        else:
            files = {"file": (file.name, file.getvalue(), file.type or "application/octet-stream")}
            data = {"caption": caption.strip()}

            try:
                with st.spinner("Uploading..."):
                    response = requests.post(api_url("/upload"), files=files, data=data, timeout=60)
                    response.raise_for_status()
                st.success("Post uploaded successfully.")
                st.json(response.json())
            except requests.RequestException as exc:
                st.error(f"Upload failed: {exc}")
                if getattr(exc, "response", None) is not None:
                    st.code(exc.response.text)

with tab_feed:
    st.subheader("Feed")

    try:
        posts = load_feed()
    except requests.RequestException as exc:
        st.error(f"Could not load feed: {exc}")
        posts = []

    if not posts:
        st.info("No posts yet.")

    for post in posts:
        post_id = post.get("id")
        caption = post.get("caption", "")
        url = post.get("url", "")
        file_type = post.get("file_type", "")
        created_at = post.get("created_at", "")

        with st.container(border=True):
            st.markdown(f"**{caption}**")
            if created_at:
                st.caption(str(created_at))

            if url:
                if str(file_type).startswith("video"):
                    st.video(url)
                else:
                    st.image(url, use_container_width=True)

            st.caption(post.get("file_name", ""))

            if st.button("Delete", key=f"delete-{post_id}", use_container_width=True):
                try:
                    response = requests.delete(api_url(f"/posts/{post_id}"), timeout=10)
                    response.raise_for_status()
                    result = response.json()
                    if result.get("success"):
                        st.success("Post deleted.")
                        st.rerun()
                    else:
                        st.warning(result.get("message", "Could not delete post."))
                except requests.RequestException as exc:
                    st.error(f"Delete failed: {exc}")
