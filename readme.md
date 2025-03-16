# PDFolderMerger

A lightweight command-line utility for merging multiple PDF files within a directory structure into a single consolidated PDF document.

## Overview

PDFolderMerger is designed to simplify the process of combining multiple PDF files scattered across folders and subfolders. It provides a straightforward command-line interface to recursively scan a directory, identify PDF files, and merge them into a single document while preserving a logical order.

## Features

- Recursive directory scanning to locate all PDF files
- Configurable sorting options for controlling merge order
- Progress tracking during the merge process
- Support for both absolute and relative file paths
- Simple command-line interface with sensible defaults
- Cross-platform compatibility (Windows, macOS, Linux)

## Installation

```bash
# Clone the repository
git clone https://github.com/Code2Construct/PDFolderMerger.git

# Navigate to the project directory
cd PDFolderMerger

# Install dependencies
pip install -r requirements.txt
```

## Usage

Basic usage:

```bash
python pdfolder_merger.py /path/to/folder -o output.pdf
```

Advanced options:

```bash
python pdfolder_merger.py /path/to/folder -o output.pdf --sort-by name --recursive --exclude-pattern "draft_*"
```

### Command-line Arguments

| Argument | Description |
|----------|-------------|
| `input_folder` | Path to the folder containing PDF files to merge |
| `-o, --output` | Output file path for the merged PDF |
| `-r, --recursive` | Scan subdirectories recursively (default: True) |
| `-s, --sort-by` | Sort files by 'name', 'date', or 'size' (default: name) |
| `-e, --exclude-pattern` | Pattern to exclude matching files |
| `-v, --verbose` | Enable verbose logging |

## Requirements

- Python 3.6+
- PyPDF2
- tqdm (for progress display)

## Examples

### Basic Merge

Merge all PDFs in the current directory:

```bash
python pdfolder_merger.py . -o merged.pdf
```

### Advanced Sorting

Merge PDFs sorted by modification date:

```bash
python pdfolder_merger.py /documents/reports -o merged_reports.pdf --sort-by date
```

### Exclude Specific Files

Merge PDFs excluding draft versions:

```bash
python pdfolder_merger.py /documents/contracts -o final_contract.pdf --exclude-pattern "*draft*"
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [PyPDF2](https://github.com/py-pdf/PyPDF2) for providing PDF manipulation capabilities
- All contributors who have helped improve this tool
