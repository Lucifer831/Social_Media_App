from imagekitio import ImageKit
import os 
from dotenv import load_dotenv

load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("IMAGENET_PRIVATE_KEY")
)