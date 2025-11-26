# Day 01 — Python + AI Learning Journal

**Date:** 
26-Nov-2025

## Topic(s) Covered
*args and **kwargs

Using flexible function arguments

Tuples & enumerate()

sum(), len(), and round() for averaging values

if __name__ == "__main__": explained

## Short Explanation

*args allows a function to accept any number of positional arguments and stores them in a tuple.

**kwargs allows a function to accept any number of named keyword arguments and stores them in a dictionary.

Tuples are immutable ordered collections; useful for read-only data such as *args.

enumerate() helps loop over items with an automatic index counter.

Average calculation uses sum(values) / len(values) and may be formatted using round().

if __name__ == "__main__": ensures that code inside this block runs only when the file is executed directly, not when it is imported.

## What I Learned
-*args allows passing a variable number of positional arguments and stores them in a tuple.

**kwargs handles key-value arguments and stores them in a dictionary.

Calculating average using sum(scores) / len(scores)

round() helps display clean results (e.g., rounding ML metrics).

if __name__ == "__main__": ensures test code runs only when the script is executed directly, not when imported.

## Code Practiced
- File: challenges/Day01/challenge.py
- Description:
def generate_report(*scores, **options):
    print(f"Scores: {scores}")

    if options.get("include_average", False):
        if len(scores) == 0:
            print("No scores available to compute average.")
            return

        avg = sum(scores) / len(scores)

        if options.get("rounding", False):
            avg = round(avg)

        print(f"Average: {avg}")


if __name__ == "__main__":
    generate_report(90, 85, 78, 92, include_average=True, rounding=True)
    generate_report(60, 70, 80, include_average=True, rounding=False)


## Doubts / Questions
- 

## Time Spent
- 
45-60 Min
## Plan for Tomorrow
Begin Day 2 topic: lambda, map, filter, reduce

Convert simple loop transformations to functional style


## Reflection

Today I learned how flexible Python functions work and practiced writing real-world-style code with optional arguments. Also learned to run Python scripts correctly from VSCode and gained clarity on __main__.