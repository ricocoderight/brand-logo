#!/usr/bin/env python3
"""
Create a youthful, modern brand logo for a podcast.
"""

from PIL import Image, ImageDraw, ImageFont
import math

def create_podcast_logo(output_path='brand-logo.jpg', size=1000):
    """
    Create a youthful, vibrant podcast brand logo.
    Features modern gradient circles representing sound waves/podcast theme.
    """
    # Create a new image with a vibrant gradient background
    img = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(img)
    
    # Create a vibrant gradient background (purple to pink - youthful colors)
    for y in range(size):
        # Gradient from deep purple/blue to vibrant pink
        r = int(138 + (255 - 138) * (y / size))  # 138 to 255
        g = int(43 + (105 - 43) * (y / size))    # 43 to 105
        b = int(226 + (180 - 226) * (y / size))  # 226 to 180
        draw.rectangle([(0, y), (size, y + 1)], fill=(r, g, b))
    
    # Draw concentric circles representing sound waves/podcast audio
    center_x, center_y = size // 2, size // 2
    
    # Outer circles (sound waves)
    circle_colors = [
        (255, 255, 255, 80),   # White with transparency effect
        (255, 255, 255, 100),
        (255, 255, 255, 120),
    ]
    
    for i, alpha in enumerate([40, 60, 80]):
        radius = 420 - (i * 60)
        # Create semi-transparent overlay for circles
        overlay = Image.new('RGBA', (size, size), (255, 255, 255, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.ellipse(
            [center_x - radius, center_y - radius, 
             center_x + radius, center_y + radius],
            outline=(255, 255, 255, alpha),
            width=8
        )
        img.paste(Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB'))
    
    # Draw microphone icon in center (simplified modern design)
    mic_color = (255, 255, 255)
    
    # Microphone head (rounded rectangle/capsule shape)
    mic_width = 80
    mic_height = 120
    mic_x = center_x - mic_width // 2
    mic_y = center_y - 100
    
    draw.rounded_rectangle(
        [mic_x, mic_y, mic_x + mic_width, mic_y + mic_height],
        radius=40,
        fill=mic_color
    )
    
    # Microphone stand
    stand_width = 12
    stand_height = 80
    stand_x = center_x - stand_width // 2
    stand_y = mic_y + mic_height
    
    draw.rectangle(
        [stand_x, stand_y, stand_x + stand_width, stand_y + stand_height],
        fill=mic_color
    )
    
    # Microphone base (arc shape)
    base_width = 100
    base_y = stand_y + stand_height
    draw.arc(
        [center_x - base_width // 2, base_y - 20,
         center_x + base_width // 2, base_y + 20],
        start=0,
        end=180,
        fill=mic_color,
        width=12
    )
    
    # Add decorative sound wave bars around the microphone
    bar_color = (255, 255, 255)
    bar_positions = [
        # Left bars
        (-150, -30, 15, 60),
        (-180, 0, 15, 40),
        (-210, 10, 15, 30),
        # Right bars
        (135, -30, 15, 60),
        (165, 0, 15, 40),
        (195, 10, 15, 30),
    ]
    
    for x_offset, y_offset, width, height in bar_positions:
        draw.rounded_rectangle(
            [center_x + x_offset, center_y + y_offset,
             center_x + x_offset + width, center_y + y_offset + height],
            radius=7,
            fill=bar_color
        )
    
    # Try to add text, but handle if font isn't available
    try:
        # Try to use a nice font
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
        text_y = center_y + 180
        text = "PODCAST"
        
        # Get text bounding box for centering
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = (size - text_width) // 2
        
        # Draw text with outline effect
        outline_color = (100, 20, 150)
        for offset_x in [-2, 2]:
            for offset_y in [-2, 2]:
                draw.text((text_x + offset_x, text_y + offset_y), text, 
                         fill=outline_color, font=font)
        
        draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)
    except:
        # Fallback if font isn't available - just use default
        pass
    
    # Save as JPEG
    img.save(output_path, 'JPEG', quality=95)
    print(f"Logo created successfully: {output_path}")
    return img

if __name__ == "__main__":
    create_podcast_logo()
