import { Agent } from "@mastra/core/agent";

import { revenueTool } from "../tools/revenue-tool";

export const analyticsAgent = new Agent({
  id: "analytics-agent",

  name: "Analytics Agent",

  instructions: `
You are responsible for analytics.

Always use tools.

You answer:

- Revenue
- Attendance
- Bookings

Never answer CRM questions.
`,

  model: "openai/gpt-4.1-mini",

  tools: {
    revenueTool,
  },
});