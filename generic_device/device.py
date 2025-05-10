import logging
from pydantic import BaseModel
from datetime import datetime, timezone
from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from home_view import HOME_VIEW, KEYPAD_VIEW

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Output to console
        logging.FileHandler(f'run_{datetime.now(timezone.utc).timestamp()}.log')  # Output to file
    ]
)

class Operand(BaseModel):
    pass

class Operation(BaseModel):
    pass

class Instruction(BaseModel):
    pass



class DeviceConfigs:
    def __init__(self):
        logging.info("Device Configs: ")
        logging.warning("test")
        
        pass
app = FastAPI()

class Device:
    def __init__(self):
        self.device_on = True
        self.router = APIRouter()
        self.router.add_api_route("/", self.home, methods=["GET"], response_class=HTMLResponse)
        self.router.add_api_route("/keypad", self.keypad, methods=["GET"], response_class=HTMLResponse)
        self.router.add_api_route("/health_check", self.health_check, methods=["GET"])
        self.router.add_api_route("/pwr_toggle", self.pwr_toggle, methods=["GET"])
        self.router.add_api_route("/connect", self.connect, methods=["GET"])
        self.router.add_api_route("/request", self.request, methods=["GET"])

    def home(self):
        return HOME_VIEW
    
    def keypad(self):
        return KEYPAD_VIEW 
    
    def health_check(self):
        logging.info("device - health_check: good")
        return True
        
    def pwr_toggle(self):
        self.device_on = not self.device_on
        logging.info(f"device - pwr_toggle {self.device_on}")
        return self.device_on
    
    def connect(self):
        logging.info(f"device - connect")
        if self.device_on:
            logging.info("Device Connect: ")
    
    def request(self):
        pass








dut = Device()
app.include_router(dut.router)







