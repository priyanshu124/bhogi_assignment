import random
from fastapi import FastAPI, Query
from dish_selector import return_all_dishes

app = FastAPI()

all_dishes = return_all_dishes()
dish_names = all_dishes['dish_name'].tolist()

@app.get("/dishes")
def get_dishes(userId: int = Query(..., ge=0, le=999999), page: int = Query(..., ge=0, le=4)):
    try:
        # Deterministic shuffle using userId as seed
        shuffled = dish_names.copy()
        random.Random(userId).shuffle(shuffled)

        # Pagination (5 dishes per page)
        start_idx = page * 5
        end_idx = start_idx + 5
        paged_dishes = shuffled[start_idx:end_idx]

        return {"dishes": paged_dishes}

    except Exception as e:
        return {"error": str(e)}
    
    
