# Menstrual Follow-Up and Fertility Levels Tracker

This application helps users track their menstrual cycle and fertility levels. It provides insights into hormone levels throughout the menstrual cycle, allows for adding personal notes, and includes graphical visualizations of hormonal changes.

## Features

- **Menstrual Tracking**: Record the start and end dates of menstrual periods.
- **Fertility Levels**: Automatically calculates and displays fertility levels (Middle, High, Weak) for each cycle.
- **Personal Notes**: Add personalized notes linked to specific dates.
- **Graphical Visualization**: Displays hormone levels (FSH, LH, Estrogen, Progesterone) throughout the menstrual cycle.

## Prerequisites

- **Python 3.8 or higher**
- **Required Python Libraries**:
  - `tkinter`
  - `matplotlib`
  - `numpy`

Install the necessary libraries using:

```bash
pip install matplotlib numpy
```

## How to Use

1. **Run the Application**:
   - Save the provided Python script as `menstrual_tracker.py`.
   - Execute the script using Python:
     ```bash
     python menstrual_tracker.py
     ```

2. **Record Menstrual Data**:
   - Enter the start date of your menstrual cycle in the `YYYY-MM-DD` format.
   - Click the `Save` button to record the cycle.

3. **View Data**:
   - Click the `Show Menstrual and Fertility Information` button to view recorded periods and calculated fertility levels.

4. **Add Personal Notes**:
   - Enter a date and note in the respective fields.
   - Click the `Add Note` button to save the note.

5. **Visualize Hormone Levels**:
   - Click the `Show Hormone Levels Graph` button to generate and display a graph of hormone levels during the menstrual cycle.

## Data Storage

- All user data is stored in a JSON file named `menstrual_follow_up.json` in the application directory.
- Data includes:
  - Menstrual cycle dates and fertility levels.
  - Personal notes linked to specific dates.

## Code Overview

### Main Components

#### 1. **Data Management**
Functions to load and save data to the JSON file:
- `load_data()`
- `save_data(data)`

#### 2. **Fertility Level Calculation**
Determines fertility levels based on the start date:
- `calculate_fertility_level(start_date)`

#### 3. **Hormone Level Generation**
Simulates hormone levels over a 28-day cycle:
- `generate_hormone_levels(start_date)`

#### 4. **Graphical Interface**
Uses `tkinter` to create a user-friendly interface with:
- Entry fields for dates and notes.
- Buttons for saving and displaying data.
- Error handling and success messages using `messagebox`.

#### 5. **Visualization**
Uses `matplotlib` to plot hormone levels over time:
- `plot_hormone_levels()`

## Example Output

### Hormone Levels Graph
![Example Graph](https://pointspecifics.com.au/wp-content/uploads/2020/01/fsh-lh-hormones.jpg)

### Fertility Information
```
Start: 2025-06-01, Finish: 2025-06-05
Fertility Levels:
  Middle: 2025-06-06 - 2025-06-13
  High: 2025-06-14 - 2025-06-14
  Weak: 2025-06-15 - 2025-06-29
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Inspiration for the application was derived from the need for a comprehensive and user-friendly menstrual tracking tool.
- Special thanks to contributors and supporters of open-source libraries.
