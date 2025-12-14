"""
Cosine Similarity Algorithm Implementation
==========================================

This module implements the Cosine Similarity algorithm, which measures the cosine
of the angle between two non-zero vectors in a multi-dimensional space. It is
commonly used in text analysis, recommendation systems, and machine learning.

Mathematical Formula:
    cosine_similarity(A, B) = (A · B) / (||A|| × ||B||)
    
    Where:
    - A · B is the dot product of vectors A and B
    - ||A|| is the magnitude (Euclidean norm) of vector A
    - ||B|| is the magnitude (Euclidean norm) of vector B

The result ranges from -1 to 1:
    - 1: Vectors are identical (same direction)
    - 0: Vectors are orthogonal (no similarity)
    - -1: Vectors are opposite (completely dissimilar)

Author: [Your Name]
Course: CC 104 - Data Structures and Algorithms
Date: 2025
"""

import math
from typing import List, Dict, Tuple, Union
from collections import Counter


class CosineSimilarity:
    """
    A class to compute cosine similarity between vectors or text documents.
    
    This class provides methods to:
    1. Calculate cosine similarity between numerical vectors
    2. Calculate cosine similarity between text documents
    3. Build term frequency vectors from text
    4. Handle various input formats
    """
    
    @staticmethod
    def dot_product(vector_a: List[float], vector_b: List[float]) -> float:
        """
        Calculate the dot product of two vectors.
        
        The dot product is the sum of the products of corresponding elements.
        
        Args:
            vector_a: First vector as a list of numbers
            vector_b: Second vector as a list of numbers (must have same length)
            
        Returns:
            float: The dot product of the two vectors
            
        Raises:
            ValueError: If vectors have different lengths
            
        Example:
            >>> CosineSimilarity.dot_product([1, 2, 3], [4, 5, 6])
            32.0
        """
        # Validate that both vectors have the same length
        if len(vector_a) != len(vector_b):
            raise ValueError("Vectors must have the same length for dot product")
        
        # Calculate dot product: sum of element-wise products
        result = sum(a * b for a, b in zip(vector_a, vector_b))
        return result
    
    @staticmethod
    def magnitude(vector: List[float]) -> float:
        """
        Calculate the magnitude (Euclidean norm) of a vector.
        
        The magnitude is the square root of the sum of squared elements.
        
        Args:
            vector: A vector as a list of numbers
            
        Returns:
            float: The magnitude of the vector
            
        Example:
            >>> CosineSimilarity.magnitude([3, 4])
            5.0
        """
        # Calculate magnitude: sqrt(sum of squares)
        sum_of_squares = sum(x * x for x in vector)
        return math.sqrt(sum_of_squares)
    
    @staticmethod
    def cosine_similarity(vector_a: List[float], vector_b: List[float]) -> float:
        """
        Calculate the cosine similarity between two numerical vectors.
        
        This is the core algorithm implementation. It computes:
        cosine_similarity = (A · B) / (||A|| × ||B||)
        
        Args:
            vector_a: First vector as a list of numbers
            vector_b: Second vector as a list of numbers (must have same length)
            
        Returns:
            float: Cosine similarity value between -1 and 1
            
        Raises:
            ValueError: If vectors have different lengths or are zero vectors
            
        Example:
            >>> CosineSimilarity.cosine_similarity([1, 2, 3], [1, 2, 3])
            1.0
            >>> CosineSimilarity.cosine_similarity([1, 0], [0, 1])
            0.0
        """
        # Validate vector lengths
        if len(vector_a) != len(vector_b):
            raise ValueError("Vectors must have the same length")
        
        # Calculate dot product
        dot_prod = CosineSimilarity.dot_product(vector_a, vector_b)
        
        # Calculate magnitudes
        magnitude_a = CosineSimilarity.magnitude(vector_a)
        magnitude_b = CosineSimilarity.magnitude(vector_b)
        
        # Handle division by zero (when one or both vectors are zero vectors)
        if magnitude_a == 0 or magnitude_b == 0:
            raise ValueError("Cannot compute cosine similarity for zero vectors")
        
        # Calculate cosine similarity
        similarity = dot_prod / (magnitude_a * magnitude_b)
        
        # Ensure result is within valid range [-1, 1] (handles floating point errors)
        return max(-1.0, min(1.0, similarity))
    
    @staticmethod
    def tokenize(text: str) -> List[str]:
        """
        Tokenize a text string into words.
        
        Converts text to lowercase and splits by whitespace.
        This is a simple tokenizer; for production use, consider using
        more sophisticated NLP libraries.
        
        Args:
            text: Input text string
            
        Returns:
            List[str]: List of tokens (words)
            
        Example:
            >>> CosineSimilarity.tokenize("Hello World Python")
            ['hello', 'world', 'python']
        """
        # Convert to lowercase and split by whitespace
        tokens = text.lower().split()
        return tokens
    
    @staticmethod
    def build_vocabulary(texts: List[str]) -> Dict[str, int]:
        """
        Build a vocabulary dictionary from a list of texts.
        
        Creates a mapping from each unique word to a unique index.
        This is used to create consistent vector representations.
        
        Args:
            texts: List of text strings
            
        Returns:
            Dict[str, int]: Dictionary mapping words to indices
            
        Example:
            >>> texts = ["hello world", "world python"]
            >>> vocab = CosineSimilarity.build_vocabulary(texts)
            >>> sorted(vocab.keys())
            ['hello', 'python', 'world']
        """
        # Collect all unique words from all texts
        vocabulary = set()
        for text in texts:
            tokens = CosineSimilarity.tokenize(text)
            vocabulary.update(tokens)
        
        # Create mapping: word -> index
        vocab_dict = {word: idx for idx, word in enumerate(sorted(vocabulary))}
        return vocab_dict
    
    @staticmethod
    def text_to_vector(text: str, vocabulary: Dict[str, int]) -> List[float]:
        """
        Convert a text document to a term frequency vector.
        
        Creates a vector where each dimension represents a word in the vocabulary,
        and the value is the frequency of that word in the text.
        
        Args:
            text: Input text string
            vocabulary: Dictionary mapping words to indices
            
        Returns:
            List[float]: Term frequency vector
            
        Example:
            >>> vocab = {'hello': 0, 'world': 1}
            >>> CosineSimilarity.text_to_vector("hello hello world", vocab)
            [2.0, 1.0]
        """
        # Initialize vector with zeros (one dimension per word in vocabulary)
        vector = [0.0] * len(vocabulary)
        
        # Tokenize the text
        tokens = CosineSimilarity.tokenize(text)
        
        # Count word frequencies
        word_counts = Counter(tokens)
        
        # Fill vector with term frequencies
        for word, count in word_counts.items():
            if word in vocabulary:
                vector[vocabulary[word]] = float(count)
        
        return vector
    
    @staticmethod
    def document_similarity(text_a: str, text_b: str) -> float:
        """
        Calculate cosine similarity between two text documents.
        
        This method handles the complete pipeline:
        1. Build vocabulary from both texts
        2. Convert texts to vectors
        3. Calculate cosine similarity
        
        Args:
            text_a: First text document
            text_b: Second text document
            
        Returns:
            float: Cosine similarity between the two documents (0 to 1)
            
        Example:
            >>> CosineSimilarity.document_similarity("hello world", "hello python")
            0.4082482904638631
        """
        # Build vocabulary from both documents
        vocabulary = CosineSimilarity.build_vocabulary([text_a, text_b])
        
        # Convert texts to vectors
        vector_a = CosineSimilarity.text_to_vector(text_a, vocabulary)
        vector_b = CosineSimilarity.text_to_vector(text_b, vocabulary)
        
        # Calculate and return cosine similarity
        return CosineSimilarity.cosine_similarity(vector_a, vector_b)
    
    @staticmethod
    def similarity_matrix(texts: List[str]) -> List[List[float]]:
        """
        Calculate pairwise cosine similarity for a list of documents.
        
        Creates a similarity matrix where each entry [i][j] represents
        the cosine similarity between document i and document j.
        
        Args:
            texts: List of text documents
            
        Returns:
            List[List[float]]: Square matrix of similarity scores
            
        Example:
            >>> texts = ["hello world", "hello python", "world python"]
            >>> matrix = CosineSimilarity.similarity_matrix(texts)
            >>> len(matrix)
            3
        """
        # Build vocabulary from all documents
        vocabulary = CosineSimilarity.build_vocabulary(texts)
        
        # Convert all texts to vectors
        vectors = [CosineSimilarity.text_to_vector(text, vocabulary) 
                  for text in texts]
        
        # Calculate pairwise similarities
        n = len(texts)
        matrix = []
        
        for i in range(n):
            row = []
            for j in range(n):
                similarity = CosineSimilarity.cosine_similarity(vectors[i], vectors[j])
                row.append(similarity)
            matrix.append(row)
        
        return matrix


