from email.policy import default

from fastapi import FastAPI, Query, Body
import uvicorn
app = FastAPI()


hotels = [
    {'id': 1, 'title': 'Sochi', 'name': 'sochi'},
    {'id': 2, 'title': 'dubai', 'name': 'dubai'}
]


@app.get('/hotels')
def get_hotels(
        id: int | None = Query(
            default=None,
            description='Айдишник'
        ),
        title: str | None = Query(
            default=None,
            description='Название отеля'
        )
):
    hotel_ = []
    for hotel in hotels:
        if id and hotel['id'] != id:
            continue
        if title and hotel['title'] != title:
            continue
        hotel_.append(hotel)
    return hotel_

@app.delete('/hotels/{hotel_id}')
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel['id'] != hotel_id]
    return {
        'status': 'OK'
    }


@app.post('/hotels')
def create_hotel(
        title: str = Body(embed=True)
):
    global hotels
    hotels.append({
        'id': hotels[-1]['id'] + 1,
        'title': title
    })
    return {
        'status': 'OK'
    }

# все параметры




if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        reload=True,
    )