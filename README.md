# HEIC to JPG Converter API

- Convert HEIC files to JPG via HTTP POST request.

**Example using curl:**

```bash
curl -X POST -F "file=@/path/to/image.heic" http://localhost:5000/convert-heic-to-jpg --output converted.jpg
```

## Deployment
I am running it like this:

```yaml
version: '3.8'

services:
  api:
    image: ghcr.io/loficafe-zx/convert-heic-to-jpg-api:master
    ports:
      - "5000:5000"
    restart: unless-stopped
```