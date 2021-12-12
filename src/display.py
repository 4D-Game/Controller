import time
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import ili9341

class Display:
    """
        Class to manage displaydata
    """
    team_A: list = [0, 1, 2] #Where Players @??
    team_B: list = [3, 4, 5]

    def __init__(self, name: str):
        self.name = name
        self.score_A = 0
        self.score_B = 0

    def configuration(self):
        """
            Configures pins and spi for connection
        """
        # Configuration for CS and DC pins (these are PiTFT defaults):
        cs_pin = digitalio.DigitalInOut(board.CE0)
        dc_pin = digitalio.DigitalInOut(board.D25)
        reset_pin = digitalio.DigitalInOut(board.D24)

        # Config for display baudrate (default max is 24mhz):
        baudrate = 24000000

        # Setup SPI bus using hardware SPI:
        spi = board.SPI()

        self.disp = ili9341.ILI9341(
            spi,
            rotation=90,  #2.2", 2.4", 2.8", 3.2" ILI9341
            cs=cs_pin,
            dc=dc_pin,
            rst=reset_pin,
            baudrate=baudrate,
        )

    def show_score(self, seat: int, score: int, team_A: list = team_A, team_B: list = team_B):
        """
            Show scores of teams on display
        """
        if seat in team_A:
            self.score_A = self.score_A + score
        elif seat in team_B:
            self.score_B = self.score_B + score
            
        score_A_str = str(self.score_A)
        score_B_str = str(self.score_B)

        # Create blank image for drawing
        if self.disp.rotation % 180 == 90:
            height = self.disp.width  #we swap height/width to rotate it to landscape!
            width = self.disp.height
        else:
            width = self.disp.width  
            height = self.disp.height

        image = Image.new("RGB", (width, height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        #Load a TTF font. .ttf font file should be same directory as the python script
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 45)

        #Draw a blue filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 155, 250))

        text1 = "Team 1: " 
        text2 = "Team 2: " 

        y = 50
        x = 30
        draw.text((x, y),text1, font=font, fill= "#FFFFFF")
        x += font.getsize(text1)[0]
        draw.text((x, y), score_A_str, font=font, fill= (255, 0, 0))  
        y += 40+font.getsize(text1)[1]
        x = 30
        draw.text((x, y), text2, font=font, fill="#FFFFFF")
        x += font.getsize(text2)[0]
        draw.text((x, y), score_B_str, font=font, fill= (255, 0, 0))  

        # Display image.
        self.disp.image(image)

    def reset(self):
        """
            Resets whole display
        """
        pass

    def start_game(self):
        """
            Display until game starts (ready)
        """
        if self.disp.rotation % 180 == 90:
            height = self.disp.width  #we swap height/width to rotate it to landscape!
            width = self.disp.height
        else:
            width = self.disp.width  
            height = self.disp.height


        image = Image.new("RGB", (width, height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 155, 250))
        draw.ellipse((80,50,230,200), fill = (0, 155, 250), outline ='white', width=10)
        #draw.ellipse((20, 180, 180, 20), outline ='white', fill=(0, 250, 0))
        self.disp.image(image)

        # Scale the image to the smaller screen dimension
        image_ratio = image.width / image.height
        screen_ratio = width / height
        if screen_ratio < image_ratio:
            scaled_width = image.width * height // image.height
            scaled_height = height
        else:
            scaled_width = width
            scaled_height = image.height * width // image.width
        image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

        
        # Display image.
        self.disp.image(image)
        
    
    def eng_game(self):
        """
            Display when game end
        """
        pass


display1 = Display("First")
display1.configuration()
#display1.show_score(2, 4) #seat and score

for x in range(20):
    display1.show_score(2, x)
    display1.show_score(4, x)

#display1.start_game()