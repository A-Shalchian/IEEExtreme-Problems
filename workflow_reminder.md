# Workflow Reminder

## When User Provides a Problem Link:

1. **Create Python file** with the name based on the problem title
2. **Add header section only** with:
   ```python
   """
   [URL]
   [Problem Title]

   [Problem Description]
   """
   ```
3. **DO NOT write any code** - just the header comment section
4. **Stop there** - let the user implement the solution themselves

## Example:
If given `https://dmoj.ca/problem/ddrp2` for "Double Doors Regional P2 - Tudor Learns DDR":

Create file: `Tudor_Learns_DDR.py`
Content:
```python
"""
https://dmoj.ca/problem/ddrp2
Double Doors Regional P2 - Tudor Learns DDR

Tudor is learning to play DDR (Dance Dance Revolution). In DDR, there are 4 arrow directions: Up (U), Down (D), Left (L), and Right (R).
A move sequence of 3 arrows can be classified as either a "Crossover", "Candle", or "Neither".
- Crossover: All 3 moves are distinct AND the first and last moves are opposite directions (L-R or R-L)
- Candle: All 3 moves are distinct AND the first and last moves are opposite directions (U-D or D-U)
- Neither: Does not meet the criteria for Crossover or Candle
"""
```

**IMPORTANT: No code implementation - header only!**