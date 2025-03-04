from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting up API...")
    yield
    # Shutdown
    print("Shutting down API...")


app = FastAPI(
    title="Python Backend",
    description="Modern Python Backend API",
    version="1.0.0",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "status": "running",
        "message": "Welcome to the Modern Python Backend",
    }


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "healthy"} 
