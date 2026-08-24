# Odoo Reports

Custom **Odoo 19** report modules for **Hospitality Information Co. Ltd. (HICL)**.

Drop this repository onto your Odoo `addons_path` (or clone it into your addons
directory) and install/upgrade the modules below.

## Modules

### `hicl_report_layout`
Customizes the **Quotation / Sales Order** PDF (`sale.order`) using Odoo's
standard *Bubble* document layout, with these behaviours:

- **Header on the first page only** — the company masthead is rendered inline at
  the top of page 1 instead of as a repeating page header, so continuation
  pages have no masthead and use the full height.
- **Repeating table header** — the `DESCRIPTION / QUANTITY / UNIT PRICE / TAXES /
  AMOUNT` row repeats at the top of every page, and rows are kept whole across
  page breaks.
- **Single-line footer** — company details span the width on the left with the
  `Page X / Y` counter pinned to the right.
- **Saudi A4 paper format** — margins tuned for the above (small uniform top
  margin, compact footer).

Brand colours come from the company settings (primary / secondary), not from the
module, so the layout follows your configured palette.

Scope is limited to `sale.order`; invoices and other reports that use the Bubble
layout are left untouched.

#### Install
```bash
# with the module on your addons_path
odoo -d <db> -i hicl_report_layout --stop-after-init
# to upgrade after pulling changes
odoo -d <db> -u hicl_report_layout --stop-after-init
```

## License
LGPL-3
