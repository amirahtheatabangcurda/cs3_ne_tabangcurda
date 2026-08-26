Annex C
Code Quality Assessment Worksheet

Section: Neon                             	Score:____________
C# / Name:# 20 - Diamante, Aliesh Jade       Date: 8/26/2026
          # 29 - Tabangcurda, Amirah Thea
     
Instructions:

The problem: Search for a Number in a Sorted List

For example: Both algorithms could search: 
numbers = [5, 12, 18, 23, 31, 47, 56, 68, 74, 90]
target = 47

Implementation 1
def linear_search(numbers, target):
   for i in range(len(numbers)):
       if numbers[i] == target:
           return i


   return -1


Implementation 2
def binary_search(numbers, target):
   low = 0
   high = len(numbers) - 1


   while low <= high:
       middle = (low + high) // 2


       if numbers[middle] == target:
           return middle
       elif numbers[middle] < target:
           low = middle + 1
       else:
           high = middle - 1


   return -1


Questions with Checklists
1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?
- Implementation 2 is best used for very large lists, since it divides the amount of elements it needs to search per step, compared to implementation 1 that checks each element one by one sequentially.

Checklist to guide your answer:
Implementation 1
How many elements might the algorithm need to check? all one by one 
Does the algorithm reduce the search area as it runs? No
Does the algorithm still work efficiently with a very large list? No

Implementation 2
How many elements might the algorithm need to check? half per step 
Does the algorithm reduce the search area as it runs? Yes
Does the algorithm still work efficiently with a very large list? Yes


2. Readability
Which algorithm is easier to understand at first glance? What makes it clearer?
- Implementation 1 is much easier to understand at first glance, due to its basic and concise structure using a for loop that directly checks each item and can be easily followed since the function only takes up 5 lines. 

Checklist to guide your answer:
Implementation 1
How meaningful are the variable names? Very meaningful compared to Implementation 2
How simple is the logic? Very simple compared to Implementation 2
How concise is the code? Very concise compared to Implementation 2
How easy is it to follow the search process? Its very easy to follow compared to Implementation 2

Implementation 2
How meaningful are the variable names?  
How simple is the logic? Its not as simple as implementation 1
How concise is the code?  Its not as concise as implementation 1
How easy is it to follow the search process?  Its not as easy to follow as implementation 1



3. Maintainability
If you had to modify the program, such as changing what happens when the target is found, which algorithm would be easier to update? Why?
- Implementation 1, in relation to the question before its logic is quite simple and easy to follow, the risks of errors is quite low compared to the chances of risks one can create when modifying and updating implementation 2's less simpler logic.

Checklist to guide your answer:
Implementation 1
Is the structure straightforward? Yes
Would adding new steps break the code easily? No
Is there less chance of errors when updating? Yes

Implementation 2
Is the structure straightforward? No
Would adding new steps break the code easily? Yes 
Is there less chance of errors when updating? No


4. Testability
Which algorithm is easier to test with different inputs? Why?
- Implementation 1 (Linear Search) is easier to test because it has fewer internal logical pathways, which means that it requires fewer test cases to achieve 100% path coverage.

Checklist to guide your answer:

Implementation 1
Can you test with small lists easily?
- Very easy to test with small lists or single-element inputs.
Does the algorithm have fewer conditions to check?
- Has only two main conditions which are the item found vs item not found.
Is the output predictable and clear?
- Output behavior remains completely predictable across all basic input variations.

Implementation 2
Can you test with small lists easily?
- Easy to test with small lists but boundary states change quickly.
Does the algorithm have fewer conditions to check?
- Has multiple conditional execution branches that must be all tested ("==", "<", ">")
Is the output predictable and clear?
- Midpoint tracking calculations make path tracing slightly more complex to verify.



5. Reliability and Input Validation
What should the algorithm check to avoid errors when receiving input from a user?
- None of the algorithms have currently features built-in validation checks. To maximize reliability, both systems should actively verify that input data types match, arrays are populated, and structural conditions are met before executing the loops.

Checklist to guide your answer:
Implementation 1
Does the algorithm check if the list is empty?
- Doesn't check if the list is empty; it safely returns "-1" by default due to range limitations.
Does it handle invalid inputs (like letters instead of numbers)?
- Doesn't handle invalid data types, which will cause comparisons to throw errors.
Does it avoid crashing when inputs are unusual?
- Can crash or behave unpredictably if elements are completely mismatched types.
Does it check that the list is sorted before using Linear Search?
- Doesn't require a sorted list to run which makes it resilient to ordering errors.

Implementation 2
Does the algorithm check if the list is empty?
- Doesn't check if the list is empty, it exists safely because the "while" condition fails.
Does it handle invalid inputs (like letters instead of numbers)?
- Doesn't handle invalid data types, throwing errors if elements can't be compared.
Does it avoid crashing when inputs are unusual?
- Will crash or experience unexpected failures if inputs fail standard numeric boundaries.
Does it check that the list is sorted before using Binary Search?
- Doesn't check if the list is sorted, it will return incorrect results without raising a warning if if unsorted data is given.


6. Final Answer
Based on your answers from 1 to 5, Which algorithm would you choose for this problem, and under what conditions would the other algorithm be more suitable? Summarize your answer.
- I would choose Implementation 2 (Binary Search) as the first choice for this specific question because the problem statement establishes that the list is already sorted. Using a sorted data set with Binary Search can lead to multiple benefits in the performance. However, Implementation 1 (Linear Search) would be more suitable if the list dataset size is tiny or if the list data undergoes constant modifications that would make maintaining a sorted order more difficult.
