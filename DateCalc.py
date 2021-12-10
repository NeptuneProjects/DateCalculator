#!/usr/bin/env python3

"""
By William Jenkins
wjenkins [at] ucsd [dot] edu
Scripps Institution of Oceanography
University of California San Diego
December 2021

This script provides a GUI to calculate a future or past date given a 
reference date and some duration in days.
"""

from datetime import datetime, timedelta
import tkinter as tk

def calculator():
    """Description: Program backend. The input requries a formatted
    datestring and an integer number of days. A negative integer will 
    yield a past date.

    Parameters
    ----------
    date1 : str (YYYY-MM-DD)
        Reference date.

    delta : int
        Duration in days; negative integer will yield past date.

    Returns
    -------
    date2 : str (YYYY-MM-DD)
        The date that is delta_input days away from date1_input.
    """
    date1 = datetime.strptime(str(date1_input.get()), "%Y-%m-%d").date()
    delta = timedelta(days=int(delta_input.get()))
    date2 = date1 + delta
    date2_disp.config(text=f"Date: {date2}")

if __name__ == "__main__":
    # Initialize and configure GUI
    window = tk.Tk()
    window.title("Date Calculator")
    window.configure(bg='#ececec')
    
    # Add field for input date
    date1_label = tk.Label(text="Enter date (YYYY-MM-DD):").pack()
    date1_input = tk.Entry(width=10)
    date1_input.pack()

    # Add field for input duration
    delta_label = tk.Label(text="Enter date difference in days:").pack()
    delta_input = tk.Entry(width=5)
    delta_input.pack()

    # Add calculator button
    button = tk.Button(
        text="Return",
        width=5,
        height=2,
        command=calculator
    ).pack()

    # Return results
    date2_disp = tk.Label(text="Date: ")
    date2_disp.pack()

    # Run program
    window.mainloop()
