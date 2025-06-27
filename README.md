# Bhogi Assignment

---

## Project Structure

```
.
├── app.py                        # Streamlit UI for interactive dish exploration (Q3)
├── api_design.py                 # FastAPI backend serving dish matching data (Q2)
├── dish_selector.py              # Python logic for dish selection and similarity (Q1)
├── notebooks/                    # Jupyter notebooks for exploration
  ├── Q1-Dish-Matching.ipynb        # Notebook for Q1
  ├── Q4-Solution-Design.ipynb      # Notebook for Q4
├── requirements.txt              # Python dependencies for both UI and backend
├── README.md                     # Project documentation (this file)
├── csv_data/                     # Folder containd csv data files
```


## How to Clone and Run

### 1. Clone the Repository

```sh
git clone https://github.com/priyanshu124/bhogi_assignment.git

```
---

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

---

### 4. Run the FastAPI Backend

```sh
uvicorn api_design:app --reload
```
- This will start the API at [http://localhost:8000](http://localhost:8000)
- The `/dishes` endpoint provides paginated dish recommendations.

---

### 5. Run the Streamlit UI

In a new terminal (still in the project directory):

```sh
streamlit run app.py
```
- This will launch the UI at [http://localhost:8501](http://localhost:8501)
- Enter a user ID and paginate through recommended dishes.

---

### 6. (Optional) Run Clustering and Dendrogram Analysis

- Open the provided Jupyter notebook or Python scripts for clustering and visualization.
- Approach is well explained with comments
- Example workflow:
  1. Preprocess and normalize flavor and ingredient features.
  2. Compute and normalize distance matrices.
  3. Combine distances and perform clustering.
  4. Visualize clusters with a dendrogram.


