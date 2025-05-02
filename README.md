# 🧹 Remove Duplicates from Sorted Array (Python)

This Python script solves the classic **Remove Duplicates from Sorted Array** problem.  
The goal is to modify the input array in-place such that each element appears only once, and return the new length.

---

## 🧠 Problem Description

Given a **sorted** array `nums`, remove the duplicates **in-place** such that each element appears only once and return the new length.

You must do this **without using extra space** for another array.

---

## ✅ Approach

- Use two pointers:
  - `i` scans the full array.
  - `j` tracks the position of the next unique element.
- Whenever a non-duplicate is found, it's moved to the `j`-th position.
- The function returns `j`, which is the length of the array with unique values.
