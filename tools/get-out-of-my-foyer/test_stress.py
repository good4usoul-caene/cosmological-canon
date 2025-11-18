#!/usr/bin/env python3

from tools.riddles_enhanced_parser import count_stressed_syllables, detect_poetic_lines, analyze_meter

# Test the current broken line
line1 = 'before the gate, the sheep could not trust those'
line2 = 'anywhere near they are on their guard for thieves and'  
line3 = 'robbers out on the frontier'

print('Current broken lines:')
for line in [line1, line2, line3]:
    words = line.split()
    stressed = count_stressed_syllables(words)
    meter = analyze_meter(line)
    print(f'  "{line}" -> {stressed} stressed syllables')
    print(f'    Stress pattern: {meter["stress_pattern"]}')

print()
# Test the suggested better break
better1 = 'before the gate, the sheep could not trust those anywhere near'
better2 = 'they are on their guard for thieves and robbers out on the frontier'

print('Suggested better lines:')
for line in [better1, better2]:
    words = line.split()
    stressed = count_stressed_syllables(words)
    meter = analyze_meter(line)
    print(f'  "{line}" -> {stressed} stressed syllables')
    print(f'    Stress pattern: {meter["stress_pattern"]}')

print()
# Test the new line-breaking algorithm
full_text = 'before the gate, the sheep could not trust those anywhere near they are on their guard for thieves and robbers out on the frontier.'
new_lines = detect_poetic_lines(full_text)
print('Algorithm-generated lines:')
for line in new_lines:
    words = line.split()
    stressed = count_stressed_syllables(words)
    meter = analyze_meter(line)
    print(f'  "{line}" -> {stressed} stressed syllables')
    print(f'    Stress pattern: {meter["stress_pattern"]}')