# MTG Vintage Cube Data Collector

## Overview
Tracks different statistics acrossed multiple sessions which will allow you to compare and contrasts statistics.
The data is stored locally in a JSON file and persists between sessions

## Categories
- **People** - win rates by player
- **Color Pairing** - performance by color combination
- **Archetype** - win rates by deck archetype
- **First Pick** - cards taken first overall
- **Last Pick** - cards taken last overall

## Requirements
``` bash
py -m pip install matplotlib
```

## usage
``` bash
python "Magic Data Code.py"
```
On first run, you will be prompted to clear the data. Type "yes" to create the data.json file to then store and input your data.
After that is done you will be prompted with different menu options
- **Option 1** - Input win rate or frequency data
- **Option 2** - Look up frequency or average win rate for an entry
- **Option 3** - Visualize data as bar charts (win rate) or pie charts (frequency)
- **Option 4** - Undo the last data entry
- **Option 5** - Quit
