# Web research: capture source URLs

When pulling facts from the **web** (search tools, browser, MCP fetch), always save the **canonical page URL** next to the extraction — not only a search-results URL.

- Open the hit, then copy the **address bar** or **Share link** for that specific post/article/page.
- Facebook: prefer `photo/?fbid=…&set=…` or post permalink, not “found via search”.
- Reporting: give **links with claims**.

Hub installs this as an always-on rule: `knowledge-hub/.cursor/rules/web-research-capture-source-urls.mdc`. Copy that rule into a project’s `.cursor/rules/` if you want the same constraint outside the hub.
