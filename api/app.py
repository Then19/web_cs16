from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import server, users


app = FastAPI(
    title="ServerInfoAPI",
    version='0.0.2'
)

app.include_router(server.router)
app.include_router(users.router)

origins = [
    "http://localhost:3000",
    "https://v-cs.ru"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

