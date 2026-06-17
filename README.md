# 📱 Social Media App

A simple full-stack social media application where users can create posts, upload images or videos, browse the feed, refresh posts, and delete posts.

---

## 📌 Project Overview

This project demonstrates how a frontend application communicates with a backend API to manage social media-style posts. The app includes a clean user interface for uploading media with captions and a backend service for storing, fetching, and deleting posts.

---

## ✨ Features

- 📝 Create posts with captions
- 🖼️ Upload images and videos
- 📰 View all posts in a feed
- 🔄 Refresh the feed
- 🗑️ Delete posts
- 🔗 Backend API integration
- ☁️ Media upload and storage support

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| Database | MongoDB |
| Media Storage | ImageKit |

---

## ⚙️ How It Works

The **frontend** is built with Streamlit and provides the user interface for creating and viewing posts.

The **backend** is built with FastAPI and handles API routes such as uploading posts, fetching the feed, and deleting posts.

**MongoDB** is used to store post data, while **ImageKit** is used for media file handling (image/video upload and hosting).

---

## 🔌 Main API Functionality

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/upload` | Upload a new post with caption and media |
| `GET` | `/feed` | Fetch all uploaded posts |
| `DELETE` | `/posts/{post_id}` | Delete a post by ID |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- MongoDB instance (local or Atlas)
- ImageKit account (API keys)

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/social-media-app.git
cd social-media-app
```

### 2. Create a virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the root directory:
```env
MONGODB_URI=your_mongodb_connection_string
IMAGEKIT_PUBLIC_KEY=your_imagekit_public_key
IMAGEKIT_PRIVATE_KEY=your_imagekit_private_key
IMAGEKIT_URL_ENDPOINT=your_imagekit_url_endpoint
```

### 4. Run the backend (FastAPI)
```bash
uvicorn main:app --reload
```

### 5. Run the frontend (Streamlit)
```bash
streamlit run app.py
```

---

## 📂 Project Structure
```
social-media-app/
├── backend/
│   ├── main.py          # FastAPI app & routes
│   ├── models.py        # Post data models
│   └── database.py      # MongoDB connection
├── frontend/
│   └── app.py            # Streamlit UI
├── requirements.txt
├── .env
└── README.md
```

---

## 🎥 Demo Summary

In the demo, the app shows a social media feed where a user can:
1. Upload an image or video with a caption
2. View the uploaded post in the feed
3. Refresh the feed
4. Delete posts using the backend API

---

## 📚 What I Learned

While building this project, I learned how to:
- Connect a frontend with a backend API
- Manage media uploads
- Structure API endpoints
- Perform basic CRUD operations

This project also helped me understand how real social media applications handle post creation, feed display, and media storage.

---

## 🔮 Future Improvements

- [ ] Add user authentication
- [ ] Add likes and comments
- [ ] Improve UI design
- [ ] Add profile pages
- [ ] Add post editing
- [ ] Add search and filters

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
