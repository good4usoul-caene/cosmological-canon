#!/usr/bin/env python3

from tools.riddles_enhanced_parser import count_stressed_syllables, analyze_meter

# Test the new verse 8 formatting
line1 = 'before the gate, the sheep could not trust those'
line2 = 'anywhere near they\'re on their guard for'
line3 = 'thieves and robbers out on the frontier'

print('New verse 8 formatting:')
for i, line in enumerate([line1, line2, line3], 1):
    words = line.split()
    stressed = count_stressed_syllables(words)
    meter = analyze_meter(line)
    print(f'  Line {i}: "{line}" -> {stressed} stressed syllables')
    print(f'    Stress pattern: {meter["stress_pattern"]}')
    print()