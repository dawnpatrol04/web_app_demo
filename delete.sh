
#!/bin/bash

# Create a placeholder main.css inside the app/main/static/css/ directory
touch app/main/static/css/main.css

# Create a placeholder logo.png inside the app/main/static/images/ directory
# Using a simple base64 encoded 1x1 pixel PNG image as a placeholder
echo "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/wcAAwAB/gnKgOMGAAAAAElFTkSuQmCC" | base64 -d > app/main/static/images/logo.png

echo "Static files created!"
