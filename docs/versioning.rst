===============
BO4E Versioning
===============

The BO4E data model uses a unique versioning system to track changes and updates.
This system is easy to understand once you're familiar with its format and rationale.

Let's break it down:

Version Format: `YYYYMM.functional.technical`

- YYYYMM: Represents the year (YYYY) and month (MM) when the version was released. For example, 202312 would mean December 2023.
- functional: A number that changes when there are significant updates or new features.
- technical: This number changes for minor updates, like bug fixes or spelling corrections.

How Does it Work?
=================

1. **Base Structure**: Think of the version number as a date followed by two additional numbers, like 202312.1.2. Here, 202312 tells you the release date, 1 is the functional number, and 2 is the technical number.
2. **Technical Changes**: If we fix a typo or a small bug, we only change the technical number. So, after a minor fix, the version might change from 202312.1.2 to 202312.1.3.
3. **Functional Changes**: For bigger changes, like adding a new business object, we update the functional number and reset the technical number to zero. For instance, if we add a significant feature to the 202312.1.2 version, it becomes 202312.2.0.

Yearly Reset: With the start of a new year, we reset both the functional and technical numbers.
So, if we're moving from December 2023 (202312.2.0) to January 2024, the new version would be 202401.0.0.

Why This System?
================

This versioning system, inspired by semantic versioning, offers a clear and systematic way to track changes.
It ensures that users can easily identify when a significant update has occurred and when minor tweaks have been made.
