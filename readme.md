# Readme

This repository is a collection of my solutions to the different problems listed under the learn section of 
[LeetCode - Explore](https://leetcode.com/explore/).

I chose the problems based on the [Explore card track](https://leetcode.com/explore/featured/card/the-leetcode-beginners-guide/679/sql-syntax/4358/)
from LeetCode.

Each section has a dedicated directory to it, and each problem has a dedicated sub-directory which would usually will
contain:
1. The "problem_statement" along with any of the given hints
2. The solution - if applicable it'll be marked speed or memory, 
   * memory: most memory efficient implementation by me 
   * speed: fastest implementation by me
   * both: most memory efficient + fastest implementation by me
   * i.e., There are possibly even faster and/or more efficient solutions out there

All solutions are in **Python3**

### Order of problems:
Completed:-
 * Arrays 101
   * Introduction
     * Max Consecutive Ones
     * Find Numbers with Even Number of Digits
     * Squares of a Sorted Array
   * Inserting Items Into an Array
     * Duplicate Zeros
     * Merge Sorted Array
   * Deleting Items From an Array
     * Remove Element
     * Remove Duplicates from Sorted Array
   * Search in an Array
     * Check If N and Its Double Exist
     * Valid Mountain Array
   * In-Place Operations
     * Replace Elements with Greatest Element on Right Side
     * Remove Duplicates from Sorted Array
     * Move Zeroes
     * Sort Array By Parity
     * Remove Element
   * Conclusion
     * Height Checker
     * Max Consecutive Ones II - (Locked for premium users - not done)
     * Third Maximum Number
     * Find All Numbers Disappeared in an Array
     * Squares of a Sorted Array
 * Linked List
   * Singly Linked List
     * Design Linked List
   * Two Pointer Technique
     * Linked List Cycle
     * Linked List Cycle II
     * Intersection of Two Linked Lists
     * Remove Nth Node From End of List
   * Classic Problems
     * Reverse Linked List
     * Remove Linked List Elements
     * Palindrome Linked List
   * Doubly Linked List
     * Design Linked List
   * Conclusion
     * Merge Two Sorted Lists
     * Add Two Numbers
     * Flatten a Multilevel Doubly Linked List
     * Insert into a Cyclic Sorted List - (Locked for premium users - not done)
     * Copy List with Random Pointer
     * Rotate List
 * Array and String
   * Introduction to Array
     * Find Pivot Index
     * Largest Number At Least Twice of Others
     * Plus One
   * Introduction to 2D Array
     * Diagonal Traverse
     * Spiral Matrix
     * Pascal's Triangle
   * Introduction to String
     * Add Binary 
     * Implement strStr()
     * Longest Common Prefix
   * Two-Pointer Technique
     * Reverse String
     * Array Partition I
     * Two Sum II - Input array is sorted
     * Remove Element - already completed in "Arrays 101" -> "Deleting Items From an Array"
     * Max Consecutive Ones - already completed in "Arrays 101" -> "Introduction"
     * Minimum Size Subarray Sum
   * Conclusion
     * Rotate Array
     * Pascal's Triangle II
     * Reverse Words in a String
     * Reverse Words in a String III
     * Remove Duplicates from Sorted Array - already completed in "Arrays 101" -> "Deleting Items From an Array"
     * Move Zeros - already completed in "Arrays 101" -> "In-Place Operations"
 * Hash Table
   * Design a Hash Table
     * Design HashSet
     * Design HashMap
   * Practical Application - Hash Set
     * Contains Duplicate
     * Single Number
     * Intersection of Two Arrays
     * Happy Number
   * Practical Application - Hash Map
   * Practical Application - Design the Key
   * Conclusion

     
Pending:-
 * Hash Table
 * Recursion I
 * Queue & Stack
 * Heap
 * Binary Search
 * Binary Tree
 * Binary Search Tree
 * Trie
 * N-ary Tree
 * Recursion II
 * Dynamic Programming
 * Graph
     

---
### Statistics of the submitted solutions
|Explore- module|Topic|Problem| Solution_type | Submission_date | Required_time | Faster_than<sup>1</sup> | Required_Memory | Less_memory_than<sup>2</sup> |Remarks|
|---|---|---|---------------|:---------------:|:-------------:|:-----------------------:|:---------------:|------------------------------|---|
|Arrays 101|Introduction|Max Consecutive Ones| memory        |   12-Jul-2022   |    483 ms     |         57.84%          |     14.2 MB     | 79.14%                       ||
|Arrays 101|Introduction|Max Consecutive Ones| speed         |   12-Jul-2022   |    361 ms     |         92.48%          |     14.4 MB     | 32.02%                       ||
|Arrays 101|Introduction|Find Numbers with Even Number of Digits| both          |   13-Jul-2022   |     62 ms     |         84.74%          |     13.8 MB     | 99.19%                       |<sup>3</sup>|
|Arrays 101|Introduction|Squares of a Sorted Array| memory        |   13-Jul-2022   |    558 ms     |          6.89%          |     16.2 MB     | 80.22%                       ||
|Arrays 101|Introduction|Squares of a Sorted Array| speed         |   13-Jul-2022   |    256 ms     |         82.02%          |     16.3 MB     | 49.26%                       ||
|Arrays 101|Inserting Items Into an Array|Duplicate Zeros| memory        |   14-Jul-2022   |    170 ms     |         21.35%          |     14.7 MB     | 97.63%                       ||
|Arrays 101|Inserting Items Into an Array|Duplicate Zeros| speed         |   15-Jul-2022   |     73 ms     |         91.46%          |     15.2 MB     | <20%                         |Memory ranking beyond displayed chart limits|
|Arrays 101|Inserting Items Into an Array|Merge Sorted Array| both          |   16-Jul-2022   |     41 ms     |         87.72%          |     13.9 MB     | 85.55%                       ||
|Arrays 101|Deleting Items From an Array|Remove Element| speed         |   16-Jul-2022   |     32 ms     |         96.28%          |     13.9 MB     | <15%                         |Memory ranking beyond displayed chart limits|
|Arrays 101|Deleting Items From an Array|Remove Duplicates from Sorted Array| memory        |   16-Jul-2022   |    205 ms     |         17.31%          |     15.5 MB     | 60.57%                       ||
|Arrays 101|Deleting Items From an Array|Remove Duplicates from Sorted Array| speed         |   16-Jul-2022   |    114 ms     |         74.93%          |     15.6 MB     | 60.57%                       |Memory improvement by 0.1 MB has no impact on ranking|
|Arrays 101|Search in an Array|Check If N and Its Double Exist| both          |   16-Jul-2022   |     55 ms     |         94.17%          |     13.9 MB     | 55.83%                       ||
|Arrays 101|Search in an Array|Valid Mountain Array| both          |   16-Jul-2022   |    204 ms     |         98.16%          |     15.4 MB     | 70.34%                       ||
|Arrays 101|In-Place Operations|Replace Elements with Greatest Element on Right Side| memory        |   16-Jul-2022   |    141 ms     |         84.24%          |     15.2 MB     | 62.39%                       ||
|Arrays 101|In-Place Operations|Replace Elements with Greatest Element on Right Side| speed         |   16-Jul-2022   |    123 ms     |         96.24%          |     15.4 MB     | 34.79%                       ||
|Arrays 101|In-Place Operations|Remove Duplicates from Sorted Array| speed         |   17-Jul-2022   |     83 ms     |         98.44%          |     15.5 MB     | 96.23%                       |The solution is same as the one from "Remove Duplicates from Sorted Array"|
|Arrays 101|In-Place Operations|Move Zeroes| both          |   17-Jul-2022   |    163 ms     |         98.23%          |     15.5 MB     | 96.87%                       ||
|Arrays 101|In-Place Operations|Sort Array By Parity| both          |   18-Jul-2022   |    100 ms     |         73.49%          |     14.6 MB     | 96.10%                       ||
|Arrays 101|In-Place Operations|Remove Element| memory        |   18-Jul-2022   |     83 ms     |          5.48%          |     13.7 MB     | 96.10%                       |The solution is exactly same as the one for speed optimisation, but LeetCode reports different results on different runs|
|Arrays 101|In-Place Operations|Remove Element| speed         |   18-Jul-2022   |     32 ms     |         97.17%          |     13.9 MB     | <15%                         ||
|Arrays 101|Conclusion|Height Checker| both          |   19-Jul-2022   |     51 ms     |         63.20%          |     13.8 MB     | 95.99%                       |The fastest solutions as per Leetcode are the exact same algorithm with slightly different variable names|
|Arrays 101|Conclusion|Third Maximum Number| memory        |   19-Jul-2022   |     57 ms     |         91.03%          |     14.8 MB     | 93.36%                       ||
|Arrays 101|Conclusion|Third Maximum Number| speed         |   19-Jul-2022   |     50 ms     |         98.34%          |     14.9 MB     | 64.34%                       ||
|Arrays 101|Conclusion|Find All Numbers Disappeared in an Array| speed         |   20-Jul-2022   |    327 ms     |         99.65%          |     24.7 MB     | 27.72%                       |Memory Optimised solution to be added|
|Arrays 101|Conclusion|Squares of a Sorted Array| memory        |   21-Jul-2022   |    328 ms     |         57.49%          |     15.7 MB     | 92.91%                       ||
|Arrays 101|Conclusion|Squares of a Sorted Array| speed         |   21-Jul-2022   |    214 ms     |         97.92%          |     16.3 MB     | 17.40%                       ||
|Linked List|Singly Linked List|Design Linked List| both          |   23-Jul-2022   |     74 ms     |         99.97%          |     14.6 MB     | 98.41%                       |This solution uses lists to hold values. Another solution with the implementation using nodes exists in the directory|
|Linked List|Two Pointer Technique|Linked List Cycle| speed         |   24-Jul-2022   |     50 ms     |         98.62%          |     17.5 MB     | 66.22%                       |<sup>3</sup>|
|Linked List|Two Pointer Technique|Linked List Cycle| memory        |   24-Jul-2022   |     56 ms     |         94.26%          |     17.4 MB     | 96.40%                       |This solution is inspired from the most memory efficient solutions available in LeetCode. Note, this solution modifies the values stored in the nodes, and there by is applicable only if losing the values in the list doesn't matter|
|Linked List|Two Pointer Technique|Linked List Cycle II| memory        |   24-Jul-2022   |     75 ms     |         57.82%          |     17.3 MB     | 94.27%                       ||
|Linked List|Two Pointer Technique|Linked List Cycle II| speed         |   24-Jul-2022   |     51 ms     |         95.04%          |      18 MB      | <10%                         |Extremely memory inefficient method since it essentially creates an another copy of the whole linked list|
|Linked List|Two Pointer Technique|Intersection of Two Linked Lists| both          |   25-Jul-2022   |    166 ms     |         91.34%          |     29.5 MB     | 93.92%                       ||
|Linked List|Two Pointer Technique|Remove Nth Node From End of List| both          |   25-Jul-2022   |     39 ms     |         81.88%          |     13.9 MB     | 69.55%                       ||
|Linked List|Classic Problems|Reverse Linked List| both          |   26-Jul-2022   |     55 ms     |         52.68%          |     15.4 MB     | 93.96%                       |The best solution both memory and speed as per LeetCode submissions are the exact algorithm, unsure why it is ranked so low in speed. NOTE: Recursive approach to be added.|
|Linked List|Classic Problems|Remove Linked List Elements| both          |   26-Jul-2022   |     71 ms     |         93.29%          |     17.1 MB     | 99.58%                       ||
|Linked List|Classic Problems|Odd Even Linked List| both          |   27-Jul-2022   |     34 ms     |         99.65%          |     16.5 MB     | 77.11%                       ||
|Linked List|Classic Problems|Palindrome Linked List| both          | 28-06-Jul-2022  |    883 ms     |         83.79%          |     31.2 MB     | 95.49%                       |<sup>3</sup>|
|Linked List|Doubly Linked List|Design Linked List| both          |   30-Jul-2022   |    122 ms     |         97.54%          |     14.6 MB     | 84.20%                       |This solution is the same as Singly Linked List -> Design Linked List|
|Linked List|Conclusion|Merge Two Sorted Lists| speed         |   31-Jul-2022   |     41 ms     |         89.02%          |     13.9 MB     | <67.34%                      |To be improved slightly on speed and must try new technique for memory|
|Linked List|Conclusion|Add Two Numbers| both          |   02-Aug-2022   |     66 ms     |         96.54%          |     13.8 MB     | 86.75%                       |<sup>3</sup>|
|Linked List|Conclusion|Flatten a Multilevel Doubly Linked List| speed         |   05-Aug-2022   |     35 ms     |         95.70%          |     14.8 MB     | 50.40%                       |<sup>3</sup>|
|Linked List|Conclusion|Copy List with Random Pointer| both          |   12-Aug-2022   |     44 ms     |         80.69%          |     14.7 MB     | 99.93%                       |<sup>3</sup>|
|Linked List|Conclusion|Rotate List| both          |   13-Aug-2022   |     36 ms     |         96.03%          |     13.8 MB     | 79.96%                       ||
|Array and String|Introduction to Array|Find Pivot Index| both          |   13-Aug-2022   |    167 ms     |         86.65%          |     15.1 MB     | 99.34%                       |<sup>3</sup>|
|Array and String|Introduction to Array|Largest Number At Least Twice of Others| memory        |   13-Aug-2022   |     71 ms     |         16.93%          |     13.8 MB     | 96.78%                       ||
|Array and String|Introduction to Array|Largest Number At Least Twice of Others| speed         |   13-Aug-2022   |     39 ms     |         88.88%          |     13.9 MB     | <11.63%                      ||
|Array and String|Introduction to Array|Plus One| both          |   14-Aug-2022   |     31 ms     |         96.60%          |     13.8 MB     | 96.68%                       ||
|Array and String|Introduction to 2D Array|Plus One| both          |   14-Aug-2022   |     31 ms     |         96.60%          |     13.8 MB     | 96.68%                       ||
|Array and String|Introduction to 2D Array|Diagonal Traverse| both          |   15-Aug-2022   |    211 ms     |         86.78%          |      17 MB      | 90.46%                       |<sup>3</sup>|
|Array and String|Introduction to 2D Array|Spiral Matrix| both          |   16-Aug-2022   |     37 ms     |         81.87%          |     13.9 MB     | 83.39%                       |<sup>3</sup>|
|Array and String|Introduction to 2D Array|Pascal's Triangle| both          |   17-Aug-2022   |     29 ms     |         96.48%          |     13.8 MB     | 97.65%                       |<sup>3</sup>|
|Array and String|Introduction to String|Add Binary| both          |   17-Aug-2022   |     39 ms     |         85.22%          |     13.7 MB     | 98.07%                       |<sup>3</sup> This solution is the same as the fastest and most memory optimal solution|
|Array and String|Introduction to String|Implement strStr()| both          |   17-Aug-2022   |     33 ms     |         90.51%          |     13.8 MB     | 97.46%                       |<sup>3</sup> The other best solution is available as solution_alternate but this uses an inbuilt function|
|Array and String|Introduction to String|Longest Common Prefix| both          |   18-Aug-2022   |     37 ms     |         91.00%          |     13.9 MB     | 88.78%                       ||
|Array and String|Two-Pointer Technique|Reverse String| both          |   18-Aug-2022   |    311 ms     |         51.26%          |     18.3 MB     | 86.20%                       |The best solution is available as solution_alternate but this uses an inbuilt function|
|Array and String|Two-Pointer Technique|Array Partition I| both          |   19-Aug-2022   |    294 ms     |         90.95%          |     16.6 MB     | 96.41%                       ||
|Array and String|Two-Pointer Technique|Two Sum II - Input array is sorted| both          |   20-Aug-2022   |    154 ms     |         79.10%          |     14.9 MB     | 89.77%                       ||
|Array and String|Two-Pointer Technique|Minimum Size Subarray Sum| memory        |   20-Aug-2022   |    486 ms     |         23.56%          |     26.6 MB     | 96.75%                       ||
|Array and String|Two-Pointer Technique|Minimum Size Subarray Sum| speed         |   21-Aug-2022   |    274 ms     |         89.06%          |     27.0 MB     | 86.86%                       |very minor change compared to memory optimised solution|
|Array and String|Conclusion|Rotate Array| both          |   22-Aug-2022   |    202 ms     |         99.69%          |     25.4 MB     | 76.32%                       ||
|Array and String|Conclusion|Pascal's Triangle II| both          |   22-Aug-2022   |     26 ms     |         98.78%          |     13.7 MB     | 97.06%                       |<sup>3</sup>|
|Array and String|Conclusion|Reverse Words in a String| both          |   22-Aug-2022   |     31 ms     |         96.45%          |     13.9 MB     | 97.72%                       |<sup>3</sup>|
|Array and String|Conclusion|Reverse Words in a String III| both          |   23-Aug-2022   |     33 ms     |         97.41%          |     14.5 MB     | 81.97%                       ||
|Hash Table|Design a Hash Table|Design HashSet| memory        |   23-Aug-2022   |    1924 ms    |         17.28%          |     18.4 MB     | 95.83%                       |<sup>3</sup> the most speed optimal solutions available in LeetCode uses set or dicts, which seem to be against the spirit of designing a hashset from scratch. Have to check for other potential solutions which solve this faster while keeping the spirit of the question.|
|Hash Table|Design a Hash Table|Design HashMap| memory        |   24-Aug-2022   |    896 ms     |         20.32%          |     17.1 MB     | 96.77%                       |<sup>3</sup> the most speed optimal solutions available in LeetCode uses set or dicts, which seem to be against the spirit of designing a hashset from scratch. Have to check for other potential solutions which solve this faster while keeping the spirit of the question.|
|Hash Table|Practical Application - Hash Set|Contains Duplicate| both          |   25-Aug-2022   |    447 ms     |         98.93%          |     25.9 MB     | 71.55%                       |<sup>3</sup>|
|Hash Table|Practical Application - Hash Set|Single Number| memory        |   25-Aug-2022   |    140 ms     |         92.68%          |     16.6 MB     | 93.49%                       |<sup>3</sup>|
|Hash Table|Practical Application - Hash Set|Single Number| alternate     |   25-Aug-2022   |    135 ms     |         96.18%          |     17.1 MB     | 9.92%                        ||
|Hash Table|Practical Application - Hash Set|Intersection of Two Arrays| memory        |   26-Aug-2022   |     68 ms     |         61.47%          |     14.0 MB     | 91.27%                       ||
|Hash Table|Practical Application - Hash Set|Intersection of Two Arrays| speed         |   26-Aug-2022   |     38 ms     |         99.66%          |     14.0 MB     | 68.63%                       |<sup>3</sup>|
|Hash Table|Practical Application - Hash Set|Happy Number| memory        |   26-Aug-2022   |     34 ms     |         95.25%          |     13.9 MB     | 61.84%                       |<sup>3</sup>|
|Hash Table|Practical Application - Hash Set|Happy Number| speed         |   26-Aug-2022   |     32 ms     |         97.01%          |     14.0 MB     | <85.00%                      |<sup>3</sup>|



<sup>1,2</sup>: The rankings for speed and memory usage are directly taken from LeetCode "Submission Details" sheet 
obtained as on the date of submission (rankings reported only on Python3 based submissions).

<sup>3</sup>: Submitting the same code a few times resulted in slightly varying results, the best speed and memory are reported together here. This also indicates the metrics reported by LeetCode are not consistent, and there by consider them only as a general indication of performance
 
