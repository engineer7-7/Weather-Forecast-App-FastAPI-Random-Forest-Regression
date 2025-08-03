# import libraries
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.templating import Jinja2Templates
import uvicorn
from model import feature_scaling_model_training_prediction
from data_collector import API_KEY
from datetime import datetime

from weather_forecast_app.dataset import create_dataframe
from weather_forecast_app.model import to_datetime

# create an instance of FastAPI
app = FastAPI()

# Templates folder
templates = Jinja2Templates(directory='templates')


# create a GET route to display the main page
@app.get('/')
def index(request: Request):
    return templates.TemplateResponse(
        'index.html', {'request': request}
    )


# create a POST route to put the city name and display the model prediction
@app.post('/prediction/', name='prediction')
async def model_prediction(request: Request, forecast_datetime=Form(...), city: str = Form(...)):
    dt = datetime.fromisoformat(forecast_datetime)
    day, month, year = dt.day, dt.month, dt.year
    df = create_dataframe(city, API_KEY)
    df = to_datetime(df)

    df = df[(df['day'] == day) & (df['month'] == month) & (df['year'] == year)]
    if df.empty:
        return HTTPException(status_code=404, detail='Dataframe is empty!')

    prediction_celsius, prediction_fahrenheit = feature_scaling_model_training_prediction(df)

    return templates.TemplateResponse('index.html',
                                      {'request': request, 'city': city, 'prediction_celsius': prediction_celsius,
                                       'prediction_fahrenheit': prediction_fahrenheit,
                                       'forecast_datetime': forecast_datetime})


# run the app
if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8001)
