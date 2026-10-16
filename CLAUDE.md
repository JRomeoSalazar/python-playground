# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A Python learning repository: each top-level `.py` file is a standalone script demonstrating one topic (variables, loops, classes, async, HTTP requests, etc.). Code, identifiers and comments are in Spanish (course material); write new docs in English.

There is no build system, test suite, or linter configured.

## Documentation

- `README.md` is written in Spanish (explicit exception to the English-docs rule, since it is aimed at Spanish-speaking learners). Keep its folder tree and topic list in sync when adding or renaming scripts.
- Target Python version is 3.12. The license is still undecided (no `LICENSE` file; the README uses a `<licencia>` placeholder).

## Commands

- Activate the virtualenv: `source .venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt` (only `requests` and its transitive deps)
- Run any script directly: `python <script>.py` (e.g. `python asincronia.py`)

## Structure

- Scripts at the repo root are independent; none import each other except `textos.py`.
- `analizador/` is the only package (a small text-utilities module, `utilidades.py`). `textos.py` imports it via `from analizador import utilidades`, so it must be run from the repo root.
- `peticiones.py` makes a live HTTP call to jsonplaceholder.typicode.com (needs network); `asincronia.py` demonstrates `asyncio.gather` running concurrent coroutines.