def demonstrate_numerical_vectors():
    """
    Demonstrate cosine similarity with numerical vectors.
    
    Shows basic usage with simple numerical examples.
    """
    print("=" * 60)
    print("DEMONSTRATION 1: Numerical Vectors")
    print("=" * 60)
    
    # Example 1: Identical vectors
    vec1 = [1, 2, 3]
    vec2 = [1, 2, 3]
    similarity = CosineSimilarity.cosine_similarity(vec1, vec2)
    print(f"\nExample 1: Identical Vectors")
    print(f"Vector A: {vec1}")
    print(f"Vector B: {vec2}")
    print(f"Cosine Similarity: {similarity:.4f}")
    print(f"Interpretation: Perfect similarity (same direction)")
    
    # Example 2: Orthogonal vectors
    vec3 = [1, 0]
    vec4 = [0, 1]
    similarity = CosineSimilarity.cosine_similarity(vec3, vec4)
    print(f"\nExample 2: Orthogonal Vectors")
    print(f"Vector A: {vec3}")
    print(f"Vector B: {vec4}")
    print(f"Cosine Similarity: {similarity:.4f}")
    print(f"Interpretation: No similarity (perpendicular)")
    
    # Example 3: Similar vectors
    vec5 = [1, 2, 3]
    vec6 = [2, 4, 6]  # vec5 scaled by 2
    similarity = CosineSimilarity.cosine_similarity(vec5, vec6)
    print(f"\nExample 3: Proportional Vectors")
    print(f"Vector A: {vec5}")
    print(f"Vector B: {vec6}")
    print(f"Cosine Similarity: {similarity:.4f}")
    print(f"Interpretation: Perfect similarity (proportional)")
    
    # Example 4: Different vectors
    vec7 = [1, 2, 3]
    vec8 = [4, 5, 6]
    similarity = CosineSimilarity.cosine_similarity(vec7, vec8)
    print(f"\nExample 4: Different Vectors")
    print(f"Vector A: {vec7}")
    print(f"Vector B: {vec8}")
    print(f"Cosine Similarity: {similarity:.4f}")
    print(f"Interpretation: Moderate similarity")


