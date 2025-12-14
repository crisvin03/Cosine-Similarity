# Cosine Similarity Algorithm Implementation

This project implements the Cosine Similarity algorithm in Python for the CC 104 - Data Structures and Algorithms course.

## Files

- `cosine_similarity.py` - Main implementation with demonstrations
- `test_cosine_similarity.py` - Unit tests for the implementation
- `run_cosine_similarity.ps1` - PowerShell script to run the program
- `check_python.ps1` - Script to check Python installation

## Running the Program

### Option 1: Using PowerShell Script (Recommended)
```powershell
.\run_cosine_similarity.ps1
```

### Option 2: Direct Python Command
```powershell
python cosine_similarity.py
```

### Option 3: If Python is not in PATH
If you get "Python was not found", you can:
1. Run `.\check_python.ps1` to diagnose the issue
2. Install Python from https://www.python.org/downloads/
3. Make sure to check "Add Python to PATH" during installation

## Running Tests

```powershell
python test_cosine_similarity.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Algorithm Overview

Cosine Similarity measures the cosine of the angle between two vectors in a multi-dimensional space. It's commonly used for:
- Text document similarity
- Recommendation systems
- Information retrieval
- Machine learning feature comparison

Formula: `cosine_similarity(A, B) = (A · B) / (||A|| × ||B||)`

## Features

- Numerical vector similarity calculation
- Text document similarity
- Recommendation system example
- Comprehensive documentation
- Multiple demonstration examples

