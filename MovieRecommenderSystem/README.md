

# Movie Recommender System

A simple web-based Movie Recommender System built using Python and Streamlit. The app suggests movies based on user selection and displays their posters using The Movie Database (TMDb) API.



## Features

- Recommends 5 movies based on your selection.
- Displays movie posters and titles.
- Interactive and user-friendly interface.




**Setup Instructions**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NigeeHettige/DataScienceProjects.git
   cd movie-recommender-system
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add TMDb API Key**:
   - Create a `.env` file in the project directory.
   - Add your API key:
     ```plaintext
     API_KEY=your_tmdb_api_key_here
     ```

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. Select a movie from the dropdown menu.
2. Click **Recommend** to see 5 movie suggestions with their posters.

---

## Requirements

- Python >= 3.8
- Libraries:
  - `streamlit`
  - `pandas`
  - `requests`
  - `python-dotenv`

---

## Project Structure

```plaintext
.
├── app.py                   # Main application file
├── movies_dict.pkl          # Movie data
├── similarity.pkl           # Similarity matrix
├── requirements.txt         # Dependencies
├── .env                     # API key file
└── README.md                # Documentation
```

---

## Note

- You need a valid API key from [TMDb](https://www.themoviedb.org/) to fetch movie posters.
- Make sure `movies_dict.pkl` and `similarity.pkl` are present in the project directory.

---