def demonstrate_text_similarity():
    """
    Demonstrate cosine similarity with text documents.
    
    Shows practical applications in document comparison.
    """
    print("\n" + "=" * 60)
    print("DEMONSTRATION 2: Text Document Similarity")
    print("=" * 60)
    
    # Example documents
    documents = [
        "Machine learning is a subset of artificial intelligence",
        "Artificial intelligence includes machine learning and deep learning",
        "Python is a popular programming language for data science",
        "Data science uses Python and machine learning algorithms"
    ]
    
    print("\nDocuments:")
    for i, doc in enumerate(documents, 1):
        print(f"  Doc {i}: {doc}")
    
    # Calculate pairwise similarities
    print("\nPairwise Similarity Matrix:")
    print("      ", end="")
    for i in range(len(documents)):
        print(f"Doc{i+1:2}", end="  ")
    print()
    
    matrix = CosineSimilarity.similarity_matrix(documents)
    for i, row in enumerate(matrix):
        print(f"Doc{i+1:2}  ", end="")
        for similarity in row:
            print(f"{similarity:6.3f}", end="  ")
        print()
    
    # Show specific comparisons
    print("\nDetailed Comparisons:")
    comparisons = [
        (0, 1, "Both about AI/ML"),
        (0, 2, "Different topics"),
        (2, 3, "Both about Python/data science")
    ]
    
    for idx1, idx2, description in comparisons:
        similarity = CosineSimilarity.document_similarity(
            documents[idx1], documents[idx2]
        )
        print(f"\n  Doc {idx1+1} vs Doc {idx2+1} ({description}):")
        print(f"    Similarity: {similarity:.4f}")
        print(f"    Doc {idx1+1}: {documents[idx1]}")
        print(f"    Doc {idx2+1}: {documents[idx2]}")


