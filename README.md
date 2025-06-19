# Menstrual Follow-Up and Fertility Levels Tracker

This application helps users track their menstrual cycle and fertility levels. It provides insights into hormone levels throughout the menstrual cycle, allows for adding personal notes, and includes graphical visualizations of hormonal changes.

## Features

- **Menstrual Tracking**: Record the start and end dates of menstrual periods.
- **Fertility Levels**: Automatically calculates and displays fertility levels (Middle, High, Weak) for each cycle.
- **Personal Notes**: Add personalized notes linked to specific dates.
- **Graphical Visualization**: Displays hormone levels (FSH, LH, Estrogen, Progesterone) throughout the menstrual cycle.

## Framework Versions

- matplotlib      3.10.0
- numpy           2.2.5
- Python 3.12.11
  

## How to Use

1. **Run the Application**:
   - Save the provided Python script as `menstrual_tracker.py`.

2. **Record Menstrual Data**:
   - In the application window, enter the start date of your menstrual cycle in the `YYYY-MM-DD` format in the input field.
   - Click the `Save` button to record the cycle. If the format is incorrect, an error message will appear.

3. **View Recorded Data**:
   - Click the `Show Menstrual and Fertility Information` button to view a detailed list of recorded periods and calculated fertility levels.

4. **Add Personal Notes**:
   - Enter a specific date and your personal note in the designated fields.
   - Click the `Add Note` button to save the note. You will receive a confirmation upon successful saving.

5. **Visualize Hormone Levels**:
   - Click the `Show Hormone Levels Graph` button to generate and display a graph of hormone levels during the menstrual cycle.

## Data Storage

- All user data is stored in a JSON file named `menstrual_follow_up.json` in the application directory.
- Data includes:
  - Menstrual cycle dates and fertility levels.
  - Personal notes linked to specific dates.

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
