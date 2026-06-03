# FG RiskMap — Financial Distortion Monitor

**FG RiskMap** is a demonstration project for pre-answer risk routing and financial distortion monitoring in legal, tax, and financial workflows.

It does **not** make compliance decisions.
It does **not** replace auditors, lawyers, CPAs, bankers, regulators, or courts.
It performs **Risk-Routing & Distortion Mapping** before a file enters audit, filing, lending, legal review, regulatory review, or litigation.

## Core Idea

Many legal and financial files look acceptable when each document is reviewed separately:

* financial statements may appear complete;
* tax filings may appear filed;
* bank records may appear consistent;
* legal agreements may appear formally valid;
* ratios may appear within normal range.

However, when the same file is read across institutional pathways, the structure may already be distorted.

FG RiskMap uses the **Institutional Distortion Index (IDI)** to compare arithmetic tension and geometric distortion:

```text
IDI = | ITI - gITI |
```

Where:

* **ITI** = Institutional Tension Index, an arithmetic or normalized institutional pressure score.
* **gITI** = geometric Institutional Tension Index, a Fiscal Geometry reading of mobility, continuity, routing compression, and institutional distortion.
* **IDI** = the divergence between the two readings.

A high IDI means that the numbers may still look acceptable, but the institutional structure may already be geometrically distorted.

## Product Positioning

FG RiskMap does not answer:

```text
Is this compliant?
```

It asks first:

```text
Before compliance review, audit, filing, lending, or litigation, where is the file structurally distorted?
```

This makes FG RiskMap a **pre-answer control layer** for document-heavy, rule-dense workflows.

## What This Demo Does

This demo shows a simplified pipeline:

1. Load a sample legal / tax / financial workflow dataset.
2. Calculate ITI.
3. Calculate gITI.
4. Calculate IDI.
5. Classify the risk-routing status.
6. Produce a distortion monitoring output.

## What This Demo Does Not Do

This demo does not determine whether a party is compliant, liable, solvent, negligent, fraudulent, in default, or legally responsible.

It only performs **pre-review routing visibility**.

## Target Users

FG RiskMap is designed for:

* CPA firms;
* law firms;
* CFOs and controllers;
* financial due diligence teams;
* lenders and bank-review teams;
* risk officers;
* RegTech / FinTech platforms;
* AI governance and Legal AI workflow designers.

## Routing States

| Status | Meaning |
|---|---|
| Stable | Low arithmetic and geometric pressure |
| Watch | Some pressure exists but no major divergence |
| Distorted | ITI and gITI diverge materially |
| Escalate | High distortion requiring human review before judgment |

## Repository Structure

```text
fg-riskmap-demo/
├── README.md
├── DISCLAIMER.md
├── data/
│   └── sample_workflow_data.csv
├── src/
│   └── riskmap.py
└── outputs/
    └── sample_output.json
```

## Run the Demo

```bash
python src/riskmap.py
```
## Intellectual Property Status

FG RiskMap is connected to the author's broader Fiscal Geometry and Institutional Tension framework.

Related intellectual property filings have been made for the author's broader institutional-risk framework.

The ZITI trademark application has received a Notice of Approval from the Canadian Intellectual Property Office (CIPO).

FG RiskMap is presented here as a demonstration repository for pre-answer risk routing, financial distortion monitoring, and non-operational framework visibility.

## Positioning Statement

FG RiskMap converts legal, tax, banking, and financial workflow evidence into pre-answer risk-routing visibility.

The purpose is not to answer the case.

The purpose is to show where the case may break before anyone answers.
