import schedule
from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from main import notification_function

app = FastAPI()


@app.post('/notify')
async def notify():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(notification_function, 'interval', seconds=3)
    scheduler.start()
    # schedule.run_pending()