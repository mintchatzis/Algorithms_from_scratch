

if __name__ == "__main__":
    
    tests = []
    
    def test_default():
        pass
    tests.append(test_default)
    
    print(f"Running all {len(tests)} tests")
    for test in tests:
        try:
            
            print(f"Test '{test.__name__}' passed.")
        except Exception as e:
            print(f"Test '{test.__name__} failed with exception {e}")
    
    print("Done")
    
    