def demonstrate_recommendation_example():
    """
    Demonstrate a simple recommendation system using cosine similarity.
    
    Simulates a user-item rating matrix and finds similar users.
    """
    print("\n" + "=" * 60)
    print("DEMONSTRATION 3: Recommendation System Example")
    print("=" * 60)
    
    # User-item rating matrix (rows = users, columns = items)
    # Ratings: 0 = not rated, 1-5 = rating
    users = {
        "Alice": [5, 4, 0, 0, 1, 2],
        "Bob": [4, 5, 3, 2, 0, 0],
        "Charlie": [0, 0, 5, 4, 3, 2],
        "Diana": [1, 2, 4, 5, 0, 0],
        "Eve": [5, 5, 0, 0, 2, 3]
    }
    
    items = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E", "Movie F"]
    
    print("\nUser Ratings:")
    print("User     ", end="")
    for item in items:
        print(f"{item:10}", end="")
    print()
    for user, ratings in users.items():
        print(f"{user:8} ", end="")
        for rating in ratings:
            print(f"{rating:10}", end="")
        print()
    
    # Find most similar users to Alice
    target_user = "Alice"
    target_ratings = users[target_user]
    
    print(f"\nFinding users similar to {target_user}:")
    similarities = []
    
    for user, ratings in users.items():
        if user != target_user:
            similarity = CosineSimilarity.cosine_similarity(target_ratings, ratings)
            similarities.append((user, similarity))
    
    # Sort by similarity (descending)
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    print(f"\nSimilarity scores with {target_user}:")
    for user, similarity in similarities:
        print(f"  {user:8}: {similarity:.4f}")
    
    # Recommend items based on most similar user
    if similarities:
        most_similar_user, similarity_score = similarities[0]
        print(f"\nMost similar user: {most_similar_user} (similarity: {similarity_score:.4f})")
        print(f"Recommendations for {target_user} based on {most_similar_user}'s preferences:")
        
        most_similar_ratings = users[most_similar_user]
        for i, (item, target_rating, similar_rating) in enumerate(
            zip(items, target_ratings, most_similar_ratings)
        ):
            if target_rating == 0 and similar_rating >= 3:
                print(f"  - {item}: {similar_rating}/5 (rated by {most_similar_user})")


def main():
    """
    Main function to run all demonstrations.
    
    This function orchestrates the execution of various examples
    showing different applications of cosine similarity.
    """
    print("\n" + "=" * 60)
    print("COSINE SIMILARITY ALGORITHM - DEMONSTRATION")
    print("=" * 60)
    print("\nThis program demonstrates the Cosine Similarity algorithm")
    print("with various examples including numerical vectors, text")
    print("document comparison, and recommendation systems.\n")
    
    try:
        # Run demonstrations
        demonstrate_numerical_vectors()
        demonstrate_text_similarity()
        demonstrate_recommendation_example()
        
        print("\n" + "=" * 60)
        print("DEMONSTRATION COMPLETE")
        print("=" * 60)
        print("\nKey Takeaways:")
        print("1. Cosine similarity measures the angle between vectors")
        print("2. Range: -1 (opposite) to 1 (identical), 0 (orthogonal)")
        print("3. Useful for text analysis, recommendations, and clustering")
        print("4. Scale-invariant: proportional vectors have similarity = 1")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("Please check your input and try again.")


if __name__ == "__main__":
    # Execute the main function when script is run directly
    main()

