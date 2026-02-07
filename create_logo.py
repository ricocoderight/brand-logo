#!/usr/bin/env python3
"""
Create a personalized brand logo for the Mchungaji podcast.
Features a caricature of a young African man in a podcast studio.
"""

from PIL import Image, ImageDraw, ImageFont
import math

def create_podcast_logo(output_path='brand-logo.jpg', size=1000):
    """
    Create a personalized podcast logo for Mchungaji brand.
    Features a caricature-style illustration of a young African man in a podcast studio.
    """
    # Create a new image with a warm studio background
    img = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(img)
    
    # Create a warm gradient background (warm brown/orange studio atmosphere)
    for y in range(size):
        # Gradient from warm orange-brown to lighter warm tone
        r = int(220 + (255 - 220) * (y / size))  # 220 to 255
        g = int(150 + (230 - 150) * (y / size))  # 150 to 230
        b = int(100 + (200 - 100) * (y / size))  # 100 to 200
        draw.rectangle([(0, y), (size, y + 1)], fill=(r, g, b))
    
    # Studio room frame (darker border to simulate walls)
    studio_color = (101, 67, 33)  # Dark brown
    draw.rectangle([50, 50, size-50, size-50], outline=studio_color, width=15)
    
    # Define center position for the character
    center_x = size // 2
    base_y = 700  # Bottom position
    
    # === DRAW YOUNG AFRICAN MAN CARICATURE ===
    
    # Skin tone (warm brown for African complexion)
    skin_tone = (139, 90, 43)
    dark_skin = (101, 67, 33)
    
    # BODY/TORSO (simple shape for seated position)
    # Shoulders and upper body
    body_points = [
        (center_x - 150, base_y - 200),  # Left shoulder
        (center_x - 140, base_y),         # Left bottom
        (center_x + 140, base_y),         # Right bottom
        (center_x + 150, base_y - 200),  # Right shoulder
    ]
    draw.polygon(body_points, fill=(80, 120, 160))  # Blue shirt
    
    # NECK
    neck_width = 60
    neck_height = 80
    draw.rectangle(
        [center_x - neck_width//2, base_y - 280,
         center_x + neck_width//2, base_y - 200],
        fill=skin_tone
    )
    
    # HEAD (large oval for caricature style)
    head_width = 180
    head_height = 220
    head_top = base_y - 280 - head_height
    
    # Main head shape
    draw.ellipse(
        [center_x - head_width//2, head_top,
         center_x + head_width//2, head_top + head_height],
        fill=skin_tone,
        outline=dark_skin,
        width=3
    )
    
    # HAIR (short African hairstyle)
    hair_color = (20, 20, 20)
    # Hair top
    draw.ellipse(
        [center_x - head_width//2 - 10, head_top - 20,
         center_x + head_width//2 + 10, head_top + 80],
        fill=hair_color
    )
    
    # FACIAL FEATURES
    face_center_y = head_top + head_height // 2
    
    # Eyes (large expressive eyes for caricature)
    eye_y = face_center_y - 30
    eye_spacing = 50
    
    # Left eye
    draw.ellipse(
        [center_x - eye_spacing - 30, eye_y - 20,
         center_x - eye_spacing + 10, eye_y + 20],
        fill=(255, 255, 255),
        outline=(0, 0, 0),
        width=2
    )
    # Left pupil
    draw.ellipse(
        [center_x - eye_spacing - 15, eye_y - 5,
         center_x - eye_spacing + 5, eye_y + 15],
        fill=(50, 30, 20)
    )
    
    # Right eye
    draw.ellipse(
        [center_x + eye_spacing - 10, eye_y - 20,
         center_x + eye_spacing + 30, eye_y + 20],
        fill=(255, 255, 255),
        outline=(0, 0, 0),
        width=2
    )
    # Right pupil
    draw.ellipse(
        [center_x + eye_spacing - 5, eye_y - 5,
         center_x + eye_spacing + 15, eye_y + 15],
        fill=(50, 30, 20)
    )
    
    # Nose (simple triangular shape)
    nose_points = [
        (center_x, face_center_y + 10),
        (center_x - 15, face_center_y + 40),
        (center_x + 15, face_center_y + 40),
    ]
    draw.polygon(nose_points, fill=dark_skin)
    
    # Mouth (friendly smile)
    mouth_y = face_center_y + 60
    draw.arc(
        [center_x - 40, mouth_y - 10,
         center_x + 40, mouth_y + 30],
        start=0,
        end=180,
        fill=(0, 0, 0),
        width=3
    )
    # Teeth highlight
    draw.arc(
        [center_x - 30, mouth_y - 5,
         center_x + 30, mouth_y + 20],
        start=0,
        end=180,
        fill=(255, 255, 255),
        width=2
    )
    
    # HEADPHONES (over-ear style)
    headphone_color = (50, 50, 50)
    headphone_accent = (200, 50, 50)  # Red accent
    
    # Headband
    draw.arc(
        [center_x - head_width//2 - 30, head_top - 30,
         center_x + head_width//2 + 30, head_top + 100],
        start=0,
        end=180,
        fill=headphone_color,
        width=20
    )
    
    # Left ear cup
    draw.ellipse(
        [center_x - head_width//2 - 40, face_center_y - 40,
         center_x - head_width//2 + 40, face_center_y + 40],
        fill=headphone_color,
        outline=headphone_accent,
        width=4
    )
    draw.ellipse(
        [center_x - head_width//2 - 25, face_center_y - 25,
         center_x - head_width//2 + 25, face_center_y + 25],
        fill=headphone_accent
    )
    
    # Right ear cup
    draw.ellipse(
        [center_x + head_width//2 - 40, face_center_y - 40,
         center_x + head_width//2 + 40, face_center_y + 40],
        fill=headphone_color,
        outline=headphone_accent,
        width=4
    )
    draw.ellipse(
        [center_x + head_width//2 - 25, face_center_y - 25,
         center_x + head_width//2 + 25, face_center_y + 25],
        fill=headphone_accent
    )
    
    # MICROPHONE (professional studio mic in front)
    mic_x = center_x + 80
    mic_y = base_y - 300
    
    # Mic stand arm
    draw.line(
        [(mic_x + 100, base_y), (mic_x + 100, mic_y - 100)],
        fill=(80, 80, 80),
        width=8
    )
    draw.line(
        [(mic_x + 100, mic_y - 100), (mic_x, mic_y)],
        fill=(80, 80, 80),
        width=8
    )
    
    # Mic body (classic studio mic)
    draw.ellipse(
        [mic_x - 30, mic_y - 80,
         mic_x + 30, mic_y + 20],
        fill=(60, 60, 60),
        outline=(40, 40, 40),
        width=3
    )
    
    # Mic mesh/grille
    for i in range(-3, 4):
        draw.line(
            [(mic_x - 20, mic_y - 60 + i*10),
             (mic_x + 20, mic_y - 60 + i*10)],
            fill=(100, 100, 100),
            width=2
        )
    
    # SOUND WAVES (visual effect around microphone)
    wave_color = (255, 200, 100, 128)
    for i in range(3):
        radius = 40 + i * 30
        overlay = Image.new('RGBA', (size, size), (255, 255, 255, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.arc(
            [mic_x - radius, mic_y - radius,
             mic_x + radius, mic_y + radius],
            start=180,
            end=360,
            fill=(255, 200, 100, 60 - i*15),
            width=3
        )
        img.paste(Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB'))
    
    # Add brand text "MCHUNGAJI"
    try:
        # Try to use a bold font
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
        
        # Main brand name at top
        text = "MCHUNGAJI"
        bbox = draw.textbbox((0, 0), text, font=font_large)
        text_width = bbox[2] - bbox[0]
        text_x = (size - text_width) // 2
        text_y = 80
        
        # Draw text with shadow effect
        shadow_color = (50, 30, 10)
        for offset in range(1, 4):
            draw.text((text_x + offset, text_y + offset), text, 
                     fill=shadow_color, font=font_large)
        
        # Main text in warm color
        draw.text((text_x, text_y), text, fill=(255, 220, 100), font=font_large)
        
        # Subtitle
        subtitle = "PODCAST"
        bbox_sub = draw.textbbox((0, 0), subtitle, font=font_small)
        text_width_sub = bbox_sub[2] - bbox_sub[0]
        text_x_sub = (size - text_width_sub) // 2
        text_y_sub = text_y + 90
        
        draw.text((text_x_sub + 2, text_y_sub + 2), subtitle, 
                 fill=shadow_color, font=font_small)
        draw.text((text_x_sub, text_y_sub), subtitle, 
                 fill=(255, 255, 255), font=font_small)
        
    except (IOError, OSError):
        # Fallback if font isn't available - just use default
        pass
    
    # Save as JPEG
    img.save(output_path, 'JPEG', quality=95)
    print(f"Mchungaji podcast logo created successfully: {output_path}")
    return img

if __name__ == "__main__":
    create_podcast_logo()
