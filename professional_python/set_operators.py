def operators():
    # Union, is the complete union of two or more sets
    print("Set operators:")
    print("\n1. Union:")
    my_set1 = {3, 4, 5}
    my_set2 = {5, 6, 7}
    print(f"my_set1 = {my_set1}")
    print(f"my_set2 = {my_set2}")
    my_set3 = my_set1 | my_set2
    print(f"my_set3 = my_set1 | my_set2 = {my_set3}")
    
    # Intersection returns a set that contains the similarity between two or more sets
    print("\n2. Intersection:")
    print(f"my_set1 = {my_set1}")
    print(f"my_set2 = {my_set2}")
    my_set3 = my_set1 & my_set2
    print(f"my_set3 = my_set1 & my_set2 = {my_set3}")
    
    # Difference method returns a set that contains the difference between two sets
    print("\n3. Difference:")
    print(f"my_set1 = {my_set1}")
    print(f"my_set2 = {my_set2}")
    my_set3 = my_set1 - my_set2
    print(f"my_set3 = my_set1 - my_set2 = {my_set3}")
    my_set3 = my_set2 - my_set1
    print(f"my_set3 = my_set2 - my_set1 = {my_set3}")
    
    # Symmetric difference returns a set that contains all items from both set, but not the items that are present in both sets
    print("\n4. Symmetric Difference:")
    print(f"my_set1 = {my_set1}")
    print(f"my_set2 = {my_set2}")
    my_set3 = my_set1 ^ my_set2
    print(f"my_set3 = my_set1 ^ my_set2 = {my_set3}")

if __name__ == "__main__":
    operators()