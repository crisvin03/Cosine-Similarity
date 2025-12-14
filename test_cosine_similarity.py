"""
Test script for Cosine Similarity implementation.

This script contains unit tests and examples to verify the correctness
of the cosine similarity algorithm implementation.
"""

from cosine_similarity import CosineSimilarity


def test_basic_operations():
    """Test basic vector operations."""
    print("Testing basic operations...")
    
    # Test dot product
    assert CosineSimilarity.dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert CosineSimilarity.dot_product([1, 0], [0, 1]) == 0
    print("✓ Dot product tests passed")
    
    # Test magnitude
    assert abs(CosineSimilarity.magnitude([3, 4]) - 5.0) < 0.0001
    assert abs(CosineSimilarity.magnitude([1, 1, 1]) - 1.732) < 0.001
    print("✓ Magnitude tests passed")


def test_cosine_similarity():
    """Test cosine similarity calculations."""
    print("\nTesting cosine similarity...")
    
    # Test identical vectors
    vec1 = [1, 2, 3]
    vec2 = [1, 2, 3]
    similarity = CosineSimilarity.cosine_similarity(vec1, vec2)
    assert abs(similarity - 1.0) < 0.0001
    print("✓ Identical vectors test passed")
    
    # Test orthogonal vectors
    vec3 = [1, 0]
    vec4 = [0, 1]
    similarity = CosineSimilarity.cosine_similarity(vec3, vec4)
    assert abs(similarity - 0.0) < 0.0001
    print("✓ Orthogonal vectors test passed")
    
    # Test proportional vectors
    vec5 = [1, 2, 3]
    vec6 = [2, 4, 6]
    similarity = CosineSimilarity.cosine_similarity(vec5, vec6)
    assert abs(similarity - 1.0) < 0.0001
    print("✓ Proportional vectors test passed")


def test_text_similarity():
    """Test text document similarity."""
    print("\nTesting text similarity...")
    
    # Test identical documents
    text1 = "hello world"
    text2 = "hello world"
    similarity = CosineSimilarity.document_similarity(text1, text2)
    assert abs(similarity - 1.0) < 0.0001
    print("✓ Identical documents test passed")
    
    # Test different documents
    text3 = "hello world"
    text4 = "python programming"
    similarity = CosineSimilarity.document_similarity(text3, text4)
    assert abs(similarity - 0.0) < 0.0001
    print("✓ Different documents test passed")
    
    # Test similar documents
    text5 = "machine learning artificial intelligence"
    text6 = "artificial intelligence machine learning"
    similarity = CosineSimilarity.document_similarity(text5, text6)
    assert similarity > 0.9  # Should be very similar
    print("✓ Similar documents test passed")


def run_all_tests():
    """Run all test functions."""
    print("=" * 60)
    print("COSINE SIMILARITY - UNIT TESTS")
    print("=" * 60)
    
    try:
        test_basic_operations()
        test_cosine_similarity()
        test_text_similarity()
        
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED! ✓")
        print("=" * 60)
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    run_all_tests()

