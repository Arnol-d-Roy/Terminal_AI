# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a resume management project for Arnold Roy Nazareth. The repository contains LaTeX source files for multiple versions of resumes tailored for different job applications.

## File Structure

- **LaTeX source files** (`.tex`): Editable resume templates
  - `Resume_Arnold.tex` - Full comprehensive resume with all work experience
  - `Resume_warehouse.tex` - Australia-focused resume with only Australian work experience
- **PDF files** (`.pdf`): Compiled resume outputs

## Working with Resumes

### Compilation

Since LaTeX may not be installed locally, use one of these approaches:

1. **Overleaf (recommended)**: Upload `.tex` files to https://www.overleaf.com for automatic compilation
2. **Local compilation** (if LaTeX is installed):
   ```bash
   cd "/mnt/d/Github Repos/Terminal_AI/Resume_Project"
   pdflatex Resume_Arnold.tex
   pdflatex Resume_warehouse.tex
   ```

### Resume Variants

- **Resume_Arnold.tex**: Contains complete work history including international experience (Oracle-Cerner, Nife Labs in India)
- **Resume_warehouse.tex**: Streamlined for Australian job market with only local experience (Pancake Parlour, Chromagen)

### LaTeX Dependencies

Required packages:
- `geometry` - page margins
- `enumitem` - list formatting
- `titlesec` - section formatting
- `hyperref` - clickable links
- `fontawesome` - icons for contact info

## Contact Information

- Phone: +61-0433842433
- Email: arnoldnazareth8@gmail.com
- LinkedIn: linkedin.com/in/arnold-nazareth-5738351a9

## Important Notes

- Always read existing PDF files before making edits to understand current content
- Maintain consistent formatting across all resume variants
- When adding new experience, place it chronologically (most recent first)
- Professional objective targets: Python developer, database analyst, data scientist, machine learning engineer
