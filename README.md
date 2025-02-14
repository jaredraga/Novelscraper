# Novelscraper

> **Note**: This project is no longer maintained (since January 2020) and is preserved here as a showcase of past work. The code may need updates to work with current website structures and Python dependencies.

A Python-based web scraping tool for downloading web novels from sites like WuxiaWorld, optimized for clean chapter extraction and offline reading.

## Features

- Downloads novel chapters in clean text format
- Supports chapter range specification
- Handles connection issues with automatic retries
- Cleans up invalid filename characters
- Provides download progress feedback
- Maintains download history
- Handles multiple URL formats
- Supports batch downloading

## Scripts Overview

### novelscraper-3.0.py

The main scraping script with comprehensive downloading capabilities:

- Command-line interface with flexible options
- Automatic retry on failed downloads
- Progress tracking with dynamic notifications
- Filename sanitization
- Error handling and logging

#### Usage:

```bash
python3 novelscraper-3.0.py -o <output folder> -u <first chapter url> -r <download range>

# Example:
python3 novelscraper-3.0.py -o ~/Downloads -u https://www.wuxiaworld.com/novel/a-will-eternal/awe-chapter-1 -r 1-100
```

#### Options:
- `-o`: Output directory for downloaded chapters
- `-u`: URL of the first chapter
- `-r`: Range of chapters to download (e.g., 1-100)

### logger.py

Logging utility for tracking downloads and operations:

- Maintains download history
- Prevents duplicate downloads
- Provides operation logging

## Project Structure

```
Novelscraper/
├── novelscraper-3.0.py    # Main scraping script
├── logger.py             # Logging functionality
├── downloaded_log.txt    # Download history
├── log.txt              # Operation logs
├── early-versions/      # Development history
├── older-versions/      # Archive of previous versions
└── version-tests/       # Testing iterations
```

## Requirements

- Python 3.x
- requests
- beautifulsoup4
- urllib3

Install dependencies:
```bash
pip3 install requests beautifulsoup4
```

## Version History

- v3.0.0: Current stable version
  - Python 3 support
  - Improved error handling
  - Dynamic progress display
  - Better filename handling

- v2.1.1: 
  - Enhanced error handling
  - File writing verification

- v2.1.0:
  - Dynamic status line
  - Reduced terminal clutter

- v2.0.0:
  - Python 2 compatibility (deprecated)

- v1.4.0:
  - Added proxy support
  - Security improvements

See `version updates` file for complete history.

## Features in Detail

1. Download Management:
   - Automatic retry on connection failures
   - Progress tracking
   - Range-based downloading
   - Download history

2. Content Processing:
   - Clean text extraction
   - Chapter title parsing
   - Filename sanitization
   - Proper formatting

3. Error Handling:
   - Connection retry logic
   - Invalid URL detection
   - File writing verification
   - Logging of failures

4. User Interface:
   - Command-line arguments
   - Dynamic progress display
   - Operation confirmation
   - Status updates

## Notes

- Designed for WuxiaWorld but may work with similar sites
- Respects website structure and rate limits
- Maintains clean, readable output format
- Includes backup URL functionality
- Preserves chapter ordering
- Handles special characters in titles

## Contributing

Feel free to submit issues and enhancement requests. Follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License. 