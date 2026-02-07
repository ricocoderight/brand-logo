#!/usr/bin/env python3
"""
Generate a youthful and unique podcast logo in JPEG format.
This script creates a modern, vibrant logo suitable for podcast branding.
"""

from PIL import Image, ImageDraw, ImageFont
import math

def create_podcast_logo(output_path='podcast_logo.jpg', size=1000):
    """
    Create a youthful podcast logo with modern design elements.
    
    Args:
        output_path (str): Path where the JPEG file will be saved
        size (int): Size of the logo (width and height in pixels)
    """
    # Create a new image with a vibrant gradient background
    img = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(img)
    
    # Create a vibrant gradient background (purple to pink to orange)
    for y in range(size):
        # Calculate color transition
        ratio = y / size
        if ratio < 0.5:
            # Purple to pink transition
            r = int(138 + (255 - 138) * (ratio * 2))
            g = int(43 + (105 - 43) * (ratio * 2))
            b = int(226 + (180 - 226) * (ratio * 2))
        else:
            # Pink to orange transition
            adjusted_ratio = (ratio - 0.5) * 2
            r = int(255 + (255 - 255) * adjusted_ratio)
            g = int(105 + (165 - 105) * adjusted_ratio)
            b = int(180 + (0 - 180) * adjusted_ratio)
        
        draw.rectangle([(0, y), (size, y + 1)], fill=(r, g, b))
    
    # Draw a circular frame
    center = size // 2
    outer_radius = int(size * 0.45)
    inner_radius = int(size * 0.38)
    
    # Draw white circular border
    draw.ellipse(
        [(center - outer_radius, center - outer_radius),
         (center + outer_radius, center + outer_radius)],
        fill='white'
    )
    
    # Create inner circle with semi-transparent dark overlay
    overlay = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.ellipse(
        [(center - inner_radius, center - inner_radius),
         (center + inner_radius, center + inner_radius)],
        fill=(255, 255, 255, 200)
    )
    img.paste(overlay, (0, 0), overlay)
    draw = ImageDraw.Draw(img)
    
    # Draw podcast microphone icon (stylized)
    mic_center_x = center
    mic_center_y = center - int(size * 0.08)
    mic_width = int(size * 0.12)
    mic_height = int(size * 0.18)
    
    # Microphone body (rounded rectangle)
    mic_color = (88, 24, 199)  # Vibrant purple
    draw.rounded_rectangle(
        [(mic_center_x - mic_width // 2, mic_center_y - mic_height // 2),
         (mic_center_x + mic_width // 2, mic_center_y + mic_height // 2)],
        radius=mic_width // 2,
        fill=mic_color
    )
    
    # Microphone stand/base
    stand_top = mic_center_y + mic_height // 2
    stand_height = int(size * 0.08)
    stand_width = int(size * 0.04)
    
    # U-shaped stand
    draw.arc(
        [(mic_center_x - stand_width, stand_top),
         (mic_center_x + stand_width, stand_top + stand_width * 2)],
        start=0, end=180, fill=mic_color, width=int(size * 0.02)
    )
    
    # Vertical stand line
    draw.line(
        [(mic_center_x, stand_top + stand_width),
         (mic_center_x, stand_top + stand_height)],
        fill=mic_color, width=int(size * 0.02)
    )
    
    # Horizontal base
    base_width = int(size * 0.1)
    draw.line(
        [(mic_center_x - base_width // 2, stand_top + stand_height),
         (mic_center_x + base_width // 2, stand_top + stand_height)],
        fill=mic_color, width=int(size * 0.02)
    )
    
    # Add sound wave elements around the microphone
    wave_color = (255, 69, 147)  # Hot pink
    for i in range(3):
        wave_offset = int(size * 0.03 * (i + 1))
        wave_arc_width = int(size * 0.015)
        
        # Left waves
        draw.arc(
            [(mic_center_x - mic_width // 2 - wave_offset - wave_arc_width,
              mic_center_y - wave_offset),
             (mic_center_x - mic_width // 2 - wave_offset + wave_arc_width,
              mic_center_y + wave_offset)],
            start=270, end=90, fill=wave_color, width=int(size * 0.01)
        )
        
        # Right waves
        draw.arc(
            [(mic_center_x + mic_width // 2 + wave_offset - wave_arc_width,
              mic_center_y - wave_offset),
             (mic_center_x + mic_width // 2 + wave_offset + wave_arc_width,
              mic_center_y + wave_offset)],
            start=90, end=270, fill=wave_color, width=int(size * 0.01)
        )
    
    # Try to add text, but handle if font is not available
    try:
        # Try to use a bold font if available (cross-platform)
        font_large = None
        font_paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  # Linux
            "/System/Library/Fonts/Helvetica.ttc",  # macOS
            "C:\\Windows\\Fonts\\arialbd.ttf",  # Windows
        ]
        
        for font_path in font_paths:
            try:
                font_large = ImageFont.truetype(font_path, int(size * 0.12))
                break
            except:
                continue
        
        # Fallback to default font if no system font found
        if font_large is None:
            font_large = ImageFont.load_default()
        
        # Add "PODCAST" text at the bottom of the circle
        text = "PODCAST"
        text_y = center + int(size * 0.2)
        
        # Get text bounding box for centering
        bbox = draw.textbbox((0, 0), text, font=font_large)
        text_width = bbox[2] - bbox[0]
        text_x = center - text_width // 2
        
        # Draw text with shadow effect
        shadow_offset = int(size * 0.005)
        draw.text((text_x + shadow_offset, text_y + shadow_offset), text, 
                 fill=(100, 100, 100), font=font_large)
        draw.text((text_x, text_y), text, fill=(88, 24, 199), font=font_large)
        
    except Exception as e:
        print(f"Note: Could not add text to logo: {e}")
    
    # Convert to RGB (in case it's RGBA) and save as JPEG
    rgb_img = img.convert('RGB')
    rgb_img.save(output_path, 'JPEG', quality=95, optimize=True)
    print(f"✓ Podcast logo successfully created: {output_path}")
    print(f"  Size: {size}x{size} pixels")
    print(f"  Format: JPEG")
    print(f"  Ready to use for videos and branding!")

if __name__ == '__main__':
    # Generate the logo
    create_podcast_logo('podcast_logo.jpg', size=1000)
    
    # Also create a high-resolution version for print/large displays
    create_podcast_logo('podcast_logo_hd.jpg', size=2000)
    
    print("\n📢 Two versions created:")
    print("  1. podcast_logo.jpg (1000x1000) - Perfect for videos and social media")
    print("  2. podcast_logo_hd.jpg (2000x2000) - High resolution for printing")
