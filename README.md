GUI_planner

A minimalist, calendar-aware GUI planner for Windows and Linux. Built for developers and power users who need deterministic scheduling, robust recurrence logic, and a customizable interface.

Overview

GUI_planner is designed for users who want a planner that behaves predictably, integrates smoothly into technical workflows, and supports recurring events without drift or duplication. It combines modular Tkinter widgets with calendar-aware logic to deliver a compact, expressive scheduling tool.

Features

- Recurring event support with deterministic rewrite-on-delete logic
- Calendar-accurate date parsing (leap-year safe)
- Scrollable event boxes using Listbox, Canvas, and Scrollbar
- Modular GUI layout for easy extension and customization
- Mnemonic keymaps and pixel-aligned formatting
- Designed for reproducible output and inspectable state

Installation

Clone the repository and run the planner:

```bash
git clone https://github.com/yourusername/ritualplanner.git
cd ritualplanner
python main.py
```

Requires Python 3.7+ and Tkinter (included with most Python distributions).

Use Cases

GUI_planner is ideal for users who:

- Need a planner for scheduled events with recurring capabilities
- Prefer deterministic behavior over hidden automation
- Want a GUI that reflects their workflow and aesthetic
- Enjoy customizing their tools with modular Python code

Philosophy

This planner is built around clarity, and control. Events are treated as inspectable objects with recurrence metadata, allowing users to delete and regenerate them without ambiguity. The interface is minimal but expressive, designed to feel like a natural extension of your terminal or desktop environment.

Contributing

Pull requests are welcome. If you have ideas for new widgets, recurrence modes, or layout tweaks, feel free to open an issue or fork the project.

---

For questions, feedback, or collaboration, reach out via GitHub Issues or Discussions.
