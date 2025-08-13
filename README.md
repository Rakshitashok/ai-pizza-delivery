# AI Pizza Delivery Service (Streamlit + OpenAI API)

## Overview
A simple Streamlit web app that runs a pizza-ordering AI agent via the OpenAI Chat API. The agent asks for pizzas, sizes, toppings, special requests, and delivery address, and outputs a final JSON order.

## Quick setup
1. Clone repo
2. Create `.env` with:
3. Install:
4. Run:


## Notes
- Speech: optional. Uses browser mic + Whisper API if enabled.
- To switch to a local model, replace `dialog_manager.py` `call_model()` function.

## Deliverables
- `menu.json` — menu catalog
- `flowchart.mmd` — Mermaid flowchart
- `report.txt` — 2-page report (convert to PDF)
- `sample_transcript.txt` — example dialog
- `sample_order.json` — produced order
