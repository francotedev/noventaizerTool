Image Processor for 90's Adventure Game Style

This Python script processes images to give them a vibrant, colorful, pixelated look inspired by 90's adventure games. It works by resizing, saturating, and adjusting colors dynamically to achieve exaggerated and artistic effects.

Features

Automatically detects and processes images in a given folder.

Supports 4:3 aspect ratio adjustments.

Applies a pixelation effect while maintaining clarity.

Enhances colors to include vibrant blues, purples, greens, oranges, and yellows.

Supports both transparent PNGs and images with backgrounds.

Maintains transparency for PNGs with alpha channels.

How It Works

Provide the path to the folder containing your images.

The script scans the folder for supported image formats.

Each image is:

Cropped to 4:3 aspect ratio.

Resized to apply a light pixelation effect.

Enhanced with exaggerated colors and effects.

If a PNG has transparency, the alpha channel is preserved.

Processed images are saved to an output subfolder inside the provided path.

Supported Formats

PNG (.png)

JPEG (.jpg, .jpeg)

Input

Specify the full path to the folder containing the images to process.

Example Input Path

/path/to/your/images

Output

The processed images will be saved in:

/path/to/your/images/output

Notes

For images without transparency, the script adds vibrant backgrounds.

Transparent PNGs retain their transparency after processing.

Maybe it's a bit late to have invented this, Franco, don't hate me... Rest in Peace (RIP) Rozu.

