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
2. Install Python from <https://www.python.org/downloads/>
3. Make sure to check "Add Python to PATH" during installation

## Running Tests

```powershell
python test_cosine_similarity.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Algorithm Overview

### What is Cosine Similarity?

Cosine Similarity is a mathematical measure used to determine how similar two vectors are, regardless of their magnitude. It measures the cosine of the angle between two non-zero vectors in a multi-dimensional space. The result is a value between -1 and 1, where:

- **1** indicates identical vectors (same direction)
- **0** indicates orthogonal vectors (no similarity)
- **-1** indicates opposite vectors (completely dissimilar)

### Mathematical Formula

The cosine similarity between two vectors **A** and **B** is calculated as:

```text
cosine_similarity(A, B) = (A · B) / (||A|| × ||B||)
```

Where:

- **A · B** is the dot product of vectors A and B
- **||A||** is the magnitude (Euclidean norm) of vector A
- **||B||** is the magnitude (Euclidean norm) of vector B

### How It Works

The cosine similarity calculation involves three main steps:

#### Step 1: Dot Product Calculation

The dot product (also called scalar product) measures how much two vectors point in the same direction. It's calculated by multiplying corresponding elements of both vectors and summing the results.

**Example:**

- Vector A = [1, 2, 3]
- Vector B = [4, 5, 6]
- Dot product = (1×4) + (2×5) + (3×6) = 4 + 10 + 18 = 32

**Explanation:** Each element in vector A is multiplied by the corresponding element in vector B at the same position. The results are then added together. A higher dot product indicates that the vectors are more aligned in the same direction.

#### Step 2: Magnitude Calculation

The magnitude (also called Euclidean norm or length) of a vector represents its size or length in the multi-dimensional space. It's calculated using the Pythagorean theorem extended to multiple dimensions.

**Example:**

- ||A|| = √(1² + 2² + 3²) = √(1 + 4 + 9) = √14 ≈ 3.74
- ||B|| = √(4² + 5² + 6²) = √(16 + 25 + 36) = √77 ≈ 8.77

**Explanation:** The magnitude is the square root of the sum of squares of all vector elements. It measures how "long" the vector is in the multi-dimensional space. This normalization step is crucial because it allows us to compare vectors of different magnitudes.

#### Step 3: Similarity Score Calculation

The final cosine similarity is obtained by dividing the dot product by the product of the two vector magnitudes. This normalization ensures the result is always between -1 and 1.

**Example:**

- cosine_similarity = 32 / (3.74 × 8.77) = 32 / 32.79 ≈ 0.9746

**Explanation:**

- The result of 0.9746 (close to 1.0) indicates that vectors A and B are very similar in direction
- This means they point in nearly the same direction in the multi-dimensional space
- The division by magnitudes normalizes the result, making it independent of vector length

**Visual Interpretation:** Think of two arrows in space. Cosine similarity measures the angle between them:

- If the angle is 0° (arrows point same direction) → similarity = 1.0
- If the angle is 90° (arrows are perpendicular) → similarity = 0.0
- If the angle is 180° (arrows point opposite) → similarity = -1.0

**Why This Works for Text:** In text analysis, documents are represented as vectors where each dimension is a word. The cosine similarity tells us how similar the "direction" of word usage is between documents, regardless of document length. Two documents discussing the same topic will have similar word distributions (similar direction), even if one is much longer than the other.

### Key Properties

- **Scale-Invariant**: Vectors with proportional values yield identical similarity scores
  - [1, 2, 3] and [2, 4, 6] have similarity = 1.0 (same direction, different magnitude)
  
- **Length Normalization**: Automatically normalizes for document length, making it ideal for comparing documents of different sizes

- **Range**: Output is always between -1 and 1, providing a normalized similarity measure

- **Efficient**: Computationally efficient, especially with sparse vectors (common in text analysis)

### Why Use Cosine Similarity?

1. **Text Analysis**: Perfect for comparing documents of varying lengths
   - A 100-word document and a 10,000-word document can be fairly compared
   - Focuses on content similarity, not document size

2. **High-Dimensional Data**: Works well in high-dimensional spaces
   - Common in text analysis where vocabulary can be thousands of dimensions
   - Handles sparse vectors efficiently

3. **Orientation Over Magnitude**: Measures direction, not size
   - Useful when the magnitude of features is less important than their presence

### Applications

Cosine Similarity is commonly used for:

- **Text Document Similarity**: Comparing documents, articles, or essays
- **Search Engine Ranking**: Ranking search results by relevance
- **Recommendation Systems**: Finding similar users or items
- **Information Retrieval**: Matching queries to documents
- **Plagiarism Detection**: Identifying similar or copied content
- **Document Clustering**: Grouping similar documents together
- **Machine Learning**: Feature comparison and similarity metrics

### Example Use Cases

**Text Document Similarity:**

```text
Document 1: "Machine learning is a subset of artificial intelligence"
Document 2: "Artificial intelligence includes machine learning"

→ High similarity score (both discuss AI/ML)
```

**Recommendation Systems:**

```text
User A likes: [Movie1, Movie2, Movie3]
User B likes: [Movie1, Movie2, Movie4]

→ High similarity → Recommend Movie3 to User B
```

### Advantages

✅ Scale-invariant (handles different document lengths)  
✅ Computationally efficient  
✅ Works well with high-dimensional sparse vectors  
✅ Normalized output (-1 to 1)  
✅ Widely used and well-understood  

### Limitations

⚠️ Semantic limitations (treats "car" and "automobile" as different)  
⚠️ High-dimensional sparsity can reduce efficiency  
⚠️ Requires same vector dimensions for comparison  
⚠️ May not capture deep semantic relationships without embeddings

## Features

- Numerical vector similarity calculation
- Text document similarity
- Recommendation system example
- Comprehensive documentation
- Multiple demonstration examples